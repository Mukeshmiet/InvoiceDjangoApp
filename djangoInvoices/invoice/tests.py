from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

class CreateAndReadAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_and_read_invoice(self):
        # Define data to create an Invoice
        data = {
            "date": "2023-10-03",
            "invoice_customer_name": "Test Customer"
        }

        # Make a POST request to create an Invoice
        response = self.client.post('/api/invoices/', data, format='json')

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if an Invoice object was created in the database
        self.assertEqual(Invoice.objects.count(), 1)

        # Get the created Invoice ID from the response
        invoice_id = response.data['id']

        # Make a GET request to read the created Invoice
        response = self.client.get(f'/api/invoices/{invoice_id}/', format='json')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Deserialize the response data and print it to the terminal
        invoice_data = response.data
        print("Created Invoice:")
        print(invoice_data)

        # Validate the retrieved Invoice data using the serializer
        serializer = InvoiceSerializer(Invoice.objects.get(id=invoice_id))
        self.assertEqual(invoice_data, serializer.data)

    def test_create_and_read_invoice_detail(self):
        # Create a sample Invoice
        invoice = Invoice.objects.create(date="2023-10-03", invoice_customer_name="Test Customer")

        # Define data to create an InvoiceDetail
        data = {
            "invoice": invoice.id,
            "description": "Test Item",
            "quantity": 5,
            "unit_price": "10.00",
            "price": "50.00"
        }

        # Make a POST request to create an InvoiceDetail
        response = self.client.post('/api/invoice_details/', data, format='json')

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if an InvoiceDetail object was created in the database
        self.assertEqual(InvoiceDetail.objects.count(), 1)

        # Get the created InvoiceDetail ID from the response
        invoice_detail_id = response.data['id']

        # Make a GET request to read the created InvoiceDetail
        response = self.client.get(f'/api/invoice_details/{invoice_detail_id}/', format='json')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Deserialize the response data and print it to the terminal
        invoice_detail_data = response.data
        print("Created InvoiceDetail:")
        print(invoice_detail_data)

        # Validate the retrieved InvoiceDetail data using the serializer
        serializer = InvoiceDetailSerializer(InvoiceDetail.objects.get(id=invoice_detail_id))
        self.assertEqual(invoice_detail_data, serializer.data)
