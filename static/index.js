const button = document.querySelector("#continue-button");

button.addEventListener('click', () => {
    window.location.replace("/auth/redirect");
});