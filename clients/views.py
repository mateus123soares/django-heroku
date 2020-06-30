from django.http import HttpResponse
from django.shortcuts import render


def list_clients(request):
    return HttpResponse("helloWorld")

def do_calculation(value1,value2):
    return value1 * value2

def test_function(request):
    tot = do_calculation(2,10)
    people = ['gregory','Jose','Pedro','John']
    p_flat = True
    return render(request,'exemple.html',{'total':tot,'people':people,'p_flat':p_flat})

def special_case_2003(request):
    return HttpResponse('retruning the case 2003')

def special_case(requset,year):
    return HttpResponse('returning the case %s' % year)

def month_arquive(request,year,month):
    return HttpResponse('returnig the case %s and month %s' % (year,month))

def hello(request,name):
    return HttpResponse('hello world %s' % name)
