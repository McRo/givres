from django.db import models

class Website(models.Model):
    TYPE_CHOICES = (
        ('WS', 'Website'),
        ('FB', 'Facebook'),
        ('IG', 'instagram'),
        ('OTHER', 'Other'),
    )

    title = models.CharField(max_length=255)
    url = models.URLField()
    type = models.CharField(choices=TYPE_CHOICES, max_length=10, blank=True)

    def __unicode__(self):
        return "{0} {1}".format(selft.type,  self.title)


class Place(models.Model):
    """
    Some place belonging to an organization
    """
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

    address = models.CharField(max_length=255, null=True)
    zipcode = models.CharField(max_length=10, blank=True, help_text="Code postal / Zipcode")
    city = models.CharField(max_length=50, blank=True)
    country = CountryField(default="")

    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __unicode__(self):
        return u'{0} ({1})'.format(self.name, selft.city)


class Contact(models.Model):
    name = models.CharField(max_length=255, help_text="title/name of the contact")
    main_phone_number = models.CharField(max_length=20)
    secondary_phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    visio_id = models.CharField(max_length=20, help_text="Skype, Messenger, Facetime, Gtalk, ...")
    fax = models.CharField(max_length=20)
