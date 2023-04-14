<template>
  <nuxt-link
    :to="`acara/${data.slug}`"
    class="event-card flex flex-col p-16 shadow"
  >
    <div class="image">
      <span>{{ data.category }}</span>
      <img :src="data.image_url" draggable="false" alt="image" />
    </div>
    <div class="description flex flex-col row-gap-12 text-small">
      <p class="f-bold mb-0 mt-12">{{ data.title }}</p>
      <div class="flex flex-col row-gap-8">
        <div>
          <i class="i-calendar1 mr-8"></i> <span>{{ data.date }}</span>
        </div>
        <div class="flex flex-row">
          <i class="i-map-marker-ghost mr-8"></i>
          <span class="location">{{ data.location }}</span>
        </div>
      </div>
    </div>
  </nuxt-link>
</template>
<script>
export default {
  name: 'EventCardComponent',
  props: {
    data: {
      type: Object,
      default: () => {},
    },
  },
}
</script>
<style lang="scss" scoped>
.event-card {
  width: 100%;
  max-width: 220px;
  background: $white;
  color: $black80;
  border-radius: 8px;
  .image {
    width: 100%;
    overflow: hidden;
    position: relative;
    span {
      color: $white;
      padding: 6px 18px;
      border-radius: 8px;
      position: absolute;
      background-color: rgba($color: $yellow, $alpha: 0.8);
      left: 12px;
      top: 12px;
    }
    img {
      width: 260px;
      height: 130px;
      border-radius: 8px;
      object-fit: cover;
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
  .location {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 1;
    line-clamp: 1;
  }
}
</style>
