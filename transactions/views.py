from datetime import datetime

from rest_framework import generics

from rest_framework.views import Response, status
from rest_framework.pagination import PageNumberPagination

from .models import Transaction
from .serializers import TransactionSerializer

from stores.models import Stores

class TransactionView(
    generics.ListCreateAPIView,
    PageNumberPagination,
):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        arquivo = request.FILES["cnab"]

        for transaction in arquivo:
            transaction = transaction.decode("utf-8")
            tipo = transaction[0]
            data = datetime.strptime(transaction[1:9], "%Y%m%d").date()
            valor = float(transaction[9:19]) / 100
            cpf = transaction[19:30]
            cartao = transaction[30:42]
            hora = datetime.strptime(transaction[42:48], "%H%M%S").time()
            dono_loja = transaction[48:62]
            nome_loja = transaction[62:81]

            type_transactions = {
                "type": tipo,
                "date": data,
                "value": valor,
                "cpf": cpf,
                "card": cartao,
                "hour": hora,
                "store_owner": dono_loja,
                "store_name": nome_loja,
            }

            store = Stores.objects.get_or_create(
                store_owner=dono_loja,
                store_name=nome_loja,
            )

            if store[0].store_name == type_transactions["store_name"]:
                if type_transactions["type"] in ["1", "4", "5", "6", "7", "8"]:
                    store[0].balance += type_transactions["value"]

                if type_transactions["type"] in ["2", "3", "9"]:
                    store[0].balance += type_transactions["value"] * -1

            store[0].save()

            serializer = TransactionSerializer(data=type_transactions)
            serializer.is_valid(raise_exception=True)
            serializer.save(store=store[0])

        return Response(type_transactions, status.HTTP_201_CREATED)
