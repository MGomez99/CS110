def squareFun(a):
    result = 0
    for c in a:
        if type(c) == int:
            result += c**2
    return result


def main():
    a = [1, 2, 3]
    a.append("apple")
    a.append(76)
    a[3:3] = ["cat"]
    a[0:0] = [99]
    print("Number of 76's in the list at the moment: ", a.count(76))
    del a[a.index(76)]
    a[a.index("apple")] = "orange"
    print(a)
    print(squareFun(a))
main()
