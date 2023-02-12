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
        return f'{self.title} | {self.level}'

    class Meta:
        db_table = 'Classes'
        verbose_name_plural = 'Classes'

class Location(models.Model):
    location = models.CharField(max_length=500)
    province = models.ForeignKey(Classes, on_delete=models.CASCADE)
    image = models.ImageField(default='img/dept.png', null=True, blank=True, upload_to='uploads/')

    def __str__(self):
        return f'{self.venue_title} | {self.prog_id}'

    class Meta:
        db_table = 'Location'
        verbose_name_plural = 'Locations'

