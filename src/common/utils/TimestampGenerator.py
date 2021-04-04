"""
Semi-Quantum Conference Key Agreement (SQCKA)

Author:
- Ruben Andre Barreiro (r.barreiro@campus.fct.unl.pt)

Supervisors:
- Andre Nuno Souto (ansouto@fc.ul.pt)
- Antonio Maria Ravara (aravara@fct.unl.pt)

Acknowledgments:
- Paulo Alexandre Mateus (pmat@math.ist.utl.pt)
"""

# Import Packages and Libraries

# Import DateTime from the DateTime Library, as date_time alias
from datetime import datetime as date_time

# Import TimeDelta from the DateTime Library, as time_delta alias
from datetime import timedelta as time_delta

# Import the Random Intervals from the Random Library
from random import randrange as random_range


# Class of the Timestamp's Generator
class TimestampGenerator:

    # Constructor for Timestamp's Generator
    def __init__(self, timestamp_generator_name):
        self.now = date_time.now()
        self.timestamp_generator_name = timestamp_generator_name

    # Retrieve the Now's DateTime
    def get_now(self):

        # Return the Now's DateTime
        return self.now

    # Retrieve the Now's DateTime, as Timestamp representation
    def get_now_timestamp(self):

        # Return the Now's DateTime, as Timestamp representation
        return date_time.timestamp(self.now)

    # Retrieve the Now's DateTime, plus a Delta DateTime
    def get_now_plus_delta(self, weeks_delta, days_delta, hours_delta, minutes_delta,
                           seconds_delta, milliseconds_delta, microseconds_delta):

        # Return the Now's DateTime, plus a Delta DateTime
        return self.now + time_delta(weeks=weeks_delta,
                                     days=days_delta,
                                     hours=hours_delta,
                                     minutes=minutes_delta,
                                     seconds=seconds_delta,
                                     milliseconds=milliseconds_delta,
                                     microseconds=microseconds_delta)

    # Retrieve the Now's DateTime, plus a Delta DateTime, as Timestamp representation
    def get_now_plus_delta_timestamp(self, weeks_delta, days_delta, hours_delta, minutes_delta,
                                     seconds_delta, milliseconds_delta, microseconds_delta):

        # Return the Now's DateTime, as Timestamp representation
        return date_time.timestamp(self.now + time_delta(weeks=weeks_delta,
                                                         days=days_delta,
                                                         hours=hours_delta,
                                                         minutes=minutes_delta,
                                                         seconds=seconds_delta,
                                                         milliseconds=milliseconds_delta,
                                                         microseconds=microseconds_delta))

    # Retrieve the current Timestamp, as a custom DateTime
    def get_now_customised_format(self):

        # Return the current Timestamp, as a custom DateTime
        return date_time(self.now.year, self.now.month, self.now.day,
                         self.now.hour, self.now.minute, self.now.second)

    # Return the current Timestamp, plus some delta, as custom DateTime
    def get_now_plus_delta_customised_format(self, weeks_delta, days_delta, hours_delta, minutes_delta,
                                             seconds_delta, milliseconds_delta, microseconds_delta):

        return self.get_now_customised_format() + time_delta(weeks=weeks_delta,
                                                             days=days_delta,
                                                             hours=hours_delta,
                                                             minutes=minutes_delta,
                                                             seconds=seconds_delta,
                                                             milliseconds=milliseconds_delta,
                                                             microseconds=microseconds_delta)

    # Generate multiple Pseudo Random Timestamps
    def generate_random_timestamps(self, num_timestamps_to_generate, weeks_delta, days_delta,
                                   hours_delta, minutes_delta, seconds_delta,
                                   milliseconds_delta, microseconds_delta):

        # Retrieve the current Timestamp
        now_timestamp = self.get_now_customised_format()

        # While there are still Pseudo Random Timestamps to be generated
        while num_timestamps_to_generate > 0:

            # If Weeks' Delta is set up, define the random range between 0 and that value
            if weeks_delta == 0:
                weeks_random_range = 0
            else:
                weeks_random_range = random_range(weeks_delta)

            # If Days' Delta is set up, define the random range between 0 and that value
            if days_delta == 0:
                days_random_range = 0
            else:
                days_random_range = random_range(days_delta)

            # If Hours' Delta is set up, define the random range between 0 and that value
            if hours_delta == 0:
                hours_random_range = 0
            else:
                hours_random_range = random_range(hours_delta)

            # If Minutes' Delta is set up, define the random range between 0 and that value
            if minutes_delta == 0:
                minutes_random_range = 0
            else:
                minutes_random_range = random_range(minutes_delta)

            # If Seconds' Delta is set up, define the random range between 0 and that value
            if seconds_delta == 0:
                seconds_random_range = 0
            else:
                seconds_random_range = random_range(seconds_delta)

            # If Milliseconds' Delta is set up, define the random range between 0 and that value
            if milliseconds_delta == 0:
                milliseconds_random_range = 0
            else:
                milliseconds_random_range = random_range(milliseconds_delta)

            # If Microseconds' Delta is set up, define the random range between 0 and that value
            if microseconds_delta == 0:
                microseconds_random_range = 0
            else:
                microseconds_random_range = random_range(microseconds_delta)

            # Generate the current Pseudo Random Timestamp
            current_pseudo_random_timestamp = now_timestamp + time_delta(weeks=weeks_random_range,
                                                                         days=days_random_range,
                                                                         hours=hours_random_range,
                                                                         minutes=minutes_random_range,
                                                                         seconds=seconds_random_range,
                                                                         milliseconds=milliseconds_random_range,
                                                                         microseconds=microseconds_random_range)

            # Yield the current Pseudo Random Timestamp generated
            yield current_pseudo_random_timestamp

            # Decrease the count of the Pseudo Random Timestamps to be generated
            num_timestamps_to_generate -= 1
