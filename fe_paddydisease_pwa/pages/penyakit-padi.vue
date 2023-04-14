<template>
  <main class="site-main">
    <section class="hero">
      <div class="container">
        <h1>Penyakit Padi</h1>
        <p>Kumpulan Penyakit yang Menyerang Tanaman Padi</p>
      </div>
    </section>
    <section>
      <div class="container">
        <div class="row">
          <div v-for="(item,index) in dataDisease" :key="index" class="disease-box col-12 col-lg-3 col-md-4 col-sm-6">
            <b-card
              :title="item.title"
              :img-src="item.image"
              img-alt="Image"
              img-top
              tag="article"
              style="max-width: 20rem;"
              class="mb-2"
            >
              <b-card-text>
                {{ item.excerpt }}
              </b-card-text>

              <NuxtLink to="/detail" variant="primary">Detail</NuxtLink>
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
      dataDisease: []
    }
  },
  async fetch() {
      await this.$axios.get(`${this.$apiurl()}/disease`)
      .then((res) => {
        this.dataDisease = res
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
.hero{
  padding-top:25px;
}

.disease-box{
  display:flex;
  flex-direction: column;
  align-items: center;
}
</style>
