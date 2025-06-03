from django.http import HttpResponse
#create your views here
def welcome_view(request):
	print('This line added by view function names welcome_view...!!!')
	return HttpResponse('<h1>Custom Middleware Demo</h1> <hr />')
from django.http import HttpResponse
# Create your views here.
def home_page_view(request):
	return HttpResponse('<h1> Hello This is from home page view </h1><hr />')
from django.http import HttpResponse
# Create your views here.
def home_page_view2(request):
	print(10/0)
	return HttpResponse('<h1>Hello This is from home page view2</h1><hr />')
def pycharmview(req):
	return HttpResponse("<h1>Hello from Pycharm</h1><hr />")
def githubview(req):
	return HttpResponse("<h1>Hello from Github</h1><hr />")

