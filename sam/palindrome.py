word ="racecar"

def pal(word):
  for i in range(len(word)//2):
    if word[i] != word[-1-i]:
      return False
  return True

print(pal("racecar")) # --> should print True
print(pal("racecbr")) # --> should print True
print(pal("jason")) # --> should print False