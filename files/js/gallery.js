    

function hideImage() {
    document.getElementById("fullImage").style.display = "none";
}

function showImage(image) {
	var bigPic = image.children[0]
    var bigFrame = document.getElementById("fullImage")
    bigFrame.style.display = "block";
    document.getElementById("bigPic").src=bigPic.src;
    var bgc = getComputedStyle(image)
    bigFrame.style.backgroundColor = bgc.backgroundColor;
    bigPic.style.backgroundColor = ""

}
