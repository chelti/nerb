def func6(arg36, arg37):
    var38 = func9()
    if var38 < var38:
        var43 = class10()
    else:
        var43 = class12()
    for var44 in xrange(1):
        var43.func11(arg36, arg37)
    var66 = var47(arg37, var38)
    result = var66 + var66 | -194 | arg36 + arg37 & ((836 + 817) - (var38 + var66) ^ var38 - (1057326666 ^ var66))
    return result
def func16(arg48, arg49):
    var50 = arg48 & -637171058
    var51 = (-278663049 | arg49 - arg48) - var50
    var52 = var51 & var50 ^ -1308583523
    var53 = (var52 ^ arg48) ^ var51 - var51
    var54 = var53 + arg49 & -398 - -896
    var55 = arg49 + (var51 | var50) & arg49
    var56 = arg49 - var52
    var57 = var53 ^ arg48
    var58 = ((var54 - var50) - var57) | var54
    var59 = 2075124201 + -2061020903
    var60 = var59 & arg48 | var55 - var54
    var61 = -744302528 ^ -267123706 & arg48
    var62 = var54 ^ 417 | var54 - var56
    var63 = var60 - (var51 | var55)
    var64 = (var53 + var53 ^ var56) | var57
    var65 = -610 + var59
    result = (var58 | var64) | var52
    return result
def func15():
    closure = [-6]
    def func14(arg45, arg46):
        closure[0] += func16(arg45, arg46)
        return closure[0]
    func = func14
    return func
var47 = func15()
class class12(object):
    def func11(self, arg41, arg42):
        result = -708243899 - ((648278101 + 0 + arg41) & 1)
        return result
class class10(class12):
    def func11(self, arg39, arg40):
        return 0
def func9():
    func7()
    result = len(range(9))
    func8()
    return result
def func8():
    global len
    del len
def func7():
    global len
    len = lambda x : 9
def func3(arg29, arg30):
    var34 = func4(arg30, arg29)
    var35 = -475 | 112
    result = var35 | -839
    return result
def func1(arg1, arg2):
    var7 = func2(arg2, arg1)
    var8 = arg2 & -1899111676
    if var8 < arg1:
        var9 = var7 ^ arg2 ^ var7 ^ var7
    else:
        var9 = var8 | -975
    if var7 < arg2:
        var10 = var8 & var7
    else:
        var10 = 137 ^ arg2 - 111659180
    var11 = arg1 | arg1 ^ arg2 | 1048939960
    var12 = -628 - 270
    var13 = arg2 | var8 & var8 + var7
    var14 = -1904056758 | (907 + arg2) ^ -128
    var15 = (var7 - arg1 & -1809468912) | var12
    var16 = var8 | (arg1 | var15)
    var17 = var13 | -1415905655 | arg1
    var18 = ((421003419 - var13) | var13) & var13
    var19 = var18 & var17 ^ 1969552001 & var17
    var20 = var17 ^ var19
    var21 = (var7 ^ var11) - var8 & var16
    var22 = var18 | var11 - -1472731298 & var8
    var23 = (var14 + var8) ^ var13 + var22
    if var15 < var18:
        var24 = 646 - var17 ^ var17 | var22
    else:
        var24 = (var7 | (var14 | var18)) + var14
    var25 = var14 - var13
    var26 = var23 | (var15 | 578) ^ var22
    var27 = 608692975 ^ (var12 - var15) | -888340841
    var28 = var27 | (var22 - var25)
    result = var20 - var11 & var26
    return result
def func2(arg3, arg4):
    var5 = 0
    for var6 in xrange(49):
        var5 += arg4 + (-1 + var6)
    return var5
def func4(arg31, arg32):
    def func5(acc, rest):
        var33 = 9 & 7
        if acc == 0:
            return var33
        else:
            result = func5(acc - 1, var33)
            return result
    result = func5(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 1'
    print 'func_number: 3'
    print 'arg_number: 29'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 2'
    print 'func_number: 6'
    print 'arg_number: 36'
    for i in xrange(25000):
        x = 5
        x = func3(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 17'
    print 'arg_number: 67'
    for i in xrange(25000):
        x = 5
        x = func6(x, i)
        print x,
