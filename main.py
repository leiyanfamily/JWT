from alterpwd import update_pwd
from login import login
from settings import redis_client, key


def access():
    """访问接口"""
    token = 0  # 获取jwt_token
    print('验证token成功')
    # 判断用户是否修改过密码
    if redis_client.exists(key):
        # 修改过密码, 再判断该token是否在白名单中
        if redis_client.sismember(key, token):  # 在白名单中
            print(token)
            print('在白名单中, 正常访问')
        else:
            print('不在白名单中, 重新登录')
    else:  # 没有修改过密码
        print('没有改过密码, 正常访问')



if __name__ == '__main__':
    update_pwd()
    login()
    access()