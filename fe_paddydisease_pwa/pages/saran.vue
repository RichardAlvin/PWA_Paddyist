<template>
  <main class="site-main">
    <section class="saran">
      <div class="container">
          <div>
            <h3>Saran dan Kritik</h3>
            <b-form v-if="show" @submit="onSubmit" @reset="onReset">
              <b-form-group
                  id="input-group-1"
                  label="Alamat Email:"
                  label-for="input-1"
                  description="Kami tidak akan menyebarkan email Anda ke orang lain."
              >
                  <b-form-input
                  id="input-1"
                  v-model="form.email"
                  type="email"
                  placeholder="Masukkan Email"
                  required
                  ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-2" label="Nama Anda:" label-for="input-2">
                  <b-form-input
                  id="input-2"
                  v-model="form.name"
                  placeholder="Masukkan Nama"
                  required
                  ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-3" label="Saran Anda:" label-for="input-2">
                <b-form-textarea
                id="input-3"
                v-model="form.saran"
                placeholder="Masukkan Saran Anda"
                required
                ></b-form-textarea>
              </b-form-group>

              <b-button type="submit" variant="primary">Submit</b-button>
              <b-button type="reset" variant="danger">Reset</b-button>
            </b-form>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
export default {
    data() {
      return {
        form: {
          email: '',
          name: '',
          saran: ''
        },
        show: true
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        alert(JSON.stringify(this.form))
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.name = ''
        this.form.saran = ''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>

<style lang="scss" scoped>
.saran{
    padding-top:25px;
    margin-bottom:25px;
}
</style>
