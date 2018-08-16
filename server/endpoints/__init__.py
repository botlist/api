import importlib
import pkgutil 

__all__ = []
__path__ = pkgutil.extend_path(__path__, __name__)
_prefix = __name__ + '.'
for importer, module, ispkg in pkgutil.walk_packages(path=__path__, prefix=_prefix):
	importlib.import_module(module)
	__all__.append(module.replace(_prefix, '', 1))