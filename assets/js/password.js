
document.addEventListener("submit", function (event) {
  const form = event.target;

  if (form.id !== "password-form") return;

  event.preventDefault();

  const passwords = {
    "おうち": "7159",
    "３１か１": "7210",
    "おと４１れた": "7236",
    "４ゅんかん": "7251",
    "３つじん": "7289",
    "せ１ぎ": "7305",
    "プップ": "7323",
    "コ１ン": "7364"
  };

  const input = form.querySelector("#password-input");
  const error = document.getElementById("password-error");
  const targetPage = passwords[input.value];

  if (targetPage) {
    window.location.href = "/?p=" + targetPage;
  } else if (error) {
    error.hidden = false;
  }
});
