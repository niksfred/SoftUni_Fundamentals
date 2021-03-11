def loading_bar(percents):
    percent_marks = int(percents / 10)
    if not percent_marks == 10:
        print(f"{percents}% [", end= "")
        for i in range(percent_marks):
            print("%", end= "")
        for i in range(10 - percent_marks):
            print(".", end="")
        print("]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")

percentage = int(input())
loading_bar(percentage)
