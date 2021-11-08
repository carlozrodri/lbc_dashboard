// Variable declaration
const amount1 = document.getElementById("amount-one");
const amount2 = document.getElementById("amount-two");
const theRate = document.getElementById("rate");

const average_ves_js = JSON.parse(document.getElementById('average_ves_js').textContent);
const average_uk_js = JSON.parse(document.getElementById('average_uk_js').textContent);
const averageuk2 = parseFloat(average_uk_js);
const averageves2 = parseFloat(average_ves_js);


// Fetch exchange rate from the API
function calculate() {
  const curr1 = parseFloat(amount1.value);

      const rate = curr1 / averageuk2
      const calculo = (rate * averageves2).toFixed(2)
      theRate.innerText = `${calculo}`;  // ${curr2}`;
    amount2.value = (rate * averageves2).toFixed(2);
  };

function calculate2() {
  const curr2 = parseFloat(amount2.value);
      const rate = curr2 / averageves2;
      const calculo = (rate * averageuk2).toFixed(2)
      theRate.innerText = `${calculo}`;  // ${curr2}`;
    amount1.value = (rate * averageuk2).toFixed(2);
  };
  
// Event  Listeners
amount1.addEventListener("input", calculate);
amount2.addEventListener("input", calculate2);
