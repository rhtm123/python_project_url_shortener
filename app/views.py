from django.shortcuts import render, redirect, Http404, HttpResponse
from .models import AppModel
# Create your views here.
import json
from django.core import serializers


def home(request):
    return render(request, 'home.html')


def creat_short_url(request):
    url = request.GET.get('url', None)
    try:
        model = AppModel.objects.get(main_url=url)
    except:
        model = AppModel(main_url=url,)
        model.save()
    data = serializers.serialize('json', [model, ])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    return HttpResponse(data, content_type='application/json')


def redirect_to_main_url(request, code):
    try:
        obj = AppModel.objects.get(code=code)
        main_url = obj.main_url
        return redirect(main_url)
    except:
        return render(request, 'error.html')
