from django.contrib import admin
from django.urls import path
from render import views
from authentication import views as auth_views 


urlpatterns = [
    path('home/', views.index , name="index"),
    path('scrappator/',views.scrappator,name="application"),
    path('about/',views.about,name="about"),
    path('admin/', admin.site.urls),
    path('',auth_views.LoginPageView.as_view(),name="login"),
    path ('signup/',auth_views.signup_page, name="signup"),
    path('logout/',auth_views.logout_user,name="logout")
] 
