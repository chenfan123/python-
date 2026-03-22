class MyIterator:
    # 初始化属性，指定：范围
    def __init__(self,start,end):
        self.start = start # 当前值，默认为 开始值
        self.end = end  # 结束值
    # 重写iterator方法，返回当前对象（当前对象就是迭代器）
    def __iter__(self):
        return self
    # 重写next方法，返回当前值，并更新当前值，如果当前值大于结束值，则抛出StopIteration异常
    def __next__(self):
        if self.start < self.end:
            value = self.start
            self.start += 1
            return value
        else:
            raise StopIteration