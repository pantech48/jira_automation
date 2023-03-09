"""Module for parsing the input excel file and creating a dictionary of the data"""
import pandas as pd
import json
import os

APP_CONFIG_FILE_NAME = "app_config.json"

with open(APP_CONFIG_FILE_NAME, "r") as f:
    app_config = json.load(f)

INPUT_FILE_NAME = app_config["input_file_name"]
INPUT_FILE_PATH = os.path.join(os.path.dirname(__file__), INPUT_FILE_NAME)


def parse_main_tickets(path: str) -> dict:
    """
    Function for parsing the main tickets from the input excel file
    :param path: path to the input excel file
    :return: dictionary of the main tickets
    """
    excel_obj = pd.read_excel(path)
    main_tickets_table = excel_obj.iloc[app_config["main_tickets_starting_row"]:app_config["main_tickets_ending_row"], app_config["main_tickets_starting_column"]:]
    main_tickets_dict = {j[0]: j[1] for _, j in main_tickets_table.items()}
    return {"MAIN_TICKETS": main_tickets_dict}


def parse_statuses(path: str) -> dict:
    """
    Function for parsing the statuses from the input excel file.
    It parses two tables: default statuses and states statuses.
    State statuses have higher priority.

    :param path: path to the input excel file
    :return: dictionary of the statuses
    """
    default_mapping = pd.read_excel(path,
                                    header=None,
                                    usecols=app_config["default_status_mapping_columns"],
                                    skiprows=app_config["default_status_mapping_starting_row"])
    state_mapping = pd.read_excel(path,
                                  header=None,
                                  usecols=app_config["state_status_mapping_columns"],
                                  skiprows=app_config["state_status_mapping_starting_row"])

    def_map_dict = {raw[1]: raw[2] for raw in default_mapping.itertuples()}
    state_map_dict = {raw[1]: raw[2] for raw in state_mapping.itertuples()}
    def_map_dict.update(state_map_dict)
    return {"STATUSES": def_map_dict}


input_config = {**parse_main_tickets(INPUT_FILE_PATH), **parse_statuses(INPUT_FILE_PATH)}


def generate_json_config(path: str, data: str) -> None:
    """
    Function for generating the json config file from the input excel file
    :param path: path to the input excel file
    :param data: dictionary with the data
    :return: None
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)






