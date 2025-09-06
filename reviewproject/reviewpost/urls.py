# reviewpost/urls.py
from django.urls import path
from .views import signupview, loginview, listview, detailview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('list/', listview, name='list'),
    path('detail/<int:pk>', detailview, name='detail'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)