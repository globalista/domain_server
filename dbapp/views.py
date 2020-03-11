from django.shortcuts import render
from .models import Domain, DomainFlag
from datetime import datetime

def active_flag(valid_from, valid_to):
    if not valid_to:
        valid_to = datetime.max
    return valid_from < datetime.now() < valid_to


def index(request):
    domains = Domain.objects.all()
    return render(request, 'dbapp/domains_view.html', {'domains': domains})

def domain_view(request, pk):
    domain0 = Domain.objects.filter(id=pk)[0]
    domain_flag = DomainFlag.objects.filter(domain = domain0)
    valid_domain_flag = []
    for i in domain_flag:
        if active_flag(i.valid_from, i.valid_to):
            valid_domain_flag.append(i)
    return render(request, 'dbapp/domain_view.html', {'domain': domain0, 'domain_flag': valid_domain_flag})

