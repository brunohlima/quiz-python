print("Seja muito bem vindo ao quiz do Bruno!")
inicio = input("Quer começar? (S/N) ")

if inicio != "S":
    quit()

score = 0

print("Começando...")

print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
questao1 = input("Resposta: ")

if questao1 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Los Santos é uma cidade fictícia baseada em uma Cidade real. Em qual cidade Los Santos foi baseada? \n (A) Los Angeles \n (B) Miami \n (C) Orlando \n (D) Las Vegas")
questao2 = input("Resposta: ")

if questao2 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print("Qual é o prédio mais alto do GTA 5? \n (A) Maze Bank Tower \n (B) Schlonberg Sachs \n (C) Didier Sachs \n (D) Penris \n")
questao3 = input("Resposta: ")

if questao3 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print(f"Quiz acabou... \n Pontuação: {score} /3 ")