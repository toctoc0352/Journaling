import random
import journaling_repository


class JournalingService:
    def __init__(self):
        self.journaling_repository = journaling_repository.JournalingRepository()

    def triger_phrase(self):
        trigger_list = self.journaling_repository.get_journaling_trigger_list()
        return random.choice(trigger_list)

    def help_phrase(self):
        return self.journaling_repository.help

    def greeting_phrase(self):
        greeting_phrase = self.journaling_repository.greeting
        help_list = self.journaling_repository.help
        help_phrase = random.choice(help_list)
        return greeting_phrase + help_phrase

    def goodbye_phrase(self):
        return self.journaling_repository.goodbye
