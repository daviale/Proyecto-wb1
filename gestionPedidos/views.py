from django.views import View
from .models import Rol, Direccion, Category, Usuario, Product, List, client 
from django.http import JsonResponse
#from django.shortcuts import render

# Create your views here.
class RolListView(View):
    def get(self, request):
        clist =  Rol.objects.all()
        return JsonResponse(list(clist.values()), safe=False)
  

class RolDetailView(View):
    def get(self, request, pk):
        list =  Rol.objects.get(pk=pk)
        return JsonResponse(list)        

class DireccionListView(View):
    def get(self, request):
        dlist =  Direccion.objects.all()
        return JsonResponse(list(dlist.values()), safe=False)

class CategoryListView(View):
    def get(self, request):
        elist =  Category.objects.all()
        return JsonResponse(list(elist.values()), safe=False)

class UsuarioListView(View):
    def get(self, request):
        flist =  Usuario.objects.all()
        return JsonResponse(list(flist.values()), safe=False)        

class ProductListView(View):
    def get(self, request):
        glist =  Product.objects.all()
        return JsonResponse(list(glist.values()), safe=False)

class ListsListView(View):
    def get(self, request):
        hlist =  List.objects.all()
        return JsonResponse(list(hlist.values()), safe=False)

class ClientListView(View):
    def get(self, request):
        ilist =  client.objects.all()
        return JsonResponse(list(ilist.values()), safe=False)
