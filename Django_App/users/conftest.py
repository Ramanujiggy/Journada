import factory 
import pytest  
from pytest_factoryboy import register 

from .factories import (UserFactory,SessionFactory)

register(SessionFactory) #registering factories to make them accessible
register(UserFactory)



@pytest.fixture()
def session(session_factory):
    return session_factory()

