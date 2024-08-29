price =1

ques = [

        {
            "question": "What is Dogesh?",
            "options":["1. 14", "2. aashiqui ka 14", "3. Mutthal", "4. all of the above"],
            "ans": 4},
        {   "question": "What is Dk?",
            "options":["1. aaurat", "2. aaurat ki moti cuchi", "3. moti cuchi", "4.cuchi "],
            "ans": 2},
        {
            "question": "What is Aslam?",
            "options":["1. molvi", "2. molvi ka aand", "3. molvi k aand ka baal", "4. boy "],
            "ans": 3},
        { 
            "question": "What is Nav?",
            "options":["1. aadmi", "2. aadmi ki aaurat", "3. tampu ki aaurat", "4. land "],
            "ans": 2

        }
]



for x in ques:
    print(x["question"])
    for option in x["options"]:
        print(option)

    user_ans = int(input("enter your option : "))

    if user_ans == x["ans"]:
        print("tere muh m",price, "land")
        price+=1

    else:
         print("galat jawab ab aap chudogi")
         continue
    
print("aapko milte hai",price,"land")
