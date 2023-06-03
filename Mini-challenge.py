import random

# Criação de uma lista com os nomes e as respectivas restrições.
bixos_dev = [("Adriel Faustino de Oliveira", 0), ("Amanda Emi Yamasaki", 0), ("Ana Werneck de Souza Dias", 0), ("André Menniti Pennini", 1), ("Felipe de Souza Lourenço", 0), ("Fernanda Mayumi Sakamoto Iizuka", 0), ("Fernanda Mees Antunes", 1), ("Gabriel Grub Vidal da Silva", 1), ("Guilherme Vinicius Afonso Dias de Freitas", 0), ("Henrique Nogueira Pedro Lindoso", 1), ("Kim Ju Hyang", 0), ("Leticia Amy Siramidu", 0), ("Marcelo Tamay Honda", 0), ("Maria Dulce Navarro de Britto Matos", 0), ("Mateus Pamio Forcione de Oliveira e Souza", 0), ("Milena da Silva Ramos", 0), ("Paulo Sergio Almeida de Oliveira", 0), ("Theo Borten Radesca Migliano", 0), ("Vitor Tatiama Gouveia", 0)]

# Variáveis controles de laço e a matriz principal que irá guardar os grupos.
x = 1
qntd = 5
grupos = []

# Laço que cuida dos grupos que irão ser criados.
while x <= 4:
    # Para que o último grupo tenha um integrante a menos.
    if x == 4:
        qntd = 4
    
    # Parâmetro para controlar que não haja dois integrantes com restrição no mesmo grupo. A príncipio, não há restrição até que seja identificada uma.
    restricao = False
    y = 1
    grupo = []

    # Laço que cuida das pessoas que estarão em cada grupo.
    while y <= qntd:
        # Função que sorteia cada pessoa.
        bixo = random.choice(bixos_dev)
        
        # Para adicionar as pessoas na lista de seu grupo.
        if restricao == False:
            grupo.append(bixo[0])
            ind = bixos_dev.index(bixo)
            # Para não haver repetições, é necessário ir excluindo cada pessoa escolhida da lista primordial bixos.dev.
            del(bixos_dev[ind])

        else:
            # Se a restrição for verdadeira (na segunda vez), o programa terá que ficar sorteando até encontrar alguém sem restrição.
            while bixo[1] == 1:
                bixo = random.choice(bixos_dev)
            grupo.append(bixo[0])
            ind = bixos_dev.index(bixo)
            del(bixos_dev[ind])
    
        if bixo[1] == 1:
            restricao = True
        y = y + 1

    # Adicionando a lista do grupo sorteado na matriz de todos os grupos.
    grupos.append(grupo)
    x = x + 1 

# Para uma impressão personalizada, tem-se o código abaixo.
for i in range(len(grupos)):
    print("Grupo: %i" %(i+1))
    for j in range(len(grupos[i])):
        print(grupos[i][j])
    print("")