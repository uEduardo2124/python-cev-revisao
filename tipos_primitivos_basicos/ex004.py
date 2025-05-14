# Coleta de resposta do usuário
resposta = input('Digite algo: ')

# Retorno no terminal das informações a respeito do input
print(f'O tipo primitivo desse valor é {type(resposta)}')
print(f'Só tem espaços ? {resposta.isspace()}')
print(f'É um número ? {resposta.isnumeric()}')
print(f'É alfabético ? {resposta.isalpha()}')
print(f'É alfanumérico ? {resposta.isalnum()}')
print(f'Está em maiúsculas ? {resposta.isupper()}')
print(f'Está em minúsculas ? {resposta.islower()}')
print(f'Está capitalizada ? {resposta.istitle()}')
