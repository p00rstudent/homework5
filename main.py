import argparse
import json
from pathlib import Path

from handlers import LogHandler
from src.row_handler import TypeCountHandler, TopFreqIpHandler, TopSlowReqHandler

ROOT_DIR = Path(__file__).parent


def parse_args():
    params = argparse.ArgumentParser('')
    params.add_argument('--logs_dir', default=None, type=str)
    params.add_argument('--log_file', default=None, type=str)
    params.add_argument('--pattern', default='*.log', type=str)
    params.add_argument('--output', default=str(ROOT_DIR.joinpath('out.json').resolve()), type=str)
    return params.parse_args()


def main():
    args = parse_args()
    log_file = args.log_file
    logs_dir = args.logs_dir
    pattern = args.pattern
    result = parse_log_files(get_dir_log_files(logs_dir, pattern), log_file)
    with Path(args.output).open('w') as f:
        json.dump(result, f, indent=4)
    print(result)


def get_dir_log_files(logs_dir: str, pattern: str = '*'):
    if logs_dir is None:
        return []
    return Path(logs_dir).rglob(pattern)


def parse_log_files(log_files, log_file: str = None):
    handler = LogHandler(handlers=[TypeCountHandler(), TopFreqIpHandler(), TopSlowReqHandler()])
    for log_file in log_files:
        with log_file.open('r') as f:
            for line in f:
                handler.process(line)
    if log_file and Path(log_file).is_file():
        with Path(log_file).open('r') as f:
            for line in f:
                handler.process(line)
    return handler.json


main()
