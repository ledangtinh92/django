from django.conf import settings
from django.shortcuts import redirect

EXEMPT_URLS = ['/login', '/home', '/admin']

class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            path = request.path_info
            if path is not None and not any(path.startswith(url) for url in EXEMPT_URLS):
                return redirect(settings.LOGIN_URL)
        response = self.get_response(request)
        return response
