import os
from pathlib import Path
import time


class Config:
    # main settings
    JIRA_INSTANCE = "https://luxproject.luxoft.com/jira/"
    PAT_TOKEN = "ODgzMTQ0NTc4NjkzOpThGMjbxpBKrvmXtnVh6R6srHsz"
    INPUT_CONFIG_JSON = "input_config.json"
    TIME_NOW = time.strftime("%Y_%m_%d_%H_%M", time.localtime())
    TIME_FORMAT_FOR_COMMENTS = "%Y-%m-%d"

    # input excel file settings
    INPUT_FILE_NAME = os.environ.get("input.xlsx", "input.xlsx") if os.environ.get("input.xlsx") else "input.xlsx"
    INPUT_FILE_PATH = os.path.join(os.path.dirname(__file__), INPUT_FILE_NAME)
    MAIN_TICKETS_STARTING_ROW = 0
    MAIN_TICKETS_ENDING_ROW = 2
    MAIN_TICKETS_STARTING_COLUMN = 1
    STATE_STATUS_MAPPING_COLUMNS = [3, 4]
    STATE_STATUS_MAPPING_STARTING_ROW = 6
    DEFAULT_STATUS_MAPPING_COLUMNS = [0, 1]
    DEFAULT_STATUS_MAPPING_STARTING_ROW = 6

    # colors
    DARK_BLUE = '#305496'
    LIGHT_BLUE = '#BDD7EE'
    LIGHTER_BLUE = '#DDEBF7'
    WHITE = 'white'

    # report file settings
    REPORT_FILE_NAME = f"report.xlsx"
    REPORT_PATH = Path(__file__).parent / REPORT_FILE_NAME
    HEADERS = {
        "Summary": 0,
        "Status": 1,
        "Labels": 2,
        "History": 3,
    }
    HEADER_FORMAT = {
                'border': 1,
                'bold': True,
                'valign': 'vcenter',
                'align': 'center',
                'bg_color': DARK_BLUE,
                'font_color': WHITE
            }
    COLUMNS_WIDTH = {
        "Summary": 50,
        "Status": 20,
        "Labels": 40,
        "History": 160,
    }

    @staticmethod
    def cell_format(color):
        return {
            'text_wrap': True,
            'valign': 'top',
            'border': 1,
            'bg_color': color,
        }

