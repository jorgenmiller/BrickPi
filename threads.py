import threading

y = 0
print "y was %s" % (y)

def worker():
    global y
    y = 1
    return
def thinker():
    print "y is %s" % (y)
    return

threads = []
for i in range(2):
    w = threading.Thread(target = worker)
    t = threading.Thread(target = thinker)
    threads.append(w)
    threads.append(t)
    w.start()
    t.start()
