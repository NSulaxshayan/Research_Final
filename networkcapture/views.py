from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
import json 
from .utils import capture_traffic
from .models import NetworkCapture

@login_required(login_url="/login/")
def scan_network(request):
    if request.method == "POST":
        capture_traffic()
        return redirect('pulse_view')
    return render(request, 'home/index.html')

@login_required(login_url="/login/")
def pulse_view(request):
    captures = NetworkCapture.objects.all().values('timestamp', 'length')  # Adjust fields as necessary
    captures_json = json.dumps(list(captures), cls=DjangoJSONEncoder)
    return render(request, 'home/pulse-view.html', {'captures': captures_json})


# Create your views here.
