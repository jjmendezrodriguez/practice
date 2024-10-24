// document.getElementById("count-el").innerText = 5;
// dec = declaras
// DOM = how use javaScript to modify a website
// utilisamos document para buscar un elemento en el DOM (Document Object Model)
let countEl = document.getElementById("count-el");
/* El .getElementById es buscar el elemento por su id ("id")
lo que este escrito en el id tiene que ser lo mismo que este en el HTML
en este ejemplo <h2 id="count-el">0</h2> */

// Un ejemplo de cambio de valor en una variable aqui comiensa el valor:
let count = 0;

// declaration of a funtion on .js:
// dec     name
function increment() {
  /* Funtion bady, programa lo que hace tu funcion cada vez que la llamas:
aqui llamas la variable y su nuevo valor imprime y le suma 1. */

  // count = count + 1
  // count += 1 otro metodo para subir o contar
  // metodo mas practico ver file practica1.js para explicacion.
  count++;
  /* como funciona
 variable.lee o modifica el texto que es. ver data type para otras opciones */
  countEl.innerText = count;
  // En este caso la variable count incrementa y luego imprime en la consola:
  console.log(count);
}
// 1. Grab the save-el paragrah and store it in a variable called saveEl
let saveEl = document.getElementById("save-el");

function save() {
  let countStr = count + " - ";
  saveEl.textContent += countStr;
  console.log(count);
}

function reset() {
  count = 0;
  document.getElementById("count-el").innerText = count;
}
