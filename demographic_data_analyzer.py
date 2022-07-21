import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df_adult = pd.read_csv('adult.data.csv')
  
      # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df_adult.groupby(['race'])['race'].count().sort_values(ascending=False).values
  
      # What is the average age of men?
    average_age_men = round( df_adult.loc[df_adult['sex'] == 'Male'].mean(numeric_only=True)[0],1)
  
  
      # What is the percentage of people who have a Bachelor's degree?
    total_nb_people = df_adult['sex'].count()
    people_having_bachelor = df_adult.loc[df_adult['education'] =='Bachelors'].count()[0]
  
    percentage_bachelors = round(people_having_bachelor/total_nb_people,3)*100
  
      # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
      # What percentage of people without advanced education make more than 50K?
  
      # with and without `Bachelors`, `Masters`, or `Doctorate`
  
    people_advanced_education_with_more_than_50k = df_adult.loc[df_adult['education'].isin(('Bachelors','Masters','Doctorate')) & (df_adult['salary']=='>50K')].count()[0] 
  
    people_advanced_education = df_adult.loc[df_adult['education'].isin(('Bachelors','Masters','Doctorate'))].count()[0]
    
    
    lower_education = None
  
      # percentage with salary >50K
    people_without_education = df_adult.loc[~df_adult['education'].isin(('Bachelors','Masters','Doctorate'))].count()[0]
    people_without_education_earning_50k = df_adult.loc[~df_adult['education'].isin(('Bachelors','Masters','Doctorate')) & (df_adult['salary']=='>50K')].count()[0]
    higher_education_rich = round(people_advanced_education_with_more_than_50k/people_advanced_education,3)*100
  
    lower_education_rich = round(people_without_education_earning_50k/people_without_education,3)*100
  
      # What is the minimum number of hours a person works per week (hours-per-week feature)?
    minimum_hour_weekly = df_adult['hours-per-week'].min()
    min_work_hours = minimum_hour_weekly
  
      # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    people_work_minimum_hour = df_adult.loc[df_adult['hours-per-week']==1].count()[0]
    people_work_minimum_hour_50k = df_adult.loc[df_adult['hours-per-week']==1 & (df_adult['salary'] == '>50K')].count()[0]
    num_min_workers = people_work_minimum_hour = df_adult.loc[df_adult['hours-per-week']==1].count()[0]
  
    rich_percentage = people_work_minimum_hour_50k/people_work_minimum_hour*100
  
      # What country has the highest percentage of people that earn >50K?
    a = df_adult.groupby(['native-country']).count()
    b = df_adult.loc[(df_adult['salary'] == '>50K')].groupby(['native-country']).count()
    c = b/a
    cc = c.loc[(c['salary'] == c.max().values[0])]
    d = c.max()
    highest_earning_country = cc.index[0]
    highest_earning_country_percentage = round(d[0],3)*100
  
      # Identify the most popular occupation for those who earn >50K in India.
    people_more50k_india = df_adult.loc[(df_adult['native-country'] == 'India') & (df_adult['salary'] == '>50K')]
    people_more50k_india_activity_number = people_more50k_india.groupby(['occupation']).count()
    most_popular_occupation_india = people_more50k_india_activity_number.loc[(people_more50k_india_activity_number)['age']== people_more50k_india_activity_number.max().values[0]]    
    top_IN_occupation = most_popular_occupation_india.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
