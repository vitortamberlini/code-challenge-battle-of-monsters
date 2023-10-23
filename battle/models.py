from django.db import models


# Create your models here.
class Battle(models.Model):
    monsterA = models.ForeignKey(
        "monster.Monster",
        verbose_name="Monster A",
        on_delete=models.CASCADE,
        related_name="+",
    )

    monsterB = models.ForeignKey(
        "monster.Monster",
        verbose_name="Monster B",
        on_delete=models.CASCADE,
        related_name="+",
    )

    winner = models.ForeignKey(
        "monster.Monster",
        verbose_name="Winner",
        on_delete=models.CASCADE,
        related_name="+",
    )

    class Meta:
        verbose_name = "Battle"
        verbose_name_plural = "Battles"
        ordering = ["id"]
