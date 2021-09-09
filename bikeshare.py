import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('\nPlease enter name of the city to analyze - (Chicago, New York, Washington)\n')
            # User inputs should be made case insensitive
            if city.lower() in CITY_DATA:
                break
            print("\nInvalid value entered\nChoose Chicago, New York, or Washington\n\n")

        except Exception as e:
            print(e)

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month=input('\nPlease enter name of the month to filter by, or "all" to apply no month filter\n(all, January, February, March, April, May, or June)\n')
            # User inputs should be made case insensitive
            if month.lower() in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
                break
            print("\nInvalid value entered\nChoose all, January,February, March, April, May, or June)\n")

        except Exception as e:
            print(e)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day=input('\nPlease enter name of the day of week to filter by, or "all" to apply no day filter\n(all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday)\n')
            print('\n\nJust one monent....loading the data\n\n')
            print('\n\nData loaded. Now applying filters.. this will be done fast.')
            # User inputs should be made case insensitive
            if day.lower() in ['all', 'monday', 'tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                break
            print("\nInvalid value entered\nChoose all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday\n")

        except Exception as e:
            print(e)

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

    # Load csv data file into DataFrame
    df= pd.read_csv(CITY_DATA[city.lower()])

    # Convert Start Time column to datetime (string->datetime)
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from start time to create new columns
    df['month'] = df['Start Time'].dt.month  # It returns int datatype (e.g. 1,2,3,...)
    df['day'] = df['Start Time'].dt.day_name() # It returns The name of day in a week (ex: Friday)

    # filter by month if applicable
    if month != 'all':
        # use the index of months list to get the corresponding earliest
        months=['january','february','march','april','may','june']

        # get the index position from the months list using user input typed
        month=months.index(month.lower())+1

        # filter by month to create the new DataFrame
        # df['month'] == month <--- It returns Ture/False values
        # If true, keep the data, if not, skip it.
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        #filter by day of week to create the new DataFrame
        day=df[df['day']== day.title()] # It uses the same logic as above code for month

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(' What is the most popular month for traveling?\n', df['month'].mode()[0])

    # display the most common day of week
    print(' What is the most popular day for traveling?\n', df['day'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour  # It returns int datatype (e.g. 1,2,3,...)
    print(' What is the most popular hour of the day to start your travels?\n',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating Statistics...\n')
    start_time = time.time()

    # display most commonly used start station
    print(' What is the most popular Start Station?\n', df['Start Station'].mode()[0])

    # display most commonly used end station
    print(' What is the most popular End Station?\n', df['End Station'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(' Total travel time: ', df['Trip Duration'].sum())

    # display mean travel time
    print(' Average travel time: ', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating Statistics...\n')
    start_time = time.time()

    # Display counts of user types
    print(' Counts of user types:\n', df['User Type'].value_counts())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    print('\nCalculating Statistics...\n')
    start_time = time.time()

    # Display counts of gender
    print('\nWhat is the breakdown of gender?\n')
    if 'Gender' in df:
        print(df['Gender'].value_counts())
    else:
        print("No gender data to share")
        print("None")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    print('\nCalculating Statistics...\n')
    start_time = time.time()

    # Display earliest, most recent, and most common year of birth
    print('\nWhat is the oldest, youngest, and most popular year of birth, respectively?\n')
    if 'Birth Year' in df:
        print(' Oldest year of birth: {}\n Youngest year of birth: {}\n The most Popular year of birth: {}\n'.format(df['Birth Year'].min(), df['Birth Year'].max(), df['Birth Year'].mode()[0]))
    else:
        print("No birth year data to share")
        print("None")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def individual_trip_stats(df):
    """Raw data is displayed upon request"""

    print('\nDisplaying Raw Data...\n')
    start_time = time.time()

    while True:
        try:
            individual_trip=input("Would you like to view individual trip data? datatype 'yes' or 'no'\n")

            each_time=5
            while individual_trip.lower() == 'yes':
                print(df.head(each_time))
                each_time+=5
                individual_trip=input("Would you like to view individual trip data? Type 'yes' or 'no'\n")

            if individual_trip.lower() == 'no':
                break
        except Exception as e:
            print(e)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        individual_trip_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
