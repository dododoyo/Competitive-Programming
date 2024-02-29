alcohol_drinks = {"ABSINTH", "BEER", "BRANDY", "CHAMPAGNE",
                  "GIN", "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE"}
checker = 0
def is_number(input):
    try:
        float(input)  
        return True    
    except:  
        return False 
for _ in range(int(input())):
  drink = input()
  if drink in alcohol_drinks:
    checker += 1
  else:
    if is_number(drink) and int(drink) < 18:
      # print(is_number(drink) < 18)
      checker += 1
  # print(drink,checker)
    # either leslasa or number
print(checker)