# 第9章 編集フォームを作ろう（Update）
from django.views.generic import ListView, DetailView  # ★ DetailView を追記（第13章：詳細表示）
from django.views.generic.edit import CreateView, UpdateView   # ★ UpdateView を追記
from django.urls import reverse_lazy                           # ★ 更新/作成後に一覧へ戻すなら追記（推奨）
from django.views.generic.edit import DeleteView   #★10章：削除フォームを追加

from .models import Product


class ProductListView(ListView):
    model = Product
    paginate_by = 3
    template_name = "core/product_list.html"


class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("list")                          # ★ 追加（推奨：作成後に一覧へ）


class ProductUpdateView(UpdateView):                            # ★ 追加（編集フォーム用）
    model = Product
    fields = "__all__"
    template_name = "core/product_update_form.html"             # ★ 追加（編集用テンプレ）
    success_url = reverse_lazy("list")                          # ★ 追加（更新後に一覧へ）


class ProductDeleteView(DeleteView):                            # ★ 10章：削除フォームを追加
    model = Product
    success_url = reverse_lazy('list')  # 削除後に一覧へ戻す


class ProductDetailView(DetailView):                             # ★第13章：商品詳細ページ
    model = Product
    template_name = "core/product_detail.html"                  # ★ 追加（詳細用テンプレ）
