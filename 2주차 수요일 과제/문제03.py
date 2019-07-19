height = []
count = 0
while count < 9:
    h = int(input())
    height.append(h)
    count += 1

value = []

for i in range(len(height)):
    for j in range(i+1,len(height)):
        total = sum(height)
        total -= height[i]
        total -= height[j]
        if total == 100:
            value.append([i,j])

if len(value) == 1:
    height.pop(value[0][0])
    height.pop(value[0][1]-1)
    height.sort()
else:
    import random
    num = random.randint(0,len(value)-1)
    height.pop(value[num][0])
    height.pop(value[num][1]-1)
    height.sort()

def result(x):
    for h in x:
        print(h)

result(height)

