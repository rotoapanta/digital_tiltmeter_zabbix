# <p align="center">Digital tiltmeter and zabbix 

<p align="center">This project is based on a Digital Inclinometer and a zabbix server.</p>

##

![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)
[![GitHub issues](https://img.shields.io/github/issues/rotoapanta/digital_tiltmeter_zabbix
)](https://github.com/rotoapanta/digital_tiltmeter_zabbix/issues)
![GitHub repo size](https://img.shields.io/github/repo-size/rotoapanta/digital_tiltmeter_zabbix
)
![GitHub last commit](https://img.shields.io/github/last-commit/rotoapanta/digital_tiltmeter_zabbix
)
![GitHub commit merge status](https://img.shields.io/github/commit-status/rotoapanta/prueba_2/main/6a500cc65d)
[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/gpl-2.0)
![Discord](https://img.shields.io/discord/996422496842694726)
[![Discord Invite](https://img.shields.io/badge/discord-join%20now-green)](https://discord.gg/Gs9b3HFd)
![GitHub forks](https://img.shields.io/github/forks/rotoapanta/ESP32-Blinking-RGB-Led?style=social)

# Contents

  * [Getting started](#getting-started)
    * [Getting started with Tiltmeter and Zabbix](#getting-started-with-tiltmeter-and-zabbix)
    * [Requirements](#requirements)
    * [Components Description](#components-description)
    * [Power Supply Options](#power-supply-options)
    * [Pin Layout](#pin-layout)
  * [Instructions](#instructions)
  * [Environment Variables](#environment-variables)
  * [Change Log](#change-log)
  * [Running Tests](#running-tests)
  * [Usage/Examples](#usage-examples)
  * [Feedback](#feedback)
  * [Support](#support)
  * [License](#license)
  * [Autors](#autors)
  * [More Info](#more-info)
  * [Links](#links)

# Getting started

## Getting started with Tiltmeter and Zabbix

The digital inclinometer is a high-precision instrument designed to measure very small changes in the horizontal plane. In the context of volcanoes, an inclinometer is used to measure very small changes in the horizontal plane of the terrain around the volcano. These changes can be indicative of volcanic activity, such as deformation of the terrain caused by inflation or deflation of magma beneath the volcano. This tutorial will guide you to obtain data from the Tiltmeter (tangential axis, radial axis, and temperature) to Zabbix.

Let’s get started!
 
## Requirements

  * Digital Tiltmeter Model D711-A.
  * USB to Serial converter cable.
  * Power Supply Adapter 12 VDC.
  * Hyperterminal.
  * Computer running Anaconda on Windows, Linux or macOS (in this case macOS is used).
  * Python 3.10 or later.
  * [Install py-zabbix 1.1.7](https://pypi.org/project/pyzabbix/)
  * [Install pyserial 3.5](https://pypi.org/project/pyserial/)

## Components Description
![tiltmeter](https://github.com/rotoapanta/digital_tiltmeter_zabbix/assets/16738424/4b84db25-066b-43fc-a19f-c36d25a4a728)

## Power Supply Options

There is a way to provide power to the tiltmeter:

  * Connect the 12V DC adapter to the tiltmeter jack.

**_It is recommended to verify the polarity of the jack (- ring and + center)._**

## Pin Layout
![Pinout-tiltmeter.png](https://github.com/rotoapanta/digital_tiltmeter_zabbix/assets/16738424/a8703cc0-d72a-41af-a456-22ba8f73b432)


# Instructions

1. Install Anaconda.

2. Create a new environment with python 3.10.

   ```bash
   conda create --name tiltmeter_zabbix_env python=3.10
   ```

3. Install pyserial library.

   ```bash
   pip install pyserial
   ```

4. Install py-zabbix library.

   ```bash
   pip install py-zabbix
   ```
5. Check tiltmeter data frame with a hyperterminal.

   ```bash
   +398.1, -12.4, 24, N234
   ```
6. Insert into the server's crontab to run periodically.
   ```bash
   chmod +x run_tiltmeter_zabbix.sh
   ```
   
   ```bash
   crontab -e
   ```
   
   ```bash
   * * * * * /home/rotoapanta/script/run_tiltmeter_zabbix.sh
   ```
## Environment Variables

To run this project, you will need to add the IP address of the Zabbix server to the `configuration.ini file.

`[zabbix_server]`

`ip=XXX.XXX.XXX.XXX`

`port=10051`

## Change Log

* Revision: 1.1 - Code cleaned.
* Revision: 1.0 - Initial commit

## Running Tests

To run tests, run the following command

```python
  ampy --port /dev/ttyUSB0 run network.py
```

## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```

## Feedback

If you have any feedback, please reach out to us at robertocarlos.toapanta@gmail.com

## Support

For support, email robertocarlos.toapanta@gmail.com or join our Discord channel.

## License

[GPL v2](https://www.gnu.org/licenses/gpl-2.0)

## Autors
- [@rotoapanta](https://github.com/rotoapanta)

## More Info

* [Zabbix Sender](https://www.zabbix.com/documentation/4.0/en/manual/concepts/sender)
* [Zabbix Handy Tips: Collect and send custom metrics with Zabbix sender](https://www.youtube.com/watch?v=AWJgEHLOHe0)
* [Official documentation for py-zabbix](https://py-zabbix.readthedocs.io/en/latest/)
* [GitHub py-zabbix](https://github.com/adubkov/py-zabbix)

## Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/roberto-carlos-toapanta-g/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/rotoapanta)
