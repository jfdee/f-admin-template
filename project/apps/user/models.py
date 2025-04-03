from tortoise import (fields, models)
from tortoise.contrib.pydantic import pydantic_model_creator


class User(models.Model):
    created_at = fields.DatetimeField(description='Дата создания', auto_now_add=True)
    username = fields.CharField(description='Логин', max_length=128)
    email = fields.CharField(description='Почта', max_length=128)
    last_name = fields.CharField(description='Фамилия', max_length=256)
    first_name = fields.CharField(description='Имя', max_length=256)
    patronymic = fields.CharField(description='Отчество', max_length=256, null=True)
    is_blocked = fields.BooleanField(description='Заблокирован', default=False)
    organization = fields.ForeignKeyField(
        model_name='models.Organization',
        description='Организация',
        related_name='users',
        on_delete=fields.SET_NULL,
        null=True,
    )
    register_at = fields.DateField(description='Дата регистрации', null=True)
    blocked_at = fields.DatetimeField(description='Дата и время блокировки', null=True)
    number = fields.IntField(description='Номер', null=True)
    note = fields.TextField(description='Примечание', null=True)

    class Meta:
        verbose_name: str = 'Пользователь'
        verbose_name_plural: str = 'Пользователи'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


UserPydantic = pydantic_model_creator(User)


__all__ = ('User', )
