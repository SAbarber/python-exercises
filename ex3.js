/*
Complete the following and name your functions accordingly:

1. create a Regular Expression to test whether a 5 digit zipcode is valid or not. (check that it's numbers only)

function zipCode(str)

2. create a Regular Expression to check if there's a whitespace in a string

function whiteSpace(str)

3. Check if a social security number is valid. The format for a SSN is  
XXX-XX-XXXX

function socialSecurityNumber(str)
*/

function zipCode(str){
  var zip = (/^[0-9]{5}$/);
  var x = zip.test(str);
  return x;
}
console.log(zipCode(74055));


function whiteSpace(str){
  var space = (/(\s)/);
  var check = space.test(str);
  return check;
}
console.log(whiteSpace("hello world"));


function socialSecurityNumber(str){
  var num =/^\d{3}-\d{2}-\d{4}$/;
  //var num = /^[0-9]{3}\-?[0-9]{2}\-?[0-9]{4}$/;
  return num.test(str);
}
console.log(socialSecurityNumber(444-22-3333));
