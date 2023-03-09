import pandas as pd
import json
import os

INPUT_FILE_NAME = "ExampleInputFile.xlsx"
INPUT_FILE_PATH = os.path.join(os.path.dirname(__file__), INPUT_FILE_NAME)
CONFIG_FILE_NAME = "input_file_config.json"


def parse_main_tickets(path):
    excel_obj = pd.read_excel(path)
    main_tickets_table = excel_obj.iloc[:2, 1:9]
    main_tickets_dict = {j[0]: j[1] for _, j in main_tickets_table.items()}
    return {"MAIN_TICKETS": main_tickets_dict}


def parse_statuses(path):
    excel_obj = pd.read_excel(path)
    statuses_table = excel_obj.iloc[5:36, :3]
    statuses_dict = {j[0]: j[1] for _, j in statuses_table.iterrows()}
    return {"STATUSES": statuses_dict}


config = {**parse_main_tickets(INPUT_FILE_PATH), **parse_statuses(INPUT_FILE_PATH)}

if __name__ == "__main__":
    with open(CONFIG_FILE_NAME, "w") as f:
        json.dump(config, f, indent=4)