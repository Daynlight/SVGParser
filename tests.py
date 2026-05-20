from utils.static_typing import typechecked
from Tests.Unit.flags import FlagsUnitTests


@typechecked
def main():
  FlagsUnitTests().run()


main()