<template>
  <main class="site-main">
    <section class="predict">
      <div class="container">
        <div class="row">
          <div class="col-12 col-sm-6">
            <b-card no-body class="overflow-hidden" style="max-width: 540px;">
              <b-row no-gutters>
                <b-col md="6">
                  <b-card-img src="https://picsum.photos/400/400/?image=20" alt="Image" class="rounded-0"></b-card-img>
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
          </div>
          
          <div class="col-12 col-sm-6">
            <NuxtLink to="/upload" class="link">
            <b-card no-body class="overflow-hidden" style="max-width: 540px;">
              <b-row no-gutters>
                <b-col md="6">
                  <b-card-img src="https://picsum.photos/400/400/?image=20" alt="Image" class="rounded-0"></b-card-img>
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
                <b-col md="9">
                  <b-card-body title="Foto Gambar">
                    <b-card-text>
                      Aktifkan izin penggunaan kamera untuk mengambil gambar padi Anda.
                    </b-card-text>
                  </b-card-body>
                </b-col>
                <b-col md="3">
                  <b-card-img src="https://picsum.photos/400/400/?image=20" alt="Image" class="rounded-0"></b-card-img>
                </b-col>
              </b-row>
            </b-card>
          </div>
        </div>
      </div>
    </section>
    <section class="saran">
      <div class="container">
        <div class="card">
          <div class="row">
            <div class="col-2">
              <p>gambar</p>
            </div>
            <div class="col-9">
              <h3>Paddyist perlu masukan Anda</h3>
              <p>Kritik dan saran dari Anda sangat membantu kami agar berkembang menjadi lebih baik lagi.</p>
            </div>
            <div class="col-1">
              <b-button href="/saran" variant="primary">Go</b-button>
            </div>
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
  .card{
    padding: 6px 26px;
    border-radius: 8px;
  }
}
</style>
