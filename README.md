# DRUMKIt-InUr-POCKET
This is a beat-making machine for improv rhythms on the go!

<img width="1182" height="857" alt="image" src="https://github.com/user-attachments/assets/e98db209-e3a4-43d7-8e08-00faadef7038" />

## What is it?

This is a Music machine PCB for week three of Half-Life HackClub! It contains various inputs for music making, focusing mainly on a Drum Kit with extra inputs such as buttons and rotary encoders. I am using the Waveshare-ESP32-S3-Zero as the brains, connected to the inputs and my custom capacitive touch Drum Kit.

## Parts:
* Waveshare ESP32-S3-zero
* 2 x Rotary Encoders
* 3 x Buttons
* 7 x Capacitive touch locations

## How was it made?

I used the beginner [MIDI Project](https://github.com/KaiPereira/MIDI-Keypad/blob/master/README.md) as a starting point, and put the components recommended in my board too. What I wanted to change up was the Piano, so I made it a drum Kit instead!

## Project status

Currently, PCB files are complete, and I am waiting for the project to be approved and shipped in week 8 of half-life!

## Bill of Materials (BOM)

| Part | What it's for | Qty | Unit | Total | Vendor | Link |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **DHT11 Digital Temp & Humidity Sensor Module** | Environmental Sensor For Pet | 1 | $2.31 | $2.31 | AliExpress | [View Link](https://www.aliexpress.com/item/1005001234567890.html) |
| **ESP 32 - C3 Mini** | For controlling the brain | 1 | $5.52 | $5.52 | AliExpress | [View Link](https://www.aliexpress.com/item/1005007890123456.html) |
| **Resistors** | Resistors for project | 1 | $1.19 | $1.19 | AliExpress | [View Link](https://www.aliexpress.com/item/1005003456789012.html) |
| **Switches** | For switches input to pet | 1 | $1.19 | $1.19 | AliExpress | [View Link](https://www.aliexpress.com/item/1005005678901234.html) |
| **MPU6050 Module 6 Axis IMU** | For the motion control | 1 | $1.66 | $1.66 | AliExpress | [View Link](https://www.aliexpress.com/item/1005006789012345.html) |
| **LEAFIE PCB** | PCB for project | 1 | $6.10 | $6.10 | JLCPCB | [View Link](https://jlcpcb.com) |

* **Parts Subtotal:** $17.97
* **Tax & Shipping:** $8.93
* **Total Estimated Cost:** **$26.90**

  
## Repository contents

- `PCB/` - KiCad source files and fabrication exports
- `Firmware/` - Arduino IDE starter sketch
