#Make a program to check whether an email address is valid or not. 
Criteria:
For instance, you could make sure that there are 
1. no spaces
2. that there is an @ symbol and a dot somewhere after it. 
3. When an email address is found to be invalid, tell the user exactly what they did wrong with their email address rather than just saying it is invalid

print('Enter your email:')

def spaces(inputstring):
  return any(char.rstrip(" ")for char in inputstring)
  
  '''
def a_symbol(inputstring):
  return any(@ for char in inputstring)
  
def b_symbol(inputstring):
  return any(. for char in inputstring)
'''

i = True

while i == True:
  email_acceptance = False
  email = input()
  if spaces(email):
    if '@' in email:
      if '.' in email:
        print('Email accepted')
        email_acceptance = True
        break
      else:
        print('Error: no period')
        print('Try Again\n')
    else:
      print('Error: no @ symbol')
      print('Try Again\n')
  else:
    print('Error: can not have spaces')
    print('Try Again\n')
      
