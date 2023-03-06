console.log("login.js loaded");

const error = document.getElementById("error");
error.style.display = "none";
function sendData() {
  console.log("sendData() called");
  const token = sessionStorage.getItem("token");
  //   if token is not null, then user is already logged in
  if (token) {
    alert("You are already logged in");
    window.location.href = "/";
    return;
  } else {
    const form = document.querySelector(".lg-frm");
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    // alert(data);

    //  send the data to the server
    const serverResponse = fetch("/login/", {
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
        console.log(data);
        return data;
      })
      .catch((error) => console.log(error))
      .then((response) => {
        console.log(response.success);
        console.log(response.error);
        if (response.success === false) {
          error.style.display = "block";
          error.innerHTML = response.error;
          error.style.color = "red";
          window.scrollTo(0, 0);
        } else {
          alert("Login successful");
          const token = response.token;
          sessionStorage.setItem("token", token);
          window.location.href = "/";
        }
      });
  }
}

function cookieValue(_cookieName) {
  const cookie = document.cookie;
  return cookie.split("=")[1];
}
