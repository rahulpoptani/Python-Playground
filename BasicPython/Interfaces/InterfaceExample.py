
class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        pass
    def extract_text(self, full_file_name: str) -> dict:
        pass

class PDFParser(InformalParserInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        pass
    def extract_text(self, full_file_name: str) -> dict:
        pass

class EMAILParser(InformalParserInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        pass
    def extract_text_from_email(self, full_file_name: str) -> dict:
        pass

# Python allows non implemented method of interface and it's not strict in this case. OK for small projects but not currect implementation of interfaces 
print(issubclass(PDFParser, InformalParserInterface))
print(issubclass(EMAILParser, InformalParserInterface))
print(PDFParser.__mro__)
print(EMAILParser.__mro__)


# Creating MetaClass which allows the strictness on top of concrete class.
class ParserMeta(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))
    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
        callable(subclass.load_data_source) and
        hasattr(subclass, 'extract_text') and
        callable(subclass.extract_text))

class UpdatedInformalParserInterface(metaclass=ParserMeta):
    pass

class PDFParserNew:
    def load_data_source(self, path: str, file_name: str) -> str:
        pass
    def extract_text(self, full_file_name: str) -> dict:
        pass

class EMAILParserNew:
    def load_data_source(self, path: str, file_name: str) -> str:
        pass
    def extract_text_from_email(self, full_file_name: str) -> dict:
        pass

# Return False for EMAILParserNew
print(issubclass(PDFParserNew, UpdatedInformalParserInterface))
print(issubclass(EMAILParserNew, UpdatedInformalParserInterface))
print(PDFParserNew.__mro__)
print(EMAILParserNew.__mro__)

# Formal Interface using ABC
import abc
class FormalParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, 'load_data_source') and
            callable(subclass.load_data_source) and
            hasattr(subclass, 'extract_text') and
            callable(subclass.extract_text)
        )
    @abc.abstractmethod
    def load_data_source(self, path: str, file_name: str) -> str:
        pass
    @abc.abstractmethod
    def extract_text(self, full_file_name: str) -> dict:
        pass

class PDFParserNew(FormalParserInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        pass
    def extract_text(self, full_file_name: str) -> dict:
        pass

class EMAILParserNew(FormalParserInterface):
    def load_data_source(self, path: str, file_name: str) -> str:
        pass
    def extract_text(self, full_file_name: str) -> dict:
        pass

# email_parser will throw error because all interface methods are not implemented
pdf_parser = PDFParserNew()
email_parser = EMAILParserNew()
