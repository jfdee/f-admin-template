from tortoise import (fields, models)


class Organization(models.Model):
    created_at = fields.DatetimeField(description='Дата создания', auto_now_add=True)
    full_name = fields.CharField(description='Полное наименование', max_length=256)
    short_name = fields.CharField(description='Краткое наименование', max_length=256)
    address = fields.CharField(description='Адрес', max_length=128)
    email = fields.CharField(description='Почта', max_length=128)

    class Meta:
        verbose_name: str = 'Организация'
        verbose_name_plural: str = 'Организации'

    def __str__(self):
        return f'{self.short_name}'


__all__ = ('Organization', )
