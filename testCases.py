# Cis 4150 A2 Part 1
# Written by: Ian McKechnie
#Written on Oct 18, 2022

#Functions to be tested
def listComparator(x, y):
    y = list(y)
    for elem in x:
        try:
            y.remove(elem)
        except ValueError:
            return False
    return True

def numCompare(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0

#Functions doing the testing
def testNumberComparator():
    print("assertValuesEqual test")
    print("If the two values are equal, then the test case passes, and if they are not equal,then the test case fails")
    assert numCompare(1, 1) == 0, "The two values are not equal"


    print("assertValuesNotEqual test")
    print("A test case passes when two values are not equal; otherwise, the test case fails")
    assert numCompare(1, 2) != 0, "The two values are equal"

    print("assertValuesGreater test")
    print("If the first value is greater than the second value, then the test passes, or else the test case fails")
    assert numCompare(2, 1) > 0, "The first value is not greater than the second value"

    print("assertValuesGreaterEqual")
    print("If value1 is greater than or equal to value2, then the test case passes, otherwise fails.")
    assert numCompare(1, 0) == 1 or 0, "The first value is less than the second value"

    print("assertValuesLess test")
    print("With assertValuesLess, a test case passes when value1 is less than value2, and the test case fails when value1 is less")
    assert numCompare(1, 2) == -1, "The first value is not less than the second value"

    print("assertValuesLessEqual test")
    print("The assertValuesLessEqual method passes the test case only when value1 is less than or equal to value2; otherwise, the test leads to failure.")
    assert numCompare(1, 2) == -1 or 0, "The first value is not less than or equal to the second value"


def listComparator():
    #Declaring lists
    a = [1, 2, 3]
    b = [2, 3, 1]
    c = [1, 2, 3, 4]
    d = [1, 2, 4]

    print("assertListEqual test")
    print("The assertListEqual function allows us to compare two lists. When both lists contain the same elements, then the test case passes; if lists do not have the same elements, then the test case fails.")
    assert listComparator(a, b) == True, "The two lists are not equal"

    print("")

print("Testing Question 1")
testNumberComparator()
print("\nFinished testing Question 1 with no Errors")

print("Testing Question 2")
listComparator()
print("\nFinished testing Question 2 with no Errors")

print("Testing Complete")
