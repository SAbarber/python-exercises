/*

Fahrenheit and centigrade are two temperature scales in use today.  The Fahrenheit scale was developed by the German physicist Daniel  Gabriel Fahrenheit . In the Fahrenheit scale, water freezes at 32  degrees and boils at 212 degrees. 

The centigrade scale, which is also called the Celsius scale, was  developed by Swedish astronomer Andres Celsius. In the centigrade scale,  water freezes at 0 degrees and boils at 100 degrees. 

 Centigrade and Fahrenheit conversion formulas:
C = (5/9) * (F - 32)
F = (C × 1.8) + 32  

Sample Output:
60°C is 140°F.
45°F is 7.222222222222222°C.

Note:
Instead of document.write(), use console.log() in repl.it

To print the degrees symbol, use '\xB0' 

*/

function cToF(celsius) {
  // this is celsius to Fahrenheit
    var fah = (celsius * 1.8) + 32
    console.log(celsius + "°C is" , fah + '°F')
}

function fToC(fahrenheit) {
  // this is Fahrenheit to Celsius
    var cel = (5/9) * (fahrenheit - 32)
    console.log(fahrenheit + "°F is" , cel + '°C')
}
