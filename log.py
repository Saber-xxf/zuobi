def log(name,meg):
    # 定义文件名和要写入的内容

    # 使用open()函数创建文件对象，并指定写入模式 "w"（写入）
    with open(name, "w") as file:
        # 使用write()方法将内容写入文件
        file.write(meg)

    # 文件会在with代码块执行完毕后自动关闭
