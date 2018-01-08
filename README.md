# This is a simulator that send device report to its management application.

## Reference
   About Lightweight M2M Resource Model please check [here](https://www.iab.org/wp-content/IAB-uploads/2016/03/OMA_LightweighM2M_Resource_Model_Summary.pdf)

## structure

- `start.py`: 		    Main script to start the simulator.
- `conf.json`:		    Configuration in json to describe your resource, device, application and their relationship.
- `iotreportsimulator`:	Sub scripts to create data models.

## operation

    ~ How do I use it?
      1. Setup dependencies:
         pip install requests

      2. configuration:
         refer to example conf.json

      3. run:
         python start.py

    ~ Logging?
      The default log is stored at the process root folder at report_data_simulator.log
