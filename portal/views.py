from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm

from .models import User

# forms

class UserDetailForm(ModelForm):
    class Meta:
        model = User
        fields= '__all__'

# Create your views here.
def index(request):
    return HttpResponse("Hello from the server side!")

def register(request):
    if request.method == 'POST':
        form = UserDetailForm(request.POST)
        if form.is_valid():
            return HttpResponse('Thanks for registering!')
    # default empty form
    else:
        form = UserDetailForm()

    return render(request, 'register.html', {'form': form, 'submit_url': request.get_full_path})
