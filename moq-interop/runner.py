import logging
from argparse import ArgumentParser


class MoqInteropRunner:

  @staticmethod
  def main() -> None:
    logging.info("Runner started")

    parser = ArgumentParser(prog="moq-interop-runner")
    parser.add_argument("-c", "--config", type=str, required=True,
                        help="Configuration file")
    args = parser.parse_args()
