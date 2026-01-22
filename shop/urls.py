from django.urls import path 
from . import views
urlpatterns=[
     path('',views.index,name='index'),
     path('about/',views.about,name='about'),
     path('contact/',views.contact,name='contact'),
     path('cart/',views.cart,name='cart'),
     path('service/',views.service,name='service'),
     path('gallery/',views.gallery,name='gallery'),
     path('product/',views.product,name='product'),
     path('signup/',views.signup,name='signup'),
     path('login/',views.user_login,name='login'),
     path('logout/',views.logout,name='logout'),
     

     path('dashboard/', views.indexDash, name='indexDash'),
     path('dashboard/add-product/', views.add_a_product, name='add_a_product'),
     path('dashboard/edit-product/<int:Pk>', views.edit_a_product, name='edit_a_product'),
     path('dashboard/delete-product/<int:Pk>', views.delete_product, name='delete_product'),
     path('dashboard/list-products/', views.list_product, name='list_product'),
     path('dashboard/add-customer/', views.add_a_customer, name='add_a_customer'),
     path('dashboard/edit-customer/<int:Pk>/', views.edit_a_customer, name='edit_a_customer'),
     path('dashboard/delete-customer/<int:Pk>/', views.delete_customer, name='delete_customer'),
     path('dashboard/list-customer/', views.list_customer, name='list_customer'),
     path('dashboard/add-order/', views.add_a_order, name='add_a_order'),
     path('dashboard/edit-order/<int:Pk>/', views.edit_a_order, name='edit_a_order'),
     path('dashboard/delete-order/<int:Pk>/', views.delete_order, name='delete_order'),
     path('dashboard/list-order/', views.list_order, name='list_order'),
     path('dashboard/add-orderitem/', views.add_a_orderitem, name='add_a_orderitem'),
     path('dashboard/edit-orderitem/<int:Pk>/', views.edit_a_orderitem, name='edit_a_orderitem'),
     path('dashboard/delete-orderitem/<int:Pk>/', views.delete_orderitem, name='delete_orderitem'),
     path('dashboard/list-orderitem/', views.list_orderitem, name='list_orderitem'),
     path('dashboard/blank/', views.pages_blank, name='pages_blank'),
     path('dashboard/profile/', views.pages_profile, name='pages_profile'),
     path('', views.pages_sign_in, name='pages_sign_in'),
     path('dashboard/sign-up/', views.pages_sign_up, name='pages_sign_up'),
     path('dashboard/sign-in/', views.pages_sign_in, name='pages_sign_in'),
     path('dashboard/upgrade/', views.upgrade_to_pro, name='upgrade_to_pro'),

    # Component / include pages
    path('dashboard/base/', views.base, name='base'),
    path('dashboard/footer/', views.footerDash, name='footerDash'),
    path('dashboard/nav/', views.navDash, name='navDash'),
    path('dashboard/side/', views.sideDash, name='sideDash'),

    # Charts / Maps / Icons
    path('dashboard/charts/', views.charts_chartjs, name='charts_chartjs'),
    path('dashboard/maps/', views.maps_google, name='maps_google'),
    path('dashboard/icons/', views.icons_feather, name='icons_feather'),

]
