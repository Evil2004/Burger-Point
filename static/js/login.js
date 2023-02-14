console.log("login.js loaded")


function sendData () {
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value

    const data = {
        email: email,
        password: password
    }

    let userData = fetch("/login/", {
        method: "POST",
        credentials: "same-origin",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
        },
    })
        .then(response => {let data = response.json(); console.log(data);return data;})
        .then(response => {
            if (response.success === false){
                const error = document.getElementById("error text-danger d-none");
                error.innerHTML = response.error;
                error.style.color = "red";
                window.scrollTo(0, 0);
            } else {
                alert("Logged in successfully");
                const token = response.token;
                sessionStorage.setItem("token", token);
                window.location.href = "/";
            }
        });
}