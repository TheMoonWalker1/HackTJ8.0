from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from urllib.request import urlopen, Request
import json
import random


# Create your views here.
def landing(request):
    return render(request, 'start.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            prof = Profile(user=user)
            prof.save()

            messages.success(
                request, f"Your account has been created! You are now able to log in"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()

    return render(request, 'signup.html', {'form': form})


def home(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            vin = form.cleaned_data['vin']

            thing = Request(f'https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{vin}?format=json')

            response_body = {d['Variable']: d['Value'].upper() for d in json.loads(urlopen(thing).read())['Results'] if d['Value'] != '0' and d['Value'] != 0 and d['Value'] is not None and d['Value'] != '' and d['Value'] != 'Not Applicable' and d['Variable'] != 'Error Text'}
            return render(request, 'results.html', {'info': response_body})
        messages.error(request, 'This VIN is invalid. It must be 17 characters long.')

    vins = ['3GNEC12078G276688', '5GRGN23U83H132227', '1C3CDFBB5FD165342', '1FMZU62E12ZC12617', '2FAFP71W93X138259', '1FTPW12V17FA12080', '1FT8W3BT4FEA96950', 'WDXPD944555842209', 'WVGBV7AX6CW559712', 'SCFAC23302B500083', 'JH4KA7630NC013822', 'JH4DA175XGS009825', '1GCEK14K8RE106083', '4F2CU08102KM50866', 'JH4DA1850HS006058', '5N1AN0NU6BC506916', '1FVACYDC37HW59012']
    return render(request, 'home.html', {'form': CarForm(), 'vin': random.choice(vins)})