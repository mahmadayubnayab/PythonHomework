# number = int(input('enter a number : '))
# if number % 2 == 0:
#     print('that number you entered  is even ')
# else :
#     print('that number you entered is odd')

# # class animal save different animals and display their habits

# class animal:
#     def __init__(self , name , speak, eats):
#         self.name = name
#         self.speak = speak
#         self.eats = eats
#     def display(self):
#         print(self.name)
#         print(self.speak)
#         print(self.eats)
# cat = animal('cat', 'woo' , 'meat')
# cat.display()
# dog = animal( 'dog ', 'ghap' , 'bread')
# dog.display()
# Eggal = animal('Eggal', 'hide','frouite')
#Eggal.display()


# practical lab : CSv grade book


# import csv
# import os
#
# INPUT_FILE = "students.csv"
# OUTPUT_FILE = "results.csv"
#
#
# PASS_THRESHOLD = 60.0
#
#
# def create_sample_csv():
#     """Create the input CSV file if it does not already exist."""
#     if os.path.exists(INPUT_FILE):
#         return
#
#     students = [
#         {"student_id": "1001", "name": "Ahmad Ali", "midterm": "75", "final": "85"},
#         {"student_id": "1002", "name": "Maryam, Khan", "midterm": "90", "final": "95"},
#         {"student_id": "1003", "name": "O'Neil John", "midterm": "55", "final": "60"},
#         {"student_id": "1004", "name": "Farid Ahmad", "midterm": "40", "final": "50"},
#         {"student_id": "1005", "name": "Zahra Noor", "midterm": "80", "final": "70"},
#     ]
#
#     fieldnames = ["student_id", "name", "midterm", "final"]
#
#     with open(INPUT_FILE, "w", newline="", encoding="utf-8") as file:
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(students)
#
#
# def read_students():
#     """Read students using csv.DictReader."""
#     records = []
#
#     with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file:
#         reader = csv.DictReader(file)
#
#         required_columns = {"student_id", "name", "midterm", "final"}
#
#         if reader.fieldnames is None:
#             raise ValueError("students.csv has no header row.")
#
#         missing = required_columns - set(reader.fieldnames)
#
#         if missing:
#             raise ValueError(
#                 "Missing columns: " + ", ".join(sorted(missing))
#             )
#
#         for line_number, row in enumerate(reader, start=2):
#
#             try:
#                 midterm = float(row["midterm"])
#                 final = float(row["final"])
#
#             except (ValueError, TypeError):
#                 raise ValueError(
#                     f"Invalid mark at line {line_number}. "
#                     "Marks must be numbers."
#                 )
#
#             total = midterm + final
#             average = total / 2
#
#             records.append({
#                 "student_id": row["student_id"],
#                 "name": row["name"],
#                 "midterm": midterm,
#                 "final": final,
#                 "total": total,
#                 "average": average,
#                 "status": (
#                     "Passed"
#                     if average >= PASS_THRESHOLD
#                     else "Failed"
#                 )
#             })
#
#     return records
#
#
# def display_passed_students(records):
#
#     print("\nStudents who passed")
#     print("-" * 70)
#
#     found = False
#
#     for student in records:
#
#         if student["average"] >= PASS_THRESHOLD:
#
#             found = True
#
#             print(
#                 f'ID: {student["student_id"]} | '
#                 f'Name: {student["name"]} | '
#                 f'Average: {student["average"]:.2f}'
#             )
#
#     if not found:
#         print("No student passed the threshold.")
#
#
# def write_results(records):
#
#     fieldnames = [
#         "student_id",
#         "name",
#         "midterm",
#         "final",
#         "total",
#         "average",
#         "status"
#     ]
#
#     with open(
#         OUTPUT_FILE,
#         "w",
#         newline="",
#         encoding="utf-8"
#     ) as file:
#
#         writer = csv.DictWriter(
#             file,
#             fieldnames=fieldnames
#         )
#
#         writer.writeheader()
#
#         for student in records:
#
#             writer.writerow({
#                 "student_id": student["student_id"],
#                 "name": student["name"],
#                 "midterm": student["midterm"],
#                 "final": student["final"],
#                 "total": student["total"],
#                 "average": f'{student["average"]:.2f}',
#                 "status": student["status"]
#             })
#
#
# def main():
#
#     print("=== CSV Gradebook ===")
#
#     try:
#
#
#         create_sample_csv()
#
#
#         records = read_students()
#
#
#         print("\nAll Students")
#         print("-" * 70)
#
#         for student in records:
#
#             print(
#                 f'ID: {student["student_id"]} | '
#                 f'Name: {student["name"]} | '
#                 f'Total: {student["total"]:.2f} | '
#                 f'Average: {student["average"]:.2f} | '
#                 f'Status: {student["status"]}'
#             )
#
#
#         display_passed_students(records)
#
#
#         write_results(records)
#
#         print("\nDone!")
#         print(f"Input file : {INPUT_FILE}")
#         print(f"Output file: {OUTPUT_FILE}")
#
#     except FileNotFoundError as error:
#         print(f"File error: {error}")
#
#     except ValueError as error:
#         print(f"Data error: {error}")
#
#     except OSError as error:
#         print(f"File system error: {error}")
#
#
# if __name__ == "__main__":
#     main()

# hackerrank issues

# use loop and print  attendence tables


#
# for i in range(1,11):
#     for j in range(1,11):
#         print(i, "x", j, "=", i*j)
#
#         if j == 10:
#             print("-----------------------------------")

# a = 1
# while(a<100):
#       a += 1
#       print(a)

