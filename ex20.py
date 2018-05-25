#Goal: Turn A1 - A7 to functions

(note: please do not delete any of the comments. I want to keep it organized and labeled.)

You will need the code from the past exercises for this one.

The goal will be to turn our past exercises into functions!

Functions are named blocks of code designed to do one specific job. Functions allow you to write code once that can then be run whenever you need to accomplish the same task. Functions can take in the information they need, and return the information they generate. 
Using functions effectively makes your programs easier to write, read, test, and fix. 


def sum_three():
  a = int(input('Enter your first number:'))
  b = int(input('Enter your second number:'))
  c = int(input('Enter your third number:'))
  return (a+b+c)
  
print(sum_three())
print("_________________")


#A2 - Area of a Triangle

def area_triangle():
  l = int(input('Enter the length:'))
  h = int(input('Enter the height:'))
  return(h*l/2)

print(area_triangle())
  
print("_________________")

#A3 - Combining Strings

def names(n = input('Whats your name?')):
  return("Hello " + n)
  
print(names())

print("_________________")


#A4 - Find the larger of 2 numbers

def bigger_number(x = int(input('Enter a number:')), y = int(input('Enter your second number:'))):
  if x > y:
    return x
  else:
    return y
    
print (bigger_number())

print("_________________")


#A5 - Printing Arrays
food_items = ["turkey","ham", "spam","eggs","nuts"]

def foods(v):
  for x in v:
    print (x)
    
foods(food_items)
  
print('________________')

#A6 - Else if statements

def numbers(a = int(input('Enter a number:')),b = int(input('Enter a number:'))):
  if a > b:
    return (a + b)
  elif a == b:
    return (a)
  else:
    return (b - a)
    
print(numbers())

print('________________')

#A7 - Partial Arrays

a1 = [1,3,5,4,10,30,58,97]

def partial_array(y)  :
  for x in y:
    if x < 30:
      print(x)
      
partial_array(a1)

