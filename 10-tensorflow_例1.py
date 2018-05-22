import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


#创建一些数据
x_data=np.random.rand(100).astype(np.float32)

y_data=x_data*0.1+0.3

###创建tensorflow的结构开始

#权重，一维数据，初始值维-1.0~1.0之间
Weights=tf.Variable(tf.random_uniform([1],-1.0,1.0))

biases=tf.Variable(tf.zeros([1]))

y=Weights*x_data+biases

loss=tf.reduce_mean(tf.square(y-y_data))

#选择激励函数
optimizer=tf.train.GradientDescentOptimizer(0.5)
train=optimizer.minimize(loss)

#初始化变量
init=tf.initialize_all_variables()
###创建tensorflow的结构结束

sess=tf.Session()
#激活init
sess.run(init)

for step in range(201):
    sess.run(train)
    if step%20==0:
        print(step,sess.run(Weights),sess.run(biases))



