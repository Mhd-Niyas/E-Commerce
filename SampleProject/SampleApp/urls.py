from django.urls import path
from SampleApp import views

urlpatterns = [
    path('indexpage/',views.indexpage,name="indexpage"),
    path('categorypage/',views.categorypage,name="categorypage"),
    path('catdata/',views.catdata,name="catdata"),
    path('catdisplay/',views.catdisplay,name="catdisplay"),
    path('editcat/<int:editid>/',views.editcat,name="editcat"),
    path('updatecat/<int:updateid>/',views.updatecat,name="updatecat"),
    path('deletecat/<int:deleid>/',views.deletecat,name="deletecat"),
    path('addproduct/',views.addproduct,name="addproduct"),
    path('productdata/',views.productdata,name="productdata"),
    path('display_product/',views.display_product,name="display_product"),
    path('edit_product/<int:editid>/', views.edit_product, name="edit_product"),
    path('update_product/<int:updateid>/', views.update_product, name="update_product"),
    path('delete_product/<int:deleid>/',views.delete_product,name="delete_product"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('contact_display/',views.contact_display,name="contact_display"),
]