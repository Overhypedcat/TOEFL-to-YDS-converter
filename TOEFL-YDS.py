while True:
    # Ask for the user input
    score = input("Enter the TOEFL score: ")

    # Convert the score to an integer
    try:
        score_int = int(score)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # TOEFL score cannot be over 120 and less than 0
    if score_int > 120:
        print("TOEFL score cannot exceed 120")
        continue

    if score_int < 0:
        print("TOEFL score cannot be less than 0")
        continue

    # Translate the score to YDS
    if score_int == 120:
        print("YDS equivalent is: 100")
    elif 114 <= score_int <= 119:
        print("YDS equivalent is: 95")
    elif 108 <= score_int <= 113:
        print("YDS equivalent is: 90")
    elif 102 <= score_int <= 107:
        print("YDS equivalent is: 85")
    elif 96 <= score_int <= 101:
        print("YDS equivalent is: 80")
    elif 90 <= score_int <= 95:
        print("YDS equivalent is: 75")
    elif 84 <= score_int <= 89:
        print("YDS equivalent is: 70")
    elif 78 <= score_int <= 83:
        print("YDS equivalent is: 65")
    elif 72 <= score_int <= 77:
        print("YDS equivalent is: 60")
    elif 66 <= score_int <= 71:
        print("YDS equivalent is: 55")
    elif 60 <= score_int <= 65:
        print("YDS equivalent is: 50")
    elif 54 <= score_int <= 59:
        print("YDS equivalent is: 45")
    elif 48 <= score_int <= 53:
        print("YDS equivalent is: 40")
    else:
        print("Score is not included in the YÖK's list.")