import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class APITestException(Exception):
    """ a custom exception for error handling on test script level(not target side)"""
    def __init__(self, message):
        self.value = message

    def __str__(self):
        return self.value
    

class GUITestException(Exception):
    """ a custom exception for error handling on test script level(not target side)"""
    def __init__(self, message):
        self.value = message

    def __str__(self):
        return self.value