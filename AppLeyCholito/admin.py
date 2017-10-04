from django.contrib import admin
from .models import Denuncia
from .models import Authentication
from .models import Login

admin.site.register(Denuncia)
admin.site.register(Authentication)
admin.site.register(Login)