def arithmetic_mean(*args):
    return round(sum(args) / len(args),3)


def geometric_mean(*args):
    product = 1
    for x in args:
        product *= x
    return round(product ** (1 / len(args)), 3)


def mean_with_type(*args, mean_type="arithmetic"):
    t = str(mean_type).lower().strip()
    if t == 'arithmetic':
        return arithmetic_mean(*args)
    if t == 'geometric':
        return geometric_mean(*args)
    else:
        print('ERROR')


print(mean_with_type(2, 4, 8, mean_type="arithmetic"))
print(mean_with_type(2, 4, 8, mean_type="geometric"))