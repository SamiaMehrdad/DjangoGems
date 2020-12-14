from django.db import models
from django.urls import reverse

# Create your models here.
# class Gem:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, theme, priceRange, description, hardness):
#     self.name = name
#     self.theme = theme
#     self.description = description
#     self.priceRange = priceRange
#     self.hardness = hardness

# gems = [
#   Gem('Amber', 'Orangish', 3, 'Fossilized resin', 2),
#   Gem('Emerald', 'Green', 8, 'The most valued variety of beryl', 8),
#   Gem('Diamond', 10, 'Clear', 'Mostly primeval, over a billion years old', 10)
# ]

class Gem(models.Model):

  name = models.CharField(max_length=50)
  theme = models.CharField(max_length=50)
  description = models.TextField(max_length=250)
  price_range = models.IntegerField()
  hardness = models.IntegerField()

  def __str__(self):
        return self.name + " the precious"

  def get_absolute_url(self):
    return reverse('detail', kwargs={'gem_id': self.id})      