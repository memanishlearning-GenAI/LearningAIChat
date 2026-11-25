import os
import json
import student_operations

def main():
    
    file_name = 'students.json'
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r') as file:
                students = json.load(file)
                print("Existing student data:")
               
        except json.JSONDecodeError:
            print("Error: The file contains invalid JSON.")
            return
        
    else:
        students = []
        print("No existing student data found. Starting fresh.")
        while True:
            try:
                name = input("Enter the student's name: ")
                age = int(input("Enter the student's age: "))
                course = input("Enter the student's course: ")

                student = student_operations.add_students(name, age, course)
                students.append(student)

                with open(file_name, 'w') as file:
                    json.dump(students, file,indent=4)

            except ValueError:
                    print("Invalid input. Please enter a valid age.")
            except FileNotFoundError:
                    print("Error: The file does not exist.")
            except Exception as e:
                    print(f"An unexpected error occurred: {e}") 

            choice = input("Do you want to add another student? (yes/no): ")
                
            if choice.lower() != "yes":
                print("Exiting the program.")
                break
            
            #Read and display the student data from the JSON file
            with open(file_name, 'r') as file:
                saved_students = json.load(file)
                print("Student data loaded from JSON:")
                
                print(json.dumps(saved_students, indent=4))

if __name__ == "__main__":
    main()