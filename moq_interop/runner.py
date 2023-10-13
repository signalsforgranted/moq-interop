import json
import logging
from argparse import ArgumentParser


class Runner:

    @staticmethod
    def main() -> None:
        logging.basicConfig(level=logging.INFO)
        logging.info("Runner started")

        parser = ArgumentParser(prog="moq-interop-runner")
        parser.add_argument("-c", "--config", type=str, required=False,
                            default="config/implementations.json",
                            help="Configuration file")
        args = parser.parse_args()

        # Generate each permutation to test
        with open(args.config) as imp_json:
            implementations = json.load(imp_json)
