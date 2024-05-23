class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.on = False

    def turnon(self):
        self.on = True

    def turnoff(self):
        self.on = False

    def getchannel(self):
        return self.channel

    def setchannel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel

    def getvolume(self):
        return self.volume

    def setvolume(self, volume):
        if 1 <= volume <= 7:
            self.volume = volume

    def channelup(self):
        if self.channel < 120:
            self.channel += 1

    def channeldown(self):
        if self.channel > 1:
            self.channel -= 1

    def volumeup(self):
        if self.volume < 7:
            self.volume += 1

    def volumedown(self):
        if self.volume > 1:
            self.volume -= 1

