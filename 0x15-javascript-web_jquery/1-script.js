// jquery
$(document).ready(function (){
    // use selector
    const element = $('header');

    // check if found
    if (element) {
        // use css to set colour
        element.css('color', '#FF0000');
    } else {
        console.error('Header element not found');
    }
});
