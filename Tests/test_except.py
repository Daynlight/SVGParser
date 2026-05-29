from utils.static_typing import typechecked
from rich import print



@typechecked
class testExcept:
  @typechecked
  def __init__(self, name: str) -> None:
    self._name: str = name
    self._total: int = 0
    self._passed: int = 0


  @typechecked
  def showResult(self) -> None:
    color: str = "red"
    if self._total == self._passed: color = "green"
    print(f"""[{color}]
================
{self._name}
{self._passed} / {self._total} passed
================
[/{color}]""")


  @typechecked
  def registerTest(self, result: bool, name: str) -> None:
    self._total += 1
    if(result): self._passed += 1
    else: print(f"[red]{self._name} - {name}: Tests doesn't passed[/red]")


  @typechecked
  def allPassed(self) -> bool:
    return self._total == self._passed
  

  @typechecked
  def success(self, name: str) -> bool:
    self.registerTest(True, name)
    return True
  

  @typechecked
  def fail(self, name: str) -> bool:
    self.registerTest(False, name)
    return False
  

  @typechecked
  def int_equal(self, name: str, result: int, expected: int) -> bool:
    result: bool = (result == expected)
    self.registerTest(result, name)
    return result
  

  @typechecked
  def float_equal(self, name: str, result: float, expected: float) -> bool:
    result: bool = (result == expected)
    self.registerTest(result, name)
    return result
  

  @typechecked
  def str_equal(self, name: str, result: str, expected: str) -> bool:
    result: bool = (result == expected)
    self.registerTest(result, name)
    return result
  

  @typechecked
  def int_not_equal(self, name: str, result: int, expected: int) -> bool:
    result: bool = (result != expected)
    self.registerTest(result, name)
    return result
  

  @typechecked
  def float_not_equal(self, name: str, result: float, expected: float) -> bool:
    result: bool = (result != expected)
    self.registerTest(result, name)
    return result
  

  @typechecked
  def str_not_equal(self, name: str, result: str, expected: str) -> bool:
    result: bool = (result != expected)
    self.registerTest(result, name)
    return result
  

  @typechecked
  def is_true(self, name: str, result: bool) -> bool:
    result: bool = (result == True)
    self.registerTest(result, name)
    return result
  
  
  @typechecked
  def is_false(self, name: str, result: bool) -> bool:
    result: bool = (result != True)
    self.registerTest(result, name)
    return result



@typechecked
class testInterface:
  @typechecked
  def __init__(self, name: str) -> None:
    self._test_except: testExcept = testExcept(name) 


  @typechecked
  def runAll(self) -> None:
    pass


  @typechecked
  def run(self) -> bool:
    self.runAll()
    self._test_except.showResult()
    return self._test_except.allPassed()
