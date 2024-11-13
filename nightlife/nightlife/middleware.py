from django.utils import translation

class CookieLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Antes de la vista: activa el idioma basado en la cookie
        language = request.COOKIES.get('django_language', None)
        if language:
            translation.activate(language)
            request.LANGUAGE_CODE = language
        # Procesa la solicitud y obtiene la respuesta
        response = self.get_response(request)
        # Después de la vista: puedes modificar la respuesta aquí si es necesario
        return response
