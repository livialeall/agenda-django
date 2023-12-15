import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent #raiz
NUMBER_OF_OBJECTS = 1000 #numero de objetos - contatos - que eu vou gerar

sys.path.append(str(DJANGO_BASE_DIR)) #faz com que o python procure arquivos na raiz - fora do arquivo
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings' #usando o django sem ser pelo manage.py 
settings.USE_TZ = False #mudei o time zone para false nesse scripts

django.setup() #inicia o django como faz o manage.py

if __name__ == '__main__':
    import faker #biblioteca para gerar dados fakes para testes 

    from contact.models import Category, Contact

    Contact.objects.all().delete() #deleta todos os contatos - limpa a base de dados
    Category.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categories = ['Amigos', 'Família', 'Conhecidos']

    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save() #salva uma por uma na bd

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile() #dicionario com perfil fake
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts) #cria todos os contatos de uma vez só