import gpib
import serial as ser

class AgilentLightWaveConnection():
    def __init__(self, gpib_num, gpib_dev_num):
        self._dev = gpib.dev(gpib_num, gpib_dev_num)

    def _write(self, cmd):
        gpib.write(self._dev, cmd)

    def _read(self, num_bytes=100):
        data = gpib.read(self._dev, num_bytes)
        return data.decode('ascii')

    def _read_raw(self, num_bytes=100):
        data = gpib.read(self._dev, num_bytes)
        return data

    def _query(self, cmd, num_bytes=100):
        self._write(cmd)
        data = self._read(num_bytes)
        return data

    def _query_raw(self, cmd, num_bytes=100):
        self._write(cmd)
        data = self._read_raw(num_bytes)
        return data
