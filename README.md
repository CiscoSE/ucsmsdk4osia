# uscmsdk4osia

*UCSM SDK for Operational Status Inquiry Assistant*

---

## Motivation

The objective of the Operational Status Inquiry Assistant is based on the computer interfaces found on Star Trek. Provides the foundation to build code that queries devices to extract data, calculate information, and format information to be used as answers to operational questions.

The goal of this code is to develop a set of functions that can be used across different user interfaces like Amazon's Alexa and Ciscos's Webex Teams.

## Show Me!

The intention of this code is to query a UCSM system and retrieve the number of Locator LEDs that are on, off, and calculated the total % of Locator LEDs that are on.  This provide validation that routines can be defined that extract data and then provide valid information.

This code requires the DevNet Intersight sandbox.  And specifically queries UCSM 10.10.20.40 using the DevNet provide admin/password.  Future variants of this code will allow for specification of the UCSM IP, User, and Password.

Example -

      python ucsmsdk4osia.py

Returns -

      6 6 50.0 %

      This means that 6 servers are off, 6 servers are on, and 50% are available

## Features

- Count the number of servers that are on/off and total % currently available

## Technologies & Frameworks Used

Python 3, UCSMSDK, DevNet Intersight Sandbox

**Cisco Products & Services:**

- Unified Compute System Manager
- DevNet

**Third-Party Products & Services:**

- Apache License, Version 2.0 (the "License")

**Tools & Frameworks:**

- DevNet Intersight Sandbox
- GitHub
- UCSM Software Development Kit for Python

## Usage

Simply install the UCSM SDK and then execute: python ucsmsdk4osia.py

## Installation

1. Install the UCSMSDK
    pip install ucsmsdk

2. execute uscmsdk4osia.py from a python shell




## Authors & Maintainers

People responsible for the creation and maintenance of this project:

- Jeff Barg <jbarg@cisco.com>

## Credits

UCSM SDK code samples on GitHub

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
