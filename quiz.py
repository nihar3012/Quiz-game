def show_menu():

    print("Quiz Game")
    print("----------")
    print()
    print("1.Run Quiz")
    print("2.Enter a Question")
    print("3.Exit")
    print()
    
    option=input("Enter options: ")
    return option

def ask_questions():
    with open("question.txt")as f:
        questions=f.read().split("\n")[:-1]
    score=0
    for q in questions:
        qlist=q.split("|")
        # quest=qlist[0]
        # ans=qlist[1]
        quest,ans=qlist
        guess = input(quest)
        if guess==ans:
            score+=1
    print("you scored is {0} ".format(score))


def add_a_question():
  question=input("Enter a Question: ")
  answer=input("Ok then tell me ,"+question.lower()+": ")
  
  with open ("question.txt","a") as f:
      line=question+"|"+answer+"\n"
      f.write(line)
      

while True:   
    option = show_menu()
    if int(option)== 1:
        ask_questions()
    if int(option)== 2:
       add_a_question()
    if int(option) == 3:
        break