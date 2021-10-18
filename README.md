# FIDO2 

[toc]

## TODO:

- [x] setup usb stick with opensk
- [x] test FIDO2 on normal websites
- [ ] setup local FIDO2 authentication flow

## structure of fido2 
![](https://i.imgur.com/nsBJaOn.png)
> [color=#EE0000]<font color=red>the target is to find a usable client api </font><br>

## things about flask




## setup a fido2 client server

### demo project in webauthn.io with java and google web app engine
![](https://i.imgur.com/DQbiEJ9.png)
This test server is from https://github.com/google/webauthndemo
(maven appengine:devserver)

use different usb stick to test the authentication 
use google web app engine and java as dev tools.

### demo project in webauthn.io with python and flask

resources:
[flask tutorial](https://flask.palletsprojects.com/en/2.0.x/)
[github repo page](https://github.com/duo-labs/py_webauthn)
[another flask tutorial](https://ithelp.ithome.com.tw/articles/10222132)

### flask guideline:
an easy sample of flask:
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return 

app.run()
```

```app = Flask(__name__)```: initialize the Flask object
```@app.route("/")```: create

## Demo

### demo in webauthn.io 
{%youtube CCfQYdA8m-U %}

### demo with test google account
{%youtube q0HzDzx-3_k %}

    

## memo
info of the old version uf2 bootloader

> UF2 Bootloader 0.2.13-42-g82464f9-dirty lib/nrfx (v2.0.0) lib/tinyusb (legacy-1500-g23df777b) s140 6.1.1
> Model: nRF52840 MDK USB Dongle
> Board-ID: nRF52840-Dongle-v1
> Date: Feb  3 2020

info of the folder of MDK-DONGLE
> ytlin@ytlin-ubuntu-Laptop:/media/ytlin/MDK-DONGLE$ ls
CURRENT.UF2  INDEX.HTM  INFO_UF2


## Resources
[getting started with opensk](https://wiki.makerdiary.com/nrf52840-mdk-usb-dongle/opensk/getting-started/)
[nRF52840 MDK USB Dongle](https://github.com/makerdiary/nrf52840-mdk-usb-dongle/)
[opensk by makerdiary](https://github.com/makerdiary/opensk)
[opensk by google](https://github.com/google/opensk)
[how to resolve rustup doesn't allow 'if' in constant](https://github.com/rust-lang/rust/issues/49146)
[FIDO2 test website](https://webauthn.io/)
[installation guide of google opensk](https://github.com/google/OpenSK/blob/stable/docs/install.md)
[make a new  uf2 bootloader](https://github.com/adafruit/Adafruit_nRF52_Bootloader#making-your-own-uf2)
[virtual-authenticators-tab](https://github.com/google/virtual-authenticators-tab)

[How to Setup FIDO2 for ASP.NET Passwordless Authentication](https://www.youtube.com/watch?v=8bxpzx6072A)
[setup FIDO2 server that supply FIDO2 authentication](https://github.com/StrongKey/fido2)
[Standalone Installation - strongkey fido2 server(SKFS)](https://docs.strongkey.com/index.php/skfs-home/skfs-installation/skfs-installation-standalone)
[getting started for developer - fido2 alliance](https://fidoalliance.org/developers/)
[another way to setup a fido2 server](https://github.com/line/line-fido2-server)
[setup fido2 client](https://github.com/VinCSS-Public-Projects/FIDO2Client)
[maven server tutorial](https://www.runoob.com/maven/maven-tutorial.html)

## meeting record
### 8/13 
hint:
build script with compile binary file 
try different branch

### 8/20
installation guide

hint:
build the file with deploy.py in google's opensk repo
than transfer it to hex file with makerdiary's opensk repo

keywords:
openocd(?)

### 8/27
deploy.sh in makerdiary's repo -> jlink emulator
deploy.py in google's repo -> generate hex file 

* trying to build up file with deploy.py with parameters
> `--board=nrf52840_dongle  --programmer=none --opensk `

(though I knew it is a diff board from mdk_usb_dongle)

![](https://i.imgur.com/r0H5f46.png)
Generating all-merged HEX file: target/nrf52840_dongle_merged.hex
can't flash merged uf2 file into usb stick:

---

## problems
### setup.sh failed (build fail with all branches) # [solution found](https://github.com/google/OpenSK/issues/371) : using branch backport_369
> result: setup.sh is runable
>
### No emulators connected via USB (JLink emulator)
![](https://i.imgur.com/hE4d3Fu.png)

---
### flash uf2 file into the usb stick:
* can't flash uf2 file into usb stick
> not sure the problems is about the conv.py(i tried two diff erent file), generated hex file, uf2 bootloader, or the usb sitck itself 

* sudo: adafruit-nrfutil: command not found
> https://github.com/platformio/platform-nordicnrf52/issues/65
> https://github.com/platformio/platform-nordicnrf52/issues/47

* flash other uf2 file from makerdiary github repo:
> [color=#90EE90]https://github.com/makerdiary/nrf52840-mdk-usb-dongle/blob/master/firmware/OpenSK/opensk_nrf52840_mdk_usb_dongle_gece14d7.uf2
> <font color=red>__*success!!*__</font><br>

> [demo video](https://hackmd.io/i9C4jxGCQl6UDexAl3IsnA?both#the-demo-video)
---
### update uf2 bootloader of the usb stick:

> origin .zip file from makerdiary document:
> https://github.com/makerdiary/nrf52840-mdk-usb-dongle/blob/master/firmware/uf2_bootloader/uf2_bootloader-0.2.13-44-gb2b4284-nosd.zip

* `sudo nrfutil dfu serial -pkg uf2_bootloader-0.2.13-44-gb2b4284-nosd_signed.zip -p /dev/ttyACM0`
![](https://i.imgur.com/nKZkNp9.png)
* `sudo adafruit-nrfutil dfu serial -
pkg uf2_bootloader-0.2.13-44-gb2b4284-nosd_signed.zip -p /dev/ttyACM0`
![](https://i.imgur.com/IG1KwrJ.png)

> with new .zip file: 
> https://github.com/makerdiary/nrf52840-mdk-usb-dongle/raw/master/firmware/open_bootloader/nrf52840_mdk_usb_dongle_open_bootloader_v1.2.0.uf2.zip

* `sudo adafruit-nrfutil dfu serial -pkg nrf52840_mdk_usb_dongle_open_bootloader_v1.2.
0.uf2.zip -p /dev/ttyACM0`
(TypeError: \_\_init\_\_() got an unexpected keyword argument 'dfu_version')
![](https://i.imgur.com/MvFXC4w.png)

---