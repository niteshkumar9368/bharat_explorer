from django.shortcuts import redirect
from functools import wraps
from django.contrib.auth import get_user_model

User = get_user_model()

def first_user_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        # Check if the user is the first registered user (id=1)
        try:
            first_user = User.objects.order_by('date_joined').first()
        except User.DoesNotExist:
            return redirect('login')
        if request.user.pk != first_user.pk:
            return redirect('places:home')  # or some "access denied" page
        return view_func(request, *args, **kwargs)
    return _wrapped_view
