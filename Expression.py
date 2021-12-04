from collections import deque


class Expression:

    def __init__(self):
        self.leftBrackets = ['(', '<', '[', '{']
        self.rightBrackets = [')', '>', ']', '}']

    def isBalanced(self, text: str) -> bool:
        stack = deque()
        for i in text:
            if self.isLeftBracket(i):
                stack.append(i)
            if self.isRightBracket(i):
                if not stack:
                    return False

                top = stack.pop()
                if not self.bracketsMatch(top, i):
                    return False

        if stack:
            return False
        else:
            return True

    def isLeftBracket(self, ch: str) -> bool:
        return self.leftBrackets.__contains__(ch)

    def isRightBracket(self, ch: str) -> bool:
        return self.rightBrackets.__contains__(ch)

    def bracketsMatch(self, left: str, right: str):
        return self.leftBrackets.index(left) == self.rightBrackets.index(right)


if __name__ == "__main__":
    string = '( 1 + 1 >'
    exp = Expression()
    print(exp.isBalanced(string))
