from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    # path('', views.home),
    path('',views.productViws.as_view(), name="home"),


    path('product-detail/<int:pk>', views.ProductDetailView.as_view() , name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),

    path('changepassword/', views.change_password, 
    name='changepassword'),
    #  this is laptop
    # path('laptop/', views.laptop, name='laptop'),
    # path('laptop/<slug:data>', views.laptop, name='laptopdata'),
#  this is loptop
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    path('accounts/login', auth_views.LoginView.as_view
         (template_name='app/login.html',
          authentication_form=LoginForm), name='login'),
          
    path('logout/', auth_views.LogoutView.as_view(next_page='logout'), name='logout'),


    path('registration/', views.CustomerRegistrationView.
    as_view(), name="customerregistration")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

