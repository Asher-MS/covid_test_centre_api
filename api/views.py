from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Center
from .serializers import CenterSerialzer
from rest_framework import viewsets,permissions
from rest_framework.response import Response
# Create your views here.
def home(req):
    
    return(HttpResponse(Center.objects.all()[0]))



# class CenterViewSet(viewsets.ModelViewSet):
#     queryset=Center.objects.all()
#     serializer_class=CenterSerialzer
#     permission_classes=[permissions.AllowAny]



class CenterViewSet(viewsets.ViewSet):
    def list(self,req):
        # print(sample)
        queryset=Center.objects.all()
        serializer=CenterSerialzer(queryset,many=True)
        permission_classes=[permissions.AllowAny]
        return Response(serializer.data)
    def list_district(self,req):
        queryset=Center.objects.filter(district=req.GET.get("district"))
        serializer=CenterSerialzer(queryset,many=True)
        permission_classes=[permissions.AllowAny]
        return Response(serializer.data)
        



district_list=CenterViewSet.as_view({
    'get':'list_district'
})


center_list=CenterViewSet.as_view({
    'get':'list',


})