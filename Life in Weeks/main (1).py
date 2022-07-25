age = input("What is your current age?")

year_days = 365
year_months = 12
year_weeks = 52

life_years = 90

life_months = int(life_years * year_months)
life_weeks = int(life_years * year_weeks)
life_days = int(life_years * year_days)

age_int = int(age)

life_remaining_months = life_months - age_int * year_months
life_remaining_weeks = life_weeks - age_int * year_weeks
life_remaining_days = life_days - age_int * year_days

print(f"You have {life_remaining_days} days, {life_remaining_weeks} weeks, and {life_remaining_months} months left.")
