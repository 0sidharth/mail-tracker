from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ProfessorModel(models.Model):
	name = models.CharField(max_length=254)
	emailid = models.EmailField(max_length=254)
	country = models.CharField(max_length=254)
	interests = models.TextField()
	university = models.CharField(max_length=254)
	userperson = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	email_subject = models.TextField()
	email_body = models.TextField()
	reminder_mail = models.TextField()
	reminder_subject = models.TextField()

class EmailModel(models.Model):
	sender = models.EmailField(max_length=254)
	receiver = models.EmailField(max_length=254)
	email_text = models.CharField(max_length=254)
	date_created = models.DateTimeField(verbose_name=("Creation date"), auto_now_add=True)
	date_seen = models.DateTimeField(verbose_name=("Seen date"), null=True, blank=True)
	seen = models.BooleanField()
	replied = models.BooleanField()
	professor = models.ForeignKey(ProfessorModel, on_delete=models.CASCADE, default=None)
	userperson = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	
	@property
	def since(self):
		return (timezone.now() - self.date_created).days