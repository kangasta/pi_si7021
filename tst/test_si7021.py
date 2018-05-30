from unittest import TestCase
from unittest.mock import MagicMock, patch
import pigpio

from si7021 import Si7021

class Si7021Test(TestCase):
	def __get_mock_pi(return_bytes):
		mock = MagicMock()
		mock.i2c_read_device.return_value = (len(return_bytes),bytearray(return_bytes),)
		return mock

	@patch.object(pigpio, 'pi')
	def test_temperature_0x00(self, mock):
		mock.return_value=Si7021Test.__get_mock_pi([0,0])

		RHTEMP = Si7021()
		temp = RHTEMP.temperature
		self.assertEqual(temp, -46.85)

	@patch.object(pigpio, 'pi')
	def test_temperature_0xFF(self, mock):
		mock.return_value=Si7021Test.__get_mock_pi([0xFF,0xFF])

		RHTEMP = Si7021()
		temp = RHTEMP.temperature
		self.assertEqual(int(temp), 128)

	@patch.object(pigpio, 'pi')
	def test_relative_humidity_0x00(self, mock):
		mock.return_value=Si7021Test.__get_mock_pi([0,0])

		RHTEMP = Si7021()
		temp = RHTEMP.relative_humidity
		self.assertEqual(temp, -6)

	@patch.object(pigpio, 'pi')
	def test_relative_humidity_0xFF(self, mock):
		mock.return_value=Si7021Test.__get_mock_pi([0xFF,0xFF])

		RHTEMP = Si7021()
		temp = RHTEMP.relative_humidity
		self.assertEqual(int(temp), 118)
