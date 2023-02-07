function flipCard(id) {
    var x = document.getElementById("flashCard" + id);
    if (x.classList.contains("flip-card-click")){
        x.classList.remove("flip-card-click")
    }
    else if (!x.classList.contains("flip-card-click")){
        x.classList.add("flip-card-click")
    }
    //console.log("The button is calling this function")
}

;(function(){
    const container = document.getElementById("modal")
    const modal = new bootstrap.Modal(container)
    
    htmx.on("htmx:afterSwap", (e) => {
        //console.log("Showing modal")
        // Response targeting #dialog => show the modal
        if (e.detail.target.id === "dialog") {
            modal.show()
        }
        
    })

    htmx.on("htmx:beforeSwap", (e) => {
        // Empty response targeting #dialog => hide the modal
        //console.log("Trying to hide")
        
        if (e.detail.target.id == "dialog" && !e.detail.xhr.response) {
            modal.hide()
            e.detail.shouldSwap = false
        }
        
    })
    
    //empty the dialog. Flush the content of the dialog after the fade transition
    htmx.on("hidden.bs.modal", () => {
        document.getElementById("dialog").innerHTML = ""
    })

})()



