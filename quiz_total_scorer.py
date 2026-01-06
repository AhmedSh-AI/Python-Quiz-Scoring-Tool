print("====== Quizzes ======")
quiz1 = int(input("Enter the score of the first quiz: "))
quiz2 = int(input("Enter the score of the second quiz:"))
quiz3 = int(input("Enter the score of the third quiz:"))

print("====== Mid-term ======")
midterm = int(input("Enter the score of the mid-term: "))

print("====== Final ======")
final = int(input("Enter the score of the final: "))

print("====== results ======")
quiz_total = quiz1+quiz2+quiz3
print("Quizzes_total",quiz_total)
print("Mid-term",midterm)
print("Final",final)

print("====== Total ======")
print(quiz_total+midterm+final ,"from 500")