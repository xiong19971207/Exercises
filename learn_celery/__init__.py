from celery import Celery

app = Celery('learn_celery')
app.config_from_object('learn_celery.celeryconfig')  # 使用config_from_object函数加载一个配置文件
