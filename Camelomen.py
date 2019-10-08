import random


Distância_Percorrida = 0
Sede = 0
Cansaço = 0
Distância_Percorrida_pelo_Dono = -20
Água_no_Cantil = 5
Oasis = 0


print ('Bem-vindo ao Camelo Louco!')
print ('')
print ('Você roubou um camelo para atravessar o grande deserto de Mobi (200km de sofrimento).')
print ('O dono do camelo o quer de volta e está te perseguindo!')
print ('Sobreviva ao deserto e escape do dono do camelo.')


while True:
	print ('')
	print ('A. Beber água do cantil')
	print ('B. Avançar com velocidade moderada')
	print ('C. Avançar com velocidade máxima')
	print ('D. Parar para descansar a noite')
	print ('E. Checar o status')
	print ('Q. Sair')
	print ('')


	x = input ('qual é a sua escolha? (A, B, C, D, E, Q):  ')


	if x is ('Q') or x is ('q'):
		print ('')
		print ('Você saiu do jogo')
		print ('Game Over')
		print ('===========================================')
		break


	elif x is ('E') or x is ('e'):
		print ('')
		print (f'Você andou {Distância_Percorrida} km')
		print (f'Você está a {Distância_Percorrida - Distância_Percorrida_pelo_Dono} Km do dono')
		print (f'Você tem {Água_no_Cantil} litros de água')
		print ('===========================================')


	elif x is ('D') or x is ('d'):
		Cansaço = 0
		print ('')
		print ('O camelo está totalmente descansado')
		Distância_Percorrida_pelo_Dono += random.randint(7, 14)
		print (f'Você está a {Distância_Percorrida - Distância_Percorrida_pelo_Dono} Km do dono')
		print ('===========================================')


	elif x is ('C') or x is ('c'):
		print ('')
		Oasis = 0
		Distância_Percorrida += random.randint(10, 20)
		print (f'Você já percorreu {Distância_Percorrida} km')
		Sede += 1
		print (f'Seu camelo está com {Sede} de sede. Se chegar a 5 seu camelo morrerá!')
		Cansaço += random.randint(1, 3)
		print (f'Seu camelo está com {Cansaço} de cansaço')
		Distância_Percorrida_pelo_Dono += random.randint(7, 14)
		print (f'Você está a {Distância_Percorrida - Distância_Percorrida_pelo_Dono} Km do dono')
		Oasis += random.randint(1,20)
		if Oasis >= 20:
			print ('')
			print ('Bônus! Você encontrou um Oasis. Você enche seu cantil, bebe água e o camelo descansa totalmente!')
			Água_no_Cantil = 5
			Sede = 0
			Cansaço = 0 
		print ('===========================================')


	elif x is ('B') or x is ('b'):
		print ('')
		Oasis = 0
		Distância_Percorrida += random.randint(5, 12)
		print (f'Você já percorreu {Distância_Percorrida} km')
		Sede += 1
		print (f'Você está com {Sede} de sede. Se chegar a 7 seu camelo morrerá!')
		Cansaço += 1
		print (f'Seu camelo está com {Cansaço} de cansaço. Se chegar a 8 ele morrerá')
		Distância_Percorrida_pelo_Dono += random.randint(7, 14)
		print (f'Você está a {Distância_Percorrida - Distância_Percorrida_pelo_Dono} Km do dono')
		Oasis += random.randint(1,20)
		if Oasis >= 20:
			print ('')
			print ('Bônus! Você encontrou um Oasis. Você enche seu cantil, bebe água e o camelo descansa totalmente!')
			Água_no_Cantil = 5
			Sede = 0
			Cansaço = 0 
		print ('===========================================')


	elif x is ('A') or x is ('a'):
		print ('')
		if Água_no_Cantil > 0 and Sede > 0:
			Água_no_Cantil -= 1
			Sede -= 1
			print ('Você bebeu água do cantil')
			print (f'Você agora está com {Sede} de sede')
		elif Água_no_Cantil <= 0:
			print ('Não há mais água no cantil!')
			print (f' Você continua com {Sede} de sede')
		elif Sede <= 0:
			print ('Você não está com sede.')
		print ('===========================================')


	if Sede >= 4 and Sede < 7:
		print('===========================================')
		print ('Você está com sede!')
		print ('===========================================')


	elif Sede >= 7:
		print ('===========================================')
		print ('Você morreu de sede!')
		print ('Game Over')
		print ('===========================================')
		break


	if Cansaço > 5 and Cansaço < 8:
		print ('===========================================')
		print ('O camelo está ficando cansado!')
		print ('===========================================')


	elif Cansaço >= 8:
		print ('===========================================')
		print ('O camelo morreu de cansaço!')
		print ('Game Over')
		print ('===========================================')
		break


	if Distância_Percorrida - Distância_Percorrida_pelo_Dono <= 15:
		print('===========================================')
		print ('O Dono está a menos de 15 km de você!')
		print ('===========================================')


	elif Distância_Percorrida_pelo_Dono >= Distância_Percorrida:
		print ('===========================================')
		print ('O dono te pegou!')
		print ('Game Over')
		print ('===========================================')
		break


	elif Distância_Percorrida >= 200:
		print ('===========================================')
		print ('Você consguiu atravessar o deserto e venceu!')
		print ('===========================================')








		







