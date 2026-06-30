from time import monotonic, sleep
from collections import namedtuple
from multiio import SMmultiio
from ...pins.pi import PiPin, PiFactory
from ...exc import PinSetInput, PinInvalidPin
import os

PinState = namedtuple('PinState', ('timestamp', 'state'))

class MultiIOAnalogPin(PiPin):
    """
    Input pin that reads a 0-10V analog input on the Multi-IO HAT via I2C.
    """
    def __init__(self, factory, info, stack=0, channel=1):
        super().__init__(factory, info)
        self._stack = stack
        self._channel = channel
        self._function = 'input'
        self._pull = info.pull or 'floating'
        self._state = 0.0
        self._bounce = None
        self._edges = 'both'
        self._when_changed = None
        self.card = SMmultiio(stack=stack)
        self.clear_states()

    def _get_state(self):
        return self.card.get_u_in(self._channel) / 10.0

    def _set_state(self, value):
        raise PinSetInput(f'MultiIOAnalogPin is read-only: {self!r}')
