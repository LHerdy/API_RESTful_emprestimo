import requests

headers_user_01 = {'Authorization': 'Token c9a956c3cbb79588ed023341cc468d9a69b22da1'}
headers_user_02 = {'Authorization': 'Token 04cb02eedd4b1a5222ccd371a11aa4cf367537f2'}

url_emprestimos = 'http://127.0.0.1:8000/emprestimos/'
url_pagamentos = 'http://127.0.0.1:8000/pagamentos/'

novo_emprestimo = {
            "banco": "Banco 02",
            "cliente": "Cliente 02",
            "valor_nominal": "2000.00",
            "parcelas": 10,
            "taxa_de_juros": "5.00",
            "endereco_de_ip": "195.156.0.100"
}
emprestimo = requests.post(url=url_emprestimos, headers=headers_user_02, data=novo_emprestimo)

assert emprestimo.status_code == 201
assert emprestimo.json()['cliente'] == novo_emprestimo['cliente']

novo_pagamento = {
    "emprestimo": "1",
    "valor_pago": "100.00"
}
pagamento = requests.post(url=url_pagamentos, headers=headers_user_01, data=novo_pagamento)

assert pagamento.status_code == 201
assert pagamento.json()['valor_pago'] == novo_pagamento['valor_pago']
