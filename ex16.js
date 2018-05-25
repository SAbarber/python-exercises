/*
Write a function called "findMinLengthOfThreeWords".
Given 3 words, "findMinLengthOfThreeWords" returns the length of the shortest word.
*/

function findMinLengthOfThreeWords(word1, word2, word3) {
  // your code here
  if (word1.length < word2.length && word1.length < word3.length){
    return word1.length;
  }
  if (word1.length > word2.length && word2.length < word3.length){
    return word2.length;
  }
  if (word3.length < word1.length && word3.length < word2.length){
    return word3.length;
  }
}

var output = findMinLengthOfThreeWords('a', 'be', 'see');
console.log(output);
