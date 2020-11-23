import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    # Asks user to specify a city, month, and day to analyze.
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
        try:
            city_select = ['Chicago','New York City','Washington']
            # Gets user input for city (chicago, new york city, washington)
            city = city_select.index(input('Would you like to see data for Chicago, New York City, or Washington?\n').lower().title())
          
            month_select = ['January','February','March','April','May','June','All']
            # Gets user input for month (all, january, february, ... , june)
            month = month_select.index(input('Would you like to see data for January, February, March, April, May, June, or all?\n').lower().title())
    
            day_select = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
            # Gets user input for day of week (all, monday, tuesday, ... sunday)
            day = day_select.index(input('Would you like to see data for Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or all?\n').lower().title())
        
            return city_select[city].lower(), month_select[month].lower(), day_select[day].lower()
        
        except ValueError:
            print('Input error. Try again.')
            
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    # Loads data for the specified city and filters by month and day if applicable.
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Wxtract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]    
        
    return df

def time_stats(df):
    # Displays statistics on the most frequent times of travel.
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Displays the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)

    # Displays the most common day of week
    df['dayofweek'] = df['Start Time'].dt.dayofweek
    common_dayofweek = df['dayofweek'].mode()[0]
    print('Most common day of week:', common_dayofweek)

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    # Displays statistics on the most popular stations and trip.
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Displays most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most common start station:', common_start)

    # Display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most common end station:', common_end)

    # Display most frequent combination of start station and end station trip
    common_startend = (df['Start Station'] + df['End Station']).mode()[0]
    print('Most common combination of start and end station trip:', common_startend)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    # Displays statistics on the total and average trip duration.
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Displays total travel time
    total_duration = df['Trip Duration'].sum()
    print('Total Trip Duration:', total_duration)

    # Display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print('Mean Trip Duration:', mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    # Displays statistics on bikeshare users.
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Displays counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Displays counts of gender
    if 'Gender' in df:
        genders = df['Gender'].value_counts()
        print(genders)
    # Displays earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('Earliest year of birth:', earliest_birth)
        print('Most recent year of birth:', recent_birth)
        print('Most common year of birth:', common_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start = 0
    stop = 5
    display = input("\nDo you want to see the raw data? Enter yes or no\n")
    while display.lower() == 'yes':
        show = df.iloc[start:stop]
        print(show)
        start += 5
        stop += 5
        display = input("\nDo you want to see more raw data? Enter yes or no\n")
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()