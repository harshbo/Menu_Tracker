from django.db import models

class Day(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  

class Lunch(models.Model):
    day = models.ForeignKey(Day,on_delete= models.CASCADE)
    rice = models.CharField(max_length=500)
    curries = models.CharField(max_length=500)
    dal = models.CharField(max_length=500)
    chips = models.BooleanField(default=True)
    curd = models.BooleanField(default=True)
    chapati=models.BooleanField(default=True)
    juice = models.CharField(max_length=500)
    salad = models.CharField(max_length=500)
    pickle = models.CharField(max_length=500)
    dessert = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.day}-lunch"


class BreakFast(models.Model):
  day=models.ForeignKey(Day,on_delete=models.CASCADE)
  tiffen=models.CharField(max_length=500)
  eggs=models.BooleanField(default=True)
  raagi=models.BooleanField(default=True)
  juice=models.CharField(max_length=200)
  oats=models.BooleanField(default=True)
  milk=models.BooleanField(default=True)
  var=models.CharField(max_length=500)

  def __str__(self):
        return f"{self.day}-Breakfast"



class Snacks(models.Model):
  day=models.ForeignKey(Day,on_delete=models.CASCADE)
  snack=models.CharField(max_length=500)
  milk=models.BooleanField(default=True)
  var=models.CharField(max_length=500)

  def __str__(self):
        return f"{self.day}-Snacks"


class Supper(models.Model):
  day=models.ForeignKey(Day,on_delete=models.CASCADE)
  rice = models.CharField(max_length=500)
  curries = models.CharField(max_length=500)
  dal = models.CharField(max_length=500)
  chips = models.BooleanField(default=True)
  curd = models.BooleanField(default=True)
  chapati=models.BooleanField(default=True)
  pickle = models.CharField(max_length=500)
  dessert = models.CharField(max_length=400)
  special=models.CharField(max_length=500)


  def __str__(self):
    return f"{self.day}-Supper"
  
  
  
  
  


# class DayMenu(models.Model):
#     day = models.CharField(max_length=255, null=False, unique=True)
#     session = models.CharField(max_length=255, null=False, unique=True)
#     menu = models.ForeignKey(Menu, null=True, on_delete=models.SET_NULL)

#     def __str__(self):
#         return f"{self.day}-{self.session}"
