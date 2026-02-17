from django.apps import AppConfig

# **Djangoに「core というアプリの設定情報」を登録するための“アプリ設定クラス”**

class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'core'
