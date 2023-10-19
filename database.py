import mysql.connector

import init

json_data = init.read_json_file("conf.json")
host = json_data["database"]
print(host)
if host=="cloud":
    db_config = {
        'host': 'www.db4free.net',
        'user': 'mysqlsaberroot',
        'password': 'mysqlsaber123',
        'database': 'mysqlsaberzuob',
    }

else:
    db_config = {
        'host': '172.19.15.26',
        'user': 'root',
        'password': '123',
        'database': 'zuob',
    }

def getKey(username,key):
    # 创建数据库连接
    conn = mysql.connector.connect(**db_config)

    # 创建游标对象
    cursor = conn.cursor()
    # 执行查询语句
    select_query = "SELECT * FROM user WHERE `name` = %s and `key` = %s"
    cursor.execute(select_query, (username,key))
    # 获取所有结果
    rows = cursor.fetchall()

    # 获取查询结果的列名
    column_names = [column[0] for column in cursor.description]

    # 遍历结果并输出
    for row in rows:
        # 将每行数据与列名对应转换为字典
        row_dict = dict(zip(column_names, row))
        # 根据列名来获取数据
        key = row_dict['key']
        num = row_dict['num']
        id = row_dict['id']
        # 关闭游标和连接
        cursor.close()
        conn.close()
        return key,num,id
    return "",0,0

def updataNum(num,id):
    conn = mysql.connector.connect(**db_config)
    # 创建游标对象
    cursor = conn.cursor()
    # 创建数据库连接
    # 执行UPDATE语句来更新key字段的值
    update_query = "UPDATE user SET `num` = %s WHERE `id` = %s"
    update_values = (num-1,id)
    s=cursor.execute(update_query, update_values)
    print(s)
    # 提交更改
    conn.commit()
    # 关闭游标和连接
    cursor.close()
    conn.close()
def updataKey(new):
    conn = mysql.connector.connect(**db_config)

    # 创建游标对象
    cursor = conn.cursor()
    # 创建数据库连接
    # 执行UPDATE语句来更新key字段的值
    update_query = "UPDATE user SET `key` = %s WHERE id = %s"
    update_values = (new, 1)
    s=cursor.execute(update_query, update_values)
    print(s)
    # 提交更改
    conn.commit()
    # 关闭游标和连接
    cursor.close()
    conn.close()
# updata("00000000")
# print(getKey("master","5f49c8173a29449"))
# updataNum(99,1)
# print(getKey("master","5f49c8173a29449"))