from utils.static_typing import typechecked
from Tests.test_except import testInterface

import io
from contextlib import redirect_stdout

from App.shapes.ellipse import Ellipse


@typechecked
class EllipseUnitTest(testInterface):
    @typechecked
    def __init__(self) -> None:
        super().__init__("EllipseUnitTests")

    @typechecked
    def runAll(self) -> None:
        self.testValidation()
        self.testParsingSuccess()
        self.testParsingMissingParams()
        self.testParsingMalformedSyntax()
        self.testParsingColors()

    @typechecked
    def testValidation(self) -> None:
        self._test_except.is_true("testValidation: Should validate 'Ellipse'", Ellipse.validate("Ellipse(x=0,y=0,rx=0,ry=0);"))
        self._test_except.is_true("testValidation: Should validate 'ellipse'", Ellipse.validate("ellipse(x=0,y=0,rx=0,ry=0);"))

    @typechecked
    def testParsingSuccess(self) -> None:
        ell = Ellipse()

        with redirect_stdout(io.StringIO()):
            success = ell.parse("Ellipse(x = 500, y = 300, rx = 120, ry = 20);", 1)
        self._test_except.is_true("testParsingSuccess: Parse should return True for standard data", success)
        self._test_except.float_equal("testParsingSuccess: Position x should be 500", ell._position[0], 500)
        self._test_except.float_equal("testParsingSuccess: Position y should be 300", ell._position[1], 300)
        self._test_except.float_equal("testParsingSuccess: rx should be 120", ell._x_radius, 120)
        self._test_except.float_equal("testParsingSuccess: ry should be 20", ell._y_radius, 20)

        with redirect_stdout(io.StringIO()):
            success = ell.parse("Ellipse(x = 300, rx = 50, ry = 150, y = 20);", 2)
        self._test_except.is_true("testParsingSuccess: Parse should handle different parameter order", success)

        with redirect_stdout(io.StringIO()):
            success = ell.parse("Ellipse(x = 200, y = 400, rx = 20, ry = 80);", 3)
        self._test_except.is_true("testParsingSuccess: Parse should handle correct spacing", success)

        with redirect_stdout(io.StringIO()):
            success = ell.parse("Ellipse(x = 500, y = 300, rx = -5, ry = -5);", 4)
        self._test_except.is_true("testParsingSuccess: Parse should handle negative parameters", success)

    @typechecked
    def testParsingMissingParams(self) -> None:
        ell = Ellipse()
        
        with redirect_stdout(io.StringIO()):
            success1 = ell.parse("Ellipse(x = 500, y = 300);", 5)
            success2 = ell.parse("Ellipse(y = 300, rx = 120, ry = 20);", 6)
            
        self._test_except.is_false("testParsingMissingParams: Parse should fail if rx and ry are missing", success1)
        self._test_except.is_false("testParsingMissingParams: Parse should fail if x is missing", success2)

    @typechecked
    def testParsingMalformedSyntax(self) -> None:
        ell = Ellipse()
        
        with redirect_stdout(io.StringIO()):
            success1 = ell.parse('Ellipse(x = 500, y = 300, rx = "duży", ry = "duży");', 7)
            success2 = ell.parse("Ellipse(x = 500, y = 300, rx = 30, ry = 20, color = );", 8)
            success3 = ell.parse("Ellipse(x = , y = 300, rx = 20, ry = 20);", 9)
            success4 = ell.parse("Ellipse(x = 500.500.500, y = 300, rx = 20, ry = 20);", 10)
            success5 = ell.parse("Ellipse(x = 500, y = 300, rx = 20, ry = 20, color = #A5FF31;", 11)

        self._test_except.is_false("testParsingMalformedSyntax: Should fail on strings instead of numbers", success1)
        self._test_except.is_false("testParsingMalformedSyntax: Should fail on empty value after equals (color=)", success2)
        self._test_except.is_false("testParsingMalformedSyntax: Should fail on missing value after equals (x=)", success3)
        self._test_except.is_false("testParsingMalformedSyntax: Should fail on multiple dots in float", success4)
        self._test_except.is_false("testParsingMalformedSyntax: Should fail on missing closing bracket", success5)

    @typechecked
    def testParsingColors(self) -> None:
        ell = Ellipse()

        with redirect_stdout(io.StringIO()):
            s1 = ell.parse("Ellipse(x = 20, y = 300, rx = 50, ry = 80, c = #A5FF31);", 12)
            s2 = ell.parse("ellipse(x = 600, rx = 140, ry = 40, y = 1.9, color = #7683A2);", 13)
            s3 = ell.parse("Ellipse(x = 500, y = 300, rx = 20, ry = 20, color = red);", 14)
        
        self._test_except.is_true("testParsingColors: Should accept valid shorthand 'c' hex color", s1)
        self._test_except.is_true("testParsingColors: Should accept valid hex color with float positions", s2)
        self._test_except.is_true("testParsingColors: Should accept valid named color", s3)

        with redirect_stdout(io.StringIO()):
            s4 = ell.parse("Ellipse(x = 500, y = 300, rx = 20, ry = 20, c = #GGGGGG);", 15)

        self._test_except.is_false("testParsingColors: Should fail on invalid hex color (out of range)", s4)