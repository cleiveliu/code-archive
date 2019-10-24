def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
# tri_recursion(6)


def with_draw(balance):
    return lambda amount: balance - amount


r = with_draw(25)
print(r(10))
print(r(5))

print(";;")


def closure_test(base=[0]):
    def plus(y):
        print(base[0] + y)
        base[0] += y
    return plus


a = closure_test()
a(1)
a(10)
a(100)


def make_account(balance):

    def with_draw(amount):
        balance = balance - amount
        return balance

    def deposit(amount):
        balance = balance + amount
        return balance

    def dispatch(m):
        if m == "with_draw":
            return with_draw
        elif m == "deposit":
            return deposit
        else:
            return "No"
    return dispatch


t = make_account(25)
print(t)
print(t("deposit")(10))
print(t("with_draw")(20))
print(t("nhfdsjk"))
