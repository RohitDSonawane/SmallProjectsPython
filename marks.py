# Create a dictionary to store student names and their corresponding
# scores in a test. Write functions to add new students, update scores,
# delete students, and find the student with the highest score.

students_scores={}
def add_student(name,score):
    students_scores[name]=score
def update_score(name, score):
    if name in students_scores:
        students_scores[name] = score
    else:
        print(f"Student {name} not found.")

def delete_student(name):
    if name in students_scores:
        del students_scores[name]
    else:
        print(f"Student {name} not found.")
def find_highest_score():
    if not students_scores:
        print("No student data available.")
        return None
    highest=max(students_scores.values())
    for name,score in students_scores.items():
        if score == highest:
            return name, score
def display_students():
    if not students_scores:
        print("No student data available.")
    for name, score in students_scores.items():
        print(f"Student: {name}, Score: {score}")
while True:
    print("\n")
    print("----------*****----------")
    print("Student Scores Menu:")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Update Score")
    print("4. Delete Student")
    print("5. Find Highest Score")
    print("6. Exit")
    print("----------*****----------")
    print("\n")
    try:
        choice=int(input("Enter your choice (1-6): "))
        if choice == 1:
            add_student(input("Enter student name: ").strip(),int(input("Enter student score: ").strip()))
        elif choice == 2:
            display_students()
        elif choice == 3:
            update_score(input("Enter student name to update: ").strip(),int(input("Enter new score: ").strip()))
        elif choice == 4:
            delete_student(input("Enter student name to delete: ").strip())
        elif choice == 5:
            print(find_highest_score())
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.\n")
    except ValueError:
        print("Invalid input. Please enter a number (1-6).\n")
    except Exception as e:
        print("An unexpected error occurred:\n",e)

