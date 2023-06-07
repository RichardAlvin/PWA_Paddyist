<template>
  <main class="site-main">
    <section class="upload">
      <div class="container">
		<form class="photo-form" enctype="multipart/form-data" @submit.prevent="submit()">
			<div class="photo-div">
				<button type="button" class="cam-button" :class="{ 'is-primary' : !isCameraOpen, 'is-danger' : isCameraOpen}" @click="toggleCamera">
					<span v-if="!isCameraOpen">Open Camera</span>
					<span v-else>Close Camera</span>
				</button>
				<div v-if="isCameraOpen" class="camera-box">  
					<video id="refCamera" ref="camera" autoplay></video>
					<canvas v-show="isPhotoTaken" id="photoTaken" ref="canvas"></canvas>
				</div>
				<div id="predict-result" class="predict-result mb-8">
				<NuxtLink :to="`/penyakit-padi/${penyakit.slug}`" style="color:black"><h1 center>{{penyakit.name}}</h1></NuxtLink>
				<!-- <NuxtLink :to="`/penyakit-padi/${penyakit.slug}`" variant="primary">Detail</NuxtLink> -->
				</div>
				<div v-if="isCameraOpen" class="camera-shoot">
					<button type="button" class="button" @click="takePhoto">
						<img src="https://img.icons8.com/material-outlined/50/000000/camera--v2.png">
					</button>
				</div>
				<button class="predict-button">Identifikasi</button>
			</div>
		</form>
      </div>
    </section>
  </main>
</template>

<script>
// import axios from 'axios';
export default {
    name: 'TakePhoto',
    data() {
      return {
		isCameraOpen: false,
		isPhotoTaken: false,
		FILE: null,
        penyakit: {
          name: '',
          slug: '',
        }
      };
    },
    methods: {
		toggleCamera() {
			if(this.isCameraOpen) {
				this.isCameraOpen = false;
				this.isPhotoTaken = false;
				this.stopCameraStream();
			} else {
				this.isCameraOpen = true;
				this.createCameraElement();
			}
		},

		createCameraElement() {
			let constraints = "";
			constraints = (window.constraints = {
				audio: false,
				video: {
					facingMode: {
						exact: "environment",
					}
				}
			});

			navigator.mediaDevices
				.getUserMedia(constraints)
				.then(stream => {
				this.$refs.camera.srcObject = stream;
				})
				// eslint-disable-next-line n/handle-callback-err
				.catch(error => {
				alert("Only Mobile Device that can use back camera");
				});
		},

		stopCameraStream() {
			// eslint-disable-next-line prefer-const
			let tracks = this.$refs.camera.srcObject.getTracks();

			tracks.forEach(track => {
				track.stop();
			});
		},

		takePhoto() {
			this.isPhotoTaken = !this.isPhotoTaken;

			const canvas = this.$refs.canvas;
			const context = this.$refs.canvas.getContext('2d');
			context.drawImage(this.$refs.camera, 0, 0, 350, 237.5);
			this.FILE = canvas.toDataURL("image/jpg");
		},

		b64toBlob(b64Data, contentType, sliceSize= null) {
			contentType = contentType || '';
			sliceSize = sliceSize || 512;

			const byteCharacters = atob(b64Data);
			const byteArrays = [];

			for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
				const slice = byteCharacters.slice(offset, offset + sliceSize);

				const byteNumbers = new Array(slice.length);
				for (let i = 0; i < slice.length; i++) {
					byteNumbers[i] = slice.charCodeAt(i);
				}

				const byteArray = new Uint8Array(byteNumbers);

				byteArrays.push(byteArray);
			}

			const blob = new Blob(byteArrays, {type: contentType});
			return blob;
		},

		async submit(){
			try {
				const formData = new FormData()
				// Split the base64 string in data and contentType
				const block = this.FILE.split(";");
				// Get the content type of the image
				const contentType = block[0].split(":")[1];// In this case "image/gif"
				// get the real base64 content of the file
				const realData = block[1].split(",")[1];// In this case "R0lGODlhPQBEAPeoAJosM...."

				// Convert it to a blob to upload
				const blob = this.b64toBlob(realData, contentType);
				formData.append('file', blob,'file')
				await this.$axios
				.post(`${this.$apiurl()}/predictPaddy`, formData)
				.then((res) => {
					// eslint-disable-next-line no-console
					console.log(res.data)
					this.penyakit.name = res.data.name
					this.penyakit.slug = res.data.slug

					document.querySelector('#predict-result').style.display = 'block'
				})
			} catch (e) {
				// eslint-disable-next-line no-console
				console.log(e)
			}
		},

    } 
}
</script>

<style lang="scss" scoped>
.photo-div{
  display:flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
  padding-top:50px;
}

.camera-box{
  margin: 5%;
  position: relative;
}

canvas{
	position:absolute;
	top:0;
	left:0;
}

.cam-button {
	display: block;
	width: 80%;
	padding: 16px 0;
	border-radius: 15px;
	background: var(--blue);
	color: #fff;
	font-weight: 500;
	font-size: 16px;
	border: none;
	cursor: pointer;
	transition: all .3s ease;
}

.predict-button{
  margin-top:10px;
  display:block;
  width: 80%;
  padding: 16px 0;
	border-radius: 15px;
	background: var(--green);
	color: #fff;
	font-weight: 500;
	font-size: 16px;
	border: none;
	cursor: pointer;
	transition: all .3s ease;
}

.predict-result{
	display:none;
}

#refCamera, #photoTaken{
	width: 350px;
	height:300px;
}

@media only screen and (max-width: 600px) {
  h1{
    font-size: 20px;
  }

  #refCamera, #photoTaken{
	width: 250px;
	height:200px;
  }
}
</style>
