from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         abstract = True

class Category(BaseModel):
    category_name= models.CharField(max_length=150)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):

        return self.category_name
    
class Priority(BaseModel):
    priority_name= models.CharField(max_length=150)

    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"
    def __str__(self):

        return self.priority_name
    
class Task(BaseModel):
    task_title = models.CharField(max_length=150)
    descript = models.CharField(max_length=150)
    deadline = models.DateTimeField(null=True, blank= True)
    status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("In Progress ", "In Progress"),
            ("Completed", "Completed"),
    ],
    )
    category = models.ForeignKey(Category,null=True, blank=True, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority,null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):

        return self.task_title
    
class Note(BaseModel):
    task = models.ForeignKey (Task,null=True,blank=True, on_delete=models.CASCADE)
    contents= models.CharField(max_length=250)

    def __str__(self):

        return self.contents
    
class SubTask(BaseModel):
    parent_task = models.ForeignKey(Task,null=True,blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("In Progress ", "In Progress"),
            ("Completed", "Completed"),
    ],
    default="pending"
    )

