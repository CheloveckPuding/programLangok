class ForStatement:
    def __init__(self, start, finish, block):
        self.start = start
        self.finish = finish
        self.block = block
    def execute(self):
        for i in range(self.start, self.finish):
            self.block.execute()
