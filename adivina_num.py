def adivina_num(puntos, num_secreto):
  while puntos > 0:
    numero = input('Type a number between 1 and 50: ')
    if numero.isdigit() == True:
      numero = int(numero)
      if numero < 1 or numero > 50:
        print('The number is out of range')
        print(f'You still have {puntos} points left')
        return adivina_num(puntos, num_secreto)
      else:
        if numero != num_secreto:
          puntos-=100
          if puntos == 0:
            print('/////////////////////////////')
            print('You have run out of points')
            print(f'The secret number was {num_secreto}')
            again = input('''---------------------------------------
  Do you want to play again?
  [1] to yes
  [2] to no
  choose: ''')
            if again == '1':
              puntos+=500
              print(f'{puntos} more points have been added')
              return adivina_num(puntos, num_secreto)
            elif again == '2':
              print('Ok bye...')
              break
            else:
              print('There are only two options available')
          else:
            if numero < num_secreto:
              print(f'You have {puntos} points left')
              print(f'The secret number is greater than {numero}')
            elif numero > num_secreto:
              print(f'You have {puntos} points left')
              print(f'The secret number is less than {numero}')
        else:
          print(f'¡Congrats, you got it!, ¡You have won {puntos} points!')
          print(f'The secret number was {num_secreto}!')
          break
    elif numero[0] == '-':
      print('The number is out of range')
      print(f'You still have {puntos} points left')
      return adivina_num(puntos, num_secreto)
    else:
      print('You have entered a letter or character')
      print(f'You still have {puntos} points left')
      return adivina_num(puntos, num_secreto)
      #el return ejecuta infinitamente hasta que cumpla