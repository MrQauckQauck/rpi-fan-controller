import unittest
from unittest.mock import patch
from src.fan_controller import FanController

class TestFanController(unittest.TestCase):

    @patch('src.fan_controller.time.sleep')
    def test_run_fan_cycle(self, mock_sleep):
        fan_controller = FanController()

        # Simulate the fan running for 2 hours
        fan_controller.run_fan_cycle()
        self.assertTrue(fan_controller.is_fan_on)
        
        # Check if the fan was turned off after 2 hours
        mock_sleep.assert_any_call(7200)  # 2 hours in seconds
        fan_controller.turn_off()
        self.assertFalse(fan_controller.is_fan_on)

        # Simulate the fan being off for 3 hours
        mock_sleep.assert_any_call(10800)  # 3 hours in seconds
        fan_controller.run_fan_cycle()
        self.assertTrue(fan_controller.is_fan_on)

        # Check if the fan was turned off after the second run
        mock_sleep.assert_any_call(7200)  # 2 hours in seconds
        fan_controller.turn_off()
        self.assertFalse(fan_controller.is_fan_on)

if __name__ == '__main__':
    unittest.main()