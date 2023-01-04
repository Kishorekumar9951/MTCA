def yield():
    print("code segment1 executed")
    x=7
    yield x*x
    print("code segment2 executed")
    yield 2
    print("code segment1 executed")
    yield 3
    print("code segment4 executed")

if __name__=="__main__":
    x=yield()
    print(next(x))
    print(next(x))
    print(next(x))

