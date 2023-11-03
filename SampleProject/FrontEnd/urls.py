from django.urls import path
from FrontEnd import views

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('product_page/',views.product_page,name="product_page"),
    path('single_product/<int:proid>/',views.single_product,name="single_product"),
    path('filtered_product/<cat_name>/',views.filtered_product,name="filtered_product"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('services/',views.services,name="services"),
    path('contactus/',views.contactus,name="contactus"),
    path('contactdata/',views.contactdata,name="contactdata"),
    path('registerpage/',views.registerpage,name="registerpage"),
    path('registerdata/',views.registerdata,name="registerdata"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('cartdata/',views.cartdata,name="cartdata"),
    path('cart_delete/<int:pro_id>/',views.cart_delete,name="cart_delete"),
    path('checkoutpage/',views.checkoutpage,name="checkoutpage"),
    path('summarypage/',views.summarypage,name="summarypage"),
]