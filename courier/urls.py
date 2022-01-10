from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('',views.index,name='index'),
    path('adminApp',views.adminApp,name='adminApp'),
    path('index',views.index,name='index'),
    path('status2',views.status2,name='status2'),
    path('status',views.status,name='status'),
    path('track',views.track,name='track'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('send',views.send,name='send'),
    path('logout',views.logout,name="logout"),
    path('suggesions',views.suggesions,name="suggesions"),
    path('profile',views.profile,name="profile"),
    path('updateProfile',views.updateProfile,name="updateProfile"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)