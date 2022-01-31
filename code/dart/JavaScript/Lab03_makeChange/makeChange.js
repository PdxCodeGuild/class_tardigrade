const form = document.querySelector("form");

form.addEventListener("submit", function (evt) {
  evt.preventDefault();
  const totalInput = parseFloat(document.getElementById("totalInput").value);
  const ttlCents = parseInt(totalInput * 100);

  quarters = Math.floor(ttlCents / 25);
  dimes = Math.floor((ttlCents % 25) / 10);
  nickels = Math.floor(((ttlCents % 25) % 10) / 5);
  pennies = Math.floor(ttlCents % 5);

  const result = document.getElementById("result");
  result.innerText = `$${totalInput} equates to\nQuarters: ${quarters}\nDimes: ${dimes}\nNickels: ${nickels}\nPennies: ${pennies}`;
});