console.log('hola');

// Variable declaration
const c1 = document.getElementById("currency-one");
const c2 = document.getElementById("currency-two");
const amount1 = document.getElementById("amount-one");
const amount2 = document.getElementById("amount-two");
const swap = document.getElementById("swap");
const theRate = document.getElementById("rate");
const valoruk = document.getElementById("valor_uk")
console.log(valoruk);

// Fetch exchange rate from the API
function calculate() {
  const curr1 = c1.value;
  const curr2 = c2.value;
  fetch(
    `https://v6.exchangerate-api.com/v6/4e8e090e24492cb8d5f48c90/latest/${curr1}`
  )
    .then((res) => res.json())
    .then((data) => {
      // console.log(data);
      // Updating the data
      const rate = data.conversion_rates[curr2];
      theRate.innerText = `1 ${curr1} = ${rate} ${curr2}`;
      amount2.value = (amount1.value * rate).toFixed(2);
    });
}

// Event  Listeners
c1.addEventListener("change", calculate);
amount1.addEventListener("input", calculate);
c2.addEventListener("change", calculate);
amount2.addEventListener("input", calculate);
swap.addEventListener("click", () => {
  const flash = c1.value;
  c1.value = c2.value;
  c2.value = flash;
  calculate();
});