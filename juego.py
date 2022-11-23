import random
print('Juego piedra papel o tijera:')
print('')
juegos= int(input('Cuantas veces vas a jugar? : '))
print('Recuerda--> 1: piedra, 2: papel, 3: tijera')
pc = 0
usuario= 0
for k in range(juegos):
    maquina = random.randint(1,3)
    user= int(input('Escoja su opción'))
    if k< juegos:
        k += 1
        if 0<user<4:
            if user==maquina:
                print('empate')
            elif user==1 and maquina==2:
                pc += 1
                print('Maquina Gana') 
            elif user==1 and maquina==3:
                usuario += 1
                print('Tu ganas') 
            elif user==2 and maquina==1:
                usuario += 1
                print('Tu ganas')        
            elif user==2 and maquina==3:
                pc += 1
                print('Maquina gana') 
            elif user==3 and maquina==1:
                pc += 1
                print('Maquina gana') 
            elif user==3 and maquina==2:
                usuario += 1
                print('Tu ganas')
print('resultado es:')
print(f'usuario {usuario} vs {pc} maquina')

r.rojas@coex.com.co

