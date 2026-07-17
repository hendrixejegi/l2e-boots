from main import remove_nonints

TestCase = tuple[list[object], list[int]]

run_cases: list[TestCase] = [
    (["200", 300, 2, False, "otherstring", 6], [300, 2, 6]),
    ([True, 300, 2, False, "otherstring", 76, 86, "morestrings"], [300, 2, 76, 86]),
]

submit_cases: list[TestCase] = run_cases + [
    ([300, 300, 2, False, "otherstring", 6, {}, 16], [300, 300, 2, 6, 16]),
    (["200", 300, 2, False, "something", 7, "something else"], [300, 2, 7]),
    (["string", True, {}, []], []),
    ([], []),
    ([123, 456, 789], [123, 456, 789]),
    (["123", "456", "789"], []),
]


def test(input_list: list[object], expected: list[int]) -> bool:
    print("---------------------------------")
    print(f"Input: {input_list}")
    print("")
    result = remove_nonints(input_list)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    if result == expected:
        return True
    return False


def main() -> None:
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            print("Pass")
            passed += 1
        else:
            print("Fail")
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases: list[TestCase] = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
