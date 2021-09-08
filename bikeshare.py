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

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Please enter name of the city to analyze - (chicago, new york city, washington)  ')
            if city in CITY_DATA:
                break
            print("Invalid value entered")

        except Exception as e:
            print(e)

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month=input('Please enter name of the month to filter by, or "all" to apply no month filter - (all, january, february, ... , june)  ')
            if month is not None:
                break
            print("Invalid value entered")

        except Exception as e:
            print(e)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day=input('Please enter name of the day of week to filter by, or "all" to apply no day filter - (all, monday, tuesday, ... sunday)  ')
            if day is not None:
                break
            print("Invalid value entered")

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
    df= pd.read_csv(CITY_DATA[city])

    # Convert Start Time column to datetime (string->datetime)
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from start time to create new columns
    df['month'] = df['Start Time'].dt.month  # It returns int datatype (e.g. 1,2,3,...)
    df['day'] = df['Start Time'].dt.day_name() # It returns The name of day in a week (ex: Friday)

    # filter by month if applicable
    if month != 'all':
        # use the index of months list to get the corresponding earliest
        months=['january','fabruary','march','april','may','june','july','august','september','october','november','december']

        # get the index position from the months list using user input typed
        month=months.index(month)+1

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
    print('The most common month: ', df['month'].mode()[0])

    # display the most common day of week
    print('The most common day of week: ', df['day'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour  # It returns int datatype (e.g. 1,2,3,...)
    print('The most common start hour: ',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station: ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The most commonly used end station: ', df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time: ', df['Trip Duration'].max())

    # display mean travel time
    print('Mean travel time: ', df['Trip Duration'].min())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types:\n', df['User Type'].value_counts())

    # Display counts of gender
    print('counts of gender:\n', df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    print('Earliest, most recent, and most common year of birth: ', df['Birth Year'].mode().min())

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
