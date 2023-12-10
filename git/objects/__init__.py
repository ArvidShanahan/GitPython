# This module is part of GitPython and is released under the
# 3-Clause BSD License: https://opensource.org/license/bsd-3-clause/

"""Import all submodules' main classes into the package space."""

# flake8: noqa

import inspect

from .base import *
from .blob import *
from .commit import *
from .submodule import util as smutil
from .submodule.base import *
from .submodule.root import *
from .tag import *
from .tree import *

# Fix import dependency - add IndexObject to the util module, so that it can be
# imported by the submodule.base.
smutil.IndexObject = IndexObject  # type: ignore[attr-defined]
smutil.Object = Object  # type: ignore[attr-defined]
del smutil

# Must come after submodule was made available.
__all__ = [name for name, obj in locals().items() if not (name.startswith("_") or inspect.ismodule(obj))]
