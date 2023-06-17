$(document).ready(function() {
    const spans = document.querySelectorAll('#price')
    spans.forEach(span => {
        $(span).text( $(span).text().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,") );
    });
   
    // $("#mydiv").html(mynumber.toLocaleString("en"));
});

 

