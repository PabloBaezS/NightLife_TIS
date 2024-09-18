from django.db import models

class NightClub(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    ageReq = models.PositiveIntegerField()  # Minimum age requirement
    categories = models.CharField(max_length=255)  # Example: "Dance, Bar"
    dressCode = models.CharField(max_length=255)  # Example: "Formal"
    daysActive = models.CharField(max_length=255)  # Example: "Friday, Saturday"
    hours = models.CharField(max_length=100)  # Example: "9:00 PM - 4:00 AM"
    nightclubID = models.AutoField(primary_key=True)  # Unique identifier for each club

    # Methods as specified in the class diagram
    def getDetails(self):
        """Returns a dictionary of nightclub details."""
        return {
            'name': self.name,
            'address': self.address,
            'ageReq': self.ageReq,
            'categories': self.categories,
            'dressCode': self.dressCode,
            'daysActive': self.daysActive,
            'hours': self.hours,
            'nightclubID': self.nightclubID
        }

    def updateHours(self, new_hours):
        """Updates the hours of the nightclub."""
        self.hours = new_hours
        self.save()

    @classmethod
    def createNightclub(cls, name, address, ageReq, categories, dressCode, daysActive):
        """Creates a new nightclub entry."""
        nightclub = cls(
            name=name,
            address=address,
            ageReq=ageReq,
            categories=categories,
            dressCode=dressCode,
            daysActive=daysActive,
            hours="9:00 PM - 4:00 AM"  # Default hours
        )
        nightclub.save()
        return nightclub

    def deleteNightclub(self):
        """Deletes the nightclub."""
        self.delete()

    def __str__(self):
        return self.name
