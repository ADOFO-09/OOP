import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey"""

# The method setUp() does two things: it creates a survey instance, 
# and it creates a list of responses.

    def setUp(self):
        """Create a survey and a set of responses for use in all methods"""
        question = "What language did you learn to speak first?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','French']
    
    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Tests that three responses are stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()

# Responding to a failed 
# test that you ran is much easier 
# than responding to a bug report from an 
# unhappy user