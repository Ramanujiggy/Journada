import factory
from Journada.users.models import User, Session


#testing that a user can be created in the postgres database 


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "test"
    password = "Test"
    first_name = "John"
    last_name= "Smithers"
    email = "testemail@gmail.com"

class SessionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Session 

    hours_trained =1
    minutes_trained =30
    grappling_type= "Gi"
    date = "2023-01-01"
    time = "09:35:40.000Z"
    user_id = factory.SubFactory(UserFactory)
    notes = "testnotes"


