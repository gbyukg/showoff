<!SLIDE >
# Python 代码

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

    """Implementation of the abstract factory pattern"""
    import six
    import abc
    import random


    class PetShop(object):

        """A pet shop"""

        def __init__(self, animal_factory=None):
            """pet_factory is our abstract factory.  We can set it at will."""

            self.pet_factory = animal_factory

        def show_pet(self):
            """Creates and shows a pet using the abstract factory"""

            pet = self.pet_factory.get_pet()
            print("We have a lovely {}".format(pet))
            print("It says {}".format(pet.speak()))
            print("We also have {}".format(self.pet_factory.get_food()))


    # Stuff that our factory makes

    class Dog(object):

        def speak(self):
            return "woof"

        def __str__(self):
            return "Dog"


    class Cat(object):

        def speak(self):
            return "meow"

        def __str__(self):
            return "Cat"