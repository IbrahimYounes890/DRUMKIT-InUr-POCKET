# DRUMKIt-InUr-POCKET
This is a beat-making machine for improv rhythms on the go!

<img width="1182" height="857" alt="image" src="https://github.com/user-attachments/assets/e98db209-e3a4-43d7-8e08-00faadef7038" />
<img width="1076" height="852" alt="image" src="https://github.com/user-attachments/assets/b9e87fcf-9db4-41dc-9a01-766b8213d829" />


## What is it?

This is a Music machine PCB for week three of Half-Life HackClub! It contains various inputs for music making, focusing mainly on a Drum Kit with extra inputs such as buttons and rotary encoders. I am using the Waveshare-ESP32-S3-Zero as the brains, connected to the inputs and my custom capacitive touch Drum Kit.

## Parts:
* Waveshare ESP32-S3-zero
* 2 x Rotary Encoders
* 3 x Buttons
* 7 x Capacitive touch locations
* 3 x NeoPixels

## How was it made?

I used the beginner [MIDI Project](https://github.com/KaiPereira/MIDI-Keypad/blob/master/README.md) as a starting point, and put the components recommended in my board too. What I wanted to change up was the Piano, so I made it a drum Kit instead!

## Project status

Currently, PCB files are complete, and I am waiting for the project to be approved and shipped in week 8 of half-life!

## Bill of Materials (BOM)

| # | Item | Vendor | Quantity | Price (USD) |
|---:|---|---|---:|---:|
| 1 | [SK6812 MINI-E RGB LEDs (100 pcs)](https://www.aliexpress.com/w/wholesale-SK6812-MINI-E-3228-SMD.html) | AliExpress | 1 pack | $2.29 |
| 2 | [Kailh Low-Profile Choc Switches (10 pcs)](https://www.aliexpress.com/w/wholesale-Kailh-Low-Profile-Choc-Switch-1350.html) | AliExpress | 1 pack | $7.84 |
| 3 | [Waveshare ESP32-C3-Zero Development Board](https://www.aliexpress.com/w/wholesale-Waveshare-ESP32-C3-Zero.html) | AliExpress | 1 unit | $8.10 |
| 4 | [EC11 Rotary Encoders (2 pcs)](https://www.aliexpress.com/item/1005012172639966.html) | AliExpress | 1 pack | $4.88 |
| 5 | [Custom MIDI Keypad PCB](https://jlcpcb.com/) | JLCPCB | 5 pcs | $4.00 |
| | | | **PCB Shipping** | **$2.00** |

### Cost Summary

| AliExpress Items Subtotal | $30.40 |
| AliExpress Shipping | $0.00 |
| **AliExpress Estimated Total** | **$22.95** |
| JLCPCB PCB Cost | $4.00 |
| JLCPCB Shipping | $2.00 |
| **PCB Order Total** | **$6.00** |
| **Total Estimated Project Cost** | **$28.95** |

  
## Repository contents

- `PCB/` - KiCad source files and fabrication exports
- `Firmware/` - Arduino IDE starter sketch
