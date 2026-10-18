from django.db import models

import uuid

class Contact(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)

    name = models.CharField(max_length = 100)

    phone = models.CharField(max_length = 15)

    email = models.EmailField()

    class ContactTypeChoices(models.TextChoices):

        GENERAL = "general" , "General"

        NEWS_SUBMIT = "news_submit" , "News Submit"

        CORRECTION_REQUEST = "correction_request" , "Correction Request"

        ADVERTISING_INQUIRY = "advertising_inquiry" , "Advertising Inquiry"

        PARTNERSHIP = "partnership" , "Partnership"

        COMPLAINT = "complaint" , "Complaint"

        TECHNICAL_ISSUE = "technical_issue" , "Technical Issue"

        CAREER = "career" , "Career"

    contact_for = models.CharField(max_length = 30, choices = ContactTypeChoices.choices, default = ContactTypeChoices.GENERAL)

    subject = models.CharField(max_length = 200)

    detail = models.TextField()

    read_status = models.BooleanField(default = False)

    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):

        return f"Message from {self.name} for {self.contact_for}"

    class Meta:
        ordering = ["-created_at"]
    