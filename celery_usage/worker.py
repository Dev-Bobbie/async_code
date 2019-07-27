import os

# 启动一个celery的worker工作进程
# -A 指定要运行的任务模块
# -l 执行log日志等级
# -P gevent表明使用gevent来运行任务

# Celery Worker 支持下列四种并发方式。
# celery.concurrency.solo (Single-threaded execution pool)
# celery.concurrency.prefork (Multiprocessing)
# celery.concurrency.eventlet
# celery.concurrency.gevent

os.system("celery -A tasks worker -E -l info -c 6 -P gevent")

