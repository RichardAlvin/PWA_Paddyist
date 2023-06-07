from typing import Union
import tensorflow as tf
from PIL import Image
import numpy as np
from tensorflow.keras import preprocessing
from io import BytesIO
from typing import Annotated
import cv2
import sys
from fastapi.middleware.cors import CORSMiddleware
import os
import schemas
import re

from fastapi import FastAPI, File, UploadFile, File, Form, HTTPException
from routers import disease
from routers import advice
import shutil

app = FastAPI()
app.include_router(disease.router)
app.include_router(advice.router)

# Ensemble import model using compile=false
# model = tf.keras.models.load_model('PaddyDisease_EnsembleAverage_OverSampling_224.h5', compile=False)

# PreTrained import model
model = tf.keras.models.load_model(
    'models/PaddyDisease_EfficientNetV2B0_OverSampling_256.h5', compile=False)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predictPaddy/", response_model=schemas.PredictResponse)
async def predict_file(file: UploadFile = File(...)):
    try:
        # validate image file
        extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
        if extension:
            return "Image must be jpg or png format!"

        with open('predict_image/paddy.jpg', "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        class_names = ["bacterial_leaf_blight", "bacterial_leaf_streak", "bacterial_panicle_blight",
                       "blast", "brown_spot", "dead_heart", "downy_mildew", "hispa", "normal", "tungro"]
        path = os.path.join("predict_image/", 'paddy.jpg')
        img = tf.keras.preprocessing.image.load_img(
            path, color_mode="rgb", target_size=(256, 256))
        images = np.expand_dims(img, axis=0)

        pred = model.predict(images)
        output_class = class_names[np.argmax(pred)]

        os.remove(path)

        # make title from slug
        title = slug_to_title(output_class)

        return {'name': title, 'slug': output_class}
    except:
        e = sys.exc_info()[1]
        raise HTTPException(status_code=500, detail=str(e))


def slug_to_title(slug):
    # Replace underscore with spaces
    title = slug.replace('_', ' ')
    # Capitalize each word
    title = title.title()

    return title
