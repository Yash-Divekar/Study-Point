from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class BaseModel(models.Model):
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    
    class Meta():
        abstract=True

class UserData(BaseModel):
    username=models.CharField(max_length=100)
    pwd=models.CharField(max_length=20)
    name=models.CharField(max_length=200)
    college_name=models.CharField(max_length=200)
    exam=models.CharField(max_length=100)
    board_10=models.CharField(max_length=200)
    marks_10=models.IntegerField()
    email=models.EmailField()
    
    def __str__(self):
        return self.username

class Exam(BaseModel):
    exam_name=models.CharField(max_length=50)
    exam_year=models.IntegerField()
    exam_date=models.DateField()
    exam_shift=models.CharField(max_length=50)
    exam_time=models.IntegerField()
    exam_marks=models.IntegerField()
    
    def __str__(self):
        return f'{self.exam_name}-{self.exam_date}-{self.exam_shift}'
    
class Exam_data(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exam')
    question_num = models.IntegerField()
    subject=models.CharField(max_length=100)
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    ans = models.CharField(max_length=100)
    img = models.FileField(default=None, null=True, blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'gif'])])
    marks = models.IntegerField(default=1)
    has_image = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.img:
            self.has_image = True
        else:
            self.has_image = False
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.exam}-{self.question_num}'
  
  
class User_history(BaseModel):
    user=models.ForeignKey(UserData,on_delete=models.CASCADE , related_name='user')
    h_exam=models.ForeignKey(Exam,on_delete=models.CASCADE,related_name='h_exam')
    h_questions=models.ForeignKey(Exam_data,on_delete=models.CASCADE,related_name='h_question')
    user_ans=models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.user}-{self.h_question}'