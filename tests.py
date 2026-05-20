from utils.static_typing import typechecked
from Tests.test_except import testExcept
from Tests.Unit.flags import FlagsUnitTests


@typechecked
def main():
  tests: testExcept = testExcept("Tests")
  tests.is_true("FlagsUnitTests", FlagsUnitTests().run())
  tests.showResult()

  if(not tests.allPassed()):
    exit(-1)


main()