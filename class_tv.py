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
    #Turn on the TV
    def turn_on(self):
        self.on = True
        print(f"{self.tv_name} is turned on")

    #Turn off the TV    
    def turn_off(self):
        self.on = False
        print(f"{self.tv_name} is turned off")
    
    #Get the current channel
    def get_channel(self):
        print(f"{self.tv_name} is on channel {self.channel}")
    
    #Set the channel
    def set_channel(self, channel):
        self.channel = channel
        if self.channel > 120:
            self.channel = 120
            print(f"{self.tv_name}: The channel limit is 120")
        if self.channel < 1:
            self.channel = 1
            print(f"{self.tv_name}: Channels lower than 1 are not available")
        else:
            print(f"You successfully set the channel of {self.tv_name} to {self.channel}")
    
    #Get the current volume level
    def get_volume(self):
        print(f"{self.tv_name} is on {self.volume_level}")

    #Set the volume level
    def set_volume(self, volume_level):
        self.volume_level = volume_level
        if self.volume_level > 7:
            self.volume_level = 7
            print(f"{self.tv_name}: The highest volume is 7")
        if self.volume_level < 1:
            self.volume_level = 1
            print(f"{self.tv_name}: The lowest volume is 1")
        else:
            print(f"You successfully set the volume level of {self.tv_name}  to {self.volume_level}")
    
    #Increase Channel by 1
    def channel_up_1(self):
        self.channel += 1
        if self.channel > 120:
            self.channel -= 1
            print(f"{self.tv_name}: The channel limit is 120")
        else:
            print(f"The new channel of {self.tv_name} is {self.channel}")
    
    #Decrease Channel by 1
    def channel_down_1(self):
        self.channel -= 1
        if self.channel < 1:
            self.channel += 1
            print(f"{self.tv_name}: Channels lower than 1 are not available")
    
    #Increase the Volume
    def volume_up(self):
        self.volume_level += 1
        if self.volume_level > 7:
            self.volume_level -= 1
            print(f"{self.tv_name}: The highest volume is 7")
        else:
            print(f"The new volume of {self.tv_name} is {self.volume_level}")

    #Decrease the Volume 
    def volume_down(self):
        self.volume_level -= 1
        if self.volume_level < 1:
            self.volume_level += 1
            print(f"{self.tv_name}: The lowest volume is 1")
        else:
            print(f"The new volume of {self.tv_name} is {self.volume_level}")
       
    def show(self):
        print(f"{self.tv_name}'s channel is {self.channel} and volume level is {self.volume_level}")

    


