import random as ra
import adivina_num as adv
import pyfiglet
num_secreto = ra.randint(1, 50)
#print(num_secreto)# para testear
puntos = 500
ascii_banner1 = pyfiglet.figlet_format('Guess')
print(ascii_banner1)
ascii_banner2 = pyfiglet.figlet_format('the number!')
print(ascii_banner2)
print(''' ____________________________________________
│                                            │
│   ______________________________________   │
│  │     ¡Let's play guess the number!    │  │ 
│   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯   │
│       Type numbers from 1 to 50 and        │
│         you start with 500 points          │
│                                            │
│     if you fail you'll lose 100 points,    │
│           but you win a hint               │
│                                            │
│                 ¡LET'S PLAY!               │
 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯''')
start = input('''Do you want to start the game?
press [1] to yes.
press [2] to no.
Choose: ''')
if start == '1':
  juego = adv.adivina_num(puntos, num_secreto)
elif start == '2':
  print('Come back when you want')
else:
  print('Please choose between [1]Yes or [2]No')