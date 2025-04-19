import calendar

def main(year):
    for month in range(1, 13):
        print(calendar.month(year, month))

if __name__ == "__main__":
    year = int(input("Enter a year: "))
    main(year)
