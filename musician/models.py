from django.db import models
from rest_framework.exceptions import ValidationError


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self) -> bool:
        return self.age >= 21

    def clean(self) -> None:
        if self.age < 14:
            raise ValidationError(
                {
                    "age": "This musician is under 14 years.",
                },
            )

    def save(
            self,
            *args,
            **kwargs,
    ):
        self.full_clean()
        return super(Musician, self).save(
            *args,
            **kwargs,
        )
