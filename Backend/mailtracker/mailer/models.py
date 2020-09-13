from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ProfessorModel(models.Model):
	name = models.CharField(max_length=254)
	emailid = models.EmailField(max_length=254)
	country = models.CharField(max_length=254)
	interests = models.TextField(default = "This blog is under Construction !")
	university = models.CharField(max_length=254)
	userperson = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	email_subject = models.TextField(default = "This blog is under Construction !")
	email_body = models.TextField(default = "This blog is under Construction !")
	reminder_mail = models.TextField(default = "This blog is under Construction !")
	reminder_subject = models.TextField(default = "This blog is under Construction !")

class EmailModel(models.Model):
	sender = models.EmailField(max_length=254)
	receiver = models.EmailField(max_length=254)
	email_text = models.TextField(default = "This blog is under Construction !")
	date_created = models.DateTimeField(verbose_name=("Creation date"), auto_now_add=True)
	date_seen = models.DateTimeField(verbose_name=("Seen date"), null=True, blank=True)
	seen = models.BooleanField()
	replied = models.BooleanField()
	professor = models.ForeignKey(ProfessorModel, on_delete=models.CASCADE, default=None)
	userperson = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	
	@property
	def since(self):
		return (timezone.now() - self.date_created).days