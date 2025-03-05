from django.db import models

class CSVFile(models.Model):
    file = models.FileField(upload_to='file/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name