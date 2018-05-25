#Given an array of scores, return true if each score is equal or greater than the one before. The array will be length 2 or more.

# Don't delete any of the given code.
def scoresIncreasing(scoresList):
  # insert your logic here
  for x in range(len(scoresList)):
    if scoresList[x] <= scoresList[x + 1] <= scoresList[x + 2]:
      if len(scoresList) >= 4:
        if scoresList[x + 2] <= scoresList[x + 3] <=scoresList[x + 4] <= scoresList[x + 5]:
          return True
        else:
          return False
      return True
    else:
      return False
  
# Test cases. Don't modify  
print(1,scoresIncreasing([1, 3, 4]))   # this would be True
print(2,scoresIncreasing([1, 3, 2]))   # this would be False
print(3,scoresIncreasing([1, 1, 4]))   # this would be True
print(4,scoresIncreasing([1, 1, 2, 4, 4, 7]))
print(5,scoresIncreasing([1, 1, 2, 4, 3, 7]))
print(6,scoresIncreasing([-5, 4, 11]))
print(7,scoresIncreasing([-5, 4, 8, 11, 13, 17, 19, 31, 92]))

#and scoresList[x + 2] <= scoresList[x + 3]and scoresList[x + 3] <=scoresList[x + 4] and scoresList[x + 4] <= scoresList[x + 5]


