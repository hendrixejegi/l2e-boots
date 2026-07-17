from main import join_strings

TestCase = tuple[list[str], str]

run_cases: list[TestCase] = [
    (["hello", "world"], "hello,world"),
    (["this", "list", "is", "so", "important"], "this,list,is,so,important"),
]

submit_cases: list[TestCase] = run_cases + [
    ([], ""),
    (["zuck", "satya", "cook", "bezos"], "zuck,satya,cook,bezos"),
    (["dota", "sc2", "overwatch", "diablo", "mtg"], "dota,sc2,overwatch,diablo,mtg"),
]


def test(input_list: list[str], expected: str) -> bool:
    print("---------------------------------")
    print(f"Input: {input_list}")
    print("")
    result = join_strings(input_list)
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
