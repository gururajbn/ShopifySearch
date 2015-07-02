from django.conf.urls import patterns, include, url
from shopify_app.decorators import shop_login_required
from .views import home,Order
urlpatterns = patterns('',
        url(r'^$', shop_login_required(home.as_view()), name='root_path'),
        url(r'^order/(?P<pk>[0-9]+)/$', shop_login_required(Order.as_view()),name="order"),
       
)
