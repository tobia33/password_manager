let list = Array.from(document.querySelectorAll("main ul li a")).slice(1);
let next = document.querySelector("#next");
let previous = document.querySelector("#previous");


function nextPage(list){
    return function(){
        let page = document.querySelector("#page");
        if (page.textContent[0] === "1"){
            list[0].textContent = "undo";
            list[1].textContent = "redo";
            list[2].textContent = "delete";
            list[3].textContent = "add description";
            page.textContent = "2 / 2";
        }
        else if (page.textContent[0] === "2") {
            list[0].textContent = "add";
            list[1].textContent = "get";
            list[2].textContent = "show all";
            list[3].textContent = "help";
            page.textContent = "1 / 2";
        }
    };
}

next.addEventListener("click", nextPage(list));
previous.addEventListener("click", nextPage(list));
