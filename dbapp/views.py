from django.shortcuts import render
from .models import Domain
# Create your views here.
from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello, world. You're at the db_app index.")
def index(request):
    domains = Domain.objects.all()
    return render(request, 'dbapp/domains_view.html', {'domains': domains})

def domain_view(request, pk):
    domain = Domain.objects.filter(id=pk)
    return render(request, 'dbapp/domain_view.html', {'domain': domain})

