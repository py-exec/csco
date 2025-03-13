from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Customer, Address, PhoneNumber
from .serializers import CustomerSerializer, AddressSerializer, PhoneNumberSerializer

# === 1. دریافت لیست مشتریان ===
@api_view(['GET'])
def api_customer_list(request):
    customers = Customer.objects.all().order_by('-registered_at')
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# === 2. ایجاد مشتری جدید ===
@api_view(['POST'])
def api_create_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "مشتری با موفقیت ثبت شد!", "customer": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# === 3. دریافت، ویرایش و حذف مشتری ===
@api_view(['GET', 'PUT', 'DELETE'])
def api_customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "اطلاعات مشتری به‌روزرسانی شد!", "customer": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response({"message": "مشتری حذف شد!"}, status=status.HTTP_204_NO_CONTENT)

# === 4. جستجوی مشتریان ===
@api_view(['GET'])
def api_search_customers(request):
    query = request.GET.get('q', '').strip()
    customers = Customer.objects.filter(name__icontains=query)[:10]
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)