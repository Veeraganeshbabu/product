from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Product

# Create your views here.
class ProductInput(View):
    def get(self,request):
        return render(request, 'p_input.html')

class ProductInsert(View):
    def get(self,request):
        p_id = int(request.GET['pro_id'])
        p_name = request.GET['pro_name']
        p_cost = float(request.GET['pro_cost'])
        p_mfdt = request.GET['pro_mfdt']
        p_expdt = request.GET['pro_expdt']
        p1 = Product(pid =p_id,pname =p_name,pcost = p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        res = HttpResponse('product inserted successfully')
        return res