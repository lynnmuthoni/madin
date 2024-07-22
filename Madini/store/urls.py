from django.urls import path
from . import views

# app_name = 'app_store'

urlpatterns = [
    # path('',views.store,name='store'),
    path('',views.test,name='test'),
    
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('insert_cart/',views.insert_into_cart,name='insert_cart'),
    path('cart/update_item/',views.update_item_quantity,name='update_item'),
    path('order_details/',views.order_details,name='order_details'),
    path('item_detail/<int:id>',views.item_detail,name='item_detail'),
    path('make_payment/<int:id>',views.make_payment,name='make_payment'),
    path('delete_address/<int:id>', views.delete_address, name='delete_address'),
    path('show_items/<int:id>',views.show_items,name='show_items'),
    path('search/',views.search,name='search'),
    path('update_address/<int:id>',views.update_address,name='update_address'),
    path('test_shop/<int:id>',views.test_shop,name='test_shop'),
    path('test_item_detail/<int:id>',views.test_item_detail,name='test_item_detail'),
    path('test_cart/',views.test_cart,name='test_cart'),
    path('test_checkout/',views.test_checkout,name='test_checkout'),
    path('test_testimonials/',views.test_testimonials,name='test_testimonials'),
    path('test_contactus/',views.test_contactus,name='test_contactus'),

]