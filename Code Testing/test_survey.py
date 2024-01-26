import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        question = "What language did you learn to speak first?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Test that three responses are stored properly"""
        question = "What language did you learn to speak first?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'French', 'Twi']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)
        

unittest.main()

# we call store_response()
# for each of these responses. Once the responses have been stored, we write 
# another loop and assert that each response is now in my_survey.responses 