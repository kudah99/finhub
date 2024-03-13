window.addEventListener('load', (event) => {
    console.log("search_bar component is fully loaded");
});
function tabs() {
    return {
        active: 1,
        isActive(tab) {
            return tab == this.active;
        },
    }
}

setActive(value) {
    this.active = value;
}