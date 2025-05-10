let userName = "";
const options = {
  "-1": "Rock",
  "0": "Paper",
  "1": "Scissor"
};

function startGame() {
  const input = document.getElementById("name").value;
  if (!input.trim()) {
    alert("Please enter your name!");
    return;
  }
  userName = input;
  document.getElementById("nameInput").classList.add("hidden");
  document.getElementById("gameSection").classList.remove("hidden");
  document.getElementById("greeting").innerText = `Hello ${userName}, welcome to the game!`;
}

function showRules() {
  document.getElementById("rules").classList.toggle("hidden");
}

function play(userChoice) {
  const compChoice = [-1, 0, 1][Math.floor(Math.random() * 3)];
  document.getElementById("userChoice").innerText = `Your selection: ${options[userChoice]}`;
  document.getElementById("compChoice").innerText = `Computer selected: ${options[compChoice]}`;

  let outcome = "";

  if (userChoice === compChoice) {
    outcome = "Match Draw";
  } else if (
    (userChoice === -1 && compChoice === 1) ||
    (userChoice === 0 && compChoice === -1) ||
    (userChoice === 1 && compChoice === 0)
  ) {
    outcome = `You Won! Congratulations ${userName}!`;
  } else if (
    (userChoice === 0 && compChoice === 1) ||
    (userChoice === 1 && compChoice === -1) ||
    (userChoice === -1 && compChoice === 0)
  ) {
    outcome = `You Lost! Try again, ${userName}.`;
  } else {
    outcome = `Oops! Invalid move.`;
  }

  document.getElementById("outcome").innerText = outcome;
  document.getElementById("result").classList.remove("hidden");
}

function resetGame() {
  document.getElementById("result").classList.add("hidden");
  document.getElementById("userChoice").innerText = "";
  document.getElementById("compChoice").innerText = "";
  document.getElementById("outcome").innerText = "";
}
