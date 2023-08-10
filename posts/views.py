from django.http import HttpResponse

def index(request):
    return HttpResponse('<h2>welcome to Django</h2>')

def home(request):
    return HttpResponse('<h3>wellcome to my blog</h3>')

