import random

from settings import redis_client, key


def login():
    """登录"""
    print('登录成功')
    # 生成token
    token = random.randint(100, 999)
    # 判断用户是否修改过密码(redis中是否有该用户对应的key)
    if redis_client.exists(key):
        # 有key, 说明修改过密码, 将token加入白名单
        redis_client.sadd(key, token)