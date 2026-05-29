from utils.static_typing import typechecked
from Tests.test_except import testInterface

from pathlib import Path
import tempfile
import io
from contextlib import redirect_stdout

import App.shapes.shapes_register
from App.parser.parser import Parser
from App.shapes.circle import Circle



@typechecked
class ParserUnitTests(testInterface):
  @typechecked
  def __init__(self) -> None:
    super().__init__("ParserUnitTests")


  @typechecked
  def runAll(self) -> None:
    self.testSuccessfulParsing()
    self.testMalformedEntry()
    self.testEmptyFile()
    self.testMissingFile()
    self.testInvalidDataTypes()
    self.testPermissionDenied()


  @typechecked
  def testSuccessfulParsing(self) -> None:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".svl", delete=False) as tmp:
      tmp.write("Circle(x=10, y=20, r=5); Circle(x=0, y=0, r=10)")
      tmp.close()
      
      parser = Parser(Path(tmp.name))
      with redirect_stdout(io.StringIO()):
        shapes = parser.getShapes()
      
      self._test_except.int_equal("testSuccessfulParsing: Should parse 2 shapes", len(shapes), 2)
      self._test_except.is_true("testSuccessfulParsing: First shape should be a Circle", isinstance(shapes[0], Circle))
      
      shape = shapes[0]
      self._test_except.float_equal("testSuccessfulParsing: Shape 1 Position x should be 10", shape._position[0], 10)
      self._test_except.float_equal("testSuccessfulParsing: Shape 1 Position y should be 20", shape._position[1], 20)
      self._test_except.float_equal("testSuccessfulParsing: Shape 1 Radius should be 5", shape._radius, 5)

      shape = shapes[0]
      self._test_except.float_equal("testSuccessfulParsing: Shape 2 Position x should be 10", shape._position[0], 10)
      self._test_except.float_equal("testSuccessfulParsing: Shape 2 Position y should be 20", shape._position[1], 20)
      self._test_except.float_equal("testSuccessfulParsing: Shape 2 Radius should be 5", shape._radius, 5)


      Path(tmp.name).unlink()


  @typechecked
  def testMalformedEntry(self) -> None:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".svl", delete=False) as tmp:
      tmp.write("Circle(x=10, y=10, r=5); Circle(x=1, y=1); Circle(x=5, y=5, r=2)")
      tmp.close()
      
      parser = Parser(Path(tmp.name))
      with redirect_stdout(io.StringIO()):
        shapes = parser.getShapes()
      
      self._test_except.int_equal("testMalformedEntry: Should only parse the 2 valid shapes", len(shapes), 2)
      
      shape = shapes[0]
      self._test_except.float_equal("testMalformedEntry: Shape 1 Position x should be 10", shape._position[0], 10)
      self._test_except.float_equal("testMalformedEntry: Shape 1 Position y should be 20", shape._position[1], 10)
      self._test_except.float_equal("testMalformedEntry: Shape 1 Radius should be 5", shape._radius, 5)

      shape = shapes[1]
      self._test_except.float_equal("testMalformedEntry: Shape 2 Position x should be 10", shape._position[0], 5)
      self._test_except.float_equal("testMalformedEntry: Shape 2 Position y should be 20", shape._position[1], 5)
      self._test_except.float_equal("testMalformedEntry: Shape 2 Radius should be 5", shape._radius, 2)

      Path(tmp.name).unlink()


  @typechecked
  def testEmptyFile(self) -> None:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".svl", delete=False) as tmp:
      tmp.write("")
      tmp.close()
      
      parser = Parser(Path(tmp.name))
      with redirect_stdout(io.StringIO()):
        shapes = parser.getShapes()
      
      self._test_except.int_equal("testEmptyFile: Empty file should return 0 shapes", len(shapes), 0)
      
      Path(tmp.name).unlink()


  @typechecked
  def testMissingFile(self) -> None:
    
    parser = Parser(Path("non_existent_file.svl"))
    with redirect_stdout(io.StringIO()):
      shapes = parser.getShapes()

    self._test_except.int_equal("testMissingFile: Missing file should return empty list", len(shapes), 0)


  @typechecked
  def testInvalidDataTypes(self) -> None:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".svl", delete=False) as tmp:
      tmp.write("Circle(x=abc, y=20, r=5)")
      tmp.close()
      
      parser = Parser(Path(tmp.name))
      with redirect_stdout(io.StringIO()):
        shapes = parser.getShapes()
      
      self._test_except.float_equal("testInvalidDataTypes: Should not parse shape with invalid coords", len(shapes), 0)
      Path(tmp.name).unlink()


  @typechecked
  def testPermissionDenied(self) -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
      parser = Parser(Path(tmpdir))
      
      with redirect_stdout(io.StringIO()):
        content = parser._getFileContent()
          
      self._test_except.str_equal("testPermissionDenied: Should return empty string on read error", content, "")
