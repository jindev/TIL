import tensorflow as tf

x_data = [1, 2, 3]
y_data = [1, 2, 3]

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))



hypothesis = W * x_data + b
hypothesisWithPH = W * X + b

cost = tf.reduce_mean(tf.square(hypothesis - y_data))
costWithPH = tf.reduce_mean(tf.square(hypothesisWithPH - Y))

a = tf.Variable(0.1)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)


# for step in xrange(3001):
#     sess.run(train)
#     if step % 20 == 0:
#         print step, sess.run(cost), sess.run(W), sess.run(b)


for step in xrange(3001):
    sess.run(train, feed_dict={X:x_data, Y:y_data})
    if step % 20 == 0:
        print step, sess.run(cost), sess.run(W), sess.run(b)

print sess.run(hypothesisWithPH, feed_dict={X: 5})
print sess.run(hypothesisWithPH, feed_dict={X: 2.5})


#tensorflow api doc
# https://www.tensorflow.org/api_docs/python/state_ops/variables#Variable
# https://www.tensorflow.org/versions/r0.10/api_docs/python/constant_op/random_tensors#random_uniform
# https://www.tensorflow.org/api_docs/python/train/optimizers#GradientDescentOptimizer
# https://www.tensorflow.org/api_docs/python/math_ops/reduction#reduce_mean

#https://www.tensorflow.org/api_docs/python/train/optimizers#Optimizer.minimize

#경사하강법 알고리즘 (이해 안됨 ㅠ )
#https://ko.wikipedia.org/wiki/%EA%B2%BD%EC%82%AC_%ED%95%98%EA%B0%95%EB%B2%95
#http://darkpgmr.tistory.com/133
#http://nobilitycat.tistory.com/entry/Gradient-Descent
