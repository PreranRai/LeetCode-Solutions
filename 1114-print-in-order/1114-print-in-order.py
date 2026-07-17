from threading import Event

class Foo(object):
    def __init__(self):
        self.first_done = Event()
        self.second_done = Event()


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done.set()


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.first_done.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_done.set()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.second_done.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()