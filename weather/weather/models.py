from django.db import models

# Create your models here.

class node(models.Model):
    Name = models.CharField(max_length=25)
    IP = models.IPAddressField()
    def __unicode__(self):
        return self.Name

class report(models.Model):
    Node = models.ForeignKey(node)
    Time = models.DateTimeField('time taken')
    TimeReceived = models.DateTimeField('time received', auto_now_add=True)
    Temp = models.FloatField('Temperature')
    Humd = models.FloatField('Humidity')
    
    def __unicode__(self):
        return (self.Time.isoformat(' '))
    
