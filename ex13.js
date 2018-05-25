/*
You must use loops! Please don't hard code 100+ lines of code. The whole program should be less than 10 lines.

Problem
Create a times table going from 0 to 10. Your output must look EXACTLY like mine below.

Example output:  

0 TIMES TABLE
1 x 0 = 0
2 x 0 = 0
3 x 0 = 0
4 x 0 = 0
5 x 0 = 0
6 x 0 = 0
7 x 0 = 0
8 x 0 = 0
9 x 0 = 0
10 x 0 = 0

1 TIMES TABLE
1 x 1 = 1
2 x 1 = 2
3 x 1 - 3
...

2 TIMES TABLE
1 x 2 = 2
2 x 2 = 4
3 x 2  = 6
...


3 TIMES TABLE
1 x 3 = 3
2 x 3 = 6
...

and so on....
*/

for (i=0;i<11;i++){
  console.log(i + ' TIMES TABLE');
  for (y=0;y<11;y++){
    console.log(i + " x " + y + ' = ' + i*y);
  }
}
