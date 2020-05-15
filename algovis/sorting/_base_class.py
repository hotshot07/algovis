# This module contains the functions
# common to sorting algorithms

class BaseClass:
    def __init__(self, datalist):
        if not isinstance(datalist, list):
            raise TypeError('parameter must be a list datatype')

        if not datalist:
            raise ValueError('parameter has invalid value')

        for _element in datalist:
            if not isinstance(_element, int):
                raise TypeError('parameter can only contain int datatype')
