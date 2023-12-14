number = int(input())
print(["YES","NO"][all([number%i for i in [4,7,47,477]])])