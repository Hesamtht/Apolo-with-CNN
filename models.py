from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Food(models.Model):
    CATEGORIES = (
        ('پیش غذا', 'پیش غذا'),
        ('غذای اصلی', 'غذای اصلی'),
        ('دسر', 'دسر')
    )

    category = models.CharField(max_length=20, choices=CATEGORIES, default='غذای اصلی')
    name = models.CharField("اسم", max_length=70)
    slug = models.SlugField(max_length=70, default='')
    description = models.CharField("توضیحات", max_length=250)
    rate = models.IntegerField("امتیاز", default=100)
    price = models.IntegerField("قیمت")
    time = models.IntegerField("زمان لازم")
    pub_date = models.DateField("تاریخ انتشار", auto_now=False, auto_now_add=True)
    photo = models.ImageField("عکس", upload_to="foods/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu:detail', args=[self.slug])

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Food, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.food.name} in cart"
