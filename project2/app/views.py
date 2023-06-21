from django.shortcuts import render
from rest_framework import serializers
# Create your views here.
from app.models import *
from rest_framework.views import APIView
from app.serializers import *
from rest_framework.response import Response

class Productcurd(APIView):
    def get(self, request, pid):
        PRD=Product.objects.all()
        PCD=ProductCS(PRD,many=True)
        return Response(PCD.data)
    
    def post(self, request, pid):
        PSD=ProductCS(data=request.data)
        if PSD.is_valid():
            PSD.save()
            return Response({'MSG':'Product is created'})
        else:
            return Response({'MSG':'Product creation is failed'})
        
    def put(self, request, pid):
        pid=request.data['pid']
        productob=Product.objects.get(pid=pid)
        PO=ProductCS(productob,data=request.data)
        if PO.is_valid():
            PO.save()
            return Response({'MSG':'Product is updated'})
        else:
            return Response({'MSG':'Product is not updated'})

    def patch(self, request, pid):
        pid=request.data['pid']
        productob=Product.objects.get(pid=pid)
        PO=ProductCS(productob,data=request.data,partial=True)
        if PO.is_valid():
            PO.save()
            return Response({'MSG':'Product is updated'})
        else:
            return Response({'MSG':'Product is not updated'})
    
    def delete(self, request, pid):
        Product.objects.get(pid=pid).delete()
        return Response({'MSG':'Success'})