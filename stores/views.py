from rest_framework import generics
from .models import Stores
from .serializers import StoresSerializers

class StoreView(generics.CreateAPIView):
    queryset = Stores.objects.all()
    serializer_class = StoresSerializers

    