export default (context, inject) => {
  const apiurl = () => {
    return process.env.API_URL
  }
  const catch404 = {
    statusCode: 404,
    message: 'Page Not Found',
  }
  const catch500 = {
    statusCode: 503,
    message: 'Error Code',
  }
  const months = {
    id: {
      short: 'Jan_Feb_Mar_Apr_Mei_Jun_Jul_Agt_Sep_Okt_Nov_Des'.split('_'),
      full: 'Januari_Februari_Maret_April_Mei_Juni_Juli_Agustus_September_Oktober_November_Desember'.split(
        '_'
      ),
    },
    en: {
      short: 'Jan_Feb_Mar_Apr_May_Jun_Jul_Agt_Sep_Oct_Nov_Dec'.split('_'),
      full: 'January_February_March_April_May_June_July_August_September_October_November_December'.split(
        '_'
      ),
    },
  }

  const days = {
    id: {
      short: 'Ming_Sen_Sel_Rab_Kam_Jum_Sab'.split('_'),
      full: 'Minggu_Senin_Selasa_Rabu_Kamis_Jumat_Sabtu'.split('_'),
    },
    en: {
      short: 'Sun_Mon_Tue_Wed_Thu_Fri_Sat'.split('_'),
      full: 'Sunday_Monday_Tuesday_Wednesday_Thursday_Friday_Saturday'.split(
        '_'
      ),
    },
  }

  const numPrefix = (num) => {
    let prefixed = num
    if (num < 10) {
      prefixed = '0' + num
    }

    return prefixed
  }

  const getMinute = (num) => {
    return Math.floor(num / 60)
  }

  const formatFullDate = (date, monthLenght = 'short', lang = 'id') => {
    const parseDate = new Date(date.replace(/-/g, '/'))
    const dates = parseDate.getDay()
    const day = parseDate.getDate()
    const month = parseDate.getMonth()
    const year = parseDate.getFullYear()

    const monthName = months[lang][monthLenght][month]
    const dateName = days[lang][monthLenght][dates]

    return `${dateName} , ${numPrefix(day)} ${monthName} ${year}`
  }

  const formatTime = (date = null) => {
    let parseDate
    if (date === null) {
      parseDate = new Date()
    } else {
      parseDate = new Date(date.replace(/-/g, '/'))
    }

    const hour = parseDate.getHours()
    const minutes = parseDate.getMinutes()

    return ` ${numPrefix(hour)} : ${numPrefix(minutes)}`
  }

  const formatDateNumber = (date) => {
    const parseDate = new Date(date.replace(/-/g, '/'))
    const day = parseDate.getDate()

    return `${numPrefix(day)}`
  }

  const formatCurrentDate = (
    date = null,
    monthLenght = 'full',
    lang = 'id'
  ) => {
    if (date != null && !(date instanceof Date)) {
      date = date.replace(/-/g, '/')
      date = date.replace(/T/g, ' ')
    }
    if (date == null) date = new Date()
    const parseDate = new Date(date)
    const day = parseDate.getDate()
    const month = parseDate.getMonth()
    const year = parseDate.getFullYear()

    const monthName = months[lang][monthLenght][month]

    return `${numPrefix(day)} ${monthName} ${year}`
  }

  inject('catch404', catch404)
  inject('catch500', catch500)
  inject('apiurl', apiurl)
  inject('getMinute', getMinute)
  inject('formatFullDate', formatFullDate)
  inject('formatTime', formatTime)
  inject('formatCurrentDate', formatCurrentDate)
  inject('formatDateNumber', formatDateNumber)
}
