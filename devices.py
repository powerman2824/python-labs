class Device:
    def __init__(self, type, model, software, location, ip_address):
        self.type = type
        self.model = model
        self.software = software
        self.location = location
        self.ip_address = ip_address
    
    def askInfo(self):
        self.type = input('What type of Network device is this?\n--> ')
        self.model = input('What model of Network device is this?\n--> ')
        self.software = input('What software is running on this Network device?\n--> ')
        self.location = input('Where is this Network device located?\n--> ')
        self.ip_address = input('What is the management ip address of this Network device?\n--> ')
        
        return (self.type, self.model, self.software, self.location, self.ip_address)

    def getInfo(self):
        info = (
            f'Device Type: {self.type}\n'
            f'Device Model: {self.model}\n'
            f'Device Software: {self.software}\n'
            f'Device Location: {self.location}\n'
            f'Device Ip Address: {self.ip_address}'
        )
        return info

print("Welcome to Joe's Network Device Manager.")
print("Let's get started!")

userInput = input('Is this a new device?\nPlease choose 1 for Yes & 2 for No.\n--> ')
if int(userInput) == 1:
    newDevice = Device('', '', '', '', '')
    newDevice.askInfo()
elif int(userInput) == 2:
    print('This function is coming soon...')
else:
    print('Something Broke.')

userReview = input("Would you like to review your device's info?\nPlease choose 1 for Yes & 2 for No.\n--> ")
if int(userReview) == 1:
    print(newDevice.getInfo())
elif int(userReview) == 2:
    print("Thank you for using Joe's Network Device Manager.")
else:
    print('Something Broke')
