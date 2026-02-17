# 第12章 画像を扱えるようにしよう

from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image_tag')  # ★ image_tag追加
    search_fields = ('name',)
    list_filter = ('category',)

    # ★ 追加（画像プレビュー）
    def image_tag(self, obj):
        return format_html('<img src="{}" width="80" height="80" />', obj.img.url)
    # ★ 追加ここまで


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Category, CategoryAdmin)








# from django.contrib import admin    #固定
# from .models import Product, Category

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price')  #一覧に表示する項目
#     search_fields = ('name',)               #検索可能にする項目

# admin.site.register(Product, ProductAdmin)

# # 第11章：データにリレーションを追加しよう

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("id", "name")
#     search_fields = ("name",)

# admin.site.register(Category, CategoryAdmin)