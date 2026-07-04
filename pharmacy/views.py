from django.http import HttpResponse

def home(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Welcome to Medicare, {request.user.username}! <a href='/accounts/logout/'>Logout</a>")
    else:
        return HttpResponse("Medicare is Live! <a href='/accounts/login/'>Login</a>")
