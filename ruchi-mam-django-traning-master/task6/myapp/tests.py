from django.test import TestCase
from django.urls import reverse
from myapp.models import product

class ProductUpdateDeleteTests(TestCase):
	def setUp(self):
		self.product = product.objects.create(
			pid=17,
			pname="Notebook",
			prize=4.5,
			offer=1.0,
		)

	def test_update_form_shows_selected_product(self):
		response = self.client.get(reverse('updateform'), {'id': self.product.id})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Notebook')

	def test_update_changes_selected_product(self):
		response = self.client.post(reverse('update'), {
			'id': self.product.id,
			'pid': 18,
			'pname': 'Pen',
			'prize': 2.5,
			'offer': 0.5,
		})

		self.assertRedirects(response, reverse('read'))
		self.product.refresh_from_db()
		self.assertEqual(self.product.pid, 18)
		self.assertEqual(self.product.pname, 'Pen')
		self.assertEqual(product.objects.count(), 1)

	def test_delete_removes_selected_product(self):
		response = self.client.post(reverse('delete'), {'id': self.product.id})

		self.assertRedirects(response, reverse('read'))
		self.assertFalse(product.objects.filter(id=self.product.id).exists())

	def test_create_requires_post(self):
		response = self.client.get(reverse('create'))

		self.assertEqual(response.status_code, 405)

	def test_update_requires_post(self):
		response = self.client.get(reverse('update'))

		self.assertEqual(response.status_code, 405)

	def test_delete_requires_post(self):
		response = self.client.get(reverse('delete'))

		self.assertEqual(response.status_code, 405)
