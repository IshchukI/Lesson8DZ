class FormulaError(Exception):
    pass


def enterExpression():
    return input("Введите выражение:")


def splitExpressionOnElements(ex):
    i = 0
    splitEx = ex.split(" ")
    if len(splitEx) < 3:
        raise FormulaError
    else:
        return splitEx


def checkConvertToFloat(els):
    i = 0
    for i in range(0, len(els)):
        if i % 2 == 0:
            try:
                float(els[i])
            except ValueError:
                raise FormulaError
            except TypeError:
                return "Необходимо ввести массив минимум из 3-х элементов"


def checkSign(els):
    i = 0
    for i in range(0, len(els)):
        if i % 2 == 1:
            if els[i] != '+' and els[i] != '-' and els[i] != '*' and els[i] != '/':
                raise FormulaError


def calculateExpression(els):
    res = float(els[0])
    try:
        for i in range(1, len(els), 2):
            sign = els[i]
            if sign == "+":
                res += float(els[i + 1])
            if sign == "-":
                res -= float(els[i + 1])
            if sign == "*":
                res *= float(els[i + 1])
            try:
                if sign == "/":
                    res /= float(els[i + 1])
            except ZeroDivisionError:
                return "На ноль делить нельзя"
    except IndexError:
        raise FormulaError
    return res


expression = enterExpression()
try:
    splitExpression = splitExpressionOnElements(expression)
    checkConvertToFloat(splitExpression)
    checkSign(splitExpression)
    result = calculateExpression(splitExpression)
    print(result)

except FormulaError:
    print("Formula Error Exception")


# tests
# _________splitExpressionOnElements_____________________________

def TEST_splitExpressionOnElements_1():
    expected = ['1', '+', '4', '+', '1']
    actual = splitExpressionOnElements("1 + 4 + 1")
    assert actual == expected


def TEST_splitExpressionOnElements_2():
    expected = ['+', '-', '+', '+']
    actual = splitExpressionOnElements('+ - + +')
    assert actual == expected


def TEST_splitExpressionOnElements_3():
    expected = ['2', '2', '3', '3']
    actual = splitExpressionOnElements('2 2 3 3')
    assert actual == expected


def TEST_splitExpressionOnElements_4():
    try:
        actual = splitExpressionOnElements('')
        print("error")
    except FormulaError:
        pass


def TEST_splitExpressionOnElements_5():
    try:
        actual = splitExpressionOnElements('1+2')
        print("error")
    except FormulaError:
        pass


TEST_splitExpressionOnElements_1()
TEST_splitExpressionOnElements_2()
TEST_splitExpressionOnElements_3()
TEST_splitExpressionOnElements_4()
TEST_splitExpressionOnElements_5()


#
# #_________checkConvertToFloat_____________________________
#
def TEST_checkConvertToFloat_1():
    try:
        actual = checkConvertToFloat(1)
        print("function error")
    except TypeError:
        pass


def TEST_checkConvertToFloat_2():
    assert checkConvertToFloat([1, 1, 3, 4, 5]) == None


def TEST_checkConvertToFloat_3():
    try:
        checkConvertToFloat()
        print("function error")
    except TypeError:
        pass


def TEST_checkConvertToFloat_4():
    try:
        checkConvertToFloat(['1', '1', '+'])
        print("function error")
    except FormulaError:
        pass


def TEST_checkConvertToFloat_5():
    try:
        checkConvertToFloat(['a', 'b', 'c'])
        print("function error")
    except FormulaError:
        pass


TEST_checkConvertToFloat_1()
TEST_checkConvertToFloat_2()
TEST_checkConvertToFloat_3()
TEST_checkConvertToFloat_4()
TEST_checkConvertToFloat_5()


# #_________calculateExpression_____________________________
def TEST_calculateExpression_1():
    expected = 7
    actual = calculateExpression(['1', '+', '3', '+', '3'])
    assert actual == expected


def TEST_calculateExpression_2():
    expected = -1
    actual = calculateExpression(['-1', '+', '-3', '+', '3'])
    assert actual == expected


def TEST_calculateExpression_3():
    expected = 1
    actual = calculateExpression(['6', '/', '2', '/', '3'])
    assert actual == expected


def TEST_calculateExpression_4():
    expected = 2
    actual = calculateExpression(['6', '-', '2', '-', '2'])
    assert actual == expected


def TEST_calculateExpression_5():
    expected = 24
    actual = calculateExpression(['6', '*', '2', '*', '2'])
    assert actual == expected


def TEST_calculateExpression_6():
    try:
        actual = calculateExpression(['6', '*'])
        print("function error")
    except FormulaError:
        pass


def TEST_calculateExpression_7():
    try:
        actual = calculateExpression()
        print("function error")
    except TypeError:
        pass


def TEST_calculateExpression_8():
    expected = 1
    actual = calculateExpression(['1', '+', '1', '*', '2', '-', '2', '/', '2'])
    assert actual == expected


TEST_calculateExpression_1()
TEST_calculateExpression_2()
TEST_calculateExpression_3()
TEST_calculateExpression_4()
TEST_calculateExpression_5()
TEST_calculateExpression_6()
TEST_calculateExpression_7()
TEST_calculateExpression_8()


# #_________checkSign_____________________________
def TEST_checkSign_1():
    assert checkSign([1, "+", 3, "+", 3]) == None


def TEST_checkSign_2():
    assert checkSign([1, "-", 3, "-", 3, "-", 3]) == None


def TEST_checkSign_3():
    assert checkSign([1, "/", 3, "/", 3, "/", 3, "/", 3]) == None


def TEST_checkSign_4():
    assert checkSign([1, "*", 3, "*", 3, "*", 3, "*", 3, "*", 3]) == None


def TEST_checkSign_5():
    try:
        checkSign([1, 2, 3])
        print("function error")
    except FormulaError:
        pass


TEST_checkSign_1()
TEST_checkSign_2()
TEST_checkSign_3()
TEST_checkSign_4()
TEST_checkSign_5()
