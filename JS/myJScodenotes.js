// Create a variable and assign any number to it, divide it by 2 and round it down


let numberOfUsers = 7;
let result = Math.floor(numberOfUsers/2);
console.log(result);

// draw a random number from range [5,100]
//

let randomNumber = Math.floor(Math.random() * (100 - 5 + 1) + 5)
console.log(randomNumber);

// assign any email address to a variable and check if it contains the sign "@"


const emailAddress = "joannagojan@gmail.com"

function checkEmailAddress() {
    if (emailAddress.includes('@') === true) {
        console.log("Email address is correct")
    } else {
        console.log("Email address is incorrect")
    }
}

checkEmailAddress(emailAddress)

// assign a random number from [1,10] to a variable. Ask user to input a number from the same range, check if the numbers are the same

let compareUserInputAndRandomNumber = () => {
    let randomGeneratedNumber = Math.floor(Math.random() * (10 - 1 + 1) + 1);
    let userInputNumber = parseInt(prompt("Input number from 1 to 10"));
    if (randomGeneratedNumber === userInputNumber) {
        console.log("he numbers are the same");
    } else {
        console.log(`The numbers are different, user input: ${userInputNumber} and generated number: ${randomGeneratedNumber}`)
    }
}

compareUserInputAndRandomNumber()

//  Create a function rockPaperScissors(player1, player2)

let player1 = prompt("User 1 choose rock, paper or scissors");
let player2 = prompt("User 2 your turn");
try {    rockPaperScissors(player1, player2); }
catch (err) {
    console.log("Input correct name")
}
let rockPaperScissors = () => {
    if (player1 === "rock") {
        if (player2 === "paper") {
            console.log("User 2 you win");
        } else if (player2 === "scissors") {
            console.log("User 1 you win");
        } else {
            console.log("It's a draw");
        }
    } else if (player1 === "paper") {
        if (player2 === "rock") {
            console.log("User 1 you win");
        } else if (player2 === "scissors") {
            console.log("User 2 you win");(player1 === "paper")
        } else {
            console.log("It's a draw");
        }
    } else if (player1 === "scissors") {
        if (player2 === "rock") {
            console.log("User 2 you win");
        } else if (player2 === "paper") {
            console.log("User 1 you win");
        } else {
            console.log("It's a draw");
        }
    }
};

rockPaperScissors()

