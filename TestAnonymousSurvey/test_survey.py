import unittest
from TestAnonymousSurvey.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Ma']

    def test_survey_one(self):
        '''测试单个数值'''
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.response)

    def test_survey_more(self):
        '''测试多个值'''
        for response in self.responses:
            self.my_survey.store_response(response)
        print(self.my_survey.show_results())
        for response in self.responses:
            self.assertIn(response, self.my_survey.response)


unittest.main()
