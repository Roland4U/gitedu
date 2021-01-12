from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('subscribe_mail', subscribe_mail, name='subscribe_mail'),
    path('facultet/<fac_slug>/', facultet_det, name='facultet_det'),
    path('service/<serv_slug>/', service_det, name='service_det'),
    path('facultets', facultets, name='facultets'),
    path('<fac_slug>/<tr_slug>/', training_det, name='training_det'),
    path('login', login1),
    path('save_reg', save_reg),
    path('reg_to_tr', reg_to_tr, name='reg_to_tr'),
    path('reg_to_serv', reg_to_serv, name='reg_to_serv'),
]
