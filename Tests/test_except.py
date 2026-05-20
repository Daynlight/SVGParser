from utils.static_typing import typechecked
from rich import print


@typechecked
class testExcept:
  @typechecked
  def __init__(self, name: str):
    self._name: str = name
    self._total: int = 0
    self._passed: int = 0


  @typechecked
  def showResult(self):
    color: str = "red"
    if self._total == self._passed: color = "green"
    print(f"""[{color}]
================
{self._name}
{self._passed} / {self._total} passed
================
[/{color}]""")

  @typechecked
  def registerTest(self, result: bool, name: str):
    self._total += 1
    if(result): self._passed += 1
    else: print(f"[red]{self._name} - {name}: Tests doesn't passed[/red]")


  @typechecked
  def equal(self, name: str, result: int, expected: int):
    result: bool = (result == expected)
    self.registerTest(result, name)
    return result
  
  @typechecked
  def not_equal(self, name: str, result: int, expected: int):
    result: bool = (result != expected)
    self.registerTest(result, name)
    return result



@typechecked
class testInterface:
  @typechecked
  def __init__(self, name: str):
    self._test_except: testExcept = testExcept(name) 

  @typechecked
  def runAll(self):
    pass

  @typechecked
  def run(self):
    self.runAll()
    self._test_except.showResult()
