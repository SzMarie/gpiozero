from .lgpio import LGPIOFactory
import megaind 
from multiio import SMmultiio

class SequentRelay():
  """
  """
  def _init_(self, stack=0):
    self.card = SMmultiio(stack=stack)
    
  def turn_on_relay(self, channel):
    self.card.set_relay(channel, 1)

  def turn_off_relay(self, channel):
    self.card.set_relay(channel, 0)
    

class CustomFactory(LGPIOFactory):
  """

  """
  pass 
