from django.test import TestCase
import json


# Create your tests here.
class Person():
    def __init__(self):
        self.name = ''
        self.age = 0


p = Person()
p.__dict__['name'] = 'wuketao'
print(json.dumps(p.__dict__))
