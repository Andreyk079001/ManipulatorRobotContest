import time, threading
from interfaces.led_indicator_interface import IIndicator

class UARTLedIndicator(IIndicator):
    def __init__(self, manipulator, gpio_name="/dev/gpiochip4/e1_pin"):
        self.manipulator = manipulator
        self.gpio_name = gpio_name
        self._blinking = False

    def on(self):
        self._blinking = False
        self.manipulator.write_gpio(self.gpio_name, 1, timeout_seconds=0.5, throw_error=False)

    def off(self):
        self._blinking = False
        self.manipulator.write_gpio(self.gpio_name, 0, timeout_seconds=0.5, throw_error=False)

    def blink(self, frequency_hz):
        import threading, time
        self._blinking = True
        interval = 1 / (2 * frequency_hz)
        def _blink():
            while self._blinking:
                self.on(); time.sleep(interval)
                self.off(); time.sleep(interval)
        threading.Thread(target=_blink, daemon=True).start()