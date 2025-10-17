#input as string
actual_title=str(input("enter a word\n").strip()).lower()
expected_title="dashboard"
if expected_title==actual_title:
    print("Test passed-Title matches")
else:
    print("Test failed-Title is not matching")
