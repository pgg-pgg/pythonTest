import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 添加层
def add_layer(inputs,in_size,out_size,activation_function=None):
    #随机生成一个变量矩阵
    Weights=tf.Variable(tf.random_normal([in_size,out_size]))
    biases=tf.Variable(tf.zeros([1,out_size])+0.1)
    Wx_puls_b=tf.matmul(inputs,Weights)+biases #预测值
    if activation_function is None:
        outputs=Wx_puls_b
    else:
        outputs=activation_function(Wx_puls_b)
    return outputs


# 创建300个数据
x_data=np.linspace(-1,1,300)[:,np.newaxis]

# 干扰点
noise=np.random.normal(0,0.05,x_data.shape)

# 根据公式计算出y
y_data=np.square(x_data)-0.5+noise

xs=tf.placeholder(tf.float32,[None,1])
ys=tf.placeholder(tf.float32,[None,1])

# 隐藏层
l1=add_layer(xs,1,10,activation_function=tf.nn.relu)
# 输出层
predition=add_layer(l1,10,1,activation_function=None)

# 计算误差
loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-predition),reduction_indices=[1]))

# 训练步骤
train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init=tf.global_variables_initializer()

sess=tf.Session()
sess.run(init)

# 输出xy点
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.scatter(x_data,y_data)
plt.ion()
plt.show()

for i in range(1000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i%50==0:
        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value=sess.run(predition,feed_dict={xs:x_data})
        lines=ax.plot(x_data,prediction_value,'r-',lw=5)
        plt.pause(1)