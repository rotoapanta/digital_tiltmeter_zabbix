# <p align="center">Digital tiltmeter and zabbix 

<p align="center">This project is based on a Digital Inclinometer and a zabbix server.</p>

##

![Python 3.9](https://img.shields.io/badge/Python-3.9-blue.svg)
[![GitHub issues](https://img.shields.io/github/issues/rotoapanta/digital_tiltmeter_zabbix
)](https://github.com/rotoapanta/digital_tiltmeter_zabbix/issues)
![GitHub repo size](https://img.shields.io/github/repo-size/rotoapanta/digital_tiltmeter_zabbix
)
![GitHub last commit](https://img.shields.io/github/last-commit/rotoapanta/digital_tiltmeter_zabbix
)
![GitHub commit merge status](https://img.shields.io/github/commit-status/rotoapanta/prueba2/main/6a500cc65d)
[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/gpl-2.0)
![Discord](https://img.shields.io/discord/996422496842694726)
[![Discord Invite](https://img.shields.io/badge/discord-join%20now-green)](https://discord.gg/pSAp2qXe)
![GitHub forks](https://img.shields.io/github/forks/rotoapanta/ESP32-Blinking-RGB-Led?style=social)

# Contents

  * [Getting started](#getting-started)
    * [Getting started with Tiltmeter and Zabbix](#getting-started-with-tiltmeter-and-zabbix)
    * [Requirements](#requirements)
    * [Description of Components](#description-of-components)
    * [Power Supply Options](#power-supply-options)
    * [Pin Layout](#pin-layout)
  * [Instructions](#instructions)
  * [Environment Variables](#environment-variables)
  * [Running Tests](#running-tests)
  * [Usage/Examples](#usage-examples)
  * [Feedback](#feedback)
  * [Support](#support)
  * [License](#license)
  * [Autors](#autors)
  * [Links](#links)

# Getting started

## Getting started with Tiltmeter and Zabbix

The digital inclinometer is a high-precision instrument designed to measure very small changes in the horizontal plane. In the context of volcanoes, an inclinometer is used to measure very small changes in the horizontal plane of the terrain around the volcano. These changes can be indicative of volcanic activity, such as deformation of the terrain caused by inflation or deflation of magma beneath the volcano. This tutorial will guide you to obtain data from the Tiltmeter (tangential axis, radial axis, and temperature) to Zabbix.

Let’s get started!
 
## Requirements

  * [Install py-zabbix 1.1.7](https://pypi.org/project/pyzabbix/)
  * [Install pyserial 3.5](https://pypi.org/project/pyserial/)
  * Digital Tiltmeter Model D711-A.
  * USB to Serial converter cable.
  * Power Supply Adapter 12 VDC.
  * Computer running Thonny on Windows, Linux or macOS (in this case macOS is used)
  * 

## Components Description

[![29986-15905531.jpg](https://i.postimg.cc/C58R1Dx6/29986-15905531.jpg)](https://postimg.cc/rR8VZDWS)

## Power Supply Options

There are three mutually exclusive ways to provide power to the board:

  * Micro-USB port, default power supply

**_It is recommended to use the first option: Micro-USB Port._**

## Pin Layout
[![Pinout-tiltmeter.png](https://i.postimg.cc/cL0jLmyk/Pinout-tiltmeter.png)](https://postimg.cc/N5CbNR0R)

# Instructions

* Install MicroPython on the ESP32, you can use [this tutorial](https://lemariva.com/blog/2017/10/micropython-getting-started);

* Or you can install using Tonny software, as follows:

1. Open the Thonny software, then go to the menu bar and click on **Tools**, then click **Manager plug-ins**.

![tonny-plug-ins-1](https://user-images.githubusercontent.com/16738424/193680097-2df312a8-6a18-45f4-b775-6c25d1d514ab.png)

2. Then search for the **esptool** plug-ins and click install. In this case, the plug-ins are already installed.

![tonny-plug-ins-2](https://user-images.githubusercontent.com/16738424/193679929-40adef10-f0d5-4b5e-a58a-1a5f99f80b8f.png)

![tonny-plug-ins-3](https://user-images.githubusercontent.com/16738424/193679194-e8c67aca-759b-40c7-ab71-3dfb24780163.png)


6. Finished uploading the firmware is ready to go!
![port-firmware-done](https://user-images.githubusercontent.com/16738424/194117896-ecffe4a5-b5f3-44dd-9f22-7ba7b48ac3dd.png)

* Create the files `network.py` and `wifi_credentials.py`

* Modify the `wifi_credentials.py` file if you want to:
  * The code line
  ```python
  ssid = 'YOUR_SSID'  # your network SSID (name)`

  password = 'YOUR_SSID_PASSWORD' # your network password (use for WPA, or use as key for WEP)
  ```

## Changelog

* Revision: 1.1 - Code cleaned.
* Revision: 1.0 - Initial commit

## Environment Variables

To run this project, you will need to add the following environment variables to your `wifi_credentials.py` file

`ssid = 'YOUR_SSID'  # your network SSID (name)`

`password = 'YOUR_SSID_PASSWORD' # your network password (use for WPA, or use as key for WEP)`

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

[MIT](https://choosealicense.com/licenses/mit/)

## Autors
- [@rotoapanta](https://github.com/rotoapanta)

More Info:
---------
* [Zabbix Sender](https://www.zabbix.com/documentation/4.0/en/manual/concepts/sender)
* [MicroPython Tutorial](https://lemariva.com/blog/2017/10/micropython-getting-started)
* [NeoPixeles](https://learn.adafruit.com/esenciales-para-circuitpython/neopixeles-circuitpython)
* [Espressif IoT Development Framework](https://github.com/espressif/esp-idf)

## Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/roberto-carlos-toapanta-g/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/rotoapanta)
