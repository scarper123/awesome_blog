# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

__authors__ = "Shanming Liu"


def blog_model_add(model, **kwargs):
    def wrapper(view):
        def inner(request, *args, **kwargs):
            return view(request, *args, **kwargs)

        return inner

    return wrapper
