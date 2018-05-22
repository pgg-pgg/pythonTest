import tensorflow as tf

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


##建立两个矩阵
matrix1=tf.constant([[3,3,3]])
matrix2=tf.constant([[2],[2],[2]])


##矩阵的乘法
product=tf.matmul(matrix1,matrix2)

# #第一中方法
# sess=tf.Session()
# result=sess.run(product)
# print(result)
# sess.close()

#第二种方法
with tf.Session() as sess:
    result2=sess.run(product)
    print(result2)
