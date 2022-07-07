// date and time
const labelDate = document.querySelector('.date');

const currentDate = new Date()

const options = {
    // month: 'long',
    year: 'numeric',
}

labelDate.textContent = new Intl.DateTimeFormat(navigator.languages, options).format(currentDate);