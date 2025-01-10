document.getElementById('generateButton').addEventListener('click', async function () {
    let imageContainer = document.getElementById('imageContainer');
    imageContainer.innerHTML = `<p>Generating image...</p>`;

    try {
        // Step (a): Call PRNG Service to get a pseudo-random number
        let randomNumber = await fetch('/prng')
            .then(response => response.json())
            .then(data => data.randomNumber);

        // Step (b): Use the random number to call the Image Service
        let imagePath = await fetch(`/image/${randomNumber}`)
            .then(response => response.json())
            .then(data => data.imagePath);

        // Step (c): Display the image
        imageContainer.innerHTML = `<img src="${imagePath}" alt="Random Image">`;
    } catch (error) {
        imageContainer.innerHTML = `<p style="color:red;">Error loading image. Please try again.</p>`;
        console.error(error);
    }
});
