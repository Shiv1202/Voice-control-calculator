import operator as op
def get_operator_func(opr):
    return {
        '+': op.add,
        '-': op.sub,
        'x': op.mul,
        'divided': op.__truediv__,
        'divide by': op.__truediv__,
        'Mod': op.mod,
        'mod': op.mod,
        'and': op.and_, 
    }[opr]

def eval_expression(num1, oper, num2):
    num1, num2 = int(num1), int(num2)
    return get_operator_func(oper)(num1, num2)