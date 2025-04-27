from django.db import models

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    meta = models.CharField(max_length=300)
    content = models.TextField()
    thumbnail_img = models.ImageField(null=True, blank=True, upload_to="images/")
    thumbnail_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=255, default="uncategorized")
    slug = models.CharField(max_length=100)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


# New Documentation Model
class Documentation(models.Model):
    title = models.CharField(max_length=255)  # Documentation title (e.g., Django Docs, AWS Docs)
    url = models.URLField()  # URL to the official documentation
    image = models.ImageField(upload_to='docs_images/', blank=True, null=True)  # Optional image for the documentation

    def __str__(self):
        return self.title
