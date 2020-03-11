from django.shortcuts import render
from .models import Domain, DomainFlag
from datetime import datetime

def active_flag(valid_from, valid_to):
    if not valid_to:
        valid_to = datetime.max
    return valid_from < datetime.now() < valid_to

def make_list_of_active_flags(domain_flags):
    valid_domain_flags = []
    for i in domain_flags:
        if active_flag(i.valid_from, i.valid_to):
            valid_domain_flags.append(i)
    return valid_domain_flags


def index(request):
    domains = Domain.objects.all()
    domain_flags = DomainFlag.objects.all()
    valid_domain_flags = make_list_of_active_flags(domain_flags)
    return render(request, 'dbapp/domains_view.html', {'domains': domains, 'domain_flags': valid_domain_flags})



def domain_view(request, pk):
    domain0 = Domain.objects.filter(id=pk)[0]
    domain_flags = DomainFlag.objects.filter(domain = domain0)
    valid_domain_flags = make_list_of_active_flags(domain_flags)
    return render(request, 'dbapp/domain_view.html', {'domain': domain0, 'domain_flag': valid_domain_flags})

