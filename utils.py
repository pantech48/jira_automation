""" This module contains utility functions for the report generator. """
import pandas as pd
from jira import JIRA

from config_parser import input_config, app_config

token = app_config["PAT_token"]
server = app_config["jira_instance"]


def get_main_tickets():
    """
    Returns list of main tickets from config file
    :return: list of main tickets
    """
    main_tickets_data_frame = pd.DataFrame.from_dict(input_config["MAIN_TICKETS"], orient="index", columns=["Report Tab name"])
    main_tickets = main_tickets_data_frame.index.values
    return main_tickets


def get_all_subtasks(issue: str) -> list:
    """
    Returns list of all subtasks for the given issue.
    :param issue: Jira issue key
    :return: list of subtasks
    """
    jira = JIRA(server=server, token_auth=token)
    subtasks = [subtask.key for subtask in jira.issue(issue, expand="subtasks").fields.subtasks]
    return subtasks


def get_subtask_data(issue: str) -> dict:
    """
    Returns dictionary with subtask data
    :param issue: Jira issue key
    :return: dictionary with subtask data
    """
    jira = JIRA(server=server, token_auth=token)
    issue_object = jira.issue(issue, fields='summary, status, labels, comment')
    status_mapping = input_config["STATUSES"]
    summary = issue_object.fields.summary
    if not issue_object.fields.labels:
        labels = ''
    else:
        labels = ', '.join(issue_object.fields.labels)
    try:
        status = status_mapping[issue_object.fields.status.name]
    except KeyError:
        status = issue_object.fields.status.name
    comments = ''
    for comment in jira.comments(issue, expand="renderedBody"):
        comments += comment.renderedBody
        comments += '\n'

    return {
        issue: {
            "summary": summary,
            "status": status,
            "labels": labels,
            "comments": comments
        }
    }


def create_report_table(main_ticket: str) -> pd.DataFrame:
    """
    Returns pandas DataFrame with report table
    :param main_ticket: Jira issue key
    :return: pandas DataFrame with report table
    """
    headers = ['Summary', 'Status', 'Labels', 'History']
    table_data_frames = []
    subtasks = get_all_subtasks(main_ticket)
    subtasks_count = len(subtasks)
    for index, subtask in enumerate(subtasks, start=1):
        print(f"Processing subtask {index} of {subtasks_count} ({round(index / subtasks_count * 100, 1)}%)")
        data = get_subtask_data(subtask)
        summary = data[subtask]['summary']
        status = data[subtask]['status']
        labels = data[subtask]['labels']
        comments = data[subtask]['comments']
        table_data_frame = pd.DataFrame({'Summary': [summary],
                                         'Status': [status],
                                         'Labels': [labels],
                                         'History': [comments]})
        table_data_frames.append(table_data_frame)
    concatenated_table_data_frame = pd.concat(table_data_frames, ignore_index=True)
    return concatenated_table_data_frame
