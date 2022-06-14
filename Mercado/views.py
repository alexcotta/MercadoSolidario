from django.shortcuts import render
from django.utils.formats import date_format
from pkg_resources import require
from .models import Estoque, Atendimento,ItensAtendimento,ProdutoSolidario,FonteDoacao,CodBarProdSol
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import FormAtendimento
from datetime import date, datetime
from django.db import connection
from django.contrib import messages

# Create your views here.
def logout_view(request):
    logout(request)
    return render(request,'index.html')

def fromCursorToTableData(cursor,rows):
   x = cursor.description
   resultsList = []   
   for r in rows:
      i = 0
      d = {}
      while i < len(x):
         d[x[i][0]] = r[i]
         i = i+1
      resultsList.append(d)
   return resultsList

@login_required
def estoque_listagem(request):
    return render(request,'estoque/estoque_lista.html',
    { 
        'estoque' : Estoque.objects.all().order_by('id_produto')
    })

@login_required
def estoque_listagem_validade(request):
    return render(request,'estoque/estoque_lista_validade.html',
    {
         'estoque' : Estoque.objects.all().order_by('validade')
    })

@login_required
def estoque_listagem_prodSol(request):
   return render(request,'estoque/estoque_lista_quantidade.html',
   {
       'estoque' : getEstoquePorProduto()
   })

def getEstoquePorProduto():
    with connection.cursor() as cursor:
        cursor.execute( 
            'select id_produto_id as produto, sum(quantidade) as quantidade from Mercado_estoque group by id_produto_id order by id_produto_id')
        row = cursor.fetchall()
        result = fromCursorToTableData(cursor,row)
    return result



