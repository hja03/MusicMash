function isSecondUser() {
    if (window.location.href.includes("?login=2")) {
        document.getElementById("login-title").innerHTML = "Log In Again";
    }
}