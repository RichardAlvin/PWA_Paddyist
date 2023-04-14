<template>
  <div class="container text-center">
    <div v-if="statusCode === 404" class="mb-24">
      <h1 class="m-0">404</h1>
      <p class="h2 text-primary">Maaf, halaman yang And cari tidak tersedia.</p>
    </div>
    <div v-else class="mb-24">
      <h1 class="m-0">500</h1>
      <p class="h2 text-primary">
        Maaf, saat ini sedang terjadi kesalahan basis data.
      </p>
    </div>
    <a class="btn--primary" href="/">Kembali ke Beranda</a>
  </div>
</template>

<script>
export default {
  layout: 'blank',
  props: {
    error: {
      type: Object,
      default: null,
    },
  },
  head() {
    return {
      title: this.error.statusCode,
    }
  },
  computed: {
    statusCode() {
      return (this.error && this.error.statusCode) || 500
    },
    message() {
      return this.error.message
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  padding: 60px 0;
  max-width: 590px !important;
}
h1 {
  font-size: 92px;
  font-weight: 900;
}
</style>
