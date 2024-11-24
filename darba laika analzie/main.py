import csv
from datetime import datetime

def calculate_hours(start_time, end_time):
    time_format = "%H:%M"
    if start_time == "Nav" or end_time == "Nav":
        return 0 
    try:
        start = datetime.strptime(start_time, time_format)
        end = datetime.strptime(end_time, time_format)
        if end < start:
            return 0
        delta = end - start
        return delta.total_seconds() / 3600
    except ValueError:
        return 0 

def process_work_hours(input_file, output_file):
    weekly_hours = {}
    daily_hours = {}
    max_hours = 0
    max_employee = ""

    with open(input_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employee = row['Darbinieks']
            day = row['Diena']
            start_time = row['Sākums']
            end_time = row['Beigas']

            daily_hours_value = calculate_hours(start_time, end_time)

            if employee not in weekly_hours:
                weekly_hours[employee] = []
                daily_hours[employee] = {}

            daily_hours[employee][day] = daily_hours_value
            weekly_hours[employee].append(daily_hours_value)

           
            total_hours = sum(weekly_hours[employee])
            if total_hours > max_hours:
                max_hours = total_hours
                max_employee = employee

    for employee, hours_per_day in daily_hours.items():
        print(f"Darbinieks {employee}:")
        for day, hours in hours_per_day.items():
            print(f"  {day}: {hours:.2f} stundas")
        print()

    print("Kopējais nostrādātais stundu skaits nedēļā:")
    for employee, hours in weekly_hours.items():
        total_weekly_hours = sum(hours)
        print(f"{employee}: {total_weekly_hours:.2f} stundas")

    print(f"\nDarbinieks ar visvairāk nostrādātajām stundām nedēļas laikā: {max_employee}, kopā: {max_hours:.2f} stundas")

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Darbinieks', 'Nedēļas kopā stundas']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for employee, hours in weekly_hours.items():
            total_weekly_hours = sum(hours)
            writer.writerow({'Darbinieks': employee, 'Nedēļas kopā stundas': total_weekly_hours})

input_file = 'darba_laiki.csv'
output_file = 'nedelas_stundas.csv'

process_work_hours(input_file, output_file)
