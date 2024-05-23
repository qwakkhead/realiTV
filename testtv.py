from tv import TV

class TestTV:
    def main():
        print("="*40)
        print("Welcome to the TV Configuration Program") # Adding some features
        print("="*40)
        
        tv1 = TV()
        tv2 = TV()

        tv1.turnon()
        tv2.turnon()

    # For TV1 Functions
        print("\nConfigure TV1") 
        print("-"*40)
        tv1_channel = int(input("Enter channel for TV1 (1-120): ")) # User need to input from 1-120 (channel)
        tv1_volume = int(input("Enter volume level for TV1 (1-7): ")) # user need to input from 1-7 (volume)

        # Validate and set user input for TV1
        if 1 <= tv1_channel <= 120:
            tv1.setchannel(tv1_channel)
        else:
            print("Invalid channel for TV1. Setting to default channel 1.")
            tv1.setchannel(1)
        
        if 1 <= tv1_volume <= 7:
            tv1.setvolume(tv1_volume)
        else:
            print("Invalid volume for TV1. Setting to default volume 1.")
            tv1.setvolume(1)

    # For TV2 Functions
        print("\nConfigure TV2") 
        print("-"*40)
        tv2_channel = int(input("Enter channel for TV2 (1-120): ")) # User need to input from 1-120 (channel)
        tv2_volume = int(input("Enter volume level for TV2 (1-7): ")) # user need to input from 1-7 (volume)

        # Validate and set user input for TV2
        if 1 <= tv2_channel <= 120:
            tv2.setchannel(tv2_channel)
        else:
            print("Invalid channel for TV2. Setting to default channel 1.")
            tv2.setchannel(1)
        
        if 1 <= tv2_volume <= 7:
            tv2.setvolume(tv2_volume)
        else:
            print("Invalid volume for TV2. Setting to default volume 1.")
            tv2.setvolume(1)

        # Print the summary of the results
        print("\nSummary")
        print("="*40)
        print(f"TV1 channel is {tv1.getchannel()} and volume level is {tv1.getvolume()}")
        print(f"TV2 channel is {tv2.getchannel()} and volume level is {tv2.getvolume()}")
        print("="*40)

if __name__ == "__main__":
    TestTV.main()
