shot = input('choose your shot (left, center, right): ').strip().lower()
import random
goalkeeper = random.choice(['left', 'center', 'right'])
if shot == goalkeeper:
    print('saved!')
else:
    print('goal!')

import random

score = 0

for i in range(5):
   print('\n shot', i + 1)

   shot = input('choose your shot (left, center, right): ').strip().lower()
   goalkeeper = random.choice(['left', 'center', 'right'])
   print('Goalkeeper', goalkeeper)

   if shot == goalkeeper:
      print('saved!')
   else:
      print('goal!')
      score += 1
      print("\nFinal score:", score, "/5")