from django.shortcuts import render, redirect
from .models import Client, Policy, Claim
from .forms import ClientForm, PolicyForm, ClaimForm

def home(request):
    clients = Client.objects.all()
    return render(request, 'insurance/home.html', {'clients': clients})
def addclient(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.isvalid():
            form.save()
            return redirect('home')
    else:
        form = ClientForm()
    return render(request, 'insurance/addclient.html', {'form': form})

def addpolicy(request):
    if request.method == 'POST':
        form = PolicyForm(request.POST)
        if form.isvalid():
            form.save()
            return redirect('home')
    else:
        form = PolicyForm()
    return render(request, 'insurance/addpolicy.html', {'form': form})

def addclaim(request):
    if request.method == 'POST':
        form = ClaimForm(request.POST)
        if form.isvalid():
            form.save()
            return redirect('home')
    else:
        form = ClaimForm()
    return render(request, 'insurance/addclaim.html', {'form': form})
