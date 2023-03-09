import pandas as pd
from pathlib import Path

from config_parser import config
from utils import create_report_table

REPORT_NAME = "report.xlsx"
REPORT_PATH = Path(__file__).parent / REPORT_NAME


def main():
    with pd.ExcelWriter(REPORT_NAME, engine='xlsxwriter') as excel_report:
        for main_ticket, sheet_name in config["MAIN_TICKETS"].items():
            # after each main ticket print how much percent of the report is already done
            print(f"===============================\n"
                  f"Processing main ticket {main_ticket}"
                  f" ({round((list(config['MAIN_TICKETS']).index(main_ticket)) / len(config['MAIN_TICKETS']) * 100, 1)}%)"
                  f"\n===============================")
            excel_report.book.add_worksheet(sheet_name)
            create_report_table(main_ticket).to_excel(excel_report, sheet_name=sheet_name, index=False)
        print(f"Report was successfully created in {REPORT_PATH}")


if __name__ == "__main__":
    main()


