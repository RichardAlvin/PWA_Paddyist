<template>
  <footer
    lazy-background="~assets/img/background-3.jpg"
    class="footer pv-48 bg-white"
  >
    <div class="container">
      <div class="flex flex-col flex-md-row f-space-between">
        <div class="flex col-gap-32">
          <div class="flex flex-col row-gap-12">
            <h1 class="mb-0">Kontak</h1>
            <a
              href="mailto: halosahabatpensiun@gmail.com"
              class="flex v-center col-gap-12"
            >
              <i class="i-mail text-black"></i>
              <span>richardalvinpratama06@gmail.com</span>
            </a>
            <a
              href="https://instagram.com/sahabat.pensiun"
              target="blank"
              class="flex v-center col-gap-12"
            >
              <i class="i-instagram text-black"></i>
              <span>Paddyist_TM</span>
            </a>
            <a href="#" class="flex v-center col-gap-12">
              <i class="i-facebook-square text-black"></i>
              <span>Paddyist_Research</span>
            </a>
          </div>
        </div>
        <div class="right pt-16">
          <div class="image">
            <img src="~assets/img/icon.png" alt="paddyist" />
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  name: 'FooterComponent',
  data() {
    return {}
  },
}
</script>
<style lang="scss" scoped>
.footer {
  background-repeat: no-repeat;
  background-position: left bottom;
  background-size: cover;
  a {
    color: $black80;
  }
  @media (max-width: 425px) {
    h1 {
      font-size: 18px;
      margin-top: 32px;
    }
  }
}

.image {
  img {
    width: 100%;
    max-width: 130px;
  }
}
.right {
  @media (max-width: 425px) {
    order: -1;
  }
}
</style>
