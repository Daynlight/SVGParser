import sys


# if not getattr(sys, "frozen", False):
#     from typeguard import typechecked
# else:
#     def typechecked(x): return x
from typeguard import typechecked