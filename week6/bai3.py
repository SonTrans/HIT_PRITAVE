class MyStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.data = []
    def initialization(self):
        print(f"Stack đã được khởi tạo với capacity = {self.capacity}")
    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else :
            return False
    def isFull(self):
        if len(self.data) == self.capacity:
            return True
        else :
            return False
    def push(self,value):
        if self.isFull():
            print(f"đã đầy không thể thêm {value}")
        else :
            self.data.append(value)
            print(f"đã thêm {value}")
    def pop(self):
        if self.isEmpty():
            print("không có ")
        else :
            value = self.data.pop()
        return value
    def top(self):
        if self.isEmpty():
            print("rỗng")
        else :
            return self.data[len(self.data)-1]
    def indata(self):
        print(self.data)
stack1 = MyStack(capacity=5)
stack1.initialization()
stack1.push(1) 
stack1.push(2)
stack1.push(5)
stack1.push(4)
stack1.push(3)
stack1.push(6)
stack1.indata()
print(stack1.isFull())
print(f"phần tử ngoài cùng : {stack1.top()}")
print( f"đã xóa phần tử ngoài cùng : {stack1.pop()}")
print(f"phần tử ngoài cùng : {stack1.top()}")
print( f"đã xóa phần tử ngoài cùng : {stack1.pop()}")
print(stack1.isEmpty())