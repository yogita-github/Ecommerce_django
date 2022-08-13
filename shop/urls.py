from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('head/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),

    path('orders/', include('orders.urls')),
    path('razorpay/callback/', views.callback, name="callback"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

