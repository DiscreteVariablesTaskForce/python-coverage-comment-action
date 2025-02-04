import logging

from coverage_comment import github

LEVEL_MAPPING = {
    50: "error",
    40: "error",
    30: "warning",
    20: "notice",
    10: "debug",
}


class GitHubFormatter(logging.Formatter):
    def format(self, record):
        log = super().format(record)
        level = LEVEL_MAPPING[record.levelno]

        return github.get_workflow_command(command=level, command_value=log)
