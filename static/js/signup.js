

function sendData(event) {
  console.log("sendData() called");
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

  }
  
  let userData = fetch("/register/", {
    method: "POST",
    credentials: "same-origin",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
  })
    .then(response => {let data = response.json(); console.log(data);return data;})
    .catch(error => console.log(error))
    .then(response => {
      console.log(response.success)
      if (response.success === false){
        const error = document.getElementById("error text-danger d-none");
        error.innerHTML = response.error;
        error.style.color = "red";
        window.scrollTo(0, 0);
      } else {
        alert("Account created successfully");
        const token = response.token;
        sessionStorage.setItem("token", token);
        window.location.href = "/";
      }
    }) 
    .catch(error => console.log(error));
}



function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    let cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue; 
}