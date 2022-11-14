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


// Create an array with numbers and calculate an arithmetic average of the numbers inside the array

const numbers = [1,2,3,4,5,6,7]
let arithmetic_average = (numbers) => {
    let sum_number = 0;
    let number_counter = 0;
    numbers.forEach(function (number) {
        sum_number += number;
        number_counter++;
    });
    let arithmetic_average_result = sum_number / number_counter;
    return arithmetic_average_result;
};


console.log(arithmetic_average(numbers));

// Create an array containing names of cities, return and display in the terminal an array with the letter count of every city
//e.g.
// ```JavaScript
// const cities = ["Kraków", "Olsztyn", "Szczecin", "Ostrów Wielkopolski"];
// ```
// The result
//
// ```JavaScript
// [6, 7, 8, 19];
// ```

const cities = ["Canggu", "Bangkok", "Phuket", "Ubud", "Koh Phangan"]
console.log(cities);
const letterCounter = (citiesArray) => {
    console.log(cities);
    return citiesArray.map(function (city) {
            let characterCounter = 0;
            for (let character of city) {
                if (character !== " ") {
                    characterCounter++;
                }
            }
            return characterCounter
        }
    )
};
console.log(letterCounter(cities));

// Write a function that will return only negative numbers from an array


const numbers = [4, -5, 0, 2, -67, 8, 10, -34 ];
const getNegativeNumbers = (function (numbers){
    const onlyNegative = numbers.filter(function (number) {
        return Math.abs(number) !== number;
    })
    return onlyNegative
});

console.log(getNegativeNumbers(numbers));


// Based on years in an array, calculated the ages

const years = [1995, 1856, 2014, 1987, 2022];
const calculateAge = (years) => {
    const calculatedAge = years.map(function (birthYear){
        let currentYear = new Date().getFullYear();
        return currentYear - birthYear
    });
    return calculatedAge
};

console.log(calculateAge(years));


// Create a function getSecondMaxNumber(array). The function should return the second biggest number
// e.g.
// ```JavaScript
// const numbers = [2, 3, 1, 6, 100, 49, 5, 7, 8, 9 ];
// console.log(getSecondMaxNumber(numbers));
//

const numbers = [2, 3, 50, 1, 6, 100, 49, 5, 7, 8, 9 ];
const getSecondMaxNumber = (array) => {
   const sortArraySmallestToBiggest = array.sort(function (a,b) {
        return a - b
    });
    return array[array.length - 2];
};

console.log(getSecondMaxNumber(numbers))

// Create a variable with an array "names1" containing names
// Then display in the terminal second element, fifth element, length of the array
// Define an empty array in a variable "names2", and one by one add 6 names to the array
// Then display in the terminal the first element, the third element and the length of the array



const names1 = ["Joonho", "Khoa", "Reira", "Claudio", "Adrian"]
console.log(`Second name of first array: ${names1[1]}, Fifth name of first array: ${names1[4]}, the length of first array: ${names1.length}`);

names2 = []
names2.push("Jay");
names2.push("Pagan");
names2.push("Joanna");
names2.push("Aga");
names2.push("Syadza");


console.log(`First name of second array: ${names2[0]}, third name of second array: ${names2[2]}, the length of second array: ${names2.length}`);


//Create a multidimensional array - 3 rows and 4 columns in a variable "arrayOfNumbers"
//e.g.
// 1,2,3,4
// 5,6,7,8
// 9,10,11,12
// Display in the terminal: the second element of the first row, the second row and the length of the third element of the first row
//Create a multi-dimensional array in a variable "mixedArray" and in the first row it should contain an array with containing names and the second array should contain integers
// Display in the terminal: third element of the first row, fifth element of the first row and the length element of the first row

const arrayOfNumbers = [[1,2,3,4], [5,6,7,8], [9,10,11,12]];
console.log(`Second element of first row: ${arrayOfNumbers[0][1]}, whole second row: ${arrayOfNumbers[1]}, the length of the third row ${arrayOfNumbers[2].length}`)

const mixedArray = [["Joonho", "Khoa", "Reira"], [1, 2, 3, 4, 5, 6]]
console.log(`Third elements of the first row: ${mixedArray[0][2]}, fifth element of the first row: ${mixedArray[0][4]}, the length of the second element of the first row ${mixedArray[0][1].length}`)