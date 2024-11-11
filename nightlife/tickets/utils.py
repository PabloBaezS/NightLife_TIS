# tickets/utils.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from django.http import HttpResponse
from .models import Order, Payment

def generate_pdf_receipt(order_id):
    # Get the order and payment information
    order = Order.objects.get(id=order_id)
    payment = Payment.objects.get(order=order)

    # Create a BytesIO buffer to receive the PDF data
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setTitle(f"Receipt for Order {order_id}")

    # PDF Content
    p.drawString(100, 750, f"Receipt for Order #{order_id}")
    p.drawString(100, 730, f"User: {order.user.username}")
    p.drawString(100, 710, f"Total Amount Paid: ${payment.amount}")
    p.drawString(100, 690, f"Payment Status: {payment.payment_status}")
    p.drawString(100, 670, f"Order Date: {order.created_at.strftime('%Y-%m-%d %H:%M:%S')}")

    # Draw additional lines as needed
    p.drawString(100, 650, "Thank you for your purchase!")

    # Save the PDF
    p.showPage()
    p.save()

    # Return the PDF as a response
    buffer.seek(0)
    return buffer
