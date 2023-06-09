from django.db import models





class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    @property
    def product_count(self):
        return self.product_set.count()


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def rating(self):
        stars = [review.stars for review in self.reviews.all() if review.stars is not None]
        if not stars:
            return 0
        else:
            return round(sum(stars) / len(stars), 2)


class Review(models.Model):
    text = models.CharField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    CHOICES = ((i, '*' * i) for i in range(1, 6))
    stars = models.IntegerField(choices=CHOICES, null=True)

    def __str__(self):
        return self.text
