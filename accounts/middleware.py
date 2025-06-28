from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """
    Middleware that requires a user to be authenticated to access any page except
    for login, logout, and register pages.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_paths = [
            reverse('login'),
            reverse('logout'),
            reverse('places:register'),
        ]

    def __call__(self, request):
        if not request.user.is_authenticated:
            path = request.path_info
            if path not in self.allowed_paths:
                return redirect('login')
        response = self.get_response(request)
        return response
