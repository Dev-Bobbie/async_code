from __future__ import absolute_import, unicode_literals
import os
import sys

# set current path for import path
sys.path.insert(0,os.getcwd())

# ## Note: Start worker with -P gevent,
# do not use the worker_pool option.
# 设置broker的信息
broker_url = 'redis://192.168.33.11:6379/0'
# 设置结果存储信息
result_backend = 'redis://192.168.33.11:6379/1'
# 设置结果的过期事件
result_expires = 30 * 60

# 设置含有task模块的模块名称
# imports = ('tasks',)