from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .serializers import CustomerSerializer
from .models import Customers

class CustomerCreateListAPIView(ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        print("errors", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    