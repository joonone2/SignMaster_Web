from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views


urlpatterns = [

    path('', views.selectoption_view, name='test'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('get_predicted_action', views.get_predicted_action, name='get_predicted_action'),
    path('get_new_action/', views.get_new_action, name='get_new_action'),
    path("admin/", admin.site.urls),

    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.Signup.as_view(), name='signup'),

    path('selectoption/', views.selectoption_view, name='selectoption'),
    path('learnsignlanguage/', views.learn_sign_language_view, name='learn'),
    #path('learn/<str:nickname>/<str:word>/', views.learn_word_view, name='learn_word'),
    path('learn/<str:word>/', views.learn_word_view, name='learn_word'),
    path('makename/', views.make_name_view, name='make_name'),
    path('make_name/', views.make_name_view, name='make_name'),
    path('test/<str:nickname>/', views.index, name='test_page'),


    #path('', )

]
