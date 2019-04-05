from mytree import MyTree, insert, create, print_tree

with open("words_36.txt") as file:
    data = file.readlines()

words = []

for i in range(len(data)-1):
    data[i] = data[i][:len(data[i]) - 1]
    words.append(data[i])

b = MyTree(words)
insert(b, words)
tree = create(words)
print_tree(tree)
