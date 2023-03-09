""" Main module for generating report """
import pandas as pd
from pathlib import Path

from config_parser import input_config, generate_json_config, app_config
from utils import create_report_table

REPORT_NAME = app_config["report_file_name"]
REPORT_PATH = Path(__file__).parent / REPORT_NAME


def main():
    """Main function for generating report"""
    print("Generating json config file...")
    generate_json_config(app_config["input_config_json"], input_config)
    with pd.ExcelWriter(REPORT_NAME, engine='xlsxwriter') as excel_report:
        for main_ticket, sheet_name in input_config["MAIN_TICKETS"].items():
            print(f"===============================\n"
                  f"Processing main ticket {main_ticket}"
                  f" ({round((list(input_config['MAIN_TICKETS']).index(main_ticket)) / len(input_config['MAIN_TICKETS']) * 100, 1)}%)"
                  f"\n===============================")
            excel_report.book.add_worksheet(sheet_name)
            create_report_table(main_ticket).to_excel(excel_report, sheet_name=sheet_name, index=False)
        print(f"Report was successfully created in {REPORT_PATH}")


if __name__ == "__main__":
    main()


