

def mlbph(img1):
    source=img1
    final = source[:]
    for y in range(len(source)):
        for x in range(y):
            final[y, x] = source[y, x]

    members = [source[0, 0]] * 9
    for y in range(1, len(source) - 1):
        for x in range(1, y - 1):
            members[0] = source[y - 1, x - 1]
            members[1] = source[y, x - 1]
            members[2] = source[y + 1, x - 1]
            members[3] = source[y - 1, x]
            members[4] = source[y, x]
            members[5] = source[y + 1, x]
            members[6] = source[y - 1, x + 1]
            members[7] = source[y, x + 1]
            members[8] = source[y + 1, x + 1]

            members.sort()
            final[y, x] = members[5]
    return final