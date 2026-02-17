# 第9章 編集フォームを作ろう（Update）

from django.urls import path
from . import views

urlpatterns = [
     path("", views.ProductListView.as_view(), name="home"),   #データにリレーションを追加
    path("crud/", views.ProductListView.as_view(), name="list"),   #リスト追加
    path("crud/new/", views.ProductCreateView.as_view(), name="new"),   #新しいフォームを追加
    path("crud/detail/<int:pk>/", views.ProductDetailView.as_view(), name="detail"),   # ★第13章：詳細ページ（末尾スラッシュなし）
    path("crud/edit/<int:pk>/", views.ProductUpdateView.as_view(), name="edit"),   #編集フォーム追加
    path('crud/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),   # ★削除フォームを crud 配下に統一
]
