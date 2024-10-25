// condicionales or conditionals
// las condicionales trabajan con resultados boolean True or False
// sintacsis:
//   logica = lo que escribes dentro de (parentesis)
if (sum < 21) {
  // si tu logica se cumple: True = ejecuta lo que esta dentro de las {llaves}
  console.log("Do you want to draw a new card? 🙂");
  // si es False, puedes tener un else if es otra logica en caso de la primera es False
} else if (sum === 21) {
  console.log("Wohoo! You've got Blackjack! 🥳");
} else if (sum > 21) {
  console.log("You're out of the game! 😭");
}
