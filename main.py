from utils.static_typing import typechecked
import sys

from App.app import app


@typechecked
def main(argv: list[str]):
  app(argv)

main(sys.argv[1:])
