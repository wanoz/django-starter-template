// Set eventlistener to check for click
document.addEventListener('click', eventHandling);

// Event handling function
function eventHandling(event) {
    var elemObj = document.getElementById(event.target.id);

    if (elemObj !== null) {
        // if (elemObj.type === "button"){
        //     var ind = elemObj.classList.contains("button_red_selected")
            
        //     if (ind === false){
        //         elemObj.classList.add("button_red_selected");
        //     } else {
        //         elemObj.classList.remove("button_red_selected");
        //     }           
        // }
    }
}

function loadStatus(){
    document.getElementById('button_primary').textContent = 'Processing...';
    document.getElementById('button_primary').classList.remove('btn_primary');
    document.getElementById('button_primary').classList.add('btn_timeout');
}

