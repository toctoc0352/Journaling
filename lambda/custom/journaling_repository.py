import yaml


class JournalingRepository:
    def __init__(self):
        with open("message.yml", "r") as yf:
            self.__messages = yaml.safe_load(yf)

        self.journaling_trigger = self.__messages["journaling_phrase"]

        self.help = self.__messages["help"]

        self.hello = self.__messages["hello"]

        self.special_phrase = self.__messages["special_phrase"]

        self.help_detail = self.__messages["help_detail"]

    def get_journaling_trigger_list(self):
        return self.journaling_trigger
