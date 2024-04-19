# /home/daniel/Dokumente/Env/Django Projekt/Whlpf_Django_Project/bibliothek/lib_app/middleware.py

from django.contrib.auth import logout

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Überprüfen, ob der Benutzer eingeloggt ist
        if request.user.is_authenticated:
            # Wenn der Benutzer eingeloggt ist, führen Sie die Abmeldung durch
            logout(request)

        return response
