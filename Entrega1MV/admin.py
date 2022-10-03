from django.contrib import admin

from Entrega1MV.models import Mensaje, Subject, Usuario,Posteo

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Subject)
admin.site.register(Posteo)
admin.site.register(Mensaje)



