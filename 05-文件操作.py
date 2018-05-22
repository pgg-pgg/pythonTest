older_file_name=input("请输入要复制的文件名")

old_file=open(older_file_name,"r")

new_file_name=older_file_name[0:older_file_name.rfind(".")]+"备份.txt"

new_file=open(new_file_name,"w")

content=old_file.read()
new_file.write(content)

old_file.close()
new_file.close()

