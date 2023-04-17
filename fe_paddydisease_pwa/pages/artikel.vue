<template>
  <main class="site-main">
    <section class="hero">
      <div class="container">
        <h1>Paddyist Artikel</h1>
        <p>Artikel Seputar Pertanian Tersedia Disini</p>
      </div>
    </section>
    <section>
      <div class="container">
        <div class="row">
          <div class="col-md-3 col-sm-4 col-6">
            <div>
              <b-card
                title="Card Title"
                img-src="https://picsum.photos/600/300/?image=25"
                img-alt="Image"
                img-top
                tag="article"
                style="max-width: 20rem;"
                class="mb-2"
              >
                <b-button href="/detail" variant="primary">Go somewhere</b-button>
              </b-card>
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
.hero{
  padding-top:25px;
}
</style>
