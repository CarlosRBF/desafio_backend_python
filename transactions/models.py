from django.db import models


class TypeTransaction(models.TextChoices):
    DEFAULT = None
    DEBITO = 1
    BOLETO = 2
    FINANCIAMENTO = 3
    CREDITO = 4
    EMPRESTIMO = 5
    VENDAS = 6
    TED = 7
    DOC = 8
    ALUGUEL = 9


class Transaction(models.Model):
    type = models.CharField(
        max_length=25, choices=TypeTransaction.choices, default=TypeTransaction.DEFAULT
    )
    date = models.DateField()
    value = models.DecimalField(decimal_places=2, max_digits=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    store_owner = models.CharField(max_length=155)
    store_name = models.CharField(max_length=155)

    store = models.ForeignKey(
        "stores.Stores",
        on_delete=models.CASCADE,
        related_name="transactions_stores",
    )
