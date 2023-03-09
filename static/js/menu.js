function addCart(id) {
  console.log("addCart() called");

  const token = sessionStorage.getItem("token");

  if (!token) {
    alert("Please login to add items to cart");
    window.location.href = "/login/";
    return;
  } else {
    let data = {
      item_id: id,
    };
    fetch("/add_to_cart/", {
      method: "POST",
      credentials: "same-origin",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": cookieValue("csrftoken"),
        authorization: `Bearer ${token}`,
      },
    })
      .then((response) => {
        let data = response.json();
        return data;
      })
      .then((response) => {
        if (response.success === false) {
          alert(response.error);
        }
      });
  }
}
// function parseJwt(token) {
//   var base64Url = token.split(".")[1];
//   var base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
//   var jsonPayload = decodeURIComponent(
//     window
//       .atob(base64)
//       .split("")
//       .map(function (c) {
//         return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
//       })
//       .join("")
//   );

//   return JSON.parse(jsonPayload);
// }

function cookieValue(_cookieName) {
  const cookie = document.cookie;
  return cookie.split("=")[1];
}