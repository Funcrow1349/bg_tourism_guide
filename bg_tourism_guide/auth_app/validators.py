from django.core.exceptions import ValidationError


def is_only_letters(value):
    if not value.isalpha():
        raise ValidationError('The name must contain only letters!')


def starts_with_uppercase(value):
    if not value[0].isupper():
        raise ValidationError('The name must start with uppercase character!')