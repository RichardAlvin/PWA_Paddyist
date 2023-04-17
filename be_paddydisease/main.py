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

from fastapi import FastAPI, File, UploadFile, File, HTTPException
from routers import disease
from routers import advice
import shutil

app = FastAPI()
app.include_router(disease.router)
app.include_router(advice.router)

MODEL = tf.keras.models.load_model('paddyDisease_EfficientNetV2B0-1.h5')
# MODEL = tf.keras.models.load_model('paddyDisease_MobileNetV3Large-1.h5')

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


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/predictPaddy/")
async def predict_file(file: UploadFile = File(...)):
    try:
        print(file.filename.split(".")[-1] in ("jpg", "jpeg", "png"))
        # validate image file
        extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
        if extension:
            return "Image must be jpg or png format!"
        # image = preprocessing.image.load_img(file, target_size=(150, 150))
        # image = preprocessing.image.img_to_array(image)
        # input_arr = np.array([image])
        # prediction = np.argmax(MODEL.predict(input_arr), axis=-1)
        # return {"filename": prediction}
        # return "wah kamu berhasil"
        # return "wah kamu berhasil"
    except:
        e = sys.exc_info()[1]
        raise HTTPException(status_code=500, detail=str(e))
