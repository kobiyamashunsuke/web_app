from django.conf.urls import url
from cms import views


urlpatterns = [
    # 書籍
    url(r'^home/$', views.home, name='home'),
    url(r'^book/$', views.book_list, name='book_list'),   # 一覧
    url(r'^book/add/$', views.book_edit, name='book_add'),  # 登録
    url(r'^book/mod/(?P<book_id>\d+)/$', views.book_edit, name='book_mod'),  # 修正
    url(r'^book/del/(?P<book_id>\d+)/$', views.book_del, name='book_del'),   # 削除

    url(r'^python/$', views.python_book_list, name='python_book_list'),   # 一覧
    url(r'^python/add/$', views.python_book_edit, name='python_book_add'),  # 登録
    url(r'^python/mod/(?P<python_book_id>\d+)/$', views.python_book_edit, name='python_book_mod'),  # 修正
    url(r'^python/del/(?P<python_book_id>\d+)/$', views.python_book_del, name='python_book_del'),   # 削除

    # 感想
    url(r'^impression/(?P<book_id>\d+)/$', views.ImpressionList.as_view(), name='impression_list'),  # 一覧
    url(r'^impression/add/(?P<book_id>\d+)/$', views.impression_edit, name='impression_add'),  # 登録
    url(r'^impression/mod/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.impression_edit, name='impression_mod'),  # 修正
    url(r'^impression/del/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.impression_del, name='impression_del'),   # 削除

    url(r'^python_impression/(?P<python_book_id>\d+)/$', views.python_ImpressionList.as_view(), name='python_impression_list'),  # 一覧
    url(r'^python_impression/add/(?P<python_book_id>\d+)/$', views.python_impression_edit, name='python_impression_add'),  # 登録
    url(r'^python_impression/mod/(?P<python_book_id>\d+)/(?P<python_impression_id>\d+)/$', views.python_impression_edit, name='python_impression_mod'),  # 修正
    url(r'^python_impression/del/(?P<python_book_id>\d+)/(?P<python_impression_id>\d+)/$', views.python_impression_del, name='python_impression_del'),   # 削除
]

