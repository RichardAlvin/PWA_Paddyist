<template>
  <main class="site-main">
    <section class="upload">
      <div class="container">
          <form class="upload-form" enctype="multipart/form-data" @submit.prevent="submit()">
            <input id="file" type="file" accept="image/*" hidden @change="onFileUpload">
            <div class="img-area" data-img="">
              <i class='bx bxs-cloud-upload icon'></i>
              <h3>Upload Image</h3>
              <p>Image size must be less than <span>2MB</span></p>
            </div>
            <button class="select-image">Select Image</button>
            <button class="predict-button">Identifikasi</button>
          </form>
          <div class="predict-result">

          </div>
        <!-- <div id="app">
            <form action=""
            class="full-width flex flex-row relative"
            @submit.prevent="getData()">
            <input type="file" @change="onFileChange" />

            <div id="preview">
                <img v-if="url" :src="url" />
            </div>
            <button type="submit" class="btn--primary">Identifikasi</button>
            </form>
        </div> -->
      </div>
    </section>
  </main>
</template>

<script>
// import axios from 'axios';
export default {
    name: 'UploadImage',
    data() {
      return {
        FILE: null,
      };
    },
    mounted() {
        const selectImage = document.querySelector('.select-image');
        const inputFile = document.querySelector('#file');
        const imgArea = document.querySelector('.img-area');

        selectImage.addEventListener('click', function () {
            inputFile.click();
        })

        inputFile.addEventListener('change', function () {
            const image = this.files[0]
            if(image.size < 2000000) {
                const reader = new FileReader();
                reader.onload = ()=> {
                    const allImg = imgArea.querySelectorAll('img');
                    allImg.forEach(item=> item.remove());
                    const imgUrl = reader.result;
                    const img = document.createElement('img');
                    img.src = imgUrl;
                    img.classList.add('img-fluid');
                    imgArea.appendChild(img);
                    imgArea.classList.add('active');
                    imgArea.dataset.img = image.name;
                }
                reader.readAsDataURL(image);
            } else {
                alert("Image size more than 2MB");
            }
        })
    },
    methods: {
        onFileUpload(event){
          this.FILE = event.target.files[0]
        },
        async submit(){
          try {
            const formData = new FormData()
            formData.append('file', this.FILE,'file')
            await this.$axios
              .post(`${this.$apiurl()}/predictPaddy`, formData)
              .then((res) => {
                // eslint-disable-next-line no-console
                console.log(res)
              })
          } catch (e) {
            // eslint-disable-next-line no-console
            console.log(e)
          }
        }
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
.select-image {
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
.select-image:hover {
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
