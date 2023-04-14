<template>
  <nuxt-link
    :to="`artikel/${data.slug}`"
    class="article-card flex flex-col p-16"
  >
    <div class="image">
      <img :src="data.image" draggable="false" alt="image" />
    </div>
    <div class="description text-small">
      <p class="f-bold mb-0 mt-12">{{ data.title }}</p>
    </div>
  </nuxt-link>
</template>
<script>
export default {
  name: 'ArticleCardComponent',
  props: {
    data: {
      type: Object,
      default: () => {},
    },
  },
}
</script>
<style lang="scss" scoped>
.article-card {
  background: $white;
  color: $black80;
  border-radius: 8px;
  .image {
    width: 100%;
    overflow: hidden;
    min-height: 160px;
    border-radius: 8px;
    img {
      width: 100%;
      height: 160px;
      background: #cfcfcf;
      border-radius: 8px;
      object-fit: cover;
      object-position: center center;
    }
  }
  .description {
    p {
      font-size: 14px;
      overflow: hidden;
      text-overflow: ellipsis;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      line-clamp: 2;
      -webkit-box-orient: vertical;
    }
  }
}
</style>
