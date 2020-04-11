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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = ['chicago', 'new york city', 'washington', 'all']
    city = input("Which city would you like to look at: Chicago, New York City, Washington or all?").lower()
    while city not in city_list:
        print("Please enter a valid value!", end=' ')
        city = input("Please try again: ")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input("Which month would you like to look at: January, February, March, April, May, June or all?").lower()
    while month not in month_list:
        print("Please enter a valid value!", end=' ')
        month = input("Please try again: ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = input("Which day would you like to look at: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?").lower()
    while day not in day_list:
        print("Please enter a valid value!", end=' ')
        day = input("Please try again: ")

    print("You have chosen: "+city+' '+month+' '+day)

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of the week: ', most_common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most popular start hour: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most common start station: ', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most common end station: ', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + 'to' + df['End Station']
    combination = df['combination'].mode()[0]
    print('Most common combination of start and end station: ', combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration'].sum()
    print('Total trip duration: ', trip_duration)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of user types: ',user_types)

    # TO DO: Display counts of gender and earliest, most recent, and most common year of birth
    if city != 'washington':
          gender_count = df['Gender'].value_counts()
          print('Count of gender: ',gender_count)

          earliest_birth_year = df['Birth Year'].min()
          print('Earliest birth year: ',earliest_birth_year)

          recent_birth_year = df['Birth Year'].max()
          print('Recent birth year: ',recent_birth_year)

          most_common_birth_year = df['Birth Year'].mode()[0]
          print('Most common birth year: ',most_common_birth_year)

    else:
          print('Gender and birth year information is not available for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    raw_data_input = input("Do you want to see raw data? Please enter 'yes' or 'no'.").lower()
    row_index = 0
    while True:
        if raw_data_input == 'yes':
            print(df[row_index:row_index+5])
            row_index = row_index +5
            raw_data_input = input("Do you want to see five more rows? Please enter 'yes' or 'no'.").lower()
        else:
            return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
