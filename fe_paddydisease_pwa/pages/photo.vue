<template>
  <main class="site-main">
    <section class="upload">
      <div class="container">
          <form class="upload-form" enctype="multipart/form-data" @submit.prevent="submit()">
            <video autoplay></video>
            <button class="take-photo get-access">Ambil Gambar</button>
            <button class="predict-button">Identifikasi</button>
          </form>
          <div class="predict-result">

          </div>
      </div>
      <script src="https://webrtc.github.io/adapter/adapter-latest.js"></script>
    </section>
  </main>
</template>

<script>
// import axios from 'axios';
export default {
    name: 'TakePhoto',
    data() {
      return {
        FILE: null,
      };
    },
    mounted() {
        // document.querySelector('#get-access').addEventListener('click', async function init(e) {
        //     try {
        //         const stream = await navigator.mediaDevices.getUserMedia({
        //         audio: false,
        //         video: true
        //         })
        //         const videoTracks = stream.getVideoTracks();
        //         const track = videoTracks[0];
        //         alert(`Getting video from: ${track.label}`);
        //         document.querySelector('video').srcObject = stream;
        //         document.querySelector('#get-access').setAttribute('hidden', true);
        //     //The video stream is stopped by track.stop() after 3 second of playback.
        //         setTimeout(() =&gt; { track.stop() }, 3 * 1000);
        //     } catch (error) {
        //         alert(`${error.name}`)
        //         console.error(error)
        //     }
        // })
    },
    methods: {
    } 
}
</script>

<style lang="scss" scoped>
.img-area {
	position: relative;
	max-width: 80%;
  max-height: 400px;
	background: var(--grey);
	margin-bottom: 30px;
	border-radius: 15px;
	overflow: hidden;
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
}

.upload-form{
  display:flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
  padding-top:50px;
}

.img-area .icon {
	font-size: 100px;
}
.img-area h3 {
	font-size: 20px;
	font-weight: 500;
	margin-bottom: 6px;
}
.img-area p {
	color: #999;
}
.img-area p span {
	font-weight: 600;
}
.img-area .img-fluid {
	position: absolute;
	top: 0;
	left: 0;
	object-fit: cover;
	object-position: center;
	z-index: 100;
}
.img-area::before {
	content: attr(data-img);
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background: rgba(0, 0, 0, .5);
	color: #fff;
	font-weight: 500;
	text-align: center;
	display: flex;
	justify-content: center;
	align-items: center;
	pointer-events: none;
	opacity: 0;
	transition: all .3s ease;
	z-index: 200;
}
.img-area.active:hover::before {
	opacity: 1;
}
.take-photo {
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
.take-photo:hover {
	background: var(--dark-blue);
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
.predict-button:hover {
  background: var(--dark-green);
}
</style>
