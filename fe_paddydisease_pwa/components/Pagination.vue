<template>
  <div class="flex h-center col-gap-16 mt-12">
    <div class="flex col-gap-8">
      <button
        class="pv-4 ph-6"
        :class="currentPage > 1 ? 'btn--primary' : 'btn--grey'"
        @click="$emit('first-page')"
      >
        <i class="i-angle-left"></i><i class="i-angle-left"></i>
      </button>
      <button
        class="pv-4 ph-6"
        :class="currentPage > 1 ? 'btn--primary' : 'btn--grey'"
        @click="$emit('previous-page')"
      >
        <i class="i-angle-left"></i>
      </button>
    </div>
    <input
      id="page"
      :value="currentPage"
      class="form-input page-input p-0"
      type="number"
      name="page"
      min="1"
      :max="totalPages"
      @keyup.enter="
        $emit('input-page', baseLink + $event.target.value.toString(), addInput)
      "
    />
    <span class="f-18 text-grey">/</span>
    <span class="f-18 text-grey">{{ totalPages }}</span>
    <div class="flex col-gap-8">
      <button
        class="pv-4 ph-6"
        :class="currentPage < totalPages ? 'btn--primary' : 'btn--grey'"
        @click="$emit('next-page')"
      >
        <i class="i-angle-right"></i>
      </button>
      <button
        class="pv-4 ph-6"
        :class="currentPage == totalPages ? 'btn--grey' : 'btn--primary'"
        @click="$emit('last-page')"
      >
        <i class="i-angle-right"></i><i class="i-angle-right"></i>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PaginationComponent',
  props: {
    currentPage: {
      type: Number,
      default: 1,
    },
    totalPages: {
      type: Number,
      default: 1,
    },
    baseLink: {
      type: String,
      default: '',
    },
    addInput: {
      type: String,
      default: '',
    },
  },
}
</script>
<style lang="scss" scoped>
.page-input {
  width: 2.5em;
  text-align: center;
  vertical-align: middle;
}
</style>
