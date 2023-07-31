from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from . import views
from .forms import LoginForm, ChangePasswordForm

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('add/', views.add, name='add'),
    path('comment/', views.comment, name='comment'),
    path('submit_assignments/', views.submit_assignments,
         name='submit_assignments'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('feedback/', views.feedback, name='feedback'),
    path('add_html_videos/', views.add_html_videos, name='htmlvideos'),
    path('add_js_videos/', views.add_js_videos, name='jsvideos'),
    path('add_python_videos/', views.add_python_videos, name='pythonvideos'),
    path('terms_and_conditions/', views.terms_and_conditions,
         name='terms_and_conditions'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='core/changepassword.html',
         success_url=reverse_lazy('changepassworddone'), form_class=ChangePasswordForm), name='changepassword'),
    path('changepassworddone/', auth_views.PasswordChangeDoneView.as_view(
        template_name='core/changepassworddone.html'), name='changepassworddone'),
    path('info/', views.info, name='info'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',
         authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
