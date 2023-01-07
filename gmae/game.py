from Question import Question

question_prompt = (
  "Who won the world cup?\n(a) Argentina\n(b) Brazil\n(c) France\n\n",
  "What's the colour of a Mango?\n(a) Yellow\n(b) Mango Yellow\n(c) Red\n\n",
  "How many colours are there is USA's flag?\n(a) 2\n(b) 4\n(c) 3\n\n",
  "Which country was always independent?\n(a) Japan\n(b) Bangladesh\n(c) Nepal\n\n",
  "Which country's flag has light blue, white and golden sun?\n(a) Brazil\n(b) Argentina\n(c) France\n\n",
)

questions = [
  Question(question_prompt[0], "a"),
  Question(question_prompt[1], "b"),
  Question(question_prompt[2], "c"),
  Question(question_prompt[3], "c"),
  Question(question_prompt[4], "b"),
]


def run_test(question_s):
  score = 0
  for question in question_s:
    answer = input(question.prompt)
    if answer == question.answer:
      score += 1
  print("You got " + str(score) + "/" + str(len(question_s)) + " correct")


run_test(questions)
