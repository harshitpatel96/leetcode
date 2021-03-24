class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.s2) > 0: 
            x = self.s2.pop()
            return x
        
        if not self.empty():
            while len(self.s1) != 0:
                x = self.s1.pop()
                self.s2.append(x)
            return self.s2.pop()        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.empty():
            if len(self.s2) > 0: return self.s2[-1]
            else: return self.s1[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0 and len(self.s2) == 0
