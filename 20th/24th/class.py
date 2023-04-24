def add():
    try:#to raise exception when non integers are given as inputs
        a=int(input())
    except ValueError as err:
        print(err)
    try:
        b=int(input())
    except ValueError as err:
        print(err)
    print(a+b)

add()