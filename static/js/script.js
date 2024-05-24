function displayResult(result)
    {
    const container = document.getElementById('result-container');
    container.innerHTML = ''; // Clear the existing content

    for (cont [key, value] of Object.entries(result))
    {
        const box = document.createElement('div');
        box.className = 'box';

        const title = document.createElement('h2');
        title.textContent = key.replace(/_/g, ' ').replace(/\b\w/g, char => char.toUpperCase());

        const content = document.createElement('p');
        content.textContent = value;

        box.appendChild(title);
        box.appendChild(content);
        container.appendChild(box);
    }

}

displayResult(result);