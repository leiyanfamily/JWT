from redis import StrictRedis

# 创建redis客户端
redis_client = StrictRedis(decode_responses=True)
user_id = 1
key = "token:{}".format(user_id)
token = 0