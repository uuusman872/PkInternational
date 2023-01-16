from django.db import models


class CarModel(models.Model):
    Name = models.CharField(max_length=50)
    Icon = models.ImageField(upload_to="model_icons")

    def __repr__(self):
        return self.Name


class Car(models.Model):
    Name = models.CharField(verbose_name="car name", max_length=50)
    Model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    Variant = models.CharField(max_length=50)
    Model_Date = models.DateField()
    Price = models.IntegerField(verbose_name="car price")
    Description = models.TextField(verbose_name="car description")
    Mileage = models.IntegerField()
    Power = models.IntegerField()
    created_at = models.DateField(auto_now=True)
    to_sell = models.BooleanField()

    def __repr__(self):
        return self.Name


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    Image = models.ImageField(verbose_name="Car Image", upload_to="car_picture")

    def __repr__(self):
        return self.car


class CarColor(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    color = models.CharField(max_length=20)

    def __repr__(self):
        return self.car


class FrequentQuestion(models.Model):
    Question = models.TextField()
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    IsAnswered = models.BooleanField()


class FrequesntAnswers(models.Model):
    QuestionId = models.ForeignKey(FrequentQuestion, on_delete=models.CASCADE)
    Answer = models.TextField()
