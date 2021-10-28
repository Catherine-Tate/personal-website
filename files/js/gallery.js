    

function hideImage() {
    document.getElementById("fullImage").style.display = "none";
}

function showImage(image) {
    document.getElementById("fullImage").style.display = "block";
    document.getElementById("bigPic").src=image.children[0].src
}
