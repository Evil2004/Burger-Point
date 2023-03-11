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
        const addId = "addCartBtn" + id;
        const removeId = "removeCartBtn" + id;
        const addBtn = document.getElementById(addId);
        const removeBtn = document.getElementById(removeId);
        if (response.added === false && response.in_cart === true) {
          addBtn.style.display = "none";
          removeBtn.style.display = "block";
          alert(response.error);
        } else if (response.added === false) {
          alert(response.error);
        } else {
          addBtn.style.display = "none";
          removeBtn.style.display = "block";
          alert("Item added to cart");
        }
      });
  }
}

function removeCart(item_id) {
  const token = sessionStorage.getItem("token");

  if (!token) {
    alert("Please login to remove items from cart");
    window.location.href = "/login/";
    return;
  } else {
    const addId = "addCartBtn" + item_id;
    const removeId = "removeCartBtn" + item_id;
    const addBtn = document.getElementById(addId);
    const removeBtn = document.getElementById(removeId);
    let data = {
      item_id: item_id,
    };
    fetch("/remove_from_cart/", {
      method: "DELETE",
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
        if (response.removed === false) {
          alert(response.error);
        } else {
          addBtn.style.display = "block";
          removeBtn.style.display = "none";
          alert("Item removed from cart");
        }
      });
  }
}

function cookieValue(_cookieName) {
  const cookie = document.cookie;
  return cookie.split("=")[1];
}
