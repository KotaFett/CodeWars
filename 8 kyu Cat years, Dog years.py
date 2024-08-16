def human_years_cat_years_dog_years(human_years):
    catYears = 0
    dogYears = 0
    for i in range(1, human_years + 1):
        if i == 1:
            catYears += 15
            dogYears += 15
        elif i == 2:
            catYears += 9
            dogYears += 9
        else:
            catYears += 4
            dogYears += 5
    return [human_years, catYears, dogYears]