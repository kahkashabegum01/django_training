from django.test import TestCase
from django.urls import reverse
from .models import employee


class DeleteEmployeeTests(TestCase):
	def test_delete_employee_removes_record(self):
		employee_record = employee.objects.create(eno=1, ename="Test Employee", esal=50000)

		response = self.client.post(reverse("deleteemployee"), {"id": employee_record.pk})

		self.assertRedirects(response, reverse("employeelist"))
		self.assertFalse(employee.objects.filter(pk=employee_record.pk).exists())
