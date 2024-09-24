
{% if results %}
    document.querySelector('.results-container').style.display = 'block';
{% endif %}

// Handle CSV download with existing search query
let download_btn = document.getElementById("id-download-button");
download_btn.addEventListener("click", function(event) {
    const queryString = window.location.search;
    window.location.href = `http://127.0.0.1:5000/download${queryString}`;
});
