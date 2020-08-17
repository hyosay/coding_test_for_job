stack = []

stack.append(1)
stack.append(25)
stack.append(4)
stack.append(6)
stack.pop()
stack.append(33)
stack.append(1)
stack.pop()

print(stack)
# reverse
#print(stack[::-1])

#a = list(reversed(stack))
#print(a)

stack.reverse()
print(stack)