"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# django自带用户模块
from django.contrib.auth import views as auth_views


from boards import views

from user import views as user_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 首页
    url(r'^$', views.home, name='home'),
    # 板块页
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    # 发布文章页
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    # 注册
    url(r'^register/$', user_views.register, name='register'),
    # 登录 as_view()中，可以传递一些额外的参数，以覆盖默认值
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # 登出
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    # 修改密码，仅适合登录用户，他们使用名为 @login_required的装饰器，此装饰器可防止非授权用户访问此页面。
    # 如果用户没有登录，Django会将他们重定向到登录页面。
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
    # 文章路径
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    # 评论路径
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
]
