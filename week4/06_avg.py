def average_grade(records):
    total_grade = sum(record[2] for record in records)
    return  total_grade /  len(records)

students =(
    ('james', 20, 85),
    ('sumeet', 22, 90),
    ('modi', 20, 95)
)

def main():
    avg_grade = average_grade(students)
    print("Average grade:" ,avg_grade)
main()