document.getElementById('generateButton').addEventListener('click', async function () {
    let imageContainer = document.getElementById('imageContainer');
    imageContainer.innerHTML = `<p>Generating image...</p>`;

    try {
        // Call the UI Service to generate the image
        let imagePath = await fetch('http://127.0.0.1:5000/generate', { method: 'POST' })
            .then(response => response.json())
            .then(data => data.imagePath);

        // Display the image
        imageContainer.innerHTML = `<img src="${imagePath}" alt="Random Image">`;
    } catch (error) {
        imageContainer.innerHTML = `<p style="color:red;">Error loading image. Please try again.</p>`;
        console.error(error);
    }
});
