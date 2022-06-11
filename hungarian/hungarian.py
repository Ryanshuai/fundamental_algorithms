def find(i, is_connected, assigned_to, tried):
    for (j, connected) in enumerate(is_connected[i]):
        if connected and not tried[j]:
            tried[j] = True
            if assigned_to[j] == - 1 or find(assigned_to[j], is_connected, assigned_to, tried):
                assigned_to[j] = i
                return True
    return False


def hungarian(is_connected):
    n = len(is_connected)
    m = len(is_connected[0])
    assigned_to = [- 1] * m
    count = 0
    for i in range(n):
        tried = [False] * m
        if find(i, is_connected, assigned_to, tried):
            count += 1
    return count


if __name__ == '__main__':
    import sys


    def line_to_ints(line):
        line = line.strip().split(" ")
        line = [int(l) for l in line]
        return line


    with open("input.txt", "r") as f:
        lines = f.readlines()

    # lines = sys.stdin.readlines()

    idx = 0
    T = int(lines[idx])
    idx += 1

    for t in range(T):
        n = int(lines[idx])
        idx += 1
        is_connected = []
        for j in range(n):
            is_connected.append(line_to_ints(lines[idx]))
            idx += 1

        if hungarian(is_connected) == n:
            print("Yes")
        else:
            print("No")
