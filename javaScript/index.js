// document.getElementById("count-el").innerText = 5;
// dec = declaras
// declaration of a funtion on .js:
// dec     name
let countEl = document.getElementById("count-el");
let count = 0;

function increment() {
  // funtion bady, programa lo que hace tu funcion cada vez que la llamas:
  // imprime un count y lo suma
  count = count + 1;
  console.log(count);
}
