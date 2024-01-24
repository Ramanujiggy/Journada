import pytest
from pytest_factoryboy import register 

from .factories import (ProfileFactory, GrappleEntryFactory)

register(GrappleEntryFactory) #registering factories to make them accessible
register(ProfileFactory)



@pytest.fixture()
def session(session_factory):
    return session_factory()

