shot = input('choose your shot (left, center, right): ').strip().lower()
import random
goalkeeper = random.choice(['left', 'center', 'right'])
if shot == goalkeeper:
    print('yasien bono ghahrman')
    print('saved!')
else:
    print('yasian bono read va')
    print('goal!')