#!/usr/bin/python3
"""
Defines a locked class that prevents 
the user from dynamically creating new instance attributes

"""


class LockedClass:
   
"""
Create new instance attributes except 'first_name'.
"""

    __slots__ = ["first_name"]
