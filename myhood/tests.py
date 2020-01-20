from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import unittest
# Create your tests here.


class Neighborhoodtestcase(TestCase):
    '''
    Class to test all neighbourhood model methods
    '''
    def setUp(Self):
        '''
        Function to create new instance of a neighbourhood class
        '''
        self.hood = Neighborhood(loc_name='Karen', location='Nairobi')
        Self.hood.save()

    def test_instance(self):
        '''
        Test neighbourhood class instantiation
        '''
        self.assertTrue(isinstance(self.hood, Neighborhood))

    def tearDown(self):
        '''
        Function to delete every test instance after it runs
        '''
        Neighborhood.objects.all().delete()

    def create_hood_test(self):
        '''
        Tests that a new hood is saved 
        '''
        self.hood.create_hood()
        hoodlist = Neighborhood.objects.all()
        self.assertTrue(len(hoodlist) == 1)

    def delete_hood_test(self):
        '''
        Tests that a Neighborhood instance can be deleted
        '''
        self.hood.save()
        self.hood.delete()
        hoods = Neighborhood.objects.all()
        self.assertEqual(len(hoods, 0))


class Profiletestcase(TestCase):
    '''
    Class to test the profile class methods
    '''

    def setUp(self):
        self.resident = User(username='Nyakinyua', email='wanyakinyua@gmail.com')
        self.profile = Profile(user=self.resident, profile_pic='img.jpg', location='Karen')

    def test_instance(self):
        '''
        Test class to check instantiation of a new profile instance
        '''
        self.assertTrue(isinstance(self.profile, Profile))

    def tearDown(self):
        '''
        Class to delete all test instances after tests finish running
        '''
        User.objects.all().delete()
        Profile.objects.all().delete()

    def create_user_test(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 1)

    def delete_profile_test(self):
        '''
        Tests that a profile instance can be deleted succesfully
        '''
        self.profile.save()
        self.hood.delete()
        profiles = Profile.objects.all()
        self.assertEqual(len(profiles, 0))
        
    
        
        
class PostsTestCase(TestCase):
    """"
    Class that tests post class
    """
    def setup(self):
        self.post = Post(title='hood vibes',image="default.jpg",description='How we roll in the hood',posted_by='Nyakinyua',where="Kikuyu")
        
        
    def test_instance(self):
        '''
        Test that checks whether poost is an instance of class post
        '''
        self.assertTrue(isinstance(self.post, Posts))
        
    def tearDown(self):
        '''
        Class to delete all test instances after tests finish running
        '''
        Post.objects.all().delete()

class Businesstestcase(TestCase):
    '''
    Class to test the business class models
    '''

    def setUp(self):
        self.bizna = Business(bs_name='bizna', b_pic='default.jpg', about="bizness about", owner="Nyakinyua", bs_email='biz@gmail.com',
                              )
        self.bizna.save()

    def tearDown(self):
        '''
        Will delete all test instances on completion
        '''
        Business.objects.all().delete()

    def create_business_test(self):
    '''
    testcase to test instantiation of business class object
    '''
    self.bizna.create_biz()
    biznalist = Business.objects.all()
    self.assertTrue(len(biznalist) == 1)

    def delete_business_test(self):
        '''
        testcase to delete a instance of business class
        '''
        self.bizna.save()
        self.bizna.delete_biz()
        biznalist = businesses.objects.all()
        self.assertTrue(len(biznalist) == 0)

    def get_biz_test(self):
    '''
    testcase to get businesses for a certain hood
    '''
    self.bizna.save()
    result = Business.search_biz('gas')
    self.assertTrue(len(found) == 1)

    def get_all_biz_test(self):
        '''
        testcase to get all business for the database
        '''
        self.bizna.save()
        result = Business.all_biz()
        self.assertEquals(len(results), 1)



