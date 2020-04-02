from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf import settings

urlpatterns= [
 # path('',views.index, name='index'),
  path('homepage/',views.home_view,name='home'),
  path('',views.signup_view,name='signup'),
  path('login/',views.login_view,name='login'),
  path('sent/',views.activation_sent_view,name='activation_sent'),
  path('activate/<slug:uidb64>/<slug:token>/',views.activate,name='activate'),
  path('logout/',views.user_logout,name='logout'),
]

urlpatterns += static((settings.STATIC_URL), document_root=(settings.STATIC_ROOT))
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static((settings.MEDIA_URL), document_root=(settings.MEDIA_ROOT))
