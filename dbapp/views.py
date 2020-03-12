from django.shortcuts import render
from .models import Domain, DomainFlag
from datetime import datetime


def is_active_flag(valid_from, valid_to=datetime.max):
    if not valid_to:
        valid_to = datetime.max
    return valid_from < datetime.now() < valid_to


def make_list_of_active_flags(domain_flags):
    return [df for df in domain_flags if is_active_flag(df.valid_from, df.valid_to)]


def index(request):
    domains = Domain.objects.all().order_by('id')
    domain_flags = DomainFlag.objects.all()
    valid_domain_flags = make_list_of_active_flags(domain_flags)
    return render(request, 'dbapp/domains_view.html', {'domains': domains, 'domain_flags': valid_domain_flags})


def domain_view(request, pk):
    domain0 = Domain.objects.filter(id=pk)[0]
    domain_flags = DomainFlag.objects.filter(domain=domain0)
    valid_domain_flags = make_list_of_active_flags(domain_flags)
    return render(request, 'dbapp/domain_view.html', {'domain': domain0, 'domain_flag': valid_domain_flags})

