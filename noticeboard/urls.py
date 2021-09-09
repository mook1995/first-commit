from django.urls import path
from . import views #.은 현재 즉 노티스 파일을 말함

app_name = 'noticeboard'
urlpatterns = [
    path('',views.index, name='index'), #views 파일의 index라는 함수를 호출하고 이걸 index이라는 주소이름을 준다.
    #그래서 noticeboard로 들어오면 무조건 저 url을 거치는데 거기서 함수가 나오므로 함수를 통해 주소를 줄수 있는것이다.
    path('write/', views.write_article, name='write_article'),
    path('add/', views.add_article, name='add_article'),
    path('<int:article_id>/', views.view_article, name='view'),
    path('update/<int:article_id>/', views.update_article, name='update'),
    path('delete/<int:article_id>', views.delete_article, name='delete'),
]