from utils.static_typing import typechecked
from Tests.test_except import testExcept

from Tests.Unit.flags import FlagsUnitTests
from Tests.Unit.parser import ParserUnitTests
from Tests.Unit.circle import CircleUnitTests



@typechecked
def main():
  tests: testExcept = testExcept("Tests")
  tests.is_true("FlagsUnitTests", FlagsUnitTests().run())
  tests.is_true("ParserUnitTests", ParserUnitTests().run())
  tests.is_true("CircleUnitTests", CircleUnitTests().run())
  tests.showResult()

  if(not tests.allPassed()):
    exit(-1)


main()