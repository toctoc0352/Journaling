import random
import journaling_repository

class JournalingService:
    def __init__(self):
        self.journaling_repository = JournalingRepository()

    def trigerPhrase:
        trigger_list = self.journaling_repository.get_journaling_trigger_list()
        random.choice(trigger_list)

