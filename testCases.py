import numberComparator

def testNumberComparator():
    print("assertValuesEqual test")
    print("If the two values are equal, then the test case passes, and if they are not equal,then the test case fails")
    assert numberComparator.numComparitor.compare(1, 1) == 0, "The two values are not equal"


    print("assertValuesNotEqual test")
    print("A test case passes when two values are not equal; otherwise, the test case fails")
    assert numberComparator.numComparitor.compare(1, 2) != 0, "The two values are not equal"

    print("assertValuesGreater test")
    print("If the first value is greater than the second value, then the test passes, or else the test case fails")

    print("assertValuesGreaterEqual")
    print("If value1 is greater than or equal to value2, then the test case passes, otherwise fails.")
    assert numberComparator.numComparitor.compare(1, 1) == 1, "The first value is not greater than the second value"

    print("assertValuesLess test")
    print("With assertValuesLess, a test case passes when value1 is less than value2, and the test case fails when value1 is less")
    assert numberComparator.numComparitor.compare(1, 2) == -1, "The first value is not less than the second value"




testNumberComparator()