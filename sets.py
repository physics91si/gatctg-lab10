import math

class Set:
    def __init__(self):
        '''initializes the set as the empty set'''
        self.list = []
    def contains(self, element):
        '''Checks to see if an element is within the set; returns Boolean'''
        for item in self.list:
            if item == element:
                return True
        return False
    def add(self, element):
        '''Adds an element to the set'''
        self.list.append(element)
    def remove(self, element):
        '''Removes an element from the set'''
        if self.contains(element) == True:
            self.list.remove(element)
    def size(self):
        '''Finds the length of the set'''
        return len(self.list)
    def __and__(self, otherSet):
        '''Finds the union of the two sets'''
        newSet = Set()
        for otherEle in otherSet.list:
            if self.contains(otherEle):
                newSet.add(otherEle)
        return newSet
    def __or__(self, otherSet):
        '''Finds the elements that are shared by both sets'''
        newSet = Set()
        for elements in self.list:
            newSet.add(elements)
        for otherEle in otherSet.list:
            if newSet.contains(otherEle):
                pass
            else:
                newSet.add(otherEle)
        return newSet
    def __sub__(otherSet, self):
        '''Finds the elements that are in the first argument but not in the second argument '''
        newSet = Set()
        for otherEle in otherSet.list:
            if self.contains(otherEle):
                pass
            else:
                newSet.add(otherEle)
        return newSet
    def __str__(self):
        '''Iterates through the elements to concatonate them into a string'''
        string = ""
        for element in self.list:
            string += str(element)
            string += " "
        return string
    def __
