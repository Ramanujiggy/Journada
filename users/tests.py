import pytest 
from django.urls import reverse
from .factories import GrappleEntryFactory
from .factories import ProfileFactory



#pytestmark = pytest.mark.django_db



@pytest.mark.django_db
def test_session_view(client):
        #create a client to simulate http requests
        user = ProfileFactory()
        
        client.force_login(user)

        #use factory boy to create new TrainingSession Instance
        grapple_entry = GrappleEntryFactory.create()
       


        response = client.post(reverse("users:log_session"), grapple_entry.__dict__)
        
        #check if the response is a redirect (indicating success)
        assert response.status_code == 302 #redirect status code 

        #check if session was saved to the database
        assert TrainingSession.objects.count() >= 1 

        #get the saved session from the database
        saved_session =TrainingSesssion.objects.first()

        assert saved_session.grappling_type == grapple_entry.grappling_type
        assert saved_session.hours_trained == grapple_entry.hours_trained
        assert saved_session.minutes_trained == grapple_entry.minutes_trained
        assert saved_session.date == grapple_entry.date
        assert saved_session.time == grapple_entry.time
        assert saved_session.notes == grapple_entry.notes


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


        

