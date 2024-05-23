from tv import TV

class TestTV:
    def main():
        tv1 = TV()
        tv1.turnon()
        tv1.setchannel(30)
        tv1.setvolume(3)

        tv2 = TV()
        tv2.turnon()
        tv2.setchannel(3)
        tv2.setvolume(2)

        print(f"TV1 channel is {tv1.getchannel()} and volume level is {tv1.getvolume()}")
        print(f"TV2 channel is {tv2.getchannel()} and volume level is {tv2.getvolume()}")

    if __name__ == "__main__":
        main()
