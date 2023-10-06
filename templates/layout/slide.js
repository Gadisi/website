<script>
document.addEventListener("DOMContentLoaded", function () {
    const imageUrls = [
        {% for i in range(1, 32) %}
            "{{ url_for('static', filename='images/gallery/image_' + i|string + '.jpg') }}",
        {% endfor %}
    ];
    let modalImage = document.getElementById('galleryImage');
    let currentIndex = 0;

    const loadedImages = imageUrls.map((url) => {
        const img = new Image();
        img.src = url;
        img.className = "img-fluid";
        img.style.visibility = "hidden";
        img.alt = "GadisiFoundation";

        return img;
    })

   function getRandomIndex(max) {
            return Math.floor(Math.random() * max);
        }
    // Function to show the next image in the slideshow
    function showNextImage() {
        const nextIndex = getRandomIndex(imageUrls.length);

        // Check if the image has already been loaded successfully
        if (loadedImages[nextIndex] && loadedImages[nextIndex].complete && loadedImages[nextIndex].src.trim() !== "") {

            modalImage.innerHTML = '';
            const img = loadedImages[nextIndex];
            modalImage.appendChild(img);
            img.style.animationDuration = "3s";
            img.style.animationDelay = "0.5s";
            {#img.style.animationName = "fadeInRightBig";#}
            img.style.visibility = "visible";

            currentIndex++;
        }
    }

    // Start the automatic slideshow
    setInterval(showNextImage, 3600); // Change image every 3 seconds (adjust the interval as needed)
});
</script>