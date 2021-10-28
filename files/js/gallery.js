    

function hideImage() {
    document.getElementById("fullImage").style.display = "none";
}

function showImage(image) {
	console.log(image.id)
    var bigFrame = document.getElementById("fullImage")
    bigFrame.style.display = "block";
    document.getElementById("bigPic").src=image.children[0].src;
    var bgc = getComputedStyle(image)
    bigFrame.style.backgroundColor = bgc.backgroundColor;

}
