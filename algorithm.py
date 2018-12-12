# 1. check wether two strings contain same letters
def al(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for s in s1:
        pos = ord(s) - ord('a')
        c1[pos] = c1[pos] + 1
    for j in s2:
        pos = ord(j) - ord('a')
        c2[pos] = c2[pos] + 1
    k = 0
    still_ok = True
    while k < 26 and still_ok:
        if c1[k] == c2[k]:
            k = k + 1
        else:
            still_ok = False
    return still_ok


# 2. create a Stack in python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, new_item):
        self.items.append(new_item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
        
# 3. bracket_checker, check a bracket string wether can symmetrical, for example'((())) or ((()()'
def bracket_checker(bracket_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(bracket_string) and balanced:
        symbol = bracket_string[index]
        if symbol == '(':
            s.push(symbol)

        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False
        
# 4. advanced bracket checking mehtod , can check string like '{{([][])}()}'
def advanced_bracket_checker(bracket_string):
    def matched(open, close):
        opens = '([{'
        closers = ')]}'
        return opens.index(open) == closers.index(close)

    s = Stack()
    balanced = True
    index = 0
    while index < len(bracket_string) and balanced:
        symbol = bracket_string[index]
        if symbol in '([{':
            s.push(symbol)

        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matched(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False
        
# 5. convert integer to binary
def divide_by_2(dec_number):
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number = dec_number // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string
