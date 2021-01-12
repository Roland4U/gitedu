from django.contrib import admin
from .models import facultet, training, subscribe, service, orderto, ordertoserv

# Register your models here.
admin.site.register(facultet)
admin.site.register(training)
admin.site.register(service)
admin.site.register(subscribe)
admin.site.register(orderto)
admin.site.register(ordertoserv)