'''
def check_parentheses(expression : str) -> bool:
    stack = []
# 만약 중괄호, 대괄호까지 프로그램을 확장 한다면, 딕셔너리 생성 => { ']' : '['} 와 같이 대응하는 값을 key, value로 설정
    for letter in expression:
        if letter == "(":
            stack.append(letter)
        if letter == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(check_parentheses("(2+3)/8"))
print(check_parentheses("(2+3)"))
print(check_parentheses("(2+3)"))
print(check_parentheses(")()"))
'''
def is_vaild_brackets(expression : str) -> bool:
    stack =[]
    brackets = {')' : '(', '}' : '{', ']' : '['}
    for letter in expression:
        if letter in brackets.values():
            stack.append(letter)
        if letter in brackets.keys():
            if not stack or stack.pop() != brackets[letter]:
                return False
    return not stack

print(is_vaild_brackets("[2+5+{6%3+7-(5+5)}]"))
print(is_vaild_brackets("([)]"))
print(is_vaild_brackets("[()]"))

