from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Character(models.Model):
    PYRO = "Pyro"
    GEO = "Geo"
    HYDRO = "Hydro"
    ELECTRO = "Electro"
    CRYO = "Cryo"
    ANEMO = "Anemo"
    ADAPTIVE = "Adaptive"

    ELEMENT_CHOICES = [
        (PYRO, "Pyro"),
        (GEO, "Geo"),
        (HYDRO, "Hydro"),
        (ELECTRO, 'Electro'),
        (CRYO, "Cryo"),
        (ANEMO, "Anemo"),
        (ADAPTIVE, "Adaptive"),
    ]


    BOW = "Bow"
    CATALYST = "Catalyst"
    CLAYMORE = "Claymore"
    POLEARM = "Polearm"
    SWORD = "Sword"

    WEAPON_CHOICES = [
        (BOW, "Bow"),
        (CATALYST, "Catalyst"),
        (CLAYMORE, "Claymore"),
        (POLEARM, "Polearm"),
        (SWORD, "Sword"),
    ]

    INAZUMA = "Inazuma"
    LIYUE = "Liyue"
    MONDSTADT = "Mondstadt"
    SNEZHNAYA = "Snezhnaya"
    OUTLANDER = "Outlander"

    REGION_CHOICES = [
        (INAZUMA, "Inazuma"),
        (LIYUE, "Liyue"),
        (MONDSTADT, "Mondstadt"),
        (SNEZHNAYA, "Snezhnaya"),
        (OUTLANDER, "Outlander")
    ]

    icon = models.ImageField(upload_to='media')
    name = models.CharField(max_length=30)
    rarity = models.IntegerField()
    element = models.CharField(max_length=20, choices=ELEMENT_CHOICES, default=PYRO)
    weapon = models.CharField(max_length=20, choices=WEAPON_CHOICES, default=SWORD)
    region = models.CharField(max_length=30, choices=REGION_CHOICES, default=OUTLANDER)


    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "rarity": self.rarity,
            "element": self.element,
            "weapon" : self.weapon,
            "region": self.region,
        }

    def __str__(self):
        return self.name
    