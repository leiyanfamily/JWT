from settings import redis_client, key


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