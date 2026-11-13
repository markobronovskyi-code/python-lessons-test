def Draw_tri(a):
    for e in range(1, a + 1):
        print(" " * (a - e) + "*" * (2 * e - 1))

Draw_tri(20)
