class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__previous_volume = self.MIN_VOLUME

    def power(self):
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False
    def channel_up(self):
        if self.__status:
            if self.__channel >= self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1
    def channel_down(self):
        if self.__status:
            if self.__channel <= self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1
    def volume_up(self): #Fixme: volume level is not updating correcting when the tv is muted
        if self.__status:
            if self.__muted:
                self.__muted == False
                if self.__volume < self.MAX_VOLUME:
                    self.__volume = self.__previous_volume + 1
            else:
                if self.__volume < self.MAX_VOLUME:
                    self.__volume += 1


    def volume_down(self): #Fixme: volume level is not updating correcting when the tv is muted
        if self.__status:
            if self.__muted:
                self.__muted == False
                if self.__volume > self.MIN_VOLUME:
                    self.__volume = self.__previous_volume - 1
            else:
                if self.__volume > self.MIN_VOLUME:
                    self.__volume -= 1


    def mute(self): #Fixme: volume level is not updating correcting when the tv is muted
        if self.__status:
            if not self.__muted:
                # Save the current volume before muting
                self.__previous_volume = self.__volume
                self.__volume = self.MIN_VOLUME
                self.__muted = True
            else:
                # If already muted, restore the volume to its previous level
                self.__volume = self.__previous_volume
                self.__muted = False

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


