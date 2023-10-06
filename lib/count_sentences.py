#!/usr/bin/env python3

class MyString:
  def __init__(self, value = "Hello"):
    self.value = value
    pass

  def value(self, val):
    if (type(val) in (str)):
      return self.value
    else: 
      print("The value must be a string.")

  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    pass
