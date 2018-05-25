#For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20.  Alternately, round down to the previous multiple of 10 if its rightmost  digit is less than 5, so 12 rounds down to 10. 

Given 3 integers, a b c,  return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum(). 

round_sum(16, 17, 18)  → 60
round_sum(12, 13, 14)  → 30
round_sum(6, 4, 4)     → 10 

Round each number individually. DON'T add all the numbers and then round.


def round_sum(a, b, c):
  # insert your logic here
  return round10(a) + round10(b) + round10(c)
  
def round10(num):
    x = num % 10
    if x >= 5:
      return(num - x + 10)
    else:
      return (num - x)
  
# Test cases. Don't modify  
print(1,'|',round_sum(16, 17, 18))   # this would be 60
print(2,'|',round_sum(12, 13, 14))   # this would be 30
print(3,'|',round_sum(6, 4, 4))      # this would be 10
print(4,'|',round_sum(4, 6, 5))
print(5,'|',round_sum(4, 4, 6))   
print(6,'|',round_sum(9, 4, 4))
print(7,'|',round_sum(0, 0, 1))   
print(8,'|',round_sum(0, 9, 0))
print(9,'|',round_sum(10, 10, 19))   
print(10,'|',round_sum(20, 30, 40))
print(11,'|',round_sum(45, 21, 30))   
print(12,'|',round_sum(23, 11, 26))
print(13,'|',round_sum(10, 10, 19))   
print(14,'|',round_sum(23, 24, 25))
print(15,'|',round_sum(25, 24, 29))   
print(16,'|',round_sum(11, 24, 36))
print(17,'|',round_sum(24, 36, 32))   
print(18,'|',round_sum(14, 12, 26))
print(19,'|',round_sum(12, 10, 24))   
