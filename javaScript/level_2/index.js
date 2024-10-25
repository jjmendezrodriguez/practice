let firsCard = 2;
let secondCard = 8;
let sum = firsCard + secondCard;
let hasBlasckJack = false;
let isAlive = true;
let message = "";

function startGame() {
  if (sum <= 20) {
    message = "Do you want to draw a new card? 🙂";
    isAlive = true;
  } else if (sum === 21) {
    message = "Wohoo! You've got Blackjack! 🥳";
    hasBlasckJack = true;
  } else {
    message = "You're out of the game! 😭";
    isAlive = false;
  }

  console.log(message);
}
