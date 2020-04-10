BROKER_URL = 'redis://127.0.0.1:6379'               # 指定broker
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'  # 指定backend

CELERY_TIMEZONE = 'Asia/Shanghai'

# 指定需要导入的任务模块
# task1和task2是模块名称
CELERY_IMPORTS = (
    'learn_celery.task1',
    'learn_celery.task2',
)
