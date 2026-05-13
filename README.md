# Project Notes
## Step-1: Clone the repo and create a template.py file.
The template.py file has all the necessary codes that is required to create a modular project structure. It has logging has well, to track the real time changes that have been made using log.info file in case of failure.

## Step-2: Fill the requirements.txt file and the setup.py file.
The requirements.txt file consists of all the packages that are needed to be imported in order to run the code properly. The setup.py file consists of code that makes the project behave like an installable Python package.

## Step-3: Created logging, exception handling and utils module.
Added code for handling the logging files and exception handling. Also added most frequently used methods to the utils module so that it can be used multiple times from anywhere inside the code, instead of being called everytime for coding.

## Step-4: Create Workflows.
1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the dvc.yaml