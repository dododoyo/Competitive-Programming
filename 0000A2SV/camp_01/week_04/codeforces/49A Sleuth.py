question = input();
left, vowels = len(question) - 1, {"A","E","I","O","U","Y","a","e","i","o","u","y"};
while not question[left].isalpha():left -= 1;
print("YES" if question[left] in vowels else "NO");