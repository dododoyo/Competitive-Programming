string = input()
vowels = set(['a','y','e','i','o','u','A','Y','E','I','O','U'])
solution = []
for character in string:
  if character not in vowels:
    solution.append('.')
    solution.append(character.lower())
print("".join(solution))


