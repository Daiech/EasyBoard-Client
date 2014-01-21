#encoding:utf-8
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from EasyBoard.apps.website.views import home as core_home


def launcher(request):
    """VIEW OF THE CLIENT APP"""
    school_card = {"url": reverse("home_school_card"), "name": _(u"Carnetización"), "class": "school-card-icon"}
    apps1 = [
        school_card,
        # {"url": reverse("home_app4"), "name": "App unica", "class": "app-unica-icon"},
    ]
    apps2 = [{"url": "/app4", "name": "App4", "class": "otro"}]
    ctx = [
        {"user_type": 1, "apps": apps1},
        {"user_type": 2, "apps": apps2},
        {"user_type": 3, "apps": None},
        {"user_type": 4, "apps": None},
        {"user_type": 5, "apps": None},
    ]
    return core_home(request, ctx)