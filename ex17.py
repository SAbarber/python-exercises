#This dice game is played with 5 standard dice (having from 1 to 6 points on their sides). The player's goal is to gather some beautiful combination of points. Suppose, the following combinations are respected:

two of dice have the same points, like 3 6 5 6 1 - called pair;
three of dice have the same points, like 2 4 5 4 4 - called three;
four of dice have the same points, like 1 4 1 1 1 - called four;
all five dice have the same points, like 2 2 2 2 2 - called yacht;
two pairs at once, like 3 6 5 3 5 - called two-pairs;
pair and three at once, like 1 6 6 1 6 - called full-house;
sequence from 1 to 5, like 2 4 3 5 1 - called small-straight;
sequence from 2 to 6, like 6 3 4 2 5 - called big-straight.

Input data contains a number of test-cases in the first line. Next lines contain 5 values each - points of player's dice. 

Answer should contain the name for each of combinations. Names could be pair, two-pairs, three, four, yacht, full-house, small-straight, big-straight or none, separated with spaces. 

# Look at A22 for reading arrays
# Use inputs and not the random dice roller.
import collections

def dice_poker():
  rolls = int(input())
  answer = []
  for roll in range(rolls):
    roll = input().split()#splits the input
    #sorts values alphanumaircally
    values = sorted([x for x in collections.Counter(roll).values()])
    
    if sorted(roll) == ['2','3','4','5','6']:
      answer.append('big-straight')
      #do the same for small-straight
    elif sorted(roll) == ['1','2','3','4','5']:
      answer.append('small-straight')
    elif values == [2,3]: #has to be 2,3 not 3,2 because they are sorted
      answer.append('full-house')
    elif values == [1,2,2]:
      answer.append('two-pairs')
    elif values == [5]:
      answer.append('yacht')
    elif values == [1,4]:
      answer.append('four')
    elif values == [1,1,3]:
      answer.append('three')
    elif values == [1,1,1,2]:
      answer.append('pair')
    else:
      answer.append('none')
  print('answer:')
  print(' '.join(answer))

dice_poker()

