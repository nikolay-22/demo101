from django.core.exceptions import ValidationError
from django.db import models

def non_empty_spaces_validator(value):
    if " " in value:
        raise ValidationError(message="The name should contain no spaces!")


NAME_MAX_LENGTH = 35


class Department(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)

    def __str__(self):
        return self.name


class Employee(models.Model):

    ROLES = (
        (1, "Developer"),
        (2, "QA"),
    )

    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            non_empty_spaces_validator,
        )
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False,
    )

    role = models.IntegerField(
        choices=ROLES,
        blank=False,
        null=False,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        default=1,
    )

    @property
    def full_name(self):
        return(f"{self.first_name} {self.last_name}")






