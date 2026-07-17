from main import divide_list

TestCase = tuple[list[int], int, list[float]]

run_cases: list[TestCase] = [
    ([6, 8, 10], 2, [3.0, 4.0, 5.0]),
    ([1, 2, 3, 4], 1, [1.0, 2.0, 3.0, 4.0]),
]

submit_cases: list[TestCase] = run_cases + [
    ([15, 30, 45], 3, [5.0, 10.0, 15.0]),
    ([0], 1, [0.0]),
    ([27, 54, 81], 9, [3.0, 6.0, 9.0]),
    ([100, 200, 300, 400], 10, [10.0, 20.0, 30.0, 40.0]),
]


def test(input_list: list[int], divisor: int, expected: list[float]) -> bool:
    print("---------------------------------")
    print("Inputs:")
    print(f" * List of numbers: {input_list}")
    print(f" * Divisor: {divisor}")
    result = divide_list(input_list, divisor)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    if result == expected:
        print("Pass")
        return True
    print("Fail")
    return False


def main() -> None:
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
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
