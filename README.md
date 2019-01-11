# agilent-lightwave
Python GPIB driver for the Agilent Lightwave 8164A/B.

Works with power meter modules and tunable laser modules.

## Installation
First install `Linux GPIB` from https://linux-gpib.sourceforge.io/.
Be sure to install the Python 3 Linux GPIB binaries; test using
```python
import gpib
```
in Python 3,

then
```
pip3 install agilent-lightwave
```
## Usage
```python
mf = lw.AgilentLightWave(gpib_num=0, gpib_dev_num=18, pm_sensor_num=2)

print(mf.laser.set_power_uW(100))
print(mf.power_meter.get_power_uW())

start_wl = 1540 # nm
stop_wl = 1580 # nm
step_wl = 0.1 # nm
sweep_power = 0.2 # mW
sweep_speed = 10 # nm/s
power_meter_slot = 1 # 1, 2, 3 or 4
power_meter_integration_time = 20 # ms
filename_data = 'wavelength_sweep.dat'
restore_settings = True
mf.laser.wavelength_sweep(start_wl,
                          stop_wl,
                          step_wl,
                          sweep_power,
                          sweep_speed,
                          power_meter_slot,
                          power_meter_integration_time,
                          filename_data,
                          restore_settings)
```
