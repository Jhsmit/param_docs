from param_docs.paramdoc import param_format_basic
from param_docs.controller import FruitStallController
import param

tc = FruitStallController()

print(isinstance(FruitStallController, param.parameterized.ParameterizedMetaclass))
lines = []

param_format_basic('app', 'class', 'name', FruitStallController, 'options', lines)

print(lines)