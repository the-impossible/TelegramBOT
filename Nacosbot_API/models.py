from django.db import models

# Create your models here.
class Level(models.Model):
    level = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.level}'

    class Meta:
        db_table = 'Level'
        verbose_name_plural = 'Levels'

class Classes(models.Model):
    title = models.CharField(max_length=200)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} | {self.level} Level'

    class Meta:
        db_table = 'Classes'
        verbose_name_plural = 'Classes'

class Location(models.Model):
    location = models.CharField(max_length=500)
    province = models.ForeignKey(Classes, on_delete=models.CASCADE)
    image = models.ImageField(default='img/dept.png', null=True, blank=True, upload_to='uploads/')

    def __str__(self):
        return f'{self.location}'

    class Meta:
        db_table = 'Location'
        verbose_name_plural = 'Locations'

class Title(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.title}'
    class Meta:
        db_table = 'Lecturer Title'
        verbose_name_plural = 'Lecturer Title'

class Course(models.Model):
    title = models.CharField(max_length=500)
    code = models.CharField(max_length=500)
    unit = models.IntegerField(default=2)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'Course'
        verbose_name_plural = 'Courses'


class Lecturer(models.Model):
    name = models.CharField(max_length=500)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    pics = models.ImageField(default='img/comlogo.png', null=True, blank=True, upload_to='uploads/')

    def __str__(self):
        return f'{self.title}{self.name}'

    class Meta:
        db_table = 'Lecturer Profile'
        verbose_name_plural = 'Lecturers profile'

class CoursesToLecturer(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.lecturer}|{self.course}'

    class Meta:
        db_table = 'Courses Assigned to Lecturers'
        verbose_name_plural = 'Courses Assigned to Lecturers'

class Semester(models.Model):
    semester = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.semester}'

    class Meta:
        db_table = 'Semester'
        verbose_name_plural = 'Semesters'

class Material(models.Model):
    file = models.FileField(upload_to='materials/')
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return f'Material for: {self.level} Level | {self.semester}'

    class Meta:
        db_table = 'Material'
        verbose_name_plural = 'Materials'
