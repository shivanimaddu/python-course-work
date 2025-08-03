questions = [
    {"question": "Which of the following is the correct file extension for Python files?",
     "options": ["A. .pyth", "B. .pt", "C. .py", "D. .pyt"],
     "answer": "C"},

    {"question": "What is the output of this code? print(type(10))",
     "options": ["A. <class 'int'>", "B. <class 'str'>", "C. <class 'float'>", "D. <class 'bool'>"],
     "answer": "A"},

    {"question": "Which keyword is used to create a function in Python?",
     "options": ["A. func", "B. def", "C. function", "D. define"],
     "answer": "B"},

    {"question": "How do you insert COMMENTS in Python code?",
     "options": ["A. /* comment */", "B. // comment", "C. # comment", "D. <!-- comment -->"],
     "answer": "C"},

    {"question": "What will be the output of this code? print(2 ** 3)",
     "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
     "answer": "B"},

    {"question": "What data type is the object below? L = [1, 2, 3]",
     "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
     "answer": "A"},

    {"question": "How do you start a for loop in Python?",
     "options": ["A. for x to range(5):", "B. for x in range(5):", "C. for (x=0; x<5; x++):", "D. foreach x in range(5):"],
     "answer": "B"},

    {"question": "What is the output of: print('Hello'[1])",
     "options": ["A. H", "B. e", "C. l", "D. o"],
     "answer": "B"},

    {"question": "Which of the following is NOT a valid variable name?",
     "options": ["A. _myvar", "B. my_var", "C. 2var", "D. var2"],
     "answer": "C"},

    {"question": "How do you create a dictionary in Python?",
     "options": ["A. dict = {}", "B. dict = []", "C. dict = ()", "D. dict = <>"],
     "answer": "A"},

    {"question": "What will this code output? print(bool(0))",
     "options": ["A. True", "B. False", "C. 0", "D. None"],
     "answer": "B"},

    {"question": "How can you generate a random number between 1 and 10 (inclusive)?",
     "options": ["A. random(1,10)", "B. randint(1,10)", "C. random.randint(1,10)", "D. rand(1,10)"],
     "answer": "C"},

    {"question": "Which of the following is used to handle exceptions?",
     "options": ["A. try/except", "B. do/catch", "C. try/catch", "D. handle/error"],
     "answer": "A"},

    {"question": "What is the output of: print(len('Python'))",
     "options": ["A. 5", "B. 6", "C. 7", "D. Error"],
     "answer": "B"},

    {"question": "Which statement is used to stop a loop?",
     "options": ["A. stop", "B. break", "C. exit", "D. return"],
     "answer": "B"},

    {"question": "How do you import a module named math?",
     "options": ["A. import math", "B. include math", "C. using math", "D. require math"],
     "answer": "A"},

    {"question": "Which operator is used for floor division?",
     "options": ["A. /", "B. //", "C. %", "D. **"],
     "answer": "B"},

    {"question": "What is the output of: print(3 == 3.0)",
     "options": ["A. True", "B. False", "C. Error", "D. None"],
     "answer": "A"},

    {"question": "What will the following code print? x = [1, 2, 3]; print(x[::2])",
     "options": ["A. [1, 3]", "B. [2]", "C. [1, 2]", "D. [3]"],
     "answer": "A"},

    {"question": "How do you start a comment block (multi-line comment) in Python?",
     "options": ["A. ''' or \"\"\"", "B. //", "C. #", "D. /*"],
     "answer": "A"},
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    while True:
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer in ['A', 'B', 'C', 'D']:
            break
        else:
            print("Invalid input. Please enter A, B, C, or D.")
    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {q['answer']}.")

print(f"\nQuiz finished! Your final score is {score}/{len(questions)}")


