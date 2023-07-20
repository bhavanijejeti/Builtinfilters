from django.shortcuts import render

# Create your views here.
import datetime
def builtinfilter(request):
    dt=datetime.datetime.now()
    d={'data':'hai bhavani reddy','c':15,'dt':dt}
    return render(request,'builtinfilter.html',d)