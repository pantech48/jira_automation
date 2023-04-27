# JIRA Comments Collector

## Usage

To use this application, follow these steps:
1. Go to https://luxproject.luxoft.com/jenkins/job/SIR/job/SIR_Jira_Comments_Collector/
2. Click on "Build with Parameters" at the left menu
3. Here you have option to download input file with configurable parameters. Click on "Choose File" -> "Build"
4. If you want to use default parameters, just skip it and click on "Build" button.
5. Wait until build is finished. You can check build status by clicking on "Status" at the left menu.
6. Upon finishing build, you can download output file with comments. Click on "report.xlsx" under "	Last Successful Artifacts" article.
7. Report generates automatically every day at midnight.

## Configuration

The input configuration file (input.xlsx) contains the main tickets and statuses required for generating the report. You can edit the input file as needed to customize the report.

### Input File Format

The input file should follow this format:

- Main tickets: A list of JIRA ticket IDs, starting at row 2, column B.
- Report Tab names, mapped with main tickets: A list of tab names, starting at row 3, column B. The tab names should be unique and should not contain any special characters.
- Default status mapping: A table containing the default status mappings, starting at row 7, columns A and B.
- State status mapping: A table containing the state-specific status mappings, starting at row 7, columns D and E.

### Updating the Input File

To update the input file, simply open it in Excel or any other spreadsheet software, edit the values as needed, save the changes and upload the file, as described in the Usage section, stage 3.


## For Developers

This application is built with Python and requires dependencies, which are listed in the `requirements.txt` file.

To maintain this application, ensure that all dependencies are up-to-date and compatible with the latest version of Python.

### Project Structure

The project consists of the following main files:

- `__init__.py`: An empty file that marks the directory as a Python package.
- `config.py`: Contains configuration settings for the application. (e.g. input file settings, JIRA API settings, etc.)
- `config_parser.py`: Parses the input configuration file and creates a dictionary of the data. Also creates `input_config.json` with mapping data.
- `.gitignore`: Contains files and folders that should be ignored by Git.
- `requirements.txt`: Contains a list of dependencies for the application.
- `jira_app.py`: Contains utility functions for interacting with the JIRA API.
- `main.py`: The entry point of the script that generates the Excel report file.
- `Jenkinsfile`: Contains the Jenkins pipeline configuration.
