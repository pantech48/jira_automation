""" Main module for generating report """
import pandas as pd

from config_parser import input_config, generate_json_config
from jira_app import create_report_table
from config import Config


def main():
    """Main function for generating report"""
    print("Generating json config file...")
    generate_json_config(Config.INPUT_CONFIG_JSON, input_config)
    with pd.ExcelWriter(Config.REPORT_FILE_NAME, engine='xlsxwriter') as excel_report:
        for main_ticket, sheet_name in input_config["MAIN_TICKETS"].items():
            print(f"===============================\n"
                  f"Processing main ticket {main_ticket}"
                  f" ({round((list(input_config['MAIN_TICKETS']).index(main_ticket)) / len(input_config['MAIN_TICKETS']) * 100, 1)}%)"
                  f"\n===============================")
            excel_report.book.add_worksheet(sheet_name)
            report_table = create_report_table(main_ticket)
            report_table.to_excel(excel_report, sheet_name=sheet_name, index=False)

            workbook = excel_report.book
            worksheet = excel_report.sheets[sheet_name]

            # Set row height for headers
            worksheet.set_row(0, 30)

            # Set headers format
            header_format = workbook.add_format(Config.HEADER_FORMAT)

            for col_num, value in enumerate(report_table.columns.values):
                worksheet.write(0, col_num, value, header_format)

            # Set cells format
            for row_num, row_data in enumerate(report_table.values):
                color = Config.LIGHT_BLUE if row_num % 2 == 0 else Config.LIGHTER_BLUE
                for column, data in enumerate(row_data):
                    if column == Config.HEADERS["History"]:
                        cell_format = workbook.add_format(Config.cell_format(color))
                        worksheet.write(row_num + 1, column, data, cell_format)
                    else:
                        cell_format = workbook.add_format(Config.cell_format(color))
                        worksheet.write(row_num + 1, column, data, cell_format)

            # Set columns width
            worksheet.set_column('A:A', Config.COLUMNS_WIDTH["Summary"])
            worksheet.set_column('B:B', Config.COLUMNS_WIDTH["Status"])
            worksheet.set_column('C:C', Config.COLUMNS_WIDTH["Labels"])
            worksheet.set_column('D:D', Config.COLUMNS_WIDTH["History"])

            # Freeze the first row.
            worksheet.freeze_panes(1, 0)
        print(f"Report was successfully created in {Config.REPORT_PATH}")


if __name__ == "__main__":
    main()
