# class tv program
# Define a class TV with attributes and methods
class TV:
    # Initialize the TV object with given parameters
    def __init__(self, name_of_tv, channel, level_of_volume, on):
        self.tv_name = name_of_tv
        self.channel = channel
        self.volume_level = level_of_volume
        self.on = on
         # Validate channel and volume levels
        if self.channel < 1:
            self.channel = 1
            print(f"{self.tv_name}: Channels lower than 1 are not available")
        
        if self.channel > 120:
            self.channel = 120
            print(f"{self.tv_name}: The channel limit is 120")

        if self.volume_level > 7:
            self.volume_level = 7
            print(f"{self.tv_name}: The highest volume is 7")
        
        if self.volume_level < 1:
            self.volume_level = 1
            print(f"{self.tv_name}: The lowest volume is 1")

# Define the methods for TV object
    #Turn off the TV    
    def turn_off(self):
        self.on = False
        print(f"{self.tv_name} is turned off")

    #Turn on the TV
    def turn_on(self):
        self.on = True
        print(f"{self.tv_name} is turned on")
    
    #Get the current volume level
    def get_volume(self):
        print(f"{self.tv_name} is on {self.volume_level}")

    
    


