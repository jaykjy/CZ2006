from django.test import TestCase
from django.contrib.auth.models import User
from ..forms import UserRegisterForm 


class UserTestForms(TestCase):

    def test_user_regist_form_is_valid_case1(self):
        form = UserRegisterForm(data={
            'username': 'dell',
            'email': 'dell@email.com',
            'password1': '1234deLl',
            'password2': '1234deLl'
        })
        self.assertTrue(form.is_valid())
    
    def test_user_register_form_is_valid_case2(self):
        form = UserRegisterForm(data={
            'username': 'dell&',
            'email': 'dell@email.com',
            'password1': '1234deLl',
            'password2': '1234deLl'
        })
        self.assertFalse(form.is_valid())
    
    def test_user_register_form_is_valid_case3(self):
        test_user1 = User.objects.create_user(username='dell', email='dell@email.com',password='1234deLl')
        form = UserRegisterForm(data={
            'username': 'dell',
            'email': 'dell@email.com',
            'password1': '1234deLl',
            'password2': '1234deLl'
        })
        self.assertFalse(form.is_valid())
    
    def test_user_register_form_is_valid_case4(self):
        form = UserRegisterForm(data={
            'username': 'dell0',
            'email': 'dell.@email.com',
            'password1': '1234deLl',
            'password2': '1234deLl'
        })
        self.assertFalse(form.is_valid())
    
    def test_user_register_form_is_valid_case5(self):
        form = UserRegisterForm(data={
            'username': 'dell0',
            'email': '@email.com',
            'password1': '1234deLl',
            'password2': '1234deLl'
        })
        self.assertFalse(form.is_valid())
    
    def test_user_register_form_is_valid_case6(self):
        form = UserRegisterForm(data={
            'username': 'dell0',
            'email': 'dell0@email',
            'password1': '1234deLl',
            'password2': '1234deLl'
        })
        self.assertFalse(form.is_valid())
    
    def test_user_register_form_is_valid_case7(self):
        form = UserRegisterForm(data={
            'username': 'dell0',
            'email': 'dell0@email.c',
            'password1': '1234deLl',
            'password2': '1234deLl'
        })
        self.assertFalse(form.is_valid())

    def test_user_register_form_is_valid_case8(self):
        form = UserRegisterForm(data={
            'username': 'dell0',
            'email': 'dell0@email.c',
            'password1': '1234deLl',
            'password2': '1234deLl'
        })
        self.assertFalse(form.is_valid())

    def test_user_register_form_is_valid_case9(self):
        form = UserRegisterForm(data={
            'username': 'dell0',
            'email': 'dell0@',
            'password1': '1234deLl',
            'password2': '1234deLl'
        })
        self.assertFalse(form.is_valid())

    def test_user_register_form_is_valid_case10(self):
        form = UserRegisterForm(data={
            'username': 'dell0',
            'email': 'dell0@email.com',
            'password1': 'dell0123',
            'password2': 'dell0123'
        })
        self.assertFalse(form.is_valid())

    def test_user_register_form_is_valid_case11(self):
        form = UserRegisterForm(data={
            'username': 'dell0',
            'email': 'dell0@email.com',
            'password1': '12345678',
            'password2': '12345678'
        })
        self.assertFalse(form.is_valid())
    
    def test_user_register_form_is_valid_case12(self):
        form = UserRegisterForm(data={
            'username': 'dell0',
            'email': 'dell0@email.com',
            'password1': '96385274',
            'password2': '96385274'
        })
        self.assertFalse(form.is_valid())
    
    def test_user_register_form_is_valid_case13(self):
        form = UserRegisterForm(data={
            'username': 'dell0',
            'email': 'dell0@email.com',
            'password1': '1234deL',
            'password2': '1234deL'
        })
        self.assertFalse(form.is_valid())

    def test_user_register_form_is_valid_case14(self):
        form = UserRegisterForm(data={
            'username': 'dell0',
            'email': 'dell0@email.com',
            'password1': '1234adeLl',
            'password2': '1234adeLl'
        })
        self.assertTrue(form.is_valid())

    def test_user_register_form_is_valid_case15(self):
        form = UserRegisterForm(data={
            'username': 'dell0',
            'email': 'dell0@email.com',
            'password1': '1234deLl',
            'password2': '1234deLk'
        })
        self.assertFalse(form.is_valid())

    def test_user_register_form_no_data(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)