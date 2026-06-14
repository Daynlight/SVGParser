from utils.static_typing import typechecked
from Tests.test_except import testExcept

from Tests.Unit.flags import FlagsUnitTests
from Tests.Unit.parser import ParserUnitTests
from Tests.Unit.circle import CircleUnitTests
from Tests.Unit.rectangle import RectangleUnitTests
from Tests.Unit.elipse import EllipseUnitTest
from Tests.Unit.line import LineUnitTest


@typechecked
def main():
  tests: testExcept = testExcept("Tests")
  tests.is_true("FlagsUnitTests", FlagsUnitTests().run())
  tests.is_true("ParserUnitTests", ParserUnitTests().run())
  tests.is_true("CircleUnitTests", CircleUnitTests().run())
  tests.is_true("RectangleUnitTests", RectangleUnitTests().run())
  tests.is_true("EllipseUnitTest", EllipseUnitTest().run())
  tests.is_true("LineUnitTest", LineUnitTest().run())
  tests.showResult()

  if(not tests.allPassed()):
    exit(-1)


main()