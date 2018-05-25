/*
There is a game in which you try not to repeat a word while your opponent tries to see if you have repeated one.

"THE RAIN IN SPAIN" has no repeats.

"IN THE RAIN AND THE SNOW" repeats THE.

"THE RAIN IN SPAIN IN THE PLAIN" repeats THE and IN.

Write a program to test a phrase.

Input
Input is a line containing words separated by single spaces, where a word consists of one or more uppercase letters. A line  contains no more than 80 characters.

Output
The output is "yes" if no word is repeated, and "no" if one or more words repeat.

Sample Input 1   
THE RAIN IN SPAIN

Sample Output 1
yes

Sample Input 2    
IN THE RAIN AND THE SNOW

Sample Output 2 
no

Sample Input 3 
THE RAIN IN SPAIN IN THE PLAIN

Sample Output 3    
no

You can test it with the following:
var output = noDuplicates("IN THE RAIN AND SNOW");
console.log(output);

*/
function noDuplicates(phrase){
 var words = phrase.split(" ");
 for(i = 0; i < words.length; i++){
   for(var x =i; x<=words.length; x++){
     if(i != x && words[i] == words[x]){
       return ('no');
     }
   }
   
 } return('yes');
  
}
var output = noDuplicates("IN THE RAIN AND SNOW");
console.log(output);
