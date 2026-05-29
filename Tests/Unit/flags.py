from utils.static_typing import typechecked
from Tests.test_except import testInterface

from pathlib import Path
import tempfile

from App.flags import fetchFlags, getPathFromArgs, parseArgv, Flags



@typechecked
class FlagsUnitTests(testInterface):
  @typechecked
  def __init__(self) -> None:
    super().__init__("FlagsUnitTests")


  @typechecked
  def runAll(self) -> None:
    self.debugParsing()
    self.helpParsing()
    self.combinedFlags()
    self.pathParsing()
    self.invalidPath()
    self.invalidExtension()
    self.parseArgvTests()


  @typechecked
  def debugParsing(self) -> None:
    argv: list[str] = ["-d", "--debug"]
    result: Flags = fetchFlags(argv)
    self._test_except.int_equal("debugParsing: Should contain debug flag", int(result & Flags.DEBUG), int(Flags.DEBUG))

    argv: list[str] = ["-d"]
    result: Flags = fetchFlags(argv)
    self._test_except.int_equal("debugParsing: Should contain debug flag", int(result & Flags.DEBUG), int(Flags.DEBUG))

    argv: list[str] = ["--debug"]
    result: Flags = fetchFlags(argv)
    self._test_except.int_equal("debugParsing: Should contain debug flag", int(result & Flags.DEBUG), int(Flags.DEBUG))

    argv = ["-hello", "--world"]
    result = fetchFlags(argv)
    self._test_except.int_not_equal("debugParsing: Shouldn't contain debug flag", int(result & Flags.DEBUG), int(Flags.DEBUG))

    argv = ["-debug"]
    result = fetchFlags(argv)
    self._test_except.int_not_equal("debugParsing: Shouldn't contain debug flag", int(result & Flags.DEBUG), int(Flags.DEBUG))

    argv = ["--d"]
    result = fetchFlags(argv)
    self._test_except.int_not_equal("debugParsing: Shouldn't contain debug flag", int(result & Flags.DEBUG), int(Flags.DEBUG))


  @typechecked
  def helpParsing(self) -> None:
    argv: list[str] = ["-h", "--help"]
    result: Flags = fetchFlags(argv)
    self._test_except.int_equal("helpParsing: Should contain help flag", int(result & Flags.HELP), int(Flags.HELP))

    argv: list[str] = ["-h"]
    result: Flags = fetchFlags(argv)
    self._test_except.int_equal("helpParsing: Should contain help flag", int(result & Flags.HELP), int(Flags.HELP))

    argv: list[str] = ["--help"]
    result: Flags = fetchFlags(argv)
    self._test_except.int_equal("helpParsing: Should contain help flag", int(result & Flags.HELP), int(Flags.HELP))

    argv = ["-hello", "--world"]
    result = fetchFlags(argv)
    self._test_except.int_not_equal("helpParsing: Shouldn't contain help flag", int(result & Flags.HELP), int(Flags.HELP))

    argv = ["-help"]
    result = fetchFlags(argv)
    self._test_except.int_not_equal("helpParsing: Shouldn't contain help flag", int(result & Flags.HELP), int(Flags.HELP))

    argv = ["--h"]
    result = fetchFlags(argv)
    self._test_except.int_not_equal("helpParsing: Shouldn't contain help flag", int(result & Flags.HELP), int(Flags.HELP))


  @typechecked
  def combinedFlags(self) -> None:
    argv: list[str] = ["-d", "--help"]
    result: Flags = fetchFlags(argv)
    self._test_except.int_equal("combinedFlags: Should contain debug flag", int(result & Flags.DEBUG), int(Flags.DEBUG))
    self._test_except.int_equal("combinedFlags: Should contain help flag", int(result & Flags.HELP), int(Flags.HELP))

    argv: list[str] = ["--debug", "--help"]
    result: Flags = fetchFlags(argv)
    self._test_except.int_equal("combinedFlags: Should contain debug flag", int(result & Flags.DEBUG), int(Flags.DEBUG))
    self._test_except.int_equal("combinedFlags: Should contain help flag", int(result & Flags.HELP), int(Flags.HELP))

    argv: list[str] = ["-d", "-h"]
    result: Flags = fetchFlags(argv)
    self._test_except.int_equal("combinedFlags: Should contain debug flag", int(result & Flags.DEBUG), int(Flags.DEBUG))
    self._test_except.int_equal("combinedFlags: Should contain help flag", int(result & Flags.HELP), int(Flags.HELP))

    argv: list[str] = ["-h", "--debug"]
    result: Flags = fetchFlags(argv)
    self._test_except.int_equal("combinedFlags: Should contain debug flag", int(result & Flags.DEBUG), int(Flags.DEBUG))
    self._test_except.int_equal("combinedFlags: Should contain help flag", int(result & Flags.HELP), int(Flags.HELP))

    argv: list[str] = ["-d", "-help"]
    result: Flags = fetchFlags(argv)
    self._test_except.int_equal("combinedFlags: Should contain debug flag", int(result & Flags.DEBUG), int(Flags.DEBUG))
    self._test_except.int_not_equal("combinedFlags: Shouldn't contain help flag", int(result & Flags.HELP), int(Flags.HELP))

    argv: list[str] = ["-h", "-debug"]
    result: Flags = fetchFlags(argv)
    self._test_except.int_not_equal("combinedFlags: Shouldn't contain debug flag", int(result & Flags.DEBUG), int(Flags.DEBUG))
    self._test_except.int_equal("combinedFlags: Should contain help flag", int(result & Flags.HELP), int(Flags.HELP))


  @typechecked
  def pathParsing(self) -> None:
    with tempfile.NamedTemporaryFile(suffix=".svl") as temp:
      argv: list[str] = [temp.name]
      result: Path = getPathFromArgs(argv)
      self._test_except.str_equal("pathParsing: Should parse valid .svl file", str(result), str(Path(temp.name).resolve()))


  @typechecked
  def invalidPath(self) -> None:
    argv: list[str] = ["missing_file.svl"]
    try:
      getPathFromArgs(argv)
      self._test_except.fail("invalidPath: Should throw FileNotFoundError")
    except FileNotFoundError:
      self._test_except.success("invalidPath: Correctly threw FileNotFoundError")


  @typechecked
  def invalidExtension(self) -> None:
    argv: list[str] = ["test.txt"]
    try:
      getPathFromArgs(argv)
      self._test_except.fail("invalidExtension: Should reject invalid extension")
    except ValueError:
      self._test_except.success("invalidExtension: Correctly rejected invalid extension")


  @typechecked
  def parseArgvTests(self) -> None:
    with tempfile.NamedTemporaryFile(suffix=".svl") as temp:
      argv: list[str] = [temp.name, "--debug"]
      path, flags = parseArgv(argv)
      self._test_except.str_equal("parseArgvTests: Should return correct path", str(path), str(Path(temp.name).resolve()))
      self._test_except.int_equal("parseArgvTests: Should contain debug flag", int(flags & Flags.DEBUG), int(Flags.DEBUG))

      argv: list[str] = [temp.name, "-d", "--help"]
      path, flags = parseArgv(argv)
      self._test_except.str_equal("parseArgvTests: Should return correct path", str(path), str(Path(temp.name).resolve()))
      self._test_except.int_equal("parseArgvTests: Should contain debug flag", int(flags & Flags.DEBUG), int(Flags.DEBUG))
      self._test_except.int_equal("parseArgvTests: Should contain help flag", int(flags & Flags.HELP), int(Flags.HELP))

      argv: list[str] = [temp.name, "--help", "-d"]
      path, flags = parseArgv(argv)
      self._test_except.str_equal("parseArgvTests: Should return correct path", str(path), str(Path(temp.name).resolve()))
      self._test_except.int_equal("parseArgvTests: Should contain debug flag", int(flags & Flags.DEBUG), int(Flags.DEBUG))
      self._test_except.int_equal("parseArgvTests: Should contain help flag", int(flags & Flags.HELP), int(Flags.HELP))

      argv: list[str] = [temp.name, "--d", "-h"]
      path, flags = parseArgv(argv)
      self._test_except.str_equal("parseArgvTests: Should return correct path", str(path), str(Path(temp.name).resolve()))
      self._test_except.int_not_equal("parseArgvTests: Shouldn't contain debug flag", int(flags & Flags.DEBUG), int(Flags.DEBUG))
      self._test_except.int_equal("parseArgvTests: Should contain help flag", int(flags & Flags.HELP), int(Flags.HELP))

      argv: list[str] = [temp.name, "--d", "--h"]
      path, flags = parseArgv(argv)
      self._test_except.str_equal("parseArgvTests: Should return correct path", str(path), str(Path(temp.name).resolve()))
      self._test_except.int_not_equal("parseArgvTests: Shouldn't contain debug flag", int(flags & Flags.DEBUG), int(Flags.DEBUG))
      self._test_except.int_not_equal("parseArgvTests: Shouldn't contain help flag", int(flags & Flags.HELP), int(Flags.HELP))
