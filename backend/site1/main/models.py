from django.db import models
from django.contrib.auth.models import User

class Offers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="offers", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Skills(models.Model):
    offers = models.ForeignKey(Offers, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text




'''The super_human pack :
- Memory upgrade ( 5 exaByte )
- Hormones shots
- Body & psychology control
- Restoring lost informations ( a maximum cache memory of one month )

The semi_robotic pack 
- Memory upgrade ( 8 exaBytes )
- Connecting to IoT and direct communication with robots & devices
- Sharing mind data with other users
- Brain internet access subscription ( 30 PetaBytes )

The free_time pack
- Memory upgrade ( 5 exaBytes )
- Eyes screenshots
- Mind traveling authorization
- Brain gaming & streaming pass'''