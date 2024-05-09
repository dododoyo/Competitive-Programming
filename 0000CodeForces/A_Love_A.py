word = input()
number_of_as = word.count("a")
none_as = len(word) - number_of_as

if number_of_as > len(word)//2:
  print(len(word))
else:
  print(number_of_as+1)
