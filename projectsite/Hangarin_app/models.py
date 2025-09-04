from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         abstract = True

class Category(BaseModel):
    cat_name = models.CharField(max_length=150)

    def __str__(self):

        return self.cat_name
    
class Priority(BaseModel):
    prio_name = models.CharField(max_length=150)

    def __str__(self):

        return self.prio_name
    
class Task(BaseModel):
    task_title = models.CharField(max_length=150)
    descript = models.CharField(max_length=150)
    deadline = models.DateTimeField(null=True, blank= True)
    status = models.CharField(max_length=150)
    category = models.ForeignKey(Category,null=True, blank=True, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority,null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):

        return self.task_title
    
class Note(BaseModel):
    task = models.ForeignKey (Task,null=True,blank=True, on_delete=models.CASCADE)
    contents= models.CharField(max_length=250)

    def __str__(self):

        return self.task
    
class SubTask(BaseModel):
    parent_task = models.ForeignKey(Task,null=True,blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    statusstatus = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("In Progress ", "In Progress"),
            ("Completed", "Completed"),
    ],
    default="pending"
    )

