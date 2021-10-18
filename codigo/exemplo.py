# import pandas as pd
#
# fields = ['nome', 'cpf', 'uf', 'turma', 'data_nascimento', 'email', 'endereco', 'período', 'modulo']
#
# data = pd.read_csv('./curso-mvcad.csv')
# df = pd.DataFrame(data, columns=fields)
# print(df)

# names = ['Andorinha', 'Azaleia', 'Amelia', 'Margarida', 'Rosa']
#
# namesWithA = 0
#
# for name in names:
#     if name[0].lower() == 'a':
#         namesWithA += 1
#
# print(f'Foram encontradas {namesWithA} nomes começados com A')

#----------------------------------------------------------------------

# nOfNumbers = int(input('Insira a quantidade de numeros desejados'))
# index = 0
# listOfNumbers = []
#
# while (index < nOfNumbers):
#     index += 1
#     listOfNumbers.append(int(input("Digite o proximo número: ")))
#
# listOfNumbers.sort()
#
# print(f'Menor número: {listOfNumbers[0]}')
# print(f'Maior número: {listOfNumbers[len(listOfNumbers) -1]}')

#----------------------------------------------------------------------

presents = int(input('Insira a quantidade de numeros desejados'))
index = 0
listOfName = []

while (index < presents):
    index += 1
    listOfName.append(input("Digite o proximo nome: "))

listOfName.sort()

print(f'Paticipantes em ordem alfabética:')
print('\n'.join(listOfName))



