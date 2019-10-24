# source::
# https://whst.github.io/2017/04/15/functionally-implemented-link-list/

#! /usr/bin/env python3


def cons(x, y):
    def set_x(v):
        nonlocal x
        x = v

    def set_y(v):
        nonlocal y
        y = v

    def dispatch(m):
        if m == 'car':
            return x
        if m == 'cdr':
            return y
        if m == 'set_car':
            return set_x
        if m == 'set_cdr':
            return set_y
        raise ValueError("Undefined operation: CONS: " + str(m))

    return dispatch


def car(z):
    return z('car')


def cdr(z):
    return z('cdr')


def set_car(z, new_value):
    z('set_car')(new_value)


def set_cdr(z, new_value):
    z('set_cdr')(new_value)


def is_null(z):
    return z is None


def is_number(z):
    return isinstance(z, (int, long, float, complex))


def is_atom(z):
    return is_number(z) or isinstance(z, string)


def list_range(a, b):
    if a > b:
        return None
    return cons(a, list_range(a + 1, b))


def list_to_str(l):
    if is_null(l):
        return ''
    return str(car(l)) + ' ' + list_to_str(cdr(l))

# 1:2:3:[] --> f(1, f(2, f(3, zero)))


def fold_r(f, zero, xs):
    if is_null(xs):
        return zero
    return f(car(xs), fold_r(f, zero, cdr(xs)))


def fold_l(f, zero, xs):
    def step(x, g):
        return lambda a: g(f(a, x))

    def identity(x): return x
    return fold_r(step, identity, xs)(zero)


def list_map(proc, xs):
    def f(x, acc): return cons(proc(x), acc)
    return fold_r(f, None, xs)


def list_filter(pred, xs):
    def step(x, acc):
        return cons(x, acc) if pred(x) else acc
    return fold_r(step, None, xs)


def list_to_str(xs):
    return fold_r(lambda x, acc: str(x) + ' ' + acc, '', xs)


if __name__ == '__main__':
    xs = list_range(1, 10)
    print(list_to_str(list_map(lambda x: x * x, xs)))     # Squares
    print(list_to_str(list_filter(lambda x: x % 2, xs)))  # Odd numbers
    def sub(x, y): return x - y
    ys = list_range(1, 3)
    print(fold_l(sub, 0, ys))  # (((0 - 1) - 2) - 3)
    print(fold_r(sub, 0, ys))  # (1 - (2 - (3 - 0)))

# lambda version::
"""
#!/usr/bin/env python3

cons = lambda x: lambda y: lambda isCar: x if isCar else y
car = lambda node: node(True)
cdr = lambda node: node(False)

null = lambda obj: obj == None
number = lambda obj: isinstance(obj, (int, float, complex))

id = lambda x: x

foldr = lambda f: lambda zero: lambda xs:\
        zero if null(xs) else f (car(xs)) (foldr (f) (zero) (cdr(xs)))
foldl = lambda f: lambda zero: lambda xs:\
        foldr (lambda x: lambda g: lambda a: g (f(a)(x))) (id) (xs) (zero)

display = lambda xs: print() if null(xs) else\
          (print(car(xs), end = ' '), display(cdr(xs)))

map = lambda proc: lambda xs:\
        foldr (lambda x: lambda ac: cons(proc(x))(ac)) (None) (xs)
filter = lambda pred: lambda xs:\
         foldr (lambda x: lambda ac:\
                cons(x)(ac) if pred(x) else ac) (None) (xs)

range = lambda a: lambda b: None if a > b else cons(a)(range(a + 1)(b))
"""
