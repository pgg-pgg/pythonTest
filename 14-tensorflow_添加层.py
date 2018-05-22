import tensorflow as tf
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
        outputs=activation_function(Weights)
    return outputs