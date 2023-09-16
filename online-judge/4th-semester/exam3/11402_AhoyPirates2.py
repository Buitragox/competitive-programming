#Made by Jhoan Buitrago 12/06/2021 dd/mm/aaaa

#Upgraded correct answer but still slow because python
#C++ version works nice

from sys import stdin, stdout

MAXN = 1030000
tree = [None for _ in range(MAXN * 2)]
pend = ["$"] * (MAXN * 2)

def reset():
    global pend
    pend = ["$"] * (MAXN * 2)

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

def push(v, v1, v2, l, r):
    select(v1, pend[v])
    #print(f"pend[{v1}] is {pend[v1]}")
    
    select(v2, pend[v])
    #print(f"pend[{v2}] is {pend[v2]}")
    #print("Push", tree[v])
    change(v1, pend[v])
    change(v2, pend[v])
    
    #print(f"tree[{v}] is {tree[v]}")
    pend[v] = "$"

def change(v, letter):
    ans = (tree[v][0], tree[v][1])
    if letter == "F":
        tree[v] = (ans[0] + ans[1], 0)
    elif letter == "E":
        tree[v] = (0, ans[0] + ans[1]) 
    elif letter == "I":
        tree[v] = (ans[1], ans[0]) 

def select(v, letter):
    if letter == "F" or letter == "E":
        pend[v] = letter
    elif letter == "I":
        if pend[v] == "I":
            pend[v] = "$"

        elif pend[v] == "F":
            pend[v] = "E"
       
        elif pend[v] == "E":
            pend[v] = "F"
        
        elif pend[v] == "$":
            pend[v] = "I"

    #elif letter == "$": do nothing

#build the segment tree
def build(a, v, l, r):
    if l == r: 
        tree[v] = createValue(a[l])
    else:
        m = l + ((r - l) >> 1)
        build(a, v + 1, l, m)
        build(a, v + 2 * (m - l + 1), m + 1, r)
        tree[v] = combine(tree[v + 1], tree[v + 2 * (m - l + 1)])

#query
def query(v, L, R, l, r):
    ans = None
    if l > r: 
        ans = invValue()
    elif l == L and r == R:
        # m = L + ((R - L) >> 1)
        # push(v, v + 1, v + 2 * (m - L + 1), L, R)
        ans = tree[v]
    else:
        m = L + ((R - L) >> 1)
        push(v, v + 1, v + 2 * (m - L + 1), L, R)
        ans = combine(query(v + 1, L, m, l, min(r, m)), 
                      query(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r))
        #print(f"combined {l} {r} = {ans}")
    return ans

def update(v, L, R, l, r, h : str):
    if l <= r:
        if l == L and r == R: 
            select(v, h)
            #change(v, pend[v])
            change(v, h)
        else:
            m = L + ((R - L) >> 1)
            push(v, v + 1, v + 2 * (m - L + 1), L, R)
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
            #print(op, left, right)
            if op == "S":
                ans = query(0, 0, last, left, right)[0]
                stdout.write(f"Q{count}: {ans}\n")
                count += 1
            else:
                update(0, 0, last, left, right, op)
                #print("after update pend[0] is", pend[0])
            # for j in range(last * 2 + 3):
            #     print(tree[j], end=" ")
            # print()


main()
