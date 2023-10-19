import json
import logging
from argparse import ArgumentParser

from typing import List


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
            imps = json.load(imp_json)
            perms = generate_permutations(imps)

        # If there's anything to run, prepare the results folder

        # Interate through each test and permutation set

    @staticmethod
    def generate_permutations(imps) -> List[...]:
        """ For each implementation work out the list of permutations of tests
        to run.
        """
        # TODO: Handle WebTransport vs Raw
        # TODO: Relay Patterns?
        permutations = []
        for s in imps:
            if not imps[s]["enabled"] or not imps[s]["sender"]:
                continue

            for c in imps:
                if not imps[c]["enabled"] or not imps[c]["consumer"]:
                    continue
                permutations.append([s, c])

        return permutations
