document.addEventListener('DOMContentLoaded', function () {
    for (const dt of document.querySelectorAll('.local-time')) {
        const utcTime = moment.utc(dt.innerHTML, 'YYYY-MM-DD').toDate();
        dt.innerHTML = moment(utcTime).local().format('DD.MM.YYYY HH:mm');
    }
});