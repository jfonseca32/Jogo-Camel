import random


Distância_Percorrida = 0
Sede = 0
Cansaço = 100
Distância_Percorrida_pelo_Dono = -20
Água_no_Cantil = 5


print ('Bem-vindo ao Camelo Louco!')
print ('Você roubou um camelo para atravessar o grande deserto de Mobi.')
print ('O dono do camelo o quer de volta e está te perseguindo!')
print ('Sobreviva ao deserto e escape do dono do camelo.')


while True:
	print ('A. beber água do cantil')
	print ('B. avançar com velocidade moderada')
	print ('C. avançar com velocidade máxima')
	print ('D. parar para descansar a noite')
	print ('E. checar o status')
	print ('Q. sair')


	x = input ('qual é a sua escolha? (A, B, C, D, E, Q):  ')


	if x is ('Q') or x is ('q'):
		print ('      ')
		print ('Você saiu do jogo')
		break


	elif x is ('E') or x is ('e'):
		print ('      ')
		print (f'Você andou {Distância_Percorrida} km')
		print (f'Você está a {Distância_Percorrida - Distância_Percorrida_pelo_Dono} Km do dono')
		print (f'Você tem {Água_no_Cantil} litros de água')
		print ('     ')


	elif x is ('D') or x is ('d'):
		Cansaço = 0
		print ('O camelo está totalmente descansado')
		Distância_Percorrida_pelo_Dono += random.randint(7, 14)
		print (f'Você está a {Distância_Percorrida - Distância_Percorrida_pelo_Dono} Km do dono')


	elif x is ('C') or x is ('c'):
		Distância_Percorrida += random.randint(10, 20)
		print (f'Você já percorreu {Distância_Percorrida} km')
		Sede += 1
		print (f'Seu camelo está com {Sede} de sede')
		Cansaço += random.randint(1, 3)
		print (f'Seu camelo está com {Cansaço} de cansaço')
		Distância_Percorrida_pelo_Dono += random.randint(7, 14)
		print (f'Você está a {Distância_Percorrida - Distância_Percorrida_pelo_Dono} Km do dono')




		







