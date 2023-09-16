from sys import stdin
# from sys import setrecursionlimit
# setrecursionlimit(1000000000)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    # def posorder(self):
    #     pos = []
    #     if self.left != None: pos.extend(self.left.posorder())
    #     if self.right != None: pos.extend(self.right.posorder())
    #     pos.append(self.data)
    #     return pos

    # def inorder(self):
    #     inord = []
    #     if self.left != None: inord.extend(self.left.inorder())
    #     inord.append(self.data)
    #     if self.right != None: inord.extend(self.right.inorder())
    #     return inord


def build(inorder : list, postorder : list):
    #print(inStart, inEnd)
    if len(inorder) == 1:
        return Node(postorder[0])
    else:
        node = Node(postorder[-1])
        index = 0
        for i in range(len(inorder)):
            if inorder[i] == node.data:
                index = i
                break
        
        #Que hallan elementos a la izquierda
        if index > 0:
            node.left = build(inorder[:index], postorder[:index])

        #Que hallan elementos a la derecha
        if index + 1 < len(inorder):
            node.right = build(inorder[index + 1:], postorder[index: -1])

        return node


def posorder(node : Node):
    #if not isinstance(node.left, Node) and not isinstance(node.right, Node):
    if node.left is None and node.right is None:
        return node.data, node
    
    elif node.left is None:
        rSum, rLeaf = posorder(node.right)
        return rSum + node.data, rLeaf
    
    elif node.right is None:
        lSum, lLeaf = posorder(node.left)
        return lSum + node.data, lLeaf
    
    else:
        lSum, lLeaf = posorder(node.left)
        rSum, rLeaf = posorder(node.right)
        if lSum < rSum:
            return lSum + node.data, lLeaf
        elif rSum < lSum:
            return rSum + node.data, rLeaf
        else:
            return lSum + node.data, (lLeaf if lLeaf.data < rLeaf.data else rLeaf)
        

def main():
    line = stdin.readline()
    while line != "":
        inor = list(map(int,line.split()))
        posor = list(map(int, stdin.readline().split()))
        n = len(inor) - 1
        root = build(inor, posor)
        # print(root.inorder())
        # print(root.posorder())
        sumN, leaf = posorder(root)
        print(leaf.data)
        line = stdin.readline()

main()
    