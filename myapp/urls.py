
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from myapp import views
from wanderlust import settings

urlpatterns = [
    path('',views.login),
    path('logout',views.logout),
    path('login_post',views.login_post),
    path('admin_home',views.admin_home),
    path('admin_add_package',views.admin_add_package),
    path('view_packages',views.view_packages),
    path('admin_add_place',views.admin_add_place),
    path('admin_view_place',views.admin_view_place),
    path('delete_place/<id>',views.delete_place),
    path('delete_user/<id>',views.delete_user),
    path('delete_packages/<id>',views.delete_packages),


    path('admin_add_hotel',views.admin_add_hotel),
    path('view_hotel',views.view_hotel),
    path('delete_hotel/<id>',views.delete_hotel),
    path('view_users',views.view_users),
    path('view_hotel_booking',views.view_hotel_booking),
    path('view_package_booking',views.view_package_booking),
    path('view_complaints',views.view_complaints),
    path('view_feedback',views.view_feedback),
    path('admin_view_guide',views.admin_view_guide),
    path('sendreply_post',views.sendreply_post),
    path('send_reply/<id>',views.send_reply),


    path('user_reg',views.user_reg),
    path('user_home',views.user_home),
    path('user_view_place',views.user_view_place),
    path('user_view_place_post',views.user_view_place_post),
    path('user_view_profile',views.user_view_profile),
    path('user_view_packages',views.user_view_packages),
    path('user_view_packages_post',views.user_view_packages_post),
    path('userview_hotel',views.userview_hotel),
    path('userview_hotel_post',views.userview_hotel_post),
    path('user_book_hotel_post',views.user_book_hotel_post),
    path('user_view_hotel_booking',views.user_view_hotel_booking),
    path('user_view_package_booking',views.user_view_package_booking),
    path('user_book_hotel/<id>',views.user_book_hotel),
    path('user_book_packages_post/<id>',views.user_book_packages_post),
    path('send_complaint',views.send_complaint),
    path('user_view_complaint',views.user_view_complaint),
    path('user_send_feedback',views.user_send_feedback),
    path('user_view_guide',views.user_view_guide),
    path('user_view_guide_post',views.user_view_guide_post),
    path('user_view_guide_booking',views.user_view_guide_booking),


    path('admin_add_guide',views.admin_add_guide),
    path('user_book_guide_post',views.user_book_guide_post),
    path('delete_guide/<id>',views.delete_guide),
    path('user_book_guide/<id>',views.user_book_guide),


    path('guide_home',views.guide_home),
    path('giude_view_booking',views.giude_view_booking),
    path('guide_view_user',views.guide_view_user),


    path('chat_view',views.chat_view),
    path('guide_chat_to_user/<id>',views.guide_chat_to_user),
    path('chat_send/<msg>', views.chat_send),


    path('user_chat_to_guide/<id>', views.user_chat_to_guide),
    path('chat_view1', views.chat_view1),
    path('chat_send1/<msg>', views.chat_send1),

    path('package_user_pay_proceed/<id>/<amt>', views.package_user_pay_proceed),
    path('package_on_payment_success', views.package_on_payment_success),

    path('user_pay_proceed/<id>/<amt>', views.user_pay_proceed),
    path('on_payment_success', views.on_payment_success),

    path('guide_booking_user_pay_proceed/<id>/<amt>', views.guide_booking_user_pay_proceed),
    path('guide_on_payment_success', views.guide_on_payment_success),

]
