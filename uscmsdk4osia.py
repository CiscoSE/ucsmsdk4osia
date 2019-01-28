#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""uscmsdk4osia Console Script.

Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Jeff Barg"
__email__ = "jbarg@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"

# Declaration and setting the default values for variables
blade_tot = 0       # Counter for the Total number of blades in the system
blade_off  = 0      # Counter for the number of blades that have their LED off
blade_on   = 0      # Counter for the number of blades that have their LED on


# Use the UCSM SDK to connect to the desired UCSM System
from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.40", "ucspe", "ucspe")

# Specify the Classes that will be needed to get the DATA
# class ComputeBlade provides the dn for the compute resource
# class ComputeRackUnit provides the data for a specific blade
compute_resources = handle.query_classids("ComputeBlade", "ComputeRackUnit")

# For every compute blade in the system query each blade to
# get the status of the Locator lED
# Increment blade_tot to count each blade
# Increment blade_on if the LED Locator light is on
# Increment blade_off if the LED Locator light is off
# Calculate the total percentage of LED Locator lights that ARE
for compute_resource_class in compute_resources:
    for compute_resource in compute_resources[compute_resource_class]:
        leds = handle.query_children(in_dn=compute_resource.dn, class_id="equipmentLocatorLed")
        if(len(leds)>0):
            testtype = leds[0].oper_state
            blade_tot = blade_tot + 1
            if(testtype=='on'):
                blade_on = blade_on + 1
            else:
                blade_off = blade_off + 1
        else:
            exit()

# At the completion of the for loop, print the values of LEDs that are off, on AND
# the total percentage of Locator LEDs that are on
    print(blade_off, blade_on, blade_on/blade_tot*100,'%')

handle.logout()
