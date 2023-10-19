import hashlib
import datetime
import database
def encrypt_date(date_str):
    # 使用SHA-256哈希算法生成密文
    sha256_hash = hashlib.sha256(date_str.encode()).hexdigest()
    # 取前15位作为密文
    encrypted_date = sha256_hash[:15]
    return encrypted_date

def getKey():
    # 获取当前日期
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    mingwen=str(current_date)+"lgd111"
    # 将当前日期加密为密文
    encrypted_date = encrypt_date(mingwen)
    return encrypted_date

# 打印密文
print( getKey())
database.updata(getKey())
