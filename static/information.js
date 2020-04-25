
var search = function(){
    var text = document.getElementById("search-input").value;
    const titles = document.getElementsByClassName("information-title");
    for(i=0;i<titles.length;i++){
        if(titles[i].textContent.includes(text) && text!=""){
            titles[i].parentNode.style.display = "block";
        }else if(text==""){
            titles[i].parentNode.style.display = "block";
        }else{
            titles[i].parentNode.style.display = "none";
        }
    }
} 