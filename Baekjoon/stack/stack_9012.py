"""
문제
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 
만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 
여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 
"""

# 처음 시도 했던 코드
n = int(input())

stack = []

for i in range(n):
    s = list(input())
    
    if s[0] == ')':
        print("NO")
        continue
        
    for element in s:
        if element == '(':
            stack.append(element)
        elif element == ')':
            if len(stack) == 0:
                stack.append(element)
            else:
                stack.pop()
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
   
    stack = []

### 모든 테스트 케이스를 통과했으나, 제출하면 '틀렸습니다'라고 나온다. 일부 코드를 조금 수정해주었더니 통과할 수 있었다. ###

# 수정한 코드
n = int(input())

stack = []

for i in range(n):
    s = list(input())
    
    for element in s:
        if element == '(':
            stack.append(element)
        elif element == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        # stack이 비어있다면...
        if not stack:
            print("YES")
        else:
            print("NO")
        
    stack = []

"""
stack 배열이 비어있다는걸 len으로 체크하려 했는데, if stack: 으로 간단하게 체크할 수 있었다.
(stack이 비어있다면 False, stack 안에 원소가 하나라도 있으면 True를 리턴한다.)

"""