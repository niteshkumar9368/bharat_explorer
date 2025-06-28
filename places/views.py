# places/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import State, TouristPlace, PlaceImage
from django.contrib.auth.forms import UserCreationForm
from .forms import TouristPlaceForm  # ✅ Make sure you have this form created
from .forms import TouristPlaceForm
from django.db.models import Q
from accounts.decorators import first_user_required

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    # Fetch 6 featured states (e.g., first 6 states)
    featured_states = State.objects.all()[:6]
    # Fetch 6 recent temples ordered by id descending
    recent_temples = TouristPlace.objects.all().order_by('-id')[:6]
    return render(request, 'places/home.html', {'featured_states': featured_states, 'recent_temples': recent_temples})

@login_required(login_url='login')
@first_user_required
def add_place(request):
    if request.method == 'POST':
        form = TouristPlaceForm(request.POST, request.FILES)
        files = request.FILES.getlist('gallery_images')
        if form.is_valid():
            place = form.save()
            for f in files:
                PlaceImage.objects.create(place=place, image=f)
            return redirect('places:place_detail', place_id=place.id)
    else:
        form = TouristPlaceForm()
    return render(request, 'places/add_place.html', {'form': form})

@login_required(login_url='login')
def all_states(request):
    states = State.objects.all()
    return render(request, 'places/all_states.html', {'states': states})

@login_required(login_url='login')
def state_places(request, state_id):
    state = get_object_or_404(State, id=state_id)
    places = TouristPlace.objects.filter(state=state)
    return render(request, 'places/state_places.html', {'state': state, 'places': places})  # ✅ fixed path

@login_required(login_url='login')
def place_detail(request, place_id):
    place = get_object_or_404(TouristPlace, pk=place_id)
    return render(request, 'places/place_detail.html', {'place': place})  # ✅ correct already

from django.contrib.auth import get_user_model, login
from django.contrib import messages

User = get_user_model()

def register(request):
    from .forms import RelaxedUserCreationForm
    if request.method == 'POST':
        form = RelaxedUserCreationForm(request.POST)
        if form.is_valid():
            user_count = User.objects.count()
            user = form.save(commit=False)
            if user_count == 0:
                user.is_superuser = True
                user.is_staff = True
            else:
                user.is_superuser = False
                user.is_staff = False
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('places:home')
    else:
        form = RelaxedUserCreationForm()
    return render(request, 'places/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'places/login_register.html'

@login_required(login_url='login')
def search_places(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = TouristPlace.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    return render(request, 'places/search_results.html', {'results': results, 'query': query})
