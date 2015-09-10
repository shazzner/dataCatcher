# BizeeBox

A smart Internet-of-Things data accumulator

## CONTACT

Chris Hardee <shazzner@gmail.com>

Please file bugs/features/help in the issue tracker

## TODOS

### General

* Write a detailed install guide
* General information in the readme
* Links to webpage

### Look & Feel

* Homepage
  * Should display updates to modules/app-recommends
  * Display any alerts
  * Links to buy more modules

* About
  * Detailed About page
  * Help page
  * Contribute Page

* Style
  * Should have a nicer visual style

### Architecture

* Dynamically add apps
  * Need a /modules app that will pull down a list of modules
  * Can add/remove modules
  * Django handles additional apps

* App -> Module hooks
  * Modules (hardware) should be separate from Apps (software)
  * Each Module 'hooks' into one or many apps
    For example a PIR module that hooks into a conversion app and a security app

### Modules

* Configuration
  * Each module will have a configuration model
    You can configure module specific items, like Fahrenheit or Celsius for a temperature module

* Programming
  * Each module will need to 'sync' with the BizeeBox
    Either done with direct programming via serial cable or only update wifi information
  * Script to program the module

* ESP8266
  * Need to write code to capture data per sensor
  * Connect to wifi and send data via rest api
  * Optionally receive information (output sensor)

* Additional Modules
  * (wireless) temp sensor
  * PIR sensor
  * CO2 sensor
  * moisture sensor
  * CO2 sensor
  * Flame sensor
  * (Output) Relay sensor

### App

* Module 'hooks'
  * Each module will send an update to the bizeebox via rest api
  * Each module should be programmed with a unique apikey
  * After receiving data, should update each app it's 'hooked' into

* Recommends
  * Each app should have a /recommends page
  * This will analyze the data and give recommendations
  * Should pull from a recommends.py
  * Should be update able

