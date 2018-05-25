#You may assume that the input is one word, no spaces, no punctuation.

Using an accumulator algorithm, calculate the number of consonants in the word.  (all except aeiou) 

function owassoRams(n){
  var a = [];
  
  for (i = 1; i < n+1; i++){
    
    if(i%5===0 && i%3===0){
      a.push("OwassoRams");
    }
    else if(i%5 === 0){
      a.push("Rams");
    }
    else if (i % 3 === 0){
      a.push('Owasso');
      
    }
    
    else{
      a.push(i);
    }
    
  
  }return (a);
}


var output = owassoRams(15);
console.log(output);
