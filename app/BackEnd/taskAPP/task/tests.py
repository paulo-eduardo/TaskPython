from django.test import TestCase, RequestFactory
from task.models import Task
import json 

# Create your tests here.
class TaskTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = Task.objects.create(titulo = "Tarefa 1", descricao = "Descricao tarefa 1")
        self.user = Task.objects.create(titulo = "Tarefa 2", descricao = "Descricao tarefa 2")
        self.user = Task.objects.create(titulo = "Tarefa 3", descricao = "Descricao tarefa 3")

    def test_can_get_all(self):
        response = self.client.get('/api/task/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) == 3)

    def test_can_create_new_task(self):
        data = {
            "titulo":"Tarefa 4",
            "descricao": "Descricao tarefa 4"
        }

        response = self.client.post('/api/task/', data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["id"], 4)
        self.assertEqual(response.data["titulo"], data["titulo"])
        self.assertEqual(response.data["descricao"], data["descricao"])

    def test_can_change_task(self):
        data = json.dumps({
            "titulo":"Novo titulo 3",
            "descricao": "Nova Descricao tarefa 4"
        })

        response = self.client.put('/api/task/1/', data, content_type="application/json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], 1)
        self.assertEqual(response.data["titulo"], "Novo titulo 3")
        self.assertEqual(response.data["descricao"], "Nova Descricao tarefa 4")

    def test_can_change_task_status(self):
        response = self.client.post('/api/task/1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], 1)
        self.assertIsNotNone(response.data["concluded"])
        self.assertTrue(response.data["status"])

    def test_can_delete_task(self):
        response = self.client.delete('/api/task/1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Task.objects.get()), 2)
        
