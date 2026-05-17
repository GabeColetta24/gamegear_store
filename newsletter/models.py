from django.db import models


# Newsletter signup model
# Stores email addresses submitted by users
class NewsletterSignup(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Shows email address in admin panel
    def __str__(self):
        return self.email