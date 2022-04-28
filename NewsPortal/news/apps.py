from django.apps import AppConfig
import redis

class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        import news.signals


red = redis.Redis(
    host='redis-12373.c282.east-us-mz.azure.cloud.redislabs.com',
    port=12373,
    password='Dm5vcIB79mdAE9wZoIi9osIz2zvsiZix'
)
