/*
Write a JavaScript function which iterates the integers from 1 to n.  
BUT... for multiples of 3 add "Owasso" to the array instead of the number and for the multiples of five, add "Rams" to the array. 

For numbers which are multiples of both three and five print "OwassoRams".

Very similar to A34.

Add the elements to an array!

*/


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
