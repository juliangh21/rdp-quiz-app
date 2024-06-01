from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  
  def __init__(self,**properties):
    # Set Form properties and Data Bindings.
    
    
    
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def Berlinbutton_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.selection = 'b'
    

  def brusselsbutton_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.selection = 'c'
    

  def lyonbutton_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.selection = 'd'

  def submitbutton_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.selection == self.answer:
      print("correct")

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.selection = 'a'
