from typing import List

from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from formtools.wizard.views import SessionWizardView
import re
from .models import Answer, Question, Result


class TestView(SessionWizardView):

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        question = Question.objects.all()[self.steps.step0]
        context['question_title'] = question.question_title
        context['question_body'] = question.question_body
        return context

    def get_template_names(self):
        return 'test.html'

    def done(self, form_list, **kwargs):
        answers = Answer.objects.all()
        questions = Question.objects.all()
        form_list = [re.split('[, ]', answer) for answer in form_list]
        result = self.__compute_result(answers=answers, form_list=form_list, questions=questions)
        Result.objects.create(
            result=result
        )
        return HttpResponseRedirect('/result')

    def __compute_result(self, answers: List[Answer], form_list: list, questions: List[Question]):
        result = 0
        for i, answer in enumerate(form_list):
            question_id = i + 1
            max_value = self.__find_max_answer_value(questions, question_id)
            current_answers = self.__find_answers(question_id, answers)
            for j in range(max_value):
                if answer[j] in current_answers:
                    result += 1
        return result

    @staticmethod
    def __find_answers(question_id, answers: List[Answer]):
        return [answer.answer for answer in answers if answer.question_id.id == question_id]

    @staticmethod
    def __find_max_answer_value(questions: List[Question], question_id: int):
        return questions[question_id].max_answer_value


class ResultView(TemplateView):
    template_name = 'result.html'
    result = Result.objects.all()[-1]

    def get_context_data(self, objects_list, **kwargs, ):
        context = super().get_context_data(**kwargs)
        context['result'] = self.result
        return context
