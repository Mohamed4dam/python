class Television:
    MIN_VOLUME:int = 0
    MAX_VOLUME:int = 2
    MIN_CHANNEL:int = 0
    MAX_CHANNEL:int = 3

    def __init__(self) -> None:
        """
        Setting up variables.
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
       # self.__previous_volume = self.MIN_VOLUME

    def power(self) -> None:
        """
        This method turns the TV on or off, if the TV is on.
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False
    def channel_up(self) -> None:
        """
        This method increases the channel level, if the TV is on.
        """
        if self.__status:
            if self.__channel >= self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1
    def channel_down(self) -> None:
        """
        This method decreases the channel level, if the TV is on.
        """
        if self.__status:
            if self.__channel <= self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1
    def volume_up(self) -> None:
        """
        This method increases the volume level, if the TV is on.
        """
        if self.__status == True:
            if self.__muted == True:
                self.mute()
            if self.__volume < self.MAX_VOLUME:
                    self.__volume  += 1



    def volume_down(self) -> None:
        """
        This method decreases the volume level, if the TV is on.
        """
        if self.__status  == True:
            if self.__muted == True:
                self.mute()
            if self.__volume > self.MIN_VOLUME:
                    self.__volume -= 1


    def mute(self) ->None:
        """
        This method mutes and unmutes the TV, if the power is on.
        """
        if self.__status:
            if self.__muted == True:
                self.__muted = False
            else:
                self.__muted = True



    def __str__(self) -> str:
        """
        This string method displays the details of the TV.
        :return: returns a string of the TV values
        """
        if self.__muted:
               return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


