#1.创建一个文件夹
import os
from multiprocessing import Pool,Manager

def copyFileTask(name,oldFolderName,newFolderName,queue):
    fr=open(oldFolderName+'/'+name)
    fw=open(newFolderName+'/'+name,'w')

    content=fr.read()
    fw.write(content)

    fr.close()
    fw.close()
    queue.put(name)
def main():
    # 0.获取用户要输入的文件夹名字
    oldFolderName = input("请输入文件夹的名字：")
    newFloderName = oldFolderName + "-复件"
    os.mkdir(newFloderName)
    # 2.获取旧文件夹中的所有文件的名字
    fileName = os.listdir(oldFolderName)
    # 3.使用多进程copy文件

    pool = Pool(5)
    queue=Manager().Queue()

    for name in fileName:
        pool.apply_async(copyFileTask, args=(name,oldFolderName,newFloderName,queue))

    num=0
    allnum=len(fileName)
    while num!=allnum:
        queue.get()
        num += 1
        copyRate=num / allnum
        print('\r copy的进度是：%.2f%%'%(copyRate*100),end='')

    print("\n 已完成copy")
if __name__=="__main__":
    main()