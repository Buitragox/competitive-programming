from sys import stdin, stdout

MAXN = 1030000
tree = [None for _ in range(MAXN * 2)]
pend = [""] * (MAXN * 2)

def reset():
    global pend
    pend = [""] * (MAXN * 2)

def invValue():
    return (0, 0)

def createValue(val):
    #(Buccaneer, Barbary)
    if val == '0':
        return (0, 1)
    else:
        return (1, 0)

def combine(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def push(v, v1, v2):
    l = pend[v]
    tree[v1] = change(v1, l)
    pend[v1] += l
    tree[v2] = change(v2, l)
    pend[v2] += l
    pend[v] = ""

    # if pend[v] == "F":
    #     tree[v1] = (tree[v1][0] + tree[v1][1], 0) 
    #     pend[v1] = "F"
    #     tree[v2] = (tree[v2][0] + tree[v2][1], 0) 
    #     pend[v2] = "F"

    # elif pend[v] == "E":
    #     tree[v1] = (0, tree[v1][0] + tree[v1][1]) 
    #     pend[v1] = "E"
    #     tree[v2] = (0, tree[v2][0] + tree[v2][1]) 
    #     pend[v2] = "E"

    # elif pend[v] == "I":
    #     tree[v1] = (tree[v1][1], tree[v1][0]) 
    #     pend[v1] = "I"
    #     tree[v2] = (tree[v2][1], tree[v2][0]) 
    #     pend[v2] = "I"
    # pend[v] = ""

    

def change(v, string):
    ans = tree[v]
    for l in string:
        if l == "F":
            ans = (ans[0] + ans[1], 0) 
        elif l == "E":
            ans = (0, ans[0] + ans[1]) 
        elif l == "I":
            ans = (ans[1], ans[0]) 
    return ans

#build the segment tree
def build(a, v, l, r):
    if l == r: tree[v] = createValue(a[l])
    else:
        m = l + ((r - l) >> 1)
        build(a, v + 1, l, m)
        build(a, v + 2 * (m - l + 1), m + 1, r)
        tree[v] = combine(tree[v + 1], tree[v + 2 * (m - l + 1)])

#query
def query(v, L, R, l, r):
    ans = None
    if l > r: ans = invValue()
    elif l == L and r == R: ans = tree[v]
    else:
        m = L + ((R - L) >> 1)
        push(v, v + 1, v + 2 * (m - L + 1))
        ans = combine(query(v + 1, L, m, l, min(r, m)), 
                      query(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r))
        #print(f"combined {l} {r} = {ans}")
    return ans

def update(v, L, R, l, r, h : str):
    if l <= r:
        if l == L and r == R: 
            tree[v] = change(v, h)
            pend[v] += h
        else:
            m = L + ((R - L) >> 1)
            push(v, v + 1, v + 2 * (m - L + 1))
            update(v + 1, L, m, l, min(r, m), h)
            update(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r, h)
            tree[v] = combine(tree[v + 1], tree[v + 2 * (m - L + 1)])
            #print(f"combined {l} {r} = {tree[v]}")
            


def main():
    cases = int(stdin.readline())
    for i in range(1, cases + 1):
        if i != 1:
            reset()
        string = ""
        mPairs = int(stdin.readline())
        for _ in range(mPairs):
            mult = int(stdin.readline())
            subString = stdin.readline().rstrip()
            string += (subString * mult)
        last = len(string) - 1
        #print(string)
        build(string, 0, 0, last)
        queries = int(stdin.readline())
        count = 1
        stdout.write(f"Case {i}:\n")
        for _ in range(queries):
            info = stdin.readline().split()
            op = info[0]
            left = int(info[1])
            right = int(info[2])
            if op == "S":
                #print(op, left, right)
                ans = query(0, 0, last, left, right)[0]
                stdout.write(f"Q{count}: {ans}\n")
                count += 1
            else:
                #print(op, left, right)
                update(0, 0, last, left, right, op)
            # for j in range(last * 2 + 2):
            #     print(tree[j], end=" ")
            # print()


main()