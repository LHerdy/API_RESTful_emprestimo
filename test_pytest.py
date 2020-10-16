import requests


class TestEmprestimos:
    headers_user_01 = {'Authorization': 'Token c9a956c3cbb79588ed023341cc468d9a69b22da1'}
    url_emprestimos = 'http://127.0.0.1:8000/emprestimos/'

    def test_get_emprestimos(self):
        emprestimos = requests.get(url=self.url_emprestimos, headers=self.headers_user_01)
        assert emprestimos.status_code == 200

    def test_get_emprestimo(self):
        emprestimo = requests.get(url=f'{self.url_emprestimos}2/', headers=self.headers_user_01)
        assert emprestimo.status_code == 200

    def test_post_emprestimo(self):
        novo = {
            "banco": "Banco 04",
            "cliente": "Cliente 04",
            "valor_nominal": "10000.00",
            "parcelas": 24,
            "taxa_de_juros": "3.00",
            "endereco_de_ip": "195.156.0.100"
        }
        resultado = requests.post(url=self.url_emprestimos, headers=self.headers_user_01, data=novo)
        assert resultado.status_code == 201


class TestPagamentos:
    headers_user_02 = {'Authorization': 'Token 04cb02eedd4b1a5222ccd371a11aa4cf367537f2'}
    url_pagamentos = 'http://127.0.0.1:8000/pagamentos/'

    def test_get_pagamentos(self):
        pagamentos = requests.get(url=self.url_pagamentos, headers=self.headers_user_02)
        assert pagamentos.status_code == 200

    def test_get_pagamento(self):
        pagamento = requests.get(url=f'{self.url_pagamentos}/1', headers=self.headers_user_02)
        assert pagamento.status_code == 200

    def test_post_pagamento(self):
        novo = {
            "emprestimo": "2",
            "valor_pago": "100.00"
        }
        resultado = requests.post(url=self.url_pagamentos, headers=self.headers_user_02, data=novo)
        assert resultado.status_code == 201
