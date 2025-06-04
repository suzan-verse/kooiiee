name= str(input("Entre the Student Name :"))
marks= int(input("Entre the Student Marks :"))

if marks >= 90:
    print(f"{name},The Grade is A+. Well done!")

elif 80 <= marks <=89 :
    print(f"{name},The Grade is A. You are on right track. Well done!")

elif 70 <= marks <=79 :
    print(f"{name},The Grade is B+.You must work hard. Keep up the work!") 

elif 60 <= marks <= 69:
    print (f"{name},The Grade is B. You need more focous on your study. Study hard!")

else:
    print(f"{name},You are Not Graded. Give your more time into studies!")      

       

    