def sum_max_task(*args):
    summ = 0
    maxx = args[0]
    for el in args:
        summ+=el
        if el > maxx:
            maxx = el
    return summ, maxx


def test_2(*args, **kwrags):
    print(type(kwrags))
    print(kwrags)
    print(args)
    for key, val in kwrags.items():
        print(f'key -- {key}, val -- {val}')
        

def search_key(**kwargs):
    for key, val in kwargs.items():
        if len(key)%2==0:
            print(f'key - {key} val - {val}')
            
            
search_key(asd=4, aw=2, asdfg=5)