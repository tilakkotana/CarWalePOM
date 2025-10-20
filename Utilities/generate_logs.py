import logging
from pathlib import Path

file_path=Path.cwd().parent/'Logs/logs_info.log'
def get_logs():
    for i in logging.root.handlers[:]:
        logging.root.removeHandler(i)
    logging.basicConfig(
        filename=file_path,
        filemode='a',
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - Line:%(lineno)d - %(message)s"
    )
    return logging.getLogger()
