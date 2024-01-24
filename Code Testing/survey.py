# A class to test
class AnonymousSurvey():
    """Collect anonymous answers from a survey question"""
    def __init__(self,question,responses = []):
        self.question = question
        self.responses = responses
    """Show the survey question"""
    def show_question(self):
        print(self.question)
    """Stores a single response to the survey"""
    def store_response(self, new_response):
        self.responses.append(new_response)
    """show all responses that have been given"""
    def show_results(self, responses):
        print("Survey results")
        for response in responses:
            print('- ' + response)
    

