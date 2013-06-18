# Create your views here.

from django.http import HttpResponse
from django.template import loader, Context


def index(request):
    t = loader.get_template('index.html')
    html = t.render(Context({'', ''}))
    return HttpResponse(html)


