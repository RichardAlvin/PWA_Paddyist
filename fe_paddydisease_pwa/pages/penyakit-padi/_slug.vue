<template>
  <main class="site-main">
    <section class="detail">
      <div class="container">
        <div class="row" style="margin-bottom:20px;">
            <div class="col-8 col-md-10 col-sm-9">
                <h2>{{dataDisease.title}}</h2>
            </div>
            <div class="col-4 col-md-2 col-sm-3">
                <div>
                    <b-button href="/penyakit-padi" class="button-sm" variant="primary">Kembali</b-button>
                </div>
            </div>
        </div>
        <div class="row img-row" style="margin-bottom:20px;">
            <div class="col-12 m-auto">
                <div class="image-box">
                    <b-img :src="`../../img/paddy-disease/${dataDisease.image}.jpg`" fluid :alt="`${dataDisease.title}`"></b-img>
                </div>
            </div>
        </div>
        <p>PublishedAt: 22 April 2023</p>
        <p>Deskripsi:<br>{{dataDisease.body}}</p>
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
      dataDisease: []
    }
  },
  async fetch() {
    await this.$axios.get(`${this.$apiurl()}/disease/${this.$route.params.slug}`)
      .then((res) => {
        this.dataDisease = res.data
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
.detail{
    padding-top:25px;
}

@media only screen and (max-width: 600px) {
  h2{
    font-size: 20px;
  }

  .image-box{
    display: flex;
    justify-content: center;
  }

  .img-fluid{
    width:80%;
    text-align: center;
  }
}
</style>
