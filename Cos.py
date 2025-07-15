def get_grade(score):
    """
    Determines the grade based on the score provided.
    """
    if 70 <= score <= 100:
        return 'A'
    elif 60 <= score <= 69:
        return 'B'
    elif 50 <= score <= 59:
        return 'C'
    elif 45 <= score <= 49:
        return 'D'
    elif 40 <= score <= 44:
        return 'E'
    elif 0 <= score < 40:
        return 'F'
    else:
        return None

def main():
    """
    Main function to receive input and display grade.
    """
    try:
        # Ask the user to enter the score
        score_input = input("Enter the student's score (0 - 100): ")
        score = int(score_input)

        # Get grade
        grade = get_grade(score)

        # Display result
        if grade is not None:
            print(f"The grade for score {score} is: {grade}")
        else:
            print("Invalid score! Please enter a number between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter a valid numeric score.")

# Run the program
if __name__ == "__main__":
    main()
