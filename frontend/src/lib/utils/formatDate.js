export function formatDate(dateString) {
    // console.log(typeof(date))

    // Get the timezone offset in minutes, then convert it to milliseconds
    // var timezoneOffset = date.getTimezoneOffset() * 60000;

    // Adjust the date by subtracting the timezone offset
    //let adjustedDate = new Date(date.getTime() - timezoneOffset);
    //date = adjustedDate;

    // let day = date.getDate();
    // let month = date.getMonth() + 1; // Months are zero-based
    // let year = date.getFullYear();
    // let hours = date.getHours();
    // let minutes = date.getMinutes();

    // Pad single digit day and month values with a leading zero
    // day = day < 10 ? '0' + day : day;
    // month = month < 10 ? '0' + month : month;
    // hours = hours < 10 ? '0' + hours : hours;
    // minutes = minutes < 10 ? '0' + minutes : minutes;

    // return `${day}.${month}.${year} ${hours}:${minutes}`;
    
     const [datePart, timePart] = dateString.split('T');
      const [year, month, day] = datePart.split('-');
      const [hour, minute] = timePart.split(':');

      // Reassemble the date string in the desired format "%d.%m.%Y %H:%M"
      return `${day}.${month}.${year} ${hour}:${minute}`;
}
