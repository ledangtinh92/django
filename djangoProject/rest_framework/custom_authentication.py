from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomAuthentication(JWTAuthentication):
    def authenticate(self, request):
        user_and_token = super().authenticate(request)
        if user_and_token is None:
            return None
        user, token = user_and_token
        if user is None or token is None:
            return None
        return user, token
