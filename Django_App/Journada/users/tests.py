import pytest 
from django.urls import reverse
from django.test import Client
from .models import Session 
from .models import User 
from .forms import TrainingSessionForm
from .factories import SessionFactory
from .factories import UserFactory 



#pytestmark = pytest.mark.django_db



@pytest.mark.django_db
def test_session_view(client,user_factory):
        #create a client to simulate http requests
        user = UserFactory()
        
        client.force_login(user)

        #use factory boy to create new TrainingSession Instance
        session = SessionFactory.create()
       


        response = client.post(reverse("users:log_session"), session.__dict__)
        
        #check if the response is a redirect (indicating success)
        assert response.status_code == 302 #redirect status code 

        #check if session was saved to the database
        assert TrainingSession.objects.count() >= 1 

        #get the saved session from the database
        saved_session =TrainingSesssion.objects.first()

        assert saved_session.grappling_type == session.grappling_type
        assert saved_session.hours_trained == session.hours_trained
        assert saved_session.minutes_trained == session.minutes_trained
        assert saved_session.date == session.date
        assert saved_session.time == session.time
        assert saved_session.notes == session.notes


"""
class TestLogSessionView:
    def test_session_view(self,client,user):
        #create a client to simualte http requests
        client.force_login(user)

        #use factory boy to create new TrainingSession Instance
        session = TrainingSessionFactory()

        response = client.post(reverse("log_session"), session.__dict__)
        
        #check if the response is a redirect (indicating success)
        assert response.status_code == 302 #redirect status code 

        #check if session was saved to the database
        assert TrainingSession.objects.count() >= 1 

        #get the saved session from the database
        saved_session =TrainingSesssion.objects.first()

        assert saved_session.grappling_type == session.grappling_type
        assert saved_session.hours_trained == session.hours_trained
        assert saved_session.minutes_trained == session.minutes_trained
        assert saved_session.date == session.date
        assert saved_session.time == session.time
        assert saved_session.notes == session.notes

 """       


        

