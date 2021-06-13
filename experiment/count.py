from sys import argv; from PIL import Image

# Init
I = Image.open(argv[1]); W, H = I.size; A = W * H
D = [sum(c) for c in I.getdata()]
Bh = [0] * H; Ch = [0] * H
Bv = [0] * W; Cv = [0] * W

# Flood-fill
Background = 3 * 255 + 1; S = [0]
while S:
    i = S.pop(); c = D[i]
    if c != Background:
        D[i] = Background
        Bh[i / W] += c; Ch[i / W] += 1
        Bv[i % W] += c; Cv[i % W] += 1
        S += [(i + o) % A for o in [1, -1, W, -W] if abs(D[(i + o) % A] - c) < 10]

# Eliminate "trapped" areas
for i in xrange(H): Bh[i] /= float(max(Ch[i], 1))
for i in xrange(W): Bv[i] /= float(max(Cv[i], 1))
for i in xrange(A):
    a = (Bh[i / W] + Bv[i % W]) / 2
    if D[i] >= a: D[i] = Background

# Estimate grain count
Foreground = -1; avg_grain_area = 3038.38; grain_count = 0
for i in xrange(A):
    if Foreground < D[i] < Background:
        S = [i]; area = 0
        while S:
            j = S.pop() % A
            if Foreground < D[j] < Background:
                D[j] = Foreground; area += 1
                S += [j - 1, j + 1, j - W, j + W]
        grain_count += int(round(area / avg_grain_area))

# Output
print grain_count