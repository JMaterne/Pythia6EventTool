# A python tool for analysing Pythia6 event records

## Overview

This repository provides a python tool for exploring and analysing Pythia6 (https://www.pythia.org/pythia6/) event files.

## Key Features

This library contains implementations for reading and analysing Pythia6 event files in an object oriented way. 
src/utils.py includes some additional functions for analysing the events, which can be used as a starting point for writing your own functions based on this library.
Below is a summary of the core classes included in this implementation:

### core.EventRecord
A class storing all the information for a single event, similar to the event header in Pythia6 event files but including additional utility functions.
The associated track records can be loaded dynamically from the EventRecord object.

### core.TrackRecord
A class storing single track records for a Pythia6 event and additional utility functions.

## Example Usage

Check out the examples/ directory for some use cases.

---

For questions or contributions, feel free to submit an issue or pull request in the GitHub repository.

## How to install

If you are using pip you can use the following command to install the package:

#### python -m pip install -e PATH/TO/Pythia6EventTool
