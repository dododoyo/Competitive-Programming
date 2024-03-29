for _ in range(int(input())):
  prediction = input()
  a_score,b_score = 0,0
  b_after = [int(prediction[i] == "1" and i%2 == 0) for i in range(10)]
  a_after = [int(prediction[i] == "1" and i%2) for i in range(10)]
  
  for i in range(1,10):
    b_after[9-i] += b_after[10-i]
    a_after[9-i] += a_after[10-i]

  print(b_after)
  print(a_after)
  # play in a's favor
  for i in range(10):
    if i%2 and (prediction[i] == "1" or prediction[i] == "?"):
        a_score += 1
    elif prediction[i] == "1":
        b_score += 1
    
    remain = 9-i
    print(a_score,b_score)
  print()