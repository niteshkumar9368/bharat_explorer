from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'places'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('all-states/', views.all_states, name='all_states'),
    path('state/<int:state_id>/', views.state_places, name='state_places'),
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
    path('register/', views.register, name='register'),  # Register route handled by places.views
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Custom login view with new template
    path('search/', views.search_places, name='search_places'),  # Search route
    path('add-place/', views.add_place, name='add_place'),  # New route for adding place
]
