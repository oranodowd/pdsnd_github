import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        input_city = input("Please enter 'c' for Chigago data, 'n' for New York data, 'w' for Washington data....or enter 'x'to quit\n")
        if input_city == 'c':
            city="chicago"
            break
        elif input_city == 'n':
            city="new york city"
            break
        elif input_city == 'w':
            city="washington"
            break
        elif input_city == 'x':
            print("Quitting the program. Bye!")
            exit()
            break
        else:
            print("That's not a valid entry\n")    
    

    # get user input for the month (Choose 'all' or select january, february, etc up to June)
    while True:
        input_month = input("Please select a time period by entering : 'all', 'january','february','march','april','may','june'....or enter 'x'to quit\n")
        if input_month == "all":
            month="all"
            break
        elif input_month == "january":
            month="january"
            break
        elif input_month == "february":
            month="february"
            break
        elif input_month == "march":
            month="march"
            break
        elif input_month == "april":
            month="april"
            break
        elif input_month == "may":
            month="may"
            break
        elif input_month == "june":
            month="june"
            break
        elif input_month == 'x':
            print("Quitting the program. Bye!")
            exit()
        else:
            print("That's not a valid entry\n")    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        input_month = input("Please select a time period by entering : 'all', 'monday','tuesday','wednesday','thursday','friday','saturday','sunday'....or enter 'x'to quit\n")
        if input_month == "all":
            day="all"
            break
        elif input_month == "monday":
            day="monday"
            break
        elif input_month == "tuesday":
            day="tuesday"
            break
        elif input_month == "wednesday":
            day="wednesday"
            break
        elif input_month == "thursday":
            day="thursday"
            break
        elif input_month == "friday":
            day="friday"
            break
        elif input_month == "saturday":
            day="saturday"
            break
        elif input_month == "sunday":
            day="sunday"
            break
        elif input_month == 'x':
            print("Quitting the program. Bye!")
            exit()
        else:
            print("That's not a valid entry\n")  
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nHere are the Most Frequent Times of Travel for the dataset you chose...\n')
    start_time = time.time()
    ## convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    most_popular_month = df['month'].mode()[0]
    print("**** The most popular month is", most_popular_month)

    # display the most common day of week
    most_popular_day = df['day_of_week'].mode()[0]
    print("**** The most popular day is", most_popular_day)

    # display the most common start hour
    ## extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    ## find the most popular hour
    most_popular_hour = df['hour'].mode()[0]
    print("**** The most popular hour is", most_popular_hour,":00 \n")

    print(">>>> These calculations took %s seconds." % round((time.time() - start_time),4))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nHere are The Most Popular Stations and Trips for the dataset you chose...\n')
    start_time = time.time()

    # display most commonly used start station
    most_popular_start_station = df['Start Station'].mode()[0]
    print("**** The most popular starting station is", most_popular_start_station)

    # display most commonly used end station
    most_popular_end_station = df['End Station'].mode()[0]
    print("**** The most popular ending station is", most_popular_end_station)

    # display most frequent combination of start station and end station trip
    # create a new column of start stationa and end stations combined..
    df['start_and_end'] = df['Start Station'] + ' to ' + df['End Station']
    # get the most popular entry..
    most_popular_start_and_end = df['start_and_end'].mode()[0]
    print("**** The most popular start and ending station combination is the journey from", most_popular_start_and_end)

    print(">>>> These calculations took %s seconds." % round((time.time() - start_time),4))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Durations for the dataset you chose...\n')
    start_time = time.time()

    total_travel_time_seconds = df['Trip Duration'].sum()
    total_travel_time_minutes = total_travel_time_seconds//60
    total_travel_time_seconds_remaining = total_travel_time_seconds%60
    print("**** The total travel time during this period was",total_travel_time_minutes,"minutes and",round(total_travel_time_seconds_remaining,0),"seconds")
    
    # display mean travel time
    mean_travel_time_seconds = df['Trip Duration'].mean()
    mean_travel_time_minutes = mean_travel_time_seconds//60
    mean_travel_time_seconds_remaining = mean_travel_time_seconds%60
    print("**** The mean travel time during this period was",mean_travel_time_minutes,"minutes and",round(mean_travel_time_seconds_remaining,0),"seconds")

    print(">>>> These calculations took %s seconds." % round((time.time() - start_time),4))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print("**** User stats *****")
    print(user_types_count,"\n")

    # Display counts of gender
    if 'Gender' in df:
        gender_types_count = df['Gender'].value_counts()
        print("\n**** Gender stats *****")
        print(gender_types_count)
    else:
        print("No data found of User genders")

    # Display earliest, most recent, and most common year of birth
    if 'Birth year' in df:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("\nThe earliest birth was in the year",int(earliest_birth_year),",the most recent birth was in the year",
            int(most_recent_birth_year),"and the most common birth year was",int(most_common_birth_year),"!")
    else:
        print("No data found of User birth years")

    print("\n>>>> These calculations took %s seconds." % round((time.time() - start_time),4))
    print('-'*40)

def get_sample_data(df,start_row,number_of_rows):
    return df.iloc[start_row:number_of_rows]

def show_sample_data(df):
    """Displays some sample data entries from the chosen dataset"""
    start_row = 0
    number_of_rows = 5
    while True:
        sample_data_answer = input("Enter 'y' to see some sample data....or any other key to continue\n")
        if sample_data_answer == 'y':
            start_time = time.time()
            # Show 5 rows of sample data from the DataFrame
            print('\nFetching sample data...\n')
            print(get_sample_data(df,start_row,number_of_rows))
            start_row = start_row + number_of_rows
            number_of_rows = number_of_rows + number_of_rows
            print("\n>>>> Fetching the sample data entries took %s seconds." % round((time.time() - start_time),4))
        else:
            print("Ok, I won't fetch some sample data from this dataset\n")
            break    
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        print("Ok! Here is what you chose:\n")
        print("CITY >> ",city)
        print("MONTHS >> ",month)
        print("DAYS >> ",day)
        print("\nLets run some calculations...stand by...\n")
        print('='*40)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_sample_data(df)

        restart = input('\nWould you like to restart the program? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
