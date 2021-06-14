from threading import Thread, Lock

glob_counter = 0
lock_counter = Lock()


def foo():
    global glob_counter

    for i in range(0, 10000):
        lock_counter.acquire()
        glob_counter += 1
        lock_counter.release()


def main():

    t1 = Thread(target=foo, args=())
    t2 = Thread(target=foo, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(glob_counter)


if __name__ == "__main__":
    main()