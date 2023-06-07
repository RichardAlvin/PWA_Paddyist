<template>
  <div v-if="showPopup" class="pwa-popup shadow">
    <div class="flex flex-col flex-md-row h-center col-gap-12 row-gap-12">
      <div class="flex v-center h-center">
        <p v-if="isChrome" class="p-0 m-0">
          Pasang aplikasi ini di layar utama Anda untuk pengalaman yang lebih
          baik.
        </p>
        <p v-else class="p-0 m-0">
          Buka halaman ini dengan Chrome untuk menginstall aplikasi.
        </p>
      </div>
      <div v-if="isChrome" class="flex flex-row col-gap-12">
        <button
          class="btn btn--green full-width height-fit-content"
          @click="installApp"
        >
          Install
        </button>
        <button
          class="btn btn--ghost-dark-grey full-width height-fit-content"
          @click="dismissPopup"
        >
          Abaikan
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showPopup: true,
      deferredPrompt: null,
      isChrome: true,
    }
  },
  mounted() {
    if (
      window.matchMedia('(display-mode: standalone)').matches ||
      window.navigator.standalone
    ) {
      return
    }
    const isChrome =
      /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor)
    if (!isChrome) {
      this.isChrome = false
    }
    window.addEventListener('beforeinstallprompt', (event) => {
      event.preventDefault()
      this.deferredPrompt = event
    })
  },

  methods: {
    installApp() {
      this.deferredPrompt.prompt()
      this.deferredPrompt.userChoice.then(() => {
        this.deferredPrompt = null
        this.showPopup = false
      })
    },

    dismissPopup() {
      this.deferredPrompt = null
      this.showPopup = false
    },
  },
}
</script>

<style lang="scss" scoped>
.pwa-popup {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 1rem;
  background-color: lightgrey;
  box-shadow: 0 -4px 12px rgba(0, 0, 0, 0.15);
  z-index: 999;
}

.pwa-popup__content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.pwa-popup__message {
  margin: 0;
  font-size: 1rem;
  font-weight: 500;
}
.full-width {
  @media #{$medium} {
    width: fit-content;
  }
}
</style>