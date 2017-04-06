import sys


def number(n):
    return(int(n))

def factor(f, a, b):
    """
    f := number | 'x' | '('expression ')'
    """
    print("factor: |{}|".format(f))
    if f == 'x':
        a = a + 1
        return a, b
    
    if f[0] == '(' and f[-1] == ')':
        print(f)
        f[1:-1]
        print(f)
        a, b = expression(f, a, b)
        return a, b
    b = number(f)
    a = 0

    sys.stdout.write("Fac:{}x+{}\n".format(a, b))
    return a, b

def term(t, a, b):
    """
    t := factor { '*' factor}
    """
    print("term: {}; a:{}, b:{}".format(t, a, b))
    if '*' not in t:
        a, b = factor(t, a, b)
        return a, b

    if t[0] == '*':
        if 'x' in t: 
            t = "{}".format(a) + t
        else:
            t = "{}".format(b) + t


    t = t.split("*")
    if (t[0][-1]) == 'x':
        c, d = factor(t[1])
        if (c != 0):
            print("not linear!!")
        a = a + d 
    elif (t[1][0]) == 'x':
        c, d = factor(t[0], a, b)
        if (c != 0):
            print("not linear!")
        a = a + d 
    else:
        a = 1
        b = 1
        for i in range(0, len(t)):
            c, d = factor(t[i], a, b)
            a = a * c
            b = b * d
    sys.stdout.write("Term:{}x+{}\n".format(a, b))
    return a, b

def addition(exp, a, b):
    """
    exp := term { ('+'|'-') Term}
    """
    exp = exp.split("+")
    for i in range(0, len(exp)):
        c, d = term(exp[i], a, b)
        a = a + c
        b = b + d
    return a, b


def expression(exp, a, b):
    if exp[0] == '(':
        # Find the last occurance of '(' in exp.
        # paran = exp from first '(' to last '('
        open_p = 1
        i = 0
        while(open_p):
            i = i + 1    
            if exp[i] == '(':
                open_p = open_p + 1
            if exp[i] == ')':
                open_p = open_p - 1
        paran = exp[1:i]
        exp = exp[i+1:]

        # evaluate the things inside the parantheses
        c, d = expression(paran, a, b)
        a = a + c
        b = b + d

        # If next symbol is a '*':
        if exp[0] == '*':
            a, b = term(exp, a, b)



    if '-' not in exp and '+' not in exp:
        a, b = term(exp, a, b)
        return a, b

    if '-' not in exp:
        a, b = addition(exp, a, b)
        sys.stdout.write("Exp:{}x+{}\n".format(a, b))
        return a, b

    t = ""
    add = False

    i = 0
    while (exp[i] != '+' and exp[i] != '-'):
        t = t +  exp[i]
        i = i + 1
    c, d = term(t, a, b)
    a = a + c
    b = b + d
    sys.stdout.write(":{}x+{}\n".format(a, b))



    if exp[i] == '+':
        add = True
    else:
        add = False
    i = i + 1

    t = ""
    while (i < len(exp)):
        s = exp[i]
        if s != '+' and s != '-':
            t = t + s
        else:
            c, d = term(t, a, b)
            t = ""
            if (add):
                a = a + c
                b = b + d 
                sys.stdout.write(":{}x+{}\n".format(a, b))

            else:
                a = a - c
                b = b - d
                sys.stdout.write(":{}x+{}\n".format(a, b))

            if s == '+':
                add = True
            else:
                add = False
        i = i + 1

    c, d = term(t, a, b)
    if (add):
        a = a + c
        b = b + d
    else:
        a = a - c
        b = b - d


    sys.stdout.write("Final:{}x+{}\n".format(a, b))
    return a, b


def simplify_eq(eq):
    eq = eq.split('=')
    lhs = eq[0]
    rhs = eq[1] 

    # Step 1: Simplify lhs, rhs seperately
    sys.stdout.write("lhs: {}\n".format(lhs))
    sys.stdout.write("rhs: {}\n".format(rhs))
    
    a, b = expression(lhs, 0, 0)
    c, d = expression(rhs, 0, 0)

    sys.stdout.write("{}x+{} = {}x+{}\n\n".format(a, b, c, d))



def load():
    while(1):
        eq = next(sys.stdin).strip()
        yield(eq)

for eq in load():
    simplify_eq(eq)

# def expression(exp):
#     if '-' not in exp and '+' not in exp:
#         a, b = term(exp)
#         return a, b

#     if '-' not in exp:
#         a, b = addition(exp)
#         sys.stdout.write("Exp:{}x+{}\n".format(a, b))
#         return a, b


#     else:
#         exp = exp.split('-')
#         a, b = expression(exp[0])
#         for i in range(1, len(exp)):
#             c, d = expression(exp[i])
#             a = a - c
#             b = b - d
#         sys.stdout.write("-Exp:{}x+{}\n".format(a, b))
#         return a, b








def add_subt(exp):
    total = 0
    i = 0
    exp = exp.split("*+-")
    print(exp)
    while(i < len(exp)):
        symbol = exp[i]
        if symbol == '+':
            i = i + 1
            total = total + exp[i]
        elif symbol == '-':
            i = i + 1
            total = total - exp[i] 
        i = i + 1
    return total 


def reduce_exp(exp):
    a = 0
    b = 0
    if str(type(exp)) == "<class 'list'>":
        exp = "".join(exp)
    
    try:
        b = int(exp)
        return a, b 
    except ValueError:
        pass

    if '(' in exp and ')' in exp:
        print(exp)
        p1 = exp.index("(")
        p2 = exp.index(")")
        print("paran from {} to {}\n".format(p1, p2))
        paran = "42-6*7"

        c, d = reduce_exp(paran)
        a = a + a
        b = b + d

    # Special Case: no x in our exp:
    if 'x' not in exp:
        if '*' not in exp:
            b = b + add_subt(exp)
            return a, b

    # Every linear equation can be reduced to the form
    # ax + b 
    return a, b