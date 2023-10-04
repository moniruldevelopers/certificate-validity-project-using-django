from django.db import models
from PIL import Image
from django.core.validators import RegexValidator

class Student(models.Model):
    id_roll = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/')
    email = models.EmailField(max_length = 50, default = "ugv@gmail.com")
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',  # Example regex for international phone numbers
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    DEPARTMENT = (
        ('CSE', 'CSE'),
        ('EEE', 'EEE'),
        ('ENGLISH', 'ENGLISH'),
        ('CE', 'CE'),
        ('BBA', 'BBA'),
        ('MECHANICAL', 'MECHANICAL'),
    )

    department = models.CharField(max_length=15, choices=DEPARTMENT)




    university_name = models.CharField(max_length=100, default="University Of Global Village, Barishal")
    semester1_gpa = models.DecimalField(max_digits=3, decimal_places=2)
    semester2_gpa = models.DecimalField(max_digits=3, decimal_places=2)
    semester3_gpa = models.DecimalField(max_digits=3, decimal_places=2)
    semester4_gpa = models.DecimalField(max_digits=3, decimal_places=2)
    semester5_gpa = models.DecimalField(max_digits=3, decimal_places=2)
    semester6_gpa = models.DecimalField(max_digits=3, decimal_places=2)
    semester7_gpa = models.DecimalField(max_digits=3, decimal_places=2)
    semester8_gpa = models.DecimalField(max_digits=3, decimal_places=2)
    # Add fields for other semesters as needed
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)
    
    
    def __str__(self):
        return self.name


