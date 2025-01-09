document.getElementById('generateButton').addEventListener('click', async function () {
    let imageContainer = document.getElementById('imageContainer');
    imageContainer.innerHTML = `<p>Generating image...</p>`; // Feedback while loading

    try {
        // Step (a): Call PRNG Service to get a pseudo-random number
        let prngResponse = await fetch('/prng');
        let prngData = await prngResponse.json();
        let randomNumber = prngData.randomNumber ?? 0; // Default to 0 if undefined

        // Step (b): Use the random number to call the Image Service
        let imageResponse = await fetch(`/image/${randomNumber}`);
        let imageData = await imageResponse.json();
        let imagePath = imageData.imagePath ?? ''; // Default to empty if undefined

        if (imagePath) {
            // Step (c): Display the image
            imageContainer.innerHTML = `<img src="${imagePath}" alt="Random Image">`;
        } else {
            throw new Error('No image path returned from the server.');
        }
    } catch (error) {
        imageContainer.innerHTML = `<p class="error">Error loading image. Please try again.</p>`;
        console.error(error);
    }
});
