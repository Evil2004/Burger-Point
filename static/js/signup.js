function sendData(event) {
  const token = sessionStorage.getItem("token");
  const error = document.getElementById("error text-danger d-none");
  error.style.display = "none";
  if (token) {
    alert("You are already logged in");
    window.location.href = "/";
    return;
  } else {
    data = {
      first_name: document.getElementById("first_name").value,
      last_name: document.getElementById("last_name").value,
      email: document.getElementById("email").value,
      password: document.getElementById("password").value,
      confirm_password: document.getElementById("confirm_password").value,
      address: document.getElementById("address").value,
      phone: document.getElementById("phone").value,
      city: document.getElementById("city").value,
      state: document.getElementById("state").value,
      pin: document.getElementById("pin").value,
    };

    let userData = fetch("/register/", {
      method: "POST",
      credentials: "same-origin",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": cookieValue("csrftoken"),
      },
    })
      .then((response) => {
        let data = response.json();

        return data;
      })
      .catch((error) => console.log(error))
      .then((response) => {
        console.log(response.success);
        if (response.success === false) {
          error.innerHTML = response.error;
          error.style.display = "block";
          error.style.color = "red";
          window.scrollTo(0, 0);
        } else {
          alert("Account created successfully");
          const token = response.token;
          sessionStorage.setItem("token", token);
          window.location.href = "/";
        }
      })
      .catch((error) => console.log(error));
  }
}

function cookieValue(_cookieName) {
  const cookie = document.cookie;
  return cookie.split("=")[1];
}
