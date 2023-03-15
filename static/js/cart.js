function incrementValue(item_id, price) {
  id = "number" + item_id;
  price_id = "item_price" + item_id;
  let value = parseInt(document.getElementById(id).value, 10);
  value = isNaN(value) ? 0 : value;
  if (value < 99) {
    value++;
    document.getElementById(id).value = value;
    document.getElementById(price_id).innerHTML = price * value + ".00";
  }
}

function decrementValue(item_id, price) {
  price_id = "item_price" + item_id;
  id = "number" + item_id;
  let value = parseInt(document.getElementById(id).value, 10);
  value = isNaN(value) ? 0 : value;
  if (value > 1) {
    value--;
    document.getElementById(id).value = value;
    document.getElementById(price_id).innerHTML = price * value + ".00";
  }
}

function removeCart(item_id) {
  const token = sessionStorage.getItem("token");
  const item = document.getElementById("item" + item_id);
  if (!token) {
    alert("Please login to remove items from cart");
    window.location.href = "/login/";
    return;
  } else {
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
          alert("Item removed from cart");
          location.reload();
        }
      });
  }
}

function order() {
  console.log("order() called");
  const items = document.getElementsByClassName("cart-item");
  const token = sessionStorage.getItem("token");
  if (items.length === 0) {
    alert("Cart is empty");
    return;
  }
  let json_data = { items: [] };
  for (let i = 0; i < items.length; i++) {
    let item_id = items[i].id.split("item")[1];
    let quantity = document.getElementById("number" + item_id).value;
    let item_cost = parseInt(
      document.getElementById("item_price" + item_id).innerHTML
    );
    console.log(item_id, quantity, item_cost);
    let data = {
      item_id: item_id,
      quantity: quantity,
      item_cost: item_cost,
    };
    json_data.items.push(data);
  }
  console.log(json_data);

  fetch("/order/", {
    method: "POST",
    credentials: "same-origin",
    body: JSON.stringify(json_data),
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
      } else {
        alert("Order placed successfully");
        location.reload();
      }
    });
}

function cookieValue(_cookieName) {
  const cookie = document.cookie;
  return cookie.split("=")[1];
}
