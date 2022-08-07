import time
import pandas as pd
import numpy as np



#Section IV: change for refactoring

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
    city=input('Please enter Chicago, Washington or New York City for your analysis: ').lower()
    cities=['chicago', 'new york city', 'washington']
    while city not in cities:
        city=input('Invalid inputs and enter city again:')

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('Enter any one of the first 6 months or enter All to select all 6 months: ').lower()
    months=['all','january', 'february', 'march', 'april', 'may', 'june']
    while month not in months:
        month=input('Invalid inputs and enter month again:')
    if month!='all':
        month=months.index(month)
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Enter All or a specific day of week: ').lower()
    days=['all', 'monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday']
    while day not in days:
        day=input('Invalid inputs and enter day again:')
    if day != 'all':
        day=day.title()   
   
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month!='all':
        df=df.loc[df.month==month]
        
    if day!='all':
        df=df.loc[df['day_of_week']==day]

    return df

def display_raw_data(df):
    """ Your docstring here """
    i = 0
    raw = input("\n Do you want to see more rows? Please enter only 'yes' or 'no'\n ").lower() 
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("\n Do you still want to see more rows? Please enter only 'yes' or 'no'\n ").lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week
    day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week:', day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['station']=df['Start Station']+' - '+df['End Station']
    popular_trip = df['station'].mode()[0]
    print('Most Popular Trip:', popular_trip)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()/3600
    print('total travel time (hours): ',round(total_travel_time,2))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()/60
    print('mean travel time (mins): ',round(mean_travel_time,2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types: ',user_types)

    # TO DO: Display counts of gender
    try:
        df=df.dropna(subset=['Gender'])
        user_gender = df['Gender'].value_counts()
        print('counts of Gender: ',user_gender)
    except:
        print('The column "Gender" does not exist.')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        df=df.dropna(subset=['Birth Year'])
        earliest=df['Birth Year'].astype('int').min()
        print('earliest year of birth: ',earliest)
        recent=df['Birth Year'].astype('int').max()
        print('most recent year of birth: ',recent)
        common=df['Birth Year'].astype('int').mode()[0]
        print('most common year of birth: ',common)
    except:
        print('The column "Birth Year" does not exist.')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    
    
    while True:
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart == 'yes':
            city, month, day = get_filters()
            df = load_data(city, month, day)
            display_raw_data(df)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        elif restart == 'no': 
            break
        else:
            restart = input('\nInvalid input and please reenter yes or no.\n').lower()


if __name__ == "__main__":
	main()
