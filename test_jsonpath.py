import requests
import jsonpath

headers_user_01 = {'Authorization': 'Token c9a956c3cbb79588ed023341cc468d9a69b22da1'}

headers_user_02 = {'Authorization': 'Token 04cb02eedd4b1a5222ccd371a11aa4cf367537f2'}

emprestimos = requests.get(url='http://127.0.0.1:8000/emprestimos/', headers=headers_user_01)
print(emprestimos)

# Nome de todos os cliente
cliente = jsonpath.jsonpath(emprestimos.json(), 'results[*].cliente')
print(cliente)

pagamentos = requests.get(url='http://127.0.0.1:8000/pagamentos/', headers=headers_user_01)
print(pagamentos)

valor_pago = jsonpath.jsonpath(pagamentos.json(), 'results[*].valor_pago')
print(valor_pago)
