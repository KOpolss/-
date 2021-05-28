import threading

def sleeper(n, name):
    print('вечер в хату я {}, где еда?'.format(name))
    print('{} наелся'.format(name))


t = threading.Thread(target=sleeper, name='Thread1', args=(5, 'Thread1'))

thread_list = []

for i in range(3):
    t = threading.Thread(target=sleeper, name='thread{}'.format(i), args=(5, 'thread{}'.format(i)))
    thread_list.append(t)
    t.start()
    print('{} has started'.format(t.name))

for t in thread_list:
    t.join()

print('all threads done')