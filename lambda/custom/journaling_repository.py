
class JournalingRepository:

    def __init__(self):
        self.journalingTrigger = ['感謝していることをノートに書いてみましょう。','今日学んだことを思い出してみましょう。','今日の改善点を振り返ってみましょう。', '今日の出来事で一番大事なことを思い出してみましょう。']

    def get_journaling_trigger_list(self):
        return self.journalingTrigger