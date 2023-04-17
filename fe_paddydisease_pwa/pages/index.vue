<template>
  <main class="site-main">
    <section class="predict">
      <div class="container">
        <div class="row">
          <div class="col-6">
            <NuxtLink to="/photo" class="link" style="text-decoration:none; color:black">
            <b-card no-body class="overflow-hidden" style="max-width: 540px;">
              <b-row no-gutters>
                <b-col md="6">
                  <b-card-img src="../../img/takepicture.jpg" alt="Take_Picture" class="rounded-0"></b-card-img>
                </b-col>
                <b-col md="6">
                  <b-card-body title="Foto Gambar">
                    <b-card-text>
                      Aktifkan izin penggunaan kamera untuk mengambil gambar padi Anda.
                    </b-card-text>
                  </b-card-body>
                </b-col>
              </b-row>
            </b-card>
            </NuxtLink>
          </div>
          
          <div class="col-6">
            <NuxtLink to="/upload" class="link" style="text-decoration:none; color:black">
            <b-card no-body class="overflow-hidden" style="max-width: 540px;">
              <b-row no-gutters>
                <b-col md="6">
                  <b-card-img src="../../img/uploadphoto.jpg" alt="Upload_Photo" class="rounded-0"></b-card-img>
                </b-col>
                <b-col md="6">
                  <b-card-body title="Upload Gambar">
                    <b-card-text>
                      Upload gambar yang telah Anda simpan untuk diprediksi.
                    </b-card-text>
                  </b-card-body>
                </b-col>
              </b-row>
            </b-card>
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>
    <section class="contribution">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <b-card no-body class="overflow-hidden">
              <b-row no-gutters>
                <b-col xs="9">
                  <b-card-body title="Foto Gambar">
                    <b-card-text>
                      <p>Anda dapat membantu Paddyist mengembangkan penelitiannya. Caranya dengan mengirimkan beberapa gambar penyakit tanaman padi.</p>
                      <b-button href="#" variant="primary">
                        Upload Data
                      </b-button>
                    </b-card-text>
                  </b-card-body>
                </b-col>
                <b-col xs="3">
                  <b-card-img src="../../img/contribution.jpg" alt="Contribution" class="rounded-0"></b-card-img>
                </b-col>
              </b-row>
            </b-card>
          </div>
        </div>
      </div>
    </section>
    <section class="saran">
      <div class="container">
        <div class="row">
          <div class="col-12">
          <b-card no-body class="overflow-hidden">
              <b-row no-gutters>
                <b-col xs="3">
                  <b-card-img src="../../img/saran.jpg" alt="Saran" class="rounded-0"></b-card-img>
                </b-col>
                <b-col xs="8">
                  <b-card-body>
                    <b-card-text>
                      <h3>Paddyist perlu masukan Anda</h3>
                      <p>Kritik dan saran dari Anda sangat membantu kami agar berkembang menjadi lebih baik lagi.</p>
                      <b-button href="/saran" variant="primary">
                        Berikan Saran
                      </b-button>
                    </b-card-text>
                  </b-card-body>
                </b-col>
              </b-row>
          </b-card>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
// import 'vue-slick-carousel/dist/vue-slick-carousel.css'
export default {
  name: 'IndexPage',
  data() {
    return {
    }
  },
  async fetch() {
    await Promise.all([
      // this.$axios.get(`${this.$apiurl()}/hero`),
    ])
      .then((res) => {
        // this.dataBanner = res[0].data[0]
      })
      .catch((error) => {
        // eslint-disable-next-line no-console
        console.log(error.response)
      })
  },
}
</script>

<style lang="scss" scoped>
.predict {
  .card {
    margin-top:20px;
    margin-bottom:20px;
    border-radius: 8px;
  }

  .link{
    .b-card-body{
      text-decoration: none;
      color:black;
    }
  }
}

.contribution{
  margin-bottom:20px;
}

.saran{
  margin-bottom:20px;
}

.arrow-right{
  height:100%;
}
</style>
