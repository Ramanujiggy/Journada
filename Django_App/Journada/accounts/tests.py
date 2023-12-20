from django.test import TestCase
from  users import User 

# Create your tests here.

#testing that a user can be created in the postgres database 
def test_register():
    newuser = User.objects.create(
        first_name='Rtest1',
        last_name='rtest1',
        username= 'Rusern',
        password = '#$&(%)#(*)')

    assert newuser.first_name=='Rtest1'


