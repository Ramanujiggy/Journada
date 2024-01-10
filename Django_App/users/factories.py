import factory
from .models import User, Session


#testing that a user can be created in the postgres database 


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    password = factory.Faker('password'), #update to 'password_hash' later
    first_name = factory.Sequence(lambda n: f'first_name{n}')
    last_name= factory.Sequence(lambda n: f'last_name{n}')
    email = factory.Sequence(lambda n: f'user{n}@example.com')
  


    

class SessionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Session 

    hours_trained =0
    minutes_trained =0
    grappling_type= "x"
    date = "2023-01-01"
    time = "09:35:40.000Z"
    user_id = factory.SubFactory(UserFactory)
    notes = "testnotes"


