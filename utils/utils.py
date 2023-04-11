from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

monster_a_data = {
    "id": 6,
    "name": "Old Shark",
    "imageUrl": "https://fsl-assessment-public-files.s3.amazonaws.com/assessment-cc-01/old"
    "-shark.png",
    "attack": 50,
    "defense": 20,
    "hp": 80,
    "speed": 90,
}

monster_b_data = {
    "id": 7,
    "name": "Dead Unicorn",
    "imageUrl": "https://fsl-assessment-public-files.s3.amazonaws.com/assessment-cc-01/dead"
    "-unicorn.png",
    "attack": 60,
    "defense": 40,
    "hp": 10,
    "speed": 80,
}


class CustomCharField(serializers.CharField):
    default_error_messages = {
        "invalid": _("This information is not valid."),
        "blank": _("This field cannot be empty."),
        "null": _("This field cannot be null."),
        "max_length": _("This field can have at most {max_length} characters."),
        "min_length": _("This field must have at least {min_length} characters."),
    }
