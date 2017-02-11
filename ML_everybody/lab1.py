import tensorflow as tf

hello = tf.constant("hello, TensorFlow")
a = tf.constant(2)
b = tf.constant(3)
c = a + b

print hello
print c

sess = tf.Session()
print sess.run(hello)
print sess.run(c)


with tf.Session() as sess:
    print sess.run(a + b)
    print sess.run(a * b)


d = tf.placeholder(tf.int16)
e = tf.placeholder(tf.int16)

add = tf.add(d, e)
mul = tf.mul(d, e)

with tf.Session() as sess:
    print "Addition with variables: %i" % (sess.run(add, feed_dict={d: 2, e: 3}))


x = tf.placeholder("float", 4)
y = x * 2

with tf.Session() as session:
    result = session.run(y, feed_dict={x: [3, 2, 3,2]})
    print(result)
