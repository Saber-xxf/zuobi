import oss2
import os
# 填写RAM用户的访问密钥（AccessKey ID和AccessKey Secret）。
# accessKeyId = 'LTAI5t9SW8XjwjSSQ8aBHmv7'
# accessKeySecret = 'OL40YJjRlc3eNHwIrfoidc5GVu481l'
#应若男的
# "KeyId": "LTAI5tSqS1791p83r9jsbpqF",
# "KeySecret": "ua0d6Xru2VShRFC0TykczO1OZ0FMYi",
# "endpoint": "https://oss-cn-beijing.aliyuncs.com",
# "bucket_name": "zuob"
class Oss():
    # 使用代码嵌入的RAM用户的访问密钥配置访问凭证。
    def init(self,id,key,ed,name):
        auth = oss2.Auth(id, key)
        return oss2.Bucket(auth, ed, name)

    def upload(self,path,id,key,ed,name):
        # print("开始上传")
        with open(path, 'rb') as fileobj:
            # Seek方法用于指定从第1000个字节位置开始读写。上传时会从您指定的第1000个字节位置开始上传，直到文件结束。
            fileobj.seek(0, os.SEEK_SET)
            # Tell方法用于返回当前位置。
            current = fileobj.tell()
            # 填写Object完整路径。Object完整路径中不能包含Bucket名称。
            bucket=self.init(id,key,ed,name)
            bucket.put_object(path, fileobj)
        # print("上传成功")