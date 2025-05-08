class Expression:
    def interpret(self, context):
        raise NotImplementedError


class Number(Expression):
    def __init__(self, value):
        self.value = int(value)

    def interpret(self, context):
        context.append(self.value)


class Plus(Expression):
    def interpret(self, context):
        a = context.pop()
        b = context.pop()
        context.append(a + b)


class Minus(Expression):
    def interpret(self, context):
        b = context.pop()
        a = context.pop()
        context.append(a - b)


class Multiply(Expression):
    def interpret(self, context):
        a = context.pop()
        b = context.pop()
        context.append(a * b)


class Divide(Expression):
    def interpret(self, context):
        b = context.pop()
        a = context.pop()
        context.append(a // b)


def pars(expression: str):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(Number(token))
        elif token == '+':
            stack.append(Plus())
        elif token == '-':
            stack.append(Minus())
        elif token == '*':
            stack.append(Multiply())
        elif token == '/':
            stack.append(Divide())
    return stack


def evaluate(expression: str):
    parsed = pars(expression)
    context = []

    for expr in parsed:
        expr.interpret(context)

    return context.pop()


print(evaluate("5 3 2 + *"))  # (3 + 2) * 5 = 25
print(evaluate("10 2 /"))  # 10 // 2 = 5
print(evaluate("7 3 - 2 *"))  # (7 - 3) * 2 = 8


# ==============

class Expression:
    def interpret(self, stack, variables=None):
        raise NotImplementedError


class Variable(Expression):
    def __init__(self, name):
        self.name = name

    def interpret(self, stack, variables):
        stack.append(variables[self.name])


class AND(Expression):
    def interpret(self, stack, variables=None):
        b = stack.pop()
        a = stack.pop()
        stack.append(a and b)


class OR(Expression):
    def interpret(self, stack, variables=None):
        b = stack.pop()
        a = stack.pop()
        stack.append(a or b)


class NOT(Expression):
    def interpret(self, stack, variables=None):
        a = stack.pop()
        stack.append(not a)


def pars_bool(expression: str):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token == "AND":
            stack.append(AND())
        elif token == "OR":
            stack.append(OR())
        elif token == "NOT":
            stack.append(NOT())
        else:
            stack.append(Variable(token))
    return stack


def evaluate_bool(expression: str, variables: dict):
    parsed = pars_bool(expression)
    stack = []

    for expr in parsed:
        expr.interpret(stack, variables)

    return stack.pop()


expr = "admin active AND NOT"
vars = {"admin": True, "active": False}

print(evaluate_bool(expr, vars))  # True
