import tensorflow as tf

hello = tf.constant('Hello! TensorFLow')
sess = tf.Session()
print sess.run(hello)
sess.close()

x1 = tf.constant([5])
x2 = tf.constant([6])
result = x1 * x2
with tf.Session() as sess :
    print sess.run(result)