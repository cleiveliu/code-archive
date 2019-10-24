# source:http://norvig.com/lispy.html

from collections import ChainMap as Environment
import operator as op
import math
Symbol = str              # A Scheme Symbol is implemented as a Python str
# A Scheme Number is implemented as a Python int or float
Number = (int, float)
Atom = (Symbol, Number)  # A Scheme Atom is a Symbol or Number
List = list             # A Scheme List is implemented as a Python list
Exp = (Atom, List)     # A Scheme expression is an Atom or List


def tokenize(chars: str) -> list:
    "Convert a string of characters into a list of tokens."
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()


def parse(program: str) -> Exp:
    "Read a Scheme expression from a string."
    return read_from_tokens(tokenize(program))


def read_from_tokens(tokens: list) -> Exp:
    "Read an expression from a sequence of tokens."
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0)  # pop off ')'
        return L
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return atom(token)


def atom(token: str) -> Atom:
    "Numbers become numbers; every other token is a symbol."
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)


def standard_env():
    "An environment with some Scheme standard procedures."
    env = {}
    env.update(vars(math))  # sin, cos, sqrt, pi, ...
    env.update({
        '+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv,
        '>': op.gt, '<': op.lt, '>=': op.ge, '<=': op.le, '=': op.eq,
        'abs': abs,
        'append': op.add,
        'apply': lambda proc, args: proc(*args),
        'begin': lambda *x: x[-1],
        'car': lambda x: x[0],
        'cdr': lambda x: x[1:],
        'cons': lambda x, y: [x] + y,
        'eq?': op.is_,
        'equal?': op.eq,
        'length': len,
        'list': lambda *x: list(x),
        'list?': lambda x: isinstance(x, list),
        'map': lambda *args: list(map(*args)),
        'max': max,
        'min': min,
        'not': op.not_,
        'null?': lambda x: x == [],
        'number?': lambda x: isinstance(x, Number),
        'procedure?': callable,
        'round': round,
        'symbol?': lambda x: isinstance(x, Symbol),
    })
    return env


global_env = standard_env()


def eval(x, env=global_env):
    "Evaluate an expression in an environment."
    if isinstance(x, Symbol):      # variable reference
        return env[x]
    elif not isinstance(x, List):  # constant literal
        return x
    elif x[0] == 'quote':          # (quote exp)
        (_, exp) = x
        return exp
    elif x[0] == 'if':             # (if test conseq alt)
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif x[0] == 'define':         # (define var exp)
        (_, var, exp) = x
        env[var] = eval(exp, env)
    elif x[0] == 'lambda':         # (lambda (var...) body)
        (_, parms, body) = x
        return Procedure(parms, body, env)
    else:                          # (proc arg...)
        proc = eval(x[0], env)
        args = [eval(exp, env) for exp in x[1:]]
        return proc(*args)


def repl(prompt='lis.py>> '):
    "A prompt-read-eval-print loop."
    while True:
        val = eval(parse(input(prompt)))
        if val is not None:
            print(schemestr(val))


def schemestr(exp):
    "Convert a Python object back into a Scheme-readable string."
    if isinstance(exp, List):
        return '(' + ' '.join(map(schemestr, exp)) + ')'
    else:
        return str(exp)


class Procedure(object):
    "A user-defined Scheme procedure."

    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env

    def __call__(self, *args):
        env = Environment(dict(zip(self.parms, args)), self.env)
        return eval(self.body, env)
