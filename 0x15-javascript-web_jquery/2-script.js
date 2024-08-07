// script
$(document).ready(function (){

    // select div by id
    const redHeaderDiv = $('Div#red_header');

    // add an event handler
    redHeaderDiv.click(function() {
        // find the header
        const headerElement = $('header');

        // check if found
        if (headerElement) {
            // user css for colour
            headerElement.css('color', '#FF0000');
        } else {
            console.error('Header element not found');
        }
    });
});
