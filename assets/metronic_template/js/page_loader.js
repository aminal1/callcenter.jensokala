


        // Populate the page loading element dynamically.
    // Optionally you can skipt this part and place the HTML
    // code in the body element by refer to the above HTML code tab.

const loadingEl = document.createElement("div");
// document.body.prepend(loadingEl);
document.head.prepend(loadingEl);
loadingEl.classList.add("page-loader");
loadingEl.classList.add("flex-column");
loadingEl.innerHTML = `
    <span class="spinner-border text-primary" role="status"></span>
    <span class="text-muted fs-6 fw-semibold mt-5">Loading...</span>
`;
// Show page loading
KTApp.showPageLoading();
// Hide after 3 seconds
setTimeout(function() {
    KTApp.hidePageLoading();
    loadingEl.remove();
}, 3000);