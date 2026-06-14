from utils.static_typing import typechecked
from Tests.test_except import testInterface

import io
from contextlib import redirect_stdout

from App.shapes.rectangle import Rectangle


@typechecked
class RectangleUnitTests(testInterface):
    @typechecked
    def __init__(self) -> None:
        super().__init__("RectangleUnitTests")


    @typechecked
    def runAll(self) -> None:
        self.testValidation()
        self.testParsingSuccess()
        self.testParsingMissingParams()
        self.testParsingMalformedSyntax()
        self.testParsingColors()


    @typechecked
    def testValidation(self) -> None:

        self._test_except.is_true("testValidation: Should validate 'Rectangle'", Rectangle.validate("Rectangle(x=0,y=0,w=0,h=0);"))
        self._test_except.is_true("testValidation: Should validate 'rectangle'", Rectangle.validate("rectangle(x=0,y=0,w=0,h=0);"))


    @typechecked
    def testParsingSuccess(self) -> None:
        rect = Rectangle()


        with redirect_stdout(io.StringIO()):
            success = rect.parse("Rectangle(x=1,y=2,w=3,h=4);", 1)
        self._test_except.is_true("testParsingSuccess: Parse should return True for standard data", success)
        self._test_except.float_equal("testParsingSuccess: Position x should be 1", rect._position[0], 1)
        self._test_except.float_equal("testParsingSuccess: Position y should be 2", rect._position[1], 2)
        self._test_except.float_equal("testParsingSuccess: Width should be 3", rect._width, 3)
        self._test_except.float_equal("testParsingSuccess: Height should be 4", rect._height, 4)


        with redirect_stdout(io.StringIO()):
            success = rect.parse("Rectangle(   x=1,y=2,w=3,h=4   );", 2)
        self._test_except.is_true("testParsingSuccess: Parse should handle internal padding", success)


        with redirect_stdout(io.StringIO()):
            success = rect.parse("Rectangle(x = 3, y = 30, w = 45, h = 67)", 3)
        self._test_except.is_true("testParsingSuccess: Parse should handle spaces around equals", success)
        self._test_except.float_equal("testParsingSuccess: Width should be 45", rect._width, 45)

        with redirect_stdout(io.StringIO()):
            success = rect.parse("Rectangle(x = -10, y = 20, w = 30, h = 40);", 4)
        self._test_except.is_true("testParsingSuccess: Parse should handle negative coordinates", success)
        self._test_except.float_equal("testParsingSuccess: Position x should be -10", rect._position[0], -10)


    @typechecked
    def testParsingMissingParams(self) -> None:
        rect = Rectangle()
        with redirect_stdout(io.StringIO()):
            success = rect.parse("Rectangle(x = 450, y = 230, h = 76);", 5)
        self._test_except.is_false("testParsingMissingParams: Parse should fail if 'w' is missing", success)


    @typechecked
    def testParsingMalformedSyntax(self) -> None:
        rect = Rectangle()
        
        with redirect_stdout(io.StringIO()):

            success1 = rect.parse('Rectangle(   x="aaa,y=2,w=3,h=4   );', 6)

            success2 = rect.parse("Rectangle(x = 200, y = 300, w = 25 h = 25);", 7)

            success3 = rect.parse("Rectangle(x = 150, y = 122, w =, h = 37);", 8)

            success4 = rect.parse("Rectangle(x = 450, y = 230, w = 122, h = 76;;", 9)

            success5 = rect.parse("Rectangle(x = 450, y = 230, w = 122, h = );", 10)

            success6 = rect.parse("Rectangle(x = 450, y = 230, w = 122, h = 76,);", 11)

            success7 = rect.parse("Rectangle(x == 450, y = 230, w = 122, h = 76);", 12)

            success8 = rect.parse("Rectangle(x = abc, y = 20, w = 30, h = 40);", 13)

            success9 = rect.parse("Rectangle(x = abc, y = jujfl, w = 30, h = 40);", 13)

        self._test_except.is_false("testParsingMalformedSyntax: Should fail on garbage string quotes", success1)
        self._test_except.is_false("testParsingMalformedSyntax: Should fail on missing comma", success2)
        self._test_except.is_false("testParsingMalformedSyntax: Should fail on missing value after equals (w=)", success3)
        self._test_except.is_false("testParsingMalformedSyntax: Should fail on double semicolons/missing bracket", success4)
        self._test_except.is_false("testParsingMalformedSyntax: Should fail on missing value at the end (h=)", success5)
        self._test_except.is_false("testParsingMalformedSyntax: Should fail on trailing comma", success6)
        self._test_except.is_false("testParsingMalformedSyntax: Should fail on double equals symbol", success7)
        self._test_except.is_false("testParsingMalformedSyntax: Should fail on letters instead of numbers", success8)
        self._test_except.is_false("testParsingMalformedSyntax: Should fail on letters instead of numbers", success9)

    @typechecked
    def testParsingColors(self) -> None:
        rect = Rectangle()

        with redirect_stdout(io.StringIO()):
            s1 = rect.parse("Rectangle(x = 400, y = 50.7, w = 50.3, h = 60.7, color = #FF0000);", 14)
            s2 = rect.parse("Rectangle(x = 40, y = 500, w = 50.3, h = 60.7, color = green);", 15)
            s3 = rect.parse("Rectangle(x = 467, y = 56, w = 50.3, h = 60.7, c = green);", 16)
        
        self._test_except.is_true("testParsingColors: Should accept valid hex color", s1)
        self._test_except.is_true("testParsingColors: Should accept valid named color", s2)
        self._test_except.is_true("testParsingColors: Should accept valid shorthand 'c'", s3)

        with redirect_stdout(io.StringIO()):
            s4 = rect.parse("Rectangle(x = 40, y = 500, w = 50.3, h = 60.7, color = greu);", 17)
            s5 = rect.parse("Rectangle(x = 40, y = 500, w = 50.3, h = 60.7, color #yt6789);", 18)
            s6 = rect.parse("Rectangle(x = 40, y = 500, w = 50.3, h = 60.7, color = #yt6789);", 19)

        self._test_except.is_false("testParsingColors: Should fail on unknown color name", s4)
        self._test_except.is_false("testParsingColors: Should fail on invalid syntax (missing equals)", s5)
        self._test_except.is_false("testParsingColors: Should fail on invalid hex format", s6)