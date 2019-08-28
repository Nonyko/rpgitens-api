from django.db import models


class Price(models.Model):
    platinumPiece = models.FloatField(default=0)
    goldPiece = models.FloatField(default=0)
    silverPiece = models.FloatField(default=0)
    copperPiece = models.FloatField(default=0)

    def __str__(self):
        dict_values = self.formatValueAsPlatinum()
        return self.getStrValuePrice(
            dict_values['valuePlatinum'],
            dict_values['valueGold'],
            dict_values['valueSilver'],
            dict_values['valueCopper'])

    def getStrValuePrice(self, platinumPiece, goldPiece, silverPiece, copperPiece):
        strvalue = ''
        if platinumPiece > 0:
            strvalue += str(platinumPiece) + ' pp '
        if goldPiece > 0:
            strvalue += str(goldPiece) + ' gp '
        if silverPiece > 0:
            strvalue += str(silverPiece) + ' sp '
        if copperPiece > 0:
            strvalue += str(copperPiece) + ' cp '
        return strvalue

    def formatValueAsPlatinum(self):
        valuePlatinum = 0
        valuePlatinum += self.platinumPiece
        valuePlatinum += int(self.goldPiece / 10)
        valueGold = self.goldPiece % 10

        valueGold += int(self.silverPiece / 10)
        valueSilver = self.silverPiece % 10
        valuePlatinum += int(valueGold / 10)
        valueGold = valueGold % 10


        valueSilver += int(self.copperPiece/10)
        valueCopper = self.copperPiece % 10


        valueGold += int(valueSilver / 10)
        valueSilver = valueSilver % 10
        valuePlatinum += int(valueGold / 10)
        valueGold = valueGold % 10

        values = {
           'valuePlatinum': valuePlatinum,
           'valueGold': valueGold,
           'valueSilver': valueSilver,
           'valueCopper': valueCopper,
        }
        return values

    def formatValueAsGold(self):
        valueGold = 0
        valueGold += self.platinumPiece * 10
        valueGold += self.goldPiece
        valueGold += int(self.silverPiece / 10)
        valueSilver = self.silverPiece % 10

        valueSilver += int(self.copperPiece/10)
        valueCopper = self.copperPiece % 10

        valueGold += int(valueSilver / 10)
        valueSilver = valueSilver % 10

        values = {
            'valuePlatinum': 0,
            'valueGold': valueGold,
            'valueSilver': valueSilver,
            'valueCopper': valueCopper,
        }

        return values

    def formatValueAsSilver(self):
        valueSilver = 0
        valueSilver += self.platinumPiece * 100
        valueSilver += self.goldPiece * 10
        valueSilver += self.silverPiece
        valueSilver += int(self.copperPiece/10)
        valueCopper = self.copperPiece % 10

        values = {
            'valuePlatinum': 0,
            'valueGold': 0,
            'valueSilver': valueSilver,
            'valueCopper': valueCopper,
        }
        return values

    def formatValueAsCopper(self):
        value = 0
        value += self.platinumPiece * 1000
        value += self.goldPiece * 100
        value += self.silverPiece * 10
        value += self.copperPiece
        values = {
            'valuePlatinum': 0,
            'valueGold': 0,
            'valueSilver': 0,
            'valueCopper': value,
        }
        return values


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.OneToOneField(Price, on_delete=models.CASCADE)
    bulk = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Armor(Item):
    ARMOR_TRAITS = (
        ('C', 'Clumsy'),
        ('F', 'Fragile'),
        ('N', 'Noisy'),
    )
    ARMOR_TYPES = (
        ('L', 'Light'),
        ('M', 'Medium'),
        ('H', 'Heavy'),
        ('S', 'Shield'),
    )
    type = models.CharField(max_length=100, choices=ARMOR_TYPES)
    ac_bonus = models.IntegerField(default=0)
    tac_bonus = models.IntegerField(default=0)
    check_penalty = models.IntegerField(default=0)
    speed_penalty = models.IntegerField(default=0)
    trait = models.CharField(max_length=100, choices=ARMOR_TRAITS, blank=True)

    def __str__(self):
        return self.name


class WeaponTrait(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' - ' + str(self.id)


class Weapon(Item):
    WEAPON_GROUPS = (
        ('AXE', 'Axe'),
        ('BOW', 'Bow'),
        ('BRAWLING', 'Brawling'),
        ('CLUB', 'Club'),
        ('DART', 'Dart'),
        ('FLAIL', 'Flail'),
        ('HAMMER', 'Hammer'),
        ('KNIFE', 'Knife'),
        ('PICK', 'Pick'),
        ('POLEARM', 'Polearm'),
        ('SHIELD', 'Shield'),
        ('SLING', 'Sling'),
        ('SPEAR', 'Spear'),
        ('SWORD', 'Sword'),
    )
    WEAPON_TYPES = (
        ('SM', 'Simple Melee'),
        ('MM', 'Martial Melee'),
        ('SR', 'Simple Ranged'),
        ('MR', 'Martial Ranged'),
        ('EM', 'Exotic Melee'),
    )
    type = models.CharField(max_length=100, choices=WEAPON_TYPES)
    damage = models.CharField(max_length=100)
    hands = models.CharField(max_length=100)
    group = models.CharField(max_length=100, choices=WEAPON_GROUPS)
    traits = models.ManyToManyField(WeaponTrait)
    uncommon = models.BooleanField(default=False)
    reload = models.IntegerField(default=0)
    range = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Ammunition(Item):
    unitiesInPackage = models.IntegerField(default=10)
    ammoForWeapons = models.ManyToManyField(Weapon)

    def __str__(self):
        return self.name

class Gear(Item):
    GEAR_TYPES = (
        ('GT', 'General Tools'),
        ('CT', 'Climbing Tools'),
        ('PT', 'Profession Tools'),
        ('S', 'Storage'),
        ('RW', 'Read & Writing'),
        ('A', 'Appearance'),
        ('AE', 'Ambush Equipment'),
        ('CE', 'Camping Equipment'),
        ('I', 'Illumination'),
        ('M', 'Miscellaneous'),
    )
    type = models.CharField(max_length=100, choices=GEAR_TYPES)
    hands = models.CharField(max_length=100)
    unitiesInPackage = models.IntegerField(default=1)

    def __str__(self):
        return self.name
