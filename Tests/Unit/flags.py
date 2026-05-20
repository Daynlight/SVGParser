from utils.static_typing import typechecked
from Tests.test_except import testInterface

from App.flags import parseFlags, Flags


@typechecked
class FlagsUnitTests(testInterface):
  @typechecked
  def __init__(self):
    super().__init__("FlagsUnitTests")


  @typechecked
  def runAll(self):
    self.debugParsing()
    self.helpParsing()
  

  @typechecked
  def debugParsing(self):
    argv: list[str] = ["-d", "--debug"]
    result: Flags = parseFlags(argv)
    self._test_except.equal("Should contains debug flag", result & Flags.DEBUG, Flags.DEBUG)

    argv: list[str] = ["-d", "--hello"]
    result: Flags = parseFlags(argv)
    self._test_except.equal("Should contains debug flag", result & Flags.DEBUG, Flags.DEBUG)
  
    argv: list[str] = ["-hello", "--debug"]
    result: Flags = parseFlags(argv)
    self._test_except.equal("Should contains debug flag", result & Flags.DEBUG, Flags.DEBUG)

    argv: list[str] = ["--debug", "--hello"]
    result: Flags = parseFlags(argv)
    self._test_except.equal("Should contains debug flag", result & Flags.DEBUG, Flags.DEBUG)

    argv: list[str] = ["-hello", "--world"]
    result: Flags = parseFlags(argv)
    self._test_except.not_equal("Shouldn't contains debug flag", result & Flags.DEBUG, Flags.DEBUG)

  @typechecked
  def helpParsing(self):
    argv: list[str] = ["-h", "--help"]
    result: Flags = parseFlags(argv)
    self._test_except.equal("Should contains help flag", result & Flags.HELP, Flags.HELP)

    argv: list[str] = ["-h", "--hello"]
    result: Flags = parseFlags(argv)
    self._test_except.equal("Should contains help flag", result & Flags.HELP, Flags.HELP)
  
    argv: list[str] = ["-hello", "--help"]
    result: Flags = parseFlags(argv)
    self._test_except.equal("Should contains help flag", result & Flags.HELP, Flags.HELP)

    argv: list[str] = ["--help", "--hello"]
    result: Flags = parseFlags(argv)
    self._test_except.equal("Should contains help flag", result & Flags.HELP, Flags.HELP)

    argv: list[str] = ["-hello", "--world"]
    result: Flags = parseFlags(argv)
    self._test_except.not_equal("Shouldn't contains help flag", result & Flags.HELP, Flags.HELP)
