
def get_answer(question):
    answers = {'hello': 'Hello there', 'how are you': 'Okay', 'bye': 'see u'}
    return answers.get(question, 'wut?')


question = input('input phrase ').lower()
print(get_answer(question))