import hashlib

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.crypto import get_random_string


def pg_records(request, all_list, num=10):
    page = request.GET.get('page', 1)
    paginator = Paginator(all_list, num)

    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)

    return records


def generate_activation_key(username):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(20, chars)
    return hashlib.sha256((secret_key + username).encode('utf-8')).hexdigest()
