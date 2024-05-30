import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            # TODO: Добавьте сохранение модели
            for row in phones:
                new = Phone(id=row['id'],
                            name=row['name'],
                            price=row['price'],
                            image=row['image'],
                            release_date=row['release_date'],
                            lte_exists=row['lte_exists'],
                            slug=slugify(row['name']))
                new.save()
                # print()
            print('Загрузка завершена')
