from django.shortcuts import render
from .models import Domain, DomainFlag


def index(request):
    domains = Domain.objects.all()
    return render(request, 'dbapp/domains_view.html', {'domains': domains})

def domain_view(request, pk):
    domain0 = Domain.objects.filter(id=pk)[0]
    domain_flag = DomainFlag.objects.filter(domain = domain0)
    return render(request, 'dbapp/domain_view.html', {'domain': domain0, 'domain_flag': domain_flag})

