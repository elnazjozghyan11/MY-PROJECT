import random

score = 0

for i in range(5):
   print('\n shot', i + 1)

   while True:
    shot = input('choose your shot (left, center, right): ').strip().lower()

    if shot in ['left', 'center', 'right']:
        break
    else:
        print('only choice one of them.')

   goalkeeper = random.choice(['left', 'center', 'right'])
   print('Goalkeeper', goalkeeper)

   if shot == goalkeeper:
    print('saved!')
   else:
    print('goal!')
    score += 1

print("\nFinal score:", score, "/5")
