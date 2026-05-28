from utils.static_typing import typechecked
from Tests.test_except import testInterface

from pathlib import Path
import tempfile

from App.flags import fetchFlags, getPathFromArgs, parseArgv, Flags



@typechecked
class FlagsUnitTests(testInterface):

  @typechecked
  def __init__(self):
    super().__init__("FlagsUnitTests")


  @typechecked
  def runAll(self):
    self.debugParsing()
    self.helpParsing()
    self.combinedFlags()
    self.pathParsing()
    self.invalidPath()
    self.invalidExtension()
    self.parseArgvTests()


  @typechecked
  def debugParsing(self):
    argv: list[str] = ["-d", "--debug"]
    result: Flags = fetchFlags(argv)
    self._test_except.int_equal("Should contain debug flag", int(result & Flags.DEBUG), int(Flags.DEBUG))

    argv = ["-hello", "--world"]
    result = fetchFlags(argv)
    self._test_except.int_not_equal("Shouldn't contain debug flag", int(result & Flags.DEBUG), int(Flags.DEBUG))


  @typechecked
  def helpParsing(self):
    argv: list[str] = ["-h", "--help"]
    result: Flags = fetchFlags(argv)
    self._test_except.int_equal("Should contain help flag", int(result & Flags.HELP), int(Flags.HELP))

    argv = ["-hello", "--world"]
    result = fetchFlags(argv)
    self._test_except.int_not_equal("Shouldn't contain help flag", int(result & Flags.HELP), int(Flags.HELP))


  @typechecked
  def combinedFlags(self):
    argv: list[str] = ["-d", "--help"]
    result: Flags = fetchFlags(argv)
    self._test_except.int_equal("Should contain debug flag", int(result & Flags.DEBUG), int(Flags.DEBUG))
    self._test_except.int_equal("Should contain help flag", int(result & Flags.HELP), int(Flags.HELP))


  @typechecked
  def pathParsing(self):
    with tempfile.NamedTemporaryFile(suffix=".svl") as temp:
      argv: list[str] = [temp.name]
      result: Path = getPathFromArgs(argv)
      self._test_except.str_equal("Should parse valid .svl file", str(result), str(Path(temp.name).resolve()))


  @typechecked
  def invalidPath(self):
    argv: list[str] = ["missing_file.svl"]
    try:
      getPathFromArgs(argv)
      self._test_except.fail("Should throw FileNotFoundError")
    except FileNotFoundError:
      self._test_except.success("Correctly threw FileNotFoundError")


  @typechecked
  def invalidExtension(self):
    argv: list[str] = ["test.txt"]
    try:
      getPathFromArgs(argv)
      self._test_except.fail("Should reject invalid extension")
    except ValueError:
      self._test_except.success("Correctly rejected invalid extension")


  @typechecked
  def parseArgvTests(self):
    with tempfile.NamedTemporaryFile(suffix=".svl") as temp:
      argv: list[str] = [temp.name, "--debug"]
      path, flags = parseArgv(argv)
      self._test_except.str_equal("Should return correct path", str(path), str(Path(temp.name).resolve()))
      self._test_except.int_equal("Should contain debug flag", int(flags & Flags.DEBUG), int(Flags.DEBUG))