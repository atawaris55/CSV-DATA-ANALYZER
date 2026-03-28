import csv
import os

file_path="data.csv"
#need to initalize
def initialize_feild():
    if not os.path.exists(file_path):
        with open(file_path,"w",newline="")as file:
            writer=csv.writer(file)
            writer.writerow(["name","age","marks"])

#add of students
def add_student():
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    marks=int(input("Enter your marks: "))
    with open(file_path,"a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([name,age,marks])

    print("Student added successfully!")

#delete student
def delete_student():
    name=input("Enter the name of student you want to delete: ").lower()
    rows=[]
    confirm=input("Are you sure you want to delete this student? (y/n): ").lower()
    if confirm!="y":
        print("Deletion Canceled!")
        return
    found=False
    with open(file_path,"r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row["name"].lower()!=name:
                rows.append(row)
            else:
                found=True
    with open(file_path,"w",newline="") as file:
        fieldnames = ["name", "age", "marks"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        if found:
            print("Student deleted successfully!")
        else:
            print("Student not found!")

#search student
def search_student():
    name=input("Enter the name of student you want to search: ").lower()
    found=False
    with open(file_path,"r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row["name"].lower()==name:
                print(f"Name:{row['name']},Age:{row['age']},Marks:{row['marks']}")
                found=True
                break
        if not found:
            print("Student not found!")

#update marks
def update_marks():
    name=input("Enter the name of student you want to update marks: ").lower()
    found=False
    rows=[]
    with open(file_path,"r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row["name"].lower()==name:
                new_marks=int(input("Enter the new marks: "))
                row["marks"]=new_marks
                found=True
            rows.append(row)

    with open(file_path,"w",newline="") as file:
        fieldnames = ["name", "age", "marks"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)

        if found:
            print("Marks updated successfully!")
        else:
            print("Student not found!")

#show all students
def all_data():
    with open(file_path,"r") as file:
        reader=csv.reader(file)
        print("--All Students Data--")
        for row in reader:
            print(row)

#analyze data
def analyze_data():
    total_std=0
    marks_list=[]
    topper={"name":"","marks":0}
    with open(file_path,"r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            total_std+=1
            marks=int(row["marks"])
            marks_list.append(marks)
            if marks>topper["marks"]:
                topper["name"]=row["name"]
                topper["marks"]=marks
        if total_std==0:
            print("No students data to analyze!")
            return
    print("\n--- ANALYSIS ---")
    print("Total Students:", total_std)
    print("Average Marks:", round(sum(marks_list) / total_std, 2))
    print("Highest Marks:", topper["marks"])
    print("Topper:", topper["name"])

def main():
    initialize_feild()

    while True:
        print("\n===== CSV DATA ANALYZER =====")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Analyze Data")
        print("6. Show All Data")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            analyze_data()
        elif choice == "6":
            all_data()
        elif choice == "7":
            print("...EXITED")
            break
        else:
            print("Invalid choice. Try again.")
                    
if __name__ == "__main__":
    main()