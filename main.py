import random
def parent(n):
    parent = []
    for i in range(0, n):
        parent.append(random.randint(0,1))
    return parent

def multiple_crossover(parents, q):
    children = []
    k = len(parents)
    n = len(parents[0])

    for j in range(q):
        child = []
        for i in range(n):
            alpha = random.randint(0, k - 1)
            print(alpha)
            child.append(parents[alpha][i])
        children.append(child)

    return children

number_of_parents = 10
number_of_children = 1

parents = []
for _ in range(number_of_parents):
    parents.append(parent(number_of_parents))

print(parents)
children = multiple_crossover(parents, number_of_children)

for child in children:
    print(child)

