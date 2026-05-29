from utils.static_typing import typechecked
from Tests.test_except import testInterface

import io
from contextlib import redirect_stdout

from App.shapes.circle import Circle



@typechecked
class CircleUnitTests(testInterface):
  @typechecked
  def __init__(self) -> None:
    super().__init__("CircleUnitTests")


  @typechecked
  def runAll(self) -> None:
    self.testValidation()
    self.testParsingSuccess()
    self.testParsingMissingParams()
    self.testParsingInvalidValues()


  @typechecked
  def testValidation(self) -> None:
    self._test_except.is_true("testValidation: Should validate 'Circle'", Circle.validate("Circle(x=1, y=2, r=3)"))
    self._test_except.is_true("testValidation: Should validate 'circle'", Circle.validate("circle(x=1, y=2, r=3)"))
    self._test_except.is_false("testValidation: Should not validate 'Rect'", Circle.validate("Rect(x=1, y=2, w=3, h=4)"))


  @typechecked
  def testParsingSuccess(self) -> None:
    circle = Circle()

    with redirect_stdout(io.StringIO()):
      success = circle.parse("Circle(x=10, y=20.3, r=5)", 1)
    self._test_except.is_true("testParsingSuccess: Parse should return True for valid data", success)
    self._test_except.float_equal("testParsingSuccess: Position x should be 10", circle._position[0], 10)
    self._test_except.float_equal("testParsingSuccess: Position y should be 20", circle._position[1], 20.3)
    self._test_except.float_equal("testParsingSuccess: Radius should be 5", circle._radius, 5)

    circle = Circle()
    with redirect_stdout(io.StringIO()):
      success = circle.parse("Circle(r=50, y=5.2, x=2.1)", 2)
    self._test_except.is_true("testParsingSuccess: Parse should handle different order", success)
    self._test_except.float_equal("testParsingSuccess: Position x should be 2", circle._position[0], 2.1)
    self._test_except.float_equal("testParsingSuccess: Position y should be 5", circle._position[1], 5.2)
    self._test_except.float_equal("testParsingSuccess: Radius should be 50", circle._radius, 50)


  @typechecked
  def testParsingMissingParams(self) -> None:
    circle = Circle()
    with redirect_stdout(io.StringIO()):
      success = circle.parse("Circle(x=10, y=20)", 3)
    self._test_except.is_false("testParsingMissingParams: Parse should fail if 'r' is missing", success)


  @typechecked
  def testParsingInvalidValues(self) -> None:
    circle = Circle()
    with redirect_stdout(io.StringIO()):
      success: bool = circle.parse("Circle(x=abc, y=20, r=5)", 4)
    self._test_except.is_false("testParsingInvalidValues: Should have return False for invalid coordinate 'abc'", success)
