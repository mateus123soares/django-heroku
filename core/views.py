from django.shortcuts import render, redirect,get_object_or_404
from .models import Client
from .forms import New_client
from django.contrib.auth.decorators import login_required

@login_required()
def list_clients(request):
    clients = Client.objects.all()
    return render(request,'clients.html',{'clients':clients})
# Create your views here.

@login_required()
def new_client(request):
    form = New_client(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(list_clients)

    return render(request,'form.html',{'form':form})

@login_required()
def update_client(request,id):
    client = get_object_or_404(Client,pk=id)
    form = New_client(request.POST or None, request.FILES or None,instance=client)

    if form.is_valid():
       form.save()
       return redirect(list_clients)

    return render(request,'form.html',{'form':form})

@login_required()
def delete_client(request,id):
    client = get_object_or_404(Client,pk=id)

    if request.method == 'POST':
        client.delete()
        return redirect(list_clients)

    return render(request,'confirm.html',{'client':client})
