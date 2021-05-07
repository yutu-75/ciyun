from celery import Celery



import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ciyunapi.settings.dev')


# 创建celery主程序对象
app = Celery("ciyunapi")

import django
django.setup()

# 加载配置
app.config_from_object("mycelery.config")

# 注册任务
# app.autodiscover_tasks(["mycelery.ciyun_img", "mycelery.sms","mycelery.mail"])
app.autodiscover_tasks(["mycelery.ciyun_img",])
# 通过终端来启动celery
# celery -A mycelery.main worker --loglevel=info