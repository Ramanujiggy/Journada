import factory
from django.contrib.auth.models import User

from .models import Profile, GrappleEntry


#testing that a user can be created in the postgres database

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    password = factory.Faker('password'),
    email = factory.Sequence(lambda n: f'user{n}@example.com')


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    first_name = factory.Sequence(lambda n: f'first_name{n}')
    last_name = factory.Sequence(lambda n: f'last_name{n}')
    user = factory.SubFactory(UserFactory)


class GrappleEntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GrappleEntry

    hours_trained =0
    minutes_trained =0
    grappling_type= "x"
    date = "2023-01-01"
    time = "09:35:40.000Z"
    user = factory.SubFactory(UserFactory)
    notes = "testnotes"
