>>> m = hashlib.md5()
>>> for i in xrange(4294967296):
...     out = socket.inet_ntoa(struct.pack("!I", i))
...         m.update(out + "\x0A")

>>> print m.hexdigest()
