/*
We are going to re-create our coin flip program now.  We should know how to code all of the logic already, but we haven't gone over inputs or random numbers.

INPUTS
For an input, we are going to create a "prompt". This is a dialogue box that will pop up on our screen to prompt the user for input. We can then store this prompt into a variable.

Copy and paste this program for the prompt to see how it works. Delete this when you're done.

Test Example 1

var person = prompt("Please enter your name", "Text goes here");

if (person != null) {
    console.log("Hello " + person + "! How are you today?");
}


RANDOM NUMBERS
Now for generating random numbers. This involves 2 functions in python. It looks more complicated than it is.

    Use Math.random() to generate a random decimal.
    Multiply that random decimal by 20.
    Use another function, Math.floor() to round the number down to its nearest whole number.

Copy and paste this program for the prompt to see how it works. Delete this when you're done.

Test Example 2

for (i = 0; i < 10; i++) {

   var num = Math.floor(Math.random() * 100)

   console.log(num);
}

This generates a random number from 1 to 100, ten times.

If you wanted to generate a random number from 1 to 20, you would make your statement look like this:

var num = Math.floor(Math.random() * 20)
*/


var flips = prompt("Please enter a number");

if (flips !== null) {
    console.log("Total coin flips: " + flips);
}

function coin_flip(num){
  var Hscore = 0;
  var Tscore = 0;
  for(i=0; i<=num;i++){
    var side = Math.floor(Math.random()*2);
    if(side == 1){
      Hscore++;
    }
    else{
      Tscore++;
    }
  }
  console.log('=====================');
 console.log('Heads: '+ Hscore , 'Tails: ' + Tscore);
 
  
}

(coin_flip(flips));







