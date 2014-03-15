class Widget(object):
    def __init__(self, left, right):
        self.explode = self.jurassic = False
        self.operands = (left, right)

    def add(self):
        if self.explode:
            if self.jurassic:
                raise Exception("RAWR!" * 1000)
            raise Exception("OMG! add failed!")
        return sum(self.operands)
