from django.db import models
from django.urls import reverse

#第11章：データにリレーションを追加しよう

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

#第8章 新規作成フォームを作ろう

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # ★カタログ追加（第10章）
    img = models.ImageField(blank=True, default='nolmage.png')    # 第12章 画像を扱えるようにしよう

    description = models.TextField(blank=True)  # ★第13章：商品説明を追加

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("list")
