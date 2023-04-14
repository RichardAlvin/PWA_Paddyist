<template>
  <div lazy-background="~assets/img/background-1.jpg" class="blank-layout">
    <nuxt />
  </div>
</template>

<style lang="scss">
#__nuxt,
#__layout,
.blank-layout {
  height: 100%;
}
</style>

<style lang="scss" scoped>
.blank-layout {
  background-repeat: no-repeat;
  background-position: center bottom;
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;

  .site-main {
    padding: 0;
  }
}

.bg-img {
  position: absolute;
  top: 0;
  left: 0;
}
</style>
