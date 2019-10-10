import random

from redis import StrictRedis

# 创建redis客户端
redis_client = StrictRedis(decode_responses=True)
user_id = 11
key = "token:{}".format(user_id)
token = None


def update_pwd():
    """修改密码"""
    print('密码修改成功')

    # 先判断是否有白名单, 如果有, 重置白名单
    if redis_client.exists(key):
        redis_client.delete(key)

    # 生成该用户对应的新白名单set
    redis_client.sadd(key, 0)
    # 设置白名单的过期时间
    redis_client.expire(key, 86400 * 14)


def login():
    """登录"""
    print('登录成功')
    # 生成token
    global token
    token = random.randint(100, 999)
    # 判断用户是否修改过密码(redis中是否有该用户对应的key)
    if redis_client.exists(key):
        # 有key, 说明修改过密码, 将token加入白名单
        redis_client.sadd(key, token)


def access():
    """访问接口"""
    print('验证token成功')
    # 判断用户是否修改过密码
    if redis_client.exists(key):
        # 修改过密码, 再判断该token是否在白名单中
        if redis_client.sismember(key, token):  # 在白名单中
            print('在白名单中, 正常访问')
        else:
            print('不在白名单中, 重新登录')
    else:  # 没有修改过密码
        print('没有改过密码, 正常访问')

if __name__ == '__main__':
    update_pwd()
    login()
    access()