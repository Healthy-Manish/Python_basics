from question import Question
questions_prompts=[
    "what color are apples?\n(a)purple\n(b)Red/Green\n(c)Orange\n\n",
    "what color are Bananas?\n(a)teal\n(b)\Magenta\n(c)Yellow\n\n",
    "what color are Strwberries?\n(a)Yellow\n(b)Red\n(c)Blue\n\n",

]
questions = [Question(questions_prompts[0],"b"),
             Question(questions_prompts[1],"c"),
             Question(questions_prompts[2],"b")
             
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("You got "+str(score)+"/"+str(len(questions)))

run_test(questions)