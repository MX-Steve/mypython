import tarfile

# 压缩文件的方法
tar = tarfile.open("/tmp/demo.tar.gz","w:gz") # gzip压缩
tar.add("/etc/hosts")
tar.add("/etc/security")
tar.close()

# tar tvzf /tmp/demo.tar.gz

tar = tarfile.open("/tmp/demo.tar.gz","r:gz")
tar.extractall()  # 解压所有文件到当前目录
tar.close()
