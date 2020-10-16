from django.contrib import admin

from emprestimos.models import Emprestimo, Pagamento

admin.site.register(Emprestimo)
admin.site.register(Pagamento)
