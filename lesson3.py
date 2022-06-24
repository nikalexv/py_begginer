def LevenshteinDistance(s, t):
    n, m = len(t), len(s)
    v0 = list(range(n))+[0]
    v1 = [0]*(n + 1)

    for i in range(m):
        v1[0] = i + 1
        #print(v1[0], end=' ')
        for j in range(n):
            deletionCost = v0[j+1] + 1
            insertionCost = v1[j] + 1
            if s[i] == t[j]:
                substitutionCost = v0[j]
            else:
                substitutionCost = v0[j] + 1
                
            v1[j+1] = min(deletionCost, insertionCost, substitutionCost)

        v0, v1 = v1, v0
    return v0[n]

pairs = [
('море', 'гора'),
('выбор', 'выборы'),
('sunday', 'monday'),
('роспись','подписи')
]

if __name__ == "__main__":
    for s, t in pairs:
        print(s,t, LevenshteinDistance(s, t))

