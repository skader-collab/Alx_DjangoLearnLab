from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from .forms import UserRegisterForm
from django.contrib.auth.models import User



def index(request):
    return render(request, 'blog/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

class ProfileUpdateView(UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'blog/profile_update.html'

    def get_object(self):
        return self.request.user
