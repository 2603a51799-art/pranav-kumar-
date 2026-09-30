feedback =input("enter student feedback")
feedback = feedback.strip()
keywords= ["good","bad","python"]
print("\n====KEYWORD ANALYSIS====")
for keyword in keywords:
    count =feedback.count(keyword)
    print(keyword, ":" ,count)
    if keyword in feedback:
        print("keyword found")
    else:
         print("sala bsdk nahi mil rha be")
        
         
         