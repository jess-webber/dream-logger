from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Snippet(models.Model):
    user = models.ForeignKey(User,
                        default = 1,
                        null = True,
                        on_delete = models.SET_NULL
                        )
    snip_description = models.TextField(max_length = 500)
    topic_description = models.TextField(max_length = 500)
    snip_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.snip_description
