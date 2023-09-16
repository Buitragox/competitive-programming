from sys import stdin, stdout


def build(a, v, l, r):
    if l == r: tree[v] = a[l]
    else:
        m = l + ((r - l) >> 1)
        build(a, v + 1, l, m)
        build(a, v + 2 * (m - l + 1), m + 1, r)
        tree[v] = combine(tree[v + 1], tree[v + 2 * (m - l + 1)])


def get_min(v, L, R, l, r):
    ans = None
    if l > r: ans = float('inf')
    elif l == L and r == R: ans = tree[v]
    else:
        m = L + ((R - L) >> 1)
        ans = combine(get_min(v + 1, L, m, l, min(r, m)), get_min(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r))
    return ans


def update(v, L, R, pos, h):
    if L == R: tree[v] = h
    else:
        m = L + ((R - L) >> 1)
        if pos <= m: update(v + 1, L, m, pos, h)
        else: update(v + 2 * (m - L + 1), m + 1, R, pos, h)
        tree[v] = combine(tree[v + 1], tree[v + 2 * (m - L + 1)])

def combine(p1, p2):
    if p1 < p2: return p1
    else: return p2


n, queries = map(int, stdin.readline().split())
last = n - 1
tree = [None for _ in range(n * 2)]
array = list(map(int, stdin.readline().split()))
build(array, 0, 0, n - 1)
for _ in range(queries):
    q = stdin.readline().rstrip()
    numbers = list(map(lambda x: int(x) - 1, q[6:-1].split(',')))
    if q[0] == 'q':
        stdout.write(str(get_min(0, 0, last, numbers[0], numbers[1])) + '\n')
    else:
        for i in range(len(numbers) - 1):
            array[numbers[i]], array[numbers[i + 1]] = array[numbers[i + 1]], array[numbers[i]]
        for i in range(len(numbers)):
            update(0, 0, last, numbers[i], array[numbers[i]])
