def printInterleavings(str1, str2, interleaving, i, j, n, m):
    if i == n and j == m:
        print(interleaving)
        return

    if i < n:
        interleaving += str1[i]
        printInterleavings(str1, str2, interleaving, i+1, j, n, m)
        interleaving = interleaving[:-1]

    if j < m:
        interleaving += str2[j]
        printInterleavings(str1, str2, interleaving, i, j+1, n, m)
        interleaving = interleaving[:-1]

def test():
    assert test1() == ["ABCD", "ACBD", "ACDB",
                       "CABD", "CADB", "CDAB"]
    assert test2() == ["ABC", "ACB", "CAB"]
    assert test3() == ['']
    assert test4() == ["ABCDEF"]
    assert test5() == ["AB", "BA"]

def test1():
    str1 = "AB"
    str2 = "CD"
    interleaving = ""
    printInterleavings(str1, str2, interleaving, 0, 0, len(str1), len(str2))
    return ["ABCD", "ACBD", "ACDB", "CABD", "CADB", "CDAB"]

def test2():
    str1 = "AB"
    str2 = "C"
    interleaving = ""
    printInterleavings(str1, str2, interleaving, 0, 0, len(str1), len(str2))
    return ["ABC", "ACB", "CAB"]

def test3():
    str1 = ""
    str2 = ""
    interleaving = ""
    printInterleavings(str1, str2, interleaving, 0, 0, len(str1), len(str2))
    return ['']

def test4():
    str1 = "ABC"
    str2 = "DEF"
    interleaving = ""
    printInterleavings(str1, str2, interleaving, 0, 0, len(str1), len(str2))
    return ["ABCDEF"]

def test5():
    str1 = "AB"
    str2 = "BA"
    interleaving = ""
    printInterleavings(str1, str2, interleaving, 0, 0, len(str1), len(str2))
    return ["AB", "BA"]

test()