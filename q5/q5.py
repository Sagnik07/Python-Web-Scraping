from num2words import num2words
answerlist = []
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None


def traverse(root):
    if root.value != -1:
        #print(root.value)
        if root.left is not None:
            traverse(root.left)
        if root.right is not None:
            traverse(root.right)
    return


def all_leaves(root):
    if root is not None:
        all_leaves(root.left)
        if root.left is None:
            if root.right is None:
                if int(root.value) != -1:
                    answerlist.append(root.value)
                    #print(root.value)
        all_leaves(root.right)


def all_left(root):
    if root is not None:
        if root.left is not None:
            if int(root.value) != -1:
                answerlist.append(root.value)
                #print(root.value)
            all_left(root.left)
        elif root.right is not None:
            if int(root.value) != -1:
                answerlist.append(root.value)
                #print(root.value)
            all_left(root.right)


def all_right(root):
    if root is not None:
        if root.right is not None:
            all_right(root.right)
            if int(root.value) != -1:
                answerlist.append(root.value)
                #print(root.value)

        elif root.left is not None:
            all_right(root.left)
            if int(root.value) != -1:
                answerlist.append(root.value)
                #print(root.value)


def all_answer(root):
    if root:
        answerlist.append(root.value)
        #print(root.value)
        all_left(root.left)
        all_leaves(root.left)
        all_leaves(root.right)
        all_right(root.right)


#def main():
l = input("Enter the node values list :")
lst = l.split()
objlst = []
for i in lst:
    if int(i) == -1:
        objlst.append(None)
    else:
        objlst.append(Node(i))

for i in range(0, len(lst)):
    if objlst[i]:
        if (2 * i + 1) < len(lst):
            objlst[i].left = objlst[2 * i + 1]
        else:
            objlst[i].left = None
        if (2 * i + 2) < len(lst):
            objlst[i].right = objlst[2 * i + 2]
        else:
            objlst[i].right = None

#print("fun call")
all_answer(objlst[0])

#print("here starts printing of array")
if int(objlst[0].value) != -1:
    answerlist.append(objlst[0].value)

sum = 0

for i in range(0, len(answerlist)):
    sum = sum + int(answerlist[i])
    #print(answerlist[i],end=" ")

print("Total Amount: ",num2words(sum))
for i in range(0, len(answerlist)):
    print(num2words(int(answerlist[i])),",",end="")

#traverse(objlst[0])
