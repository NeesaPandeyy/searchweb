// Ensure results container is displayed
if ({{ total_results|gt:0 }}) {
    document.querySelector('.results-container').style.display = 'block';
}

// Handle CSV download with existing search query
let download_btn = document.getElementById("id-download-button");
download_btn.addEventListener("click", function(event) {
    const queryString = window.location.search;

    // Update this to match your Django URL configuration
    window.location.href = `/download/${queryString}`;
});

// Optional: Disable download button if there are no results
if (!{{ total_results }}) {
    download_btn.disabled = true; // Disable the button if no results
    download_btn.title = "No results available for download"; // Tooltip for feedback
}
