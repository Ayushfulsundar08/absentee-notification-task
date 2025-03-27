import pandas as pd

attendance_file = input("Enter attendance file name (with .xlsx extension): ")

try:
    attendance_df = pd.read_excel(attendance_file)
    print("Attendance Data Loaded Successfully")

except Exception as e:
    print("Error loading attendance file:", e)
    exit()

try:
    master_roll_df = pd.read_excel('master_roll.xlsx')
    print("Master Roll Loaded Successfully")

except Exception as e:
    print("Error loading master roll file:", e)
    exit()

try:
    # Use 'roll' instead of 'student_id'
    present_rolls = set(attendance_df['roll'])
    all_rolls = set(master_roll_df['roll'])

    absentees = all_rolls - present_rolls

    print("Absentee Roll Numbers:")
    print(absentees)

except Exception as e:
    print("Error:", e)
