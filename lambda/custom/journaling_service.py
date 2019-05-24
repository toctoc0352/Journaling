import random
import journaling_repository

class JournalingService:
    def __init__(self):
        self.journaling_repository = journaling_repository.JournalingRepository()

    def trigerPhrase(self):
        trigger_list = self.journaling_repository.get_journaling_trigger_list()
        return random.choice(trigger_list)

