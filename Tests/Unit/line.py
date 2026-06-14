from utils.static_typing import typechecked
from Tests.test_except import testInterface

import io
from contextlib import redirect_stdout

from App.shapes.line import Line


@typechecked
class LineUnitTest(testInterface):
    @typechecked
    def __init__(self) -> None:
        super().__init__("LineUnitTests")

    @typechecked
    def runAll(self) -> None:
        self.testValidation()
        self.testParsingSuccess()
        self.testParsingMissingParams()
        self.testParsingMalformedSyntax()
        self.testParsingColors()

    @typechecked
    def testValidation(self) -> None:
        self._test_except.is_true("testValidation: Should validate 'Line'", Line.validate("Line(x1=0,y1=0,x2=0,y2=0,w=1);"))
        self._test_except.is_true("testValidation: Should validate 'line'", Line.validate("line(x1=0,y1=0,x2=0,y2=0,w=1);"))

    @typechecked
    def testParsingSuccess(self) -> None:
        line_obj = Line()

        with redirect_stdout(io.StringIO()):
            success = line_obj.parse("Line(x1 = 100, y1 = 100, x2 = 500, y2 = 300, w = 5);", 1)
        self._test_except.is_true("testParsingSuccess: Parse should return True for standard data", success)
        
        self._test_except.float_equal("testParsingSuccess: Position x1 should be 100", line_obj._start_position[0], 100)
        self._test_except.float_equal("testParsingSuccess: Position y1 should be 100", line_obj._start_position[1], 100)
        self._test_except.float_equal("testParsingSuccess: Position x2 should be 500", line_obj._end_position[0], 500)
        self._test_except.float_equal("testParsingSuccess: Position y2 should be 300", line_obj._end_position[1], 300)
        self._test_except.float_equal("testParsingSuccess: Width w should be 5", line_obj._line_width, 5)

        with redirect_stdout(io.StringIO()):
            success = line_obj.parse("Line(y2 = 20, x1 = 300, w = 10, y1 = 50, x2 = 150);", 2)
        self._test_except.is_true("testParsingSuccess: Parse should handle different parameter order", success)

        with redirect_stdout(io.StringIO()):
            success = line_obj.parse("Line(x1 = 200, y1 = 400, x2 = 20, y2 = 80, w = 2);", 3)
        self._test_except.is_true("testParsingSuccess: Parse should handle correct spacing", success)

        with redirect_stdout(io.StringIO()):
            success = line_obj.parse("Line(x1 = 500, y1 = 300, x2 = -5, y2 = -5, w = -2);", 4)
        self._test_except.is_true("testParsingSuccess: Parse should handle negative parameters", success)

    @typechecked
    def testParsingMissingParams(self) -> None:
        line_obj = Line()
        
        with redirect_stdout(io.StringIO()):
            success1 = line_obj.parse("Line(x1 = 500, y1 = 300);", 5)
            success2 = line_obj.parse("Line(y1 = 300, x2 = 120, y2 = 20, w = 5);", 6)
            
        self._test_except.is_false("testParsingMissingParams: Parse should fail if x2, y2 and w are missing", success1)
        self._test_except.is_false("testParsingMissingParams: Parse should fail if x1 is missing", success2)

    @typechecked
    def testParsingMalformedSyntax(self) -> None:
        line_obj = Line()
        
        with redirect_stdout(io.StringIO()):
            success1 = line_obj.parse('Line(x1 = 500, y1 = 300, x2 = "duży", y2 = "duży", w = 5);', 7)
            success2 = line_obj.parse("Line(x1 = , y1 = 300, x2 = 20, y2 = 20, w = 5);", 8)
            success3 = line_obj.parse("Line(x1 = 500.500.500, y1 = 300, x2 = 20, y2 = 20, w = 5);", 9)
            success4 = line_obj.parse("Line(x1 = 500, y1 = 300, x2 = 20, y2 = 20, w = 5, color = #A5FF31;", 10)

        self._test_except.is_false("testParsingMalformedSyntax: Should fail on strings instead of numbers", success1)
        self._test_except.is_false("testParsingMalformedSyntax: Should fail on missing value after equals (x1=)", success2)
        self._test_except.is_false("testParsingMalformedSyntax: Should fail on multiple dots in float", success3)
        self._test_except.is_false("testParsingMalformedSyntax: Should fail on missing closing bracket", success4)

    @typechecked
    def testParsingColors(self) -> None:
        line_obj = Line()

        with redirect_stdout(io.StringIO()):
            s1 = line_obj.parse("Line(x1 = 20, y1 = 300, x2 = 50, y2 = 80, w = 3, c = #A5FF31);", 11)
            s2 = line_obj.parse("line(x1 = 600, x2 = 140, y2 = 40, y1 = 1.9, w = 4.5, color = #7683A2);", 12)
            s3 = line_obj.parse("Line(x1 = 500, y1 = 300, x2 = 20, y2 = 20, w = 5, color = red);", 13)
        
        self._test_except.is_true("testParsingColors: Should accept valid shorthand 'c' hex color", s1)
        self._test_except.is_true("testParsingColors: Should accept valid hex color with float positions", s2)
        self._test_except.is_true("testParsingColors: Should accept valid named color", s3)

        with redirect_stdout(io.StringIO()):
            s4 = line_obj.parse("Line(x1 = 500, y1 = 300, x2 = 20, y2 = 20, w = 5, c = #GGGGGG);", 14)

        self._test_except.is_false("testParsingColors: Should fail on invalid hex color (out of range)", s4)