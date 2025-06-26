def quiz():
    questions = {}
    n = int(input("How many questions do you want to add? "))
    for i in range(n):
        q = input(f"Enter question {i+1}: ")
        a = input("Enter correct answer: ")
        questions[q] = a
    score = 0
    for q, ans in questions.items():
        user_ans = input(q + " ")
        check = lambda x, y: x.strip().lower() == y.strip().lower()
        if check(user_ans, ans):
            print("Correct!\n")
            score += 1
        else:
            print(f" Wrong! Correct answer is: {ans}\n")
    print(f"Your Score: {score}/{n}")

# Demo
quiz()
