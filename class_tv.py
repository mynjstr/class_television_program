# class tv program
# Define a class TV with attributes and methods
class TV:
    def __init__(self, name_of_tv, channel, level_of_volume, on):
        self.tvname = name_of_tv
        self.channel = channel
        self.volumelevel = level_of_volume
        self.on = on
         # Validate channel and volume levels
        if self.channel < 1:
            self.channel = 1
            print(f"{self.tvname}: Channels lower than 1 are not available")
        
        if self.channel > 120:
            self.channel = 120
            print(f"{self.tvname}: The channel limit is 120")

        if self.volumelevel > 7:
            self.channel = 7
            print(f"{self.tvname}: The highest volume is 7")
        
        if self.volumelevel < 1:
            self.volumelevel = 1
            print(f"{self.tvname}: The lowest volume is 1")
# Initialize the TV object with given parameters
# Define the methods for TV object