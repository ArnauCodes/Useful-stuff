from math import sqrt
# Third day on python :)
while True:
  print("Note: Don\'t use literal parts, (use: ax^2 bx c = 0)")
  n1 = float(input('\'A\' term: '))
  n2 = float(input('\'B\' Term: '))
  n3 = float(input('\'C\' Term: '))
  ans0 = pow(n2, 2)
  ans1 = -4 * n1 * n3
  ans2 = ans0 + ans1
  if ans2 < 0:
    print('No answers')
    continue 
  ans3 = sqrt(ans2)
  ans4 = -n2 + ans3 
  ans5 = ans4 / (2*n1)
  print(f'{ans5} is the first answer')
  ans1 = -4 * n1 * n3
  ans2 = ans0 + ans1
  if ans2 < 0:
    print('No answers')
    continue 
  ans3 = sqrt(ans2)
  ans4 = -n2 - ans3 
  ans5 = ans4 / (2*n1)
  print(f'{ans5} is the second answer')
