# MQTT Server on IONOS

This project implements an MQTT server for monitoring and controlling connected IoT devices and sensors. The server communicates efficiently with both sensors and actuators using multiple versions of the MQTT protocol.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)

## Features

- Supports MQTT protocol versions 3.1, 3.1.1, and 5.0.
- Bi-directional communication between sensors and actuators.
- Backup system for MQTT messages.
- Configurable connection to any MQTT broker (local or remote IONOS server).

## Requirements

### Software Dependencies

- Python 3.8 or higher
- Required Python packages (install via `requirements.txt`):
  - `paho-mqtt`

### Hardware Requirements

- MQTT broker (e.g., Mosquitto) installed and running locally or on a remote server (such as IONOS).
