from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

class CreateUpdateReadDeleteAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_update_read_delete_invoice(self):
        # Define data to create an Invoice
        create_data = {
            "date": "2023-10-03",
            "invoice_customer_name": "Test Customer"
        }

        # Make a POST request to create an Invoice
        response = self.client.post('/api/invoices/', create_data, format='json')

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Get the created Invoice ID from the response
        invoice_id = response.data['id']

        # Print a message indicating this is a Create test with data
        print("1. Create test: Creating Invoice with data")
        print(create_data)

        # Make a GET request to read the created Invoice before updating
        response = self.client.get(f'/api/invoices/{invoice_id}/', format='json')
        invoice_data_before_update = response.data
        print("2. Before Update:")
        print(invoice_data_before_update)

        # Define data for updating the Invoice
        update_data = {
            "date": "2023-10-04",
            "invoice_customer_name": "Updated Customer"
        }

        # Make a PUT request to update the Invoice
        response = self.client.put(f'/api/invoices/{invoice_id}/', update_data, format='json')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Make a GET request to read the updated Invoice
        response = self.client.get(f'/api/invoices/{invoice_id}/', format='json')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Deserialize the response data and print it to the terminal
        updated_invoice_data = response.data
        print("3. Update test: Updated Invoice data")
        print(updated_invoice_data)

        # Validate the retrieved updated Invoice data using the serializer
        updated_serializer = InvoiceSerializer(Invoice.objects.get(id=invoice_id))
        self.assertEqual(updated_invoice_data, updated_serializer.data)

        # Make a DELETE request to delete the Invoice
        response = self.client.delete(f'/api/invoices/{invoice_id}/', format='json')

        # Check if the response status code is 204 (No Content)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Make a GET request to read the deleted Invoice
        response = self.client.get(f'/api/invoices/{invoice_id}/', format='json')

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Print data after delete method to the terminal
        afterDelete_invoice_detail_data = response.data
        print("4. Delete test: After delete Invoice data")
        print(afterDelete_invoice_detail_data)

    def test_create_update_read_delete_invoice_detail(self):
        # Create a sample Invoice
        invoice = Invoice.objects.create(date="2023-10-03", invoice_customer_name="Test Customer")

        # Define data to create an InvoiceDetail
        create_data = {
            "invoice": invoice.id,
            "description": "Test Item",
            "quantity": 5,
            "unit_price": "10.00",
            "price": "50.00"
        }

        # Make a POST request to create an InvoiceDetail
        response = self.client.post('/api/invoice_details/', create_data, format='json')

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Get the created InvoiceDetail ID from the response
        invoice_detail_id = response.data['id']

        # Print a message indicating this is a Create test with data
        print("1. Create test: Creating InvoiceDetail with data")
        print(create_data)

        # Make a GET request to read the created InvoiceDetail before updating
        response = self.client.get(f'/api/invoice_details/{invoice_detail_id}/', format='json')
        invoice_detail_data_before_update = response.data
        print("2. Before Update:")
        print(invoice_detail_data_before_update)

        # Define data for updating the InvoiceDetail
        update_data = {
            'invoice': invoice.id,
            "description": "Updated Item",
            "quantity": 10,
            "unit_price": "15.00",
            "price": "150.00"
        }

        # Make a PUT request to update the InvoiceDetail
        response = self.client.put(f'/api/invoice_details/{invoice_detail_id}/', update_data, format='json')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Make a GET request to read the updated InvoiceDetail
        response = self.client.get(f'/api/invoice_details/{invoice_detail_id}/', format='json')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Deserialize the response data and print it to the terminal
        updated_invoice_detail_data = response.data
        print("3. Update test: Updated InvoiceDetail data")
        print(updated_invoice_detail_data)

        # Validate the retrieved updated InvoiceDetail data using the serializer
        updated_serializer = InvoiceDetailSerializer(InvoiceDetail.objects.get(id=invoice_detail_id))
        self.assertEqual(updated_invoice_detail_data, updated_serializer.data)

        # Make a DELETE request to delete the InvoiceDetail
        response = self.client.delete(f'/api/invoice_details/{invoice_detail_id}/', format='json')

        # Check if the response status code is 204 (No Content)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Make a GET request to read the deleted InvoiceDetail
        response = self.client.get(f'/api/invoice_details/{invoice_detail_id}/', format='json')

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Print data after delete method to the terminal
        afterdelete_invoice_detail_data = response.data
        print("4. Delete test: After delete InvoiceDetail data")
        print(afterdelete_invoice_detail_data)