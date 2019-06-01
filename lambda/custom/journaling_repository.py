
class JournalingRepository:

    def __init__(self):
        self.journalingTrigger = [
            '感謝していることを書いてみましょう。',
            '今日学んだことを書いてみましょう。',
            'どうすれば今日をもっと良くできたか書いてみましょう',
            '今日の出来事で一番大事なことを書いてみましょう。'
        ]

        self.help = '''
        ノートや日記に今日の出来事について
        １つだけでもいいので書いてみてください。
        何を書けばいいかわからない場合は、何を書けばいい、と話しかけてください。
        書き終わったら、書いたよ、と話しかけてください。
        '''

        self.greeting = '''
        今日の出来事を振り返ってみましょう。
        ノートや日記に書いてみてください。
        書き終わったら、書いたよ、と話しかけてください
        '''

        self.goodbye = '''
        お疲れ様でした。
        がんばった自分を褒めてあげて下さい
        '''

    def get_journaling_trigger_list(self):
        return self.journalingTrigger
