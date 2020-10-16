import requests


headers_user_01 = {'Authorization': 'Token c9a956c3cbb79588ed023341cc468d9a69b22da1'}
headers_user_02 = {'Authorization': 'Token 04cb02eedd4b1a5222ccd371a11aa4cf367537f2'}

# Teste acesso sem Token
emprestimo = requests.get('http://127.0.0.1:8000/emprestimos/')
print(emprestimo)

pagamento = requests.get('http://127.0.0.1:8000/pagamentos/')
print(pagamento)

emprestimo_id_0 = requests.get('http://127.0.0.1:8000/emprestimos/0/')
print(emprestimo_id_0.json())

# Teste acesso com Token emprestimo
emprestimos = requests.get(url='http://127.0.0.1:8000/emprestimos/', headers=headers_user_01)

print(emprestimos.status_code)
print(emprestimos.json())
print(type(emprestimos.json()))

# Acessando a quantidade de registros
print(emprestimos.json()['count'])

# Acessando o primeiro objeto
print(emprestimos.json()['results'][0])

# Acessando o último objeto
print(emprestimos.json()['results'][-1])

# Acessando o último cliente que solicitou o emprestimo
print(emprestimos.json()['results'][-1]['cliente'])

emprestimos = requests.get(url='http://127.0.0.1:8000/emprestimos/', headers=headers_user_02)

print(emprestimos.status_code)
print(emprestimos.json())
print(type(emprestimos.json()))

# Acessando a quantidade de registros
print(emprestimos.json()['count'])

# Acessando o primeiro objeto
print(emprestimos.json()['results'][0])

# Acessando o último objeto
print(emprestimos.json()['results'][-1])

# Acessando o último cliente que solicitou o emprestimo
print(emprestimos.json()['results'][-1]['cliente'])

# Teste acesso com Token pagamento
pagamentos = requests.get(url='http://127.0.0.1:8000/pagamentos/', headers=headers_user_01)

print(pagamentos.status_code)
print(pagamentos.json())
print(type(pagamentos.json()))
