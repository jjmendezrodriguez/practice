let firsCard = 2;
let secondCard = 8;
let sum = firsCard + secondCard;
let hasBlasckJack = false;
let isAlive = true;

if (sum <= 20) {
  console.log("Do you want to draw a new card? 🙂");
  isAlive = true;
} else if (sum === 21) {
  console.log("Wohoo! You've got Blackjack! 🥳");
  hasBlasckJack = true;
} else {
  console.log("You're out of the game! 😭");
  isAlive = false;
}
