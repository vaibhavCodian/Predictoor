// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");


function set_data(img, data){
    data = data.replace("b&#39;", "") //to get rid of start curly brace code 
    data = data.replace("&#39;", "")  //to get rid of end curly bracecode 
    document.getElementById(img).src = "data:image/png;base64,"+data; // set src
    console.log("1")
}
    console.log("________jdjd")