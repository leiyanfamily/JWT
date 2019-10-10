from redis import StrictRedis

# 创建redis客户端
redis_client = StrictRedis(decode_responses=True)
user_id = 1
key = "token_{}".format(user_id)

