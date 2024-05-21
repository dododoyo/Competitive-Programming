input()
word = input()
vowels, solution, last_is_consonant = {"a", "e", "i", "o", "u", "y"}, [], True

for char in word:
	current_is_consonant = (char not in vowels)
	if current_is_consonant or last_is_consonant:
		solution.append(char)
	last_is_consonant = current_is_consonant

print("".join(solution))
