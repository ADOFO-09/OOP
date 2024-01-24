from survey import AnonymousSurvey

# Define a question, and make a survey
question = "What language did you learn to speak first?"
my_survey = AnonymousSurvey(question)

# Show the question and store responses to the question
my_survey.show_question()
print("Enter 'q' at any time to quit\n")
while True:
    response = input("Language:")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results
print("\nThank you to everyone who participated in the survey")
my_survey.show_results(my_survey.responses)

# When you call my_survey.show_results(response), you are passing a single response (the last one entered) 
# instead of the list of all responses. This results in the unexpected output.
# To fix this issue, you should pass the entire list of responses to the show_results method. 
# Also, there is no need to pass the question to the show_question method because the question is already 
# stored in the object during initialization.