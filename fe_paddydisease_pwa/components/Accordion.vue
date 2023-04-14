<template>
  <li @click="show">
    <div class="title">
      <div class="text-title" :class="{ 'text-title--open': isShow }">
        {{ title }}
      </div>
      <div
        class="bzi-angle-down arrow-box"
        :class="{ 'arrow-box--open': isShow }"
      ></div>
    </div>
    <div v-show="isShow" class="item">
      <!-- eslint-disable-next-line vue/no-v-html -->
      <div class="p-0 m-0" v-html="description"></div>
    </div>
  </li>
</template>
<script>
export default {
  name: 'AccordionComponent',
  props: {
    title: {
      type: String,
      default: '',
    },
    description: {
      type: String,
      default: '',
    },
    active: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      isShow: false,
    }
  },
  mounted() {
    if (this.active) this.isShow = this.active
  },
  methods: {
    show() {
      this.isShow = !this.isShow
    },
  },
}
</script>
<style lang="scss" scoped>
li {
  background: #fff;
  margin-bottom: 20px;
  list-style: none;
  cursor: pointer;
  -moz-box-shadow: 0px 3px 5px #929292;
  -webkit-box-shadow: 0px 3px 5px #929292;
  box-shadow: 0px 2px 3px rgba(#929292, 0.3);
  border-radius: 10px;

  .title {
    position: relative;
    height: auto;
    padding: 20px 20px;
    display: flex;
    align-items: center;

    .arrow-box {
      position: absolute;
      right: 20px;
      transition: 0.3s ease-in-out;
      font-size: 20px;
      font-weight: bold;
      color: #243545;
    }

    .arrow-box--open {
      -webkit-transform: rotate(180deg);
      -moz-transform: rotate(180deg);
      transform: rotate(180deg);
      color: $primary;
    }

    .text-title {
      font-weight: bold;
      font-size: 18px;
      color: #243545;
    }

    .text-title--open {
      color: $primary;
    }
  }
  .item {
    overflow: hidden;
    height: auto;
    padding: 20px 20px 20px 20px;
    border-top: solid 2px #e6ecec;
    font-size: 14px;
  }
}
</style>
