document.getElementById('generateButton').addEventListener('click', async function () {
    let imageContainer = document.getElementById('imageContainer');
    imageContainer.innerHTML = `<p>Generating image...</p>`;

    try {
        // Step (a): Call PRNG Service to get a pseudo-random number
        let randomNumber = await fetch('http://127.0.0.1:5001/prng')
            .then(response => response.json())
            .then(data => data.randomNumber);

        // Step (b): Use the random number to call the Image Service
        let imagePath = await fetch(`http://127.0.0.1:5002/image/${randomNumber}`)
            .then(response => response.json())
            .then(data => data.imagePath);

        // Step (c): Display the image
        imageContainer.innerHTML = `<img src="http://127.0.0.1:5002/static/${imagePath}" alt="Random Image">`;
    } catch (error) {
        imageContainer.innerHTML = `<p style="color:red;">Error loading image. Please try again.</p>`;
        console.error(error);
    }
});
