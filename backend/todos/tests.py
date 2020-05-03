from django.test import TestCase
from .models import Todo
# Create your tests here.


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="This is a test Todo",
                            description="Learning how to use tests in django", completed=False)

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, 'This is a test Todo')

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_body = f'{todo.description}'
        self.assertEqual(expected_object_body,
                         'Learning how to use tests in django')

    def test_todo_completion(self):
        todo = Todo.objects.get(id=1)
        expected_todo_completion = todo.completed
        self.assertEqual(expected_todo_completion, False)
