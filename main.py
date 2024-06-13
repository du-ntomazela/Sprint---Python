def num(msg):
    x = input(msg)
    while not x.isnumeric():
        x = input(msg)
    return x


def find_index(li, element):
    for i in range(len(li)):
        x = li[i]
        if x == element:
            return i


def compare(l1, msg1):
    for x in l1:
        print(x)
    element = input(msg1)
    while element not in l1:
        element = input("Escolha uma das opções existentes! ")
    return element


def login_novo():
    username = input("Informe um nome de usuário: ")
    gmail = input("Informe seu melhor e-mail para contato: ")
    while True:
        password1 = input("Informe sua senha: ")
        password2 = input("Confirme sua senha: ")
        if password1 == password2:
            break
        else:
            print("As senhas devem coincidir!")
    list_passwords.append(password1)
    list_email.append(gmail)
    list_usernames.append(username)

    return username


def login_existente(l1, l2):
    x = 4
    username = input("Informe seu usuário: ")
    password = input("Informe sua senha: ")
    while not (username in l1 and password in l2 )and  x > 0:
        x -= 1
        username = input("Informe seu usuário: ")
        password = input("Informe a sua senha: ")

    if x == 0:
        print("Usuário ou senha invalidos, será nescessário criar uma nova conta")
        user = login_novo()
        return user
    else:
        return username


# Listas:

print("Bem vindo a Mahindra Racing!")

# Listas referentes a login:

list_usernames = ["fiap2024"]
list_email = ["email.teste@gmail.com"]
list_passwords = ["1234"]

# Listas referentes aos participantes da Solução:

list_countries = ["Brazil", "USA", "India", "Argentina"]
list_influencers1 = ["Jorginho", "Jimmy Donaldson", "Virat Kohli", "Alejandro Natale"]
list_influencers2 = ["Peter Jordan", "Mark Rober", "Salman Khan", "Ignacio Chardin"]
list_votos1 = [0, 0, 0, 0]
list_votos2 = [0, 0, 0, 0]

# Lista das funcionalidades do programa:

list_functions = ["Votação", "Notícias", "Pilotos", "Veículo"]

# Lista referente aos pilotos da Mahindra Racing:

list_pilots = ["Nyck De Vries", "Edoardo Mortara"]
list_ages = [29, 37]

# Listas referentes aos veículos da Mahindra Racing:

list_car = ["M10ELECTRO"]
list_car_max_speed = ["200mph (320kph)"]
list_car_weight = ["840kg"]
list_car_charge_capability = ["600kW"]


# Verificando se o usuário já possui login:

verify = compare(["sim", "não"], "Você ja possui cadastro?")

if verify == "sim":
    username = login_existente(list_usernames, list_passwords)
else:
    username = login_novo()

# Nossa solução é voltada para a forma que a formula E chega até o público.
# Por meio de parcerias com influenciadores digitais em areas proximas ao automobilismo, tecnologia, etc...
# Uma dulpa por país é aderida a Mahindra Racing, formando assim o que denominamos a Familia MR
# Cada influenciador deve criar um contúdo criativo e de boa qualidade e que será avaliado pelo público.
# O público deve entrar no site da Mahindra contendo nossa solução e votar em um dos integrantes da dupla do país selecionado.
# E ao final de cada Temporada da Formula E, estabelecer um vencedor entre os influenciaodres que será premiado.

while True:
    # Selecionando a funcionalidade que o usuário deseja consultar:
    function = compare(list_functions, "O que deseja consultar(selecione uma das opções acima): ")

    # Iniciando o código de contabilidade de votos:
    if function == "Votação":
        while True:
            countrie = compare(list_countries, "Selecione um dos paises acima: ")
            indice = find_index(list_countries, countrie)

            option1 = list_influencers1[indice]
            option2 = list_influencers2[indice]

            escolha = compare([option1, option2], f"escolha entre {option1} e {option2}: ")

            if escolha == option1:
                value = list_votos1[indice]
                value += 1
                list_votos1[indice] = value
            else:
                value = list_votos2[indice]
                value += 1
                list_votos2[indice] = value

            # Mostrando os votos que cada participante tem:

            for i in range(len(list_countries)):
                print(f"País - {list_countries[i]} \n {list_influencers1[i]}: {list_votos1[i]}   /    {list_influencers2[i]}: {list_votos2[i]} \n")

            # Verificando se o usuário deseja continuar navegando na aplicação:
            continuar1 = compare(["sim", "não"], "Deseja continuar votando? ")
            if continuar1 == "não":
                print(f"Obragado por ter participado da votação {username}")
                break

    elif function == "Notícias":
        print(f"{username}, essas são as notícias mais atualizadas sobre a Formula E:")
        print("Recuperação de António Félix da Costa: O piloto António Félix da Costa da equipe Porsche celebrou suas recentes vitórias na Fórmula E, especialmente no ePrix de Xangai, afirmando que essas conquistas o ajudaram a 'sair do buraco' após uma fase difícil. Ele destacou a importância dessas vitórias para sua confiança e para a equipe Porsche, que continua a ser uma das principais concorrentes na temporada")
        print("Desempenho da Porsche: A Porsche ampliou sua vantagem sobre a Jaguar no Troféu de Fabricantes após as corridas em Xangai. A equipe tem mostrado um desempenho sólido e consistente, consolidando sua posição como líder na competição de construtores da Fórmula E nesta temporada")
        print("Entrada da Ferrari na Fórmula E: O CEO da Fórmula E expressou interesse na entrada da Ferrari na competição. Ele mencionou que a Ferrari estaria em uma 'prateleira própria' dentro da Fórmula E, dada sua história e prestígio no automobilismo, o que poderia trazer ainda mais atenção e prestígio para a categoria")
    elif function == "Veículo":
        for i in range(len(list_car)):
            print(f"Nome do veículo: {list_car[i]} \n Velocidade máxima: {list_car_max_speed[i]} \n Peso: {list_car_weight[i]} \n Carga máxima: {list_car_charge_capability[i]}\n ")
    else:
        for i in range(len(list_pilots)):
            print(f"Piloto {i + 1} - {list_pilots[i]} e sua idade é de {list_ages[i]} anos")


    continuar2 = compare(["sim", "não"], "Deseja continuar navegando pelas funcionalidades? ")
    if continuar2 == "não":
        print(f"Volte sempre {username}!")
        break
