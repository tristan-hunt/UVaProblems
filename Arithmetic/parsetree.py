class Node:
    def __init__(self, parent, equation):
        self.parent = parent
        self.string = string
        self.lchild = None
        self.rchild = None

    def evaluate(self, string):


    def parse(self, equation):
        eq = [e for e in equation]
        for e in eq:
            curr = eq.pop(e)
            if e == '(':
                self.lchlid = new Node(self, )



equation = "(3+(4*5))"
parse(equation)