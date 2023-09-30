class Question:

    def __init__(self, text, is_true, explanation):
        self.text: str = text
        self.is_true: bool = is_true
        self.explanation: str = explanation


q = Question('test', True, 'because')
print(q.text)
