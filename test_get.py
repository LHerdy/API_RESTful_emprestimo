import requests

headers_user_01 = {'Authorization': 'Token c9a956c3cbb79588ed023341cc468d9a69b22da1'}
headers_user_02 = {'Authorization': 'Token 04cb02eedd4b1a5222ccd371a11aa4cf367537f2'}

url_emprestimos = 'http://127.0.0.1:8000/emprestimos/'
url_pagamentos = 'http://127.0.0.1:8000/pagamentos/'

emprestimos = requests.get(url=url_emprestimos, headers=headers_user_01)
# print(emprestimos.json())

assert emprestimos.status_code == 200

# Testando a quantidade de requistro
assert emprestimos.json()['count'] == 1
