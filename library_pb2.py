# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: library.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'library.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rlibrary.proto\x12\x07library\"h\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x0c\n\x04isbn\x18\x04 \x01(\t\x12\x18\n\x10publication_year\x18\x05 \x01(\x05\x12\r\n\x05genre\x18\x06 \x01(\t\"0\n\x11\x43reateBookRequest\x12\x1b\n\x04\x62ook\x18\x01 \x01(\x0b\x32\r.library.Book\"1\n\x12\x43reateBookResponse\x12\x1b\n\x04\x62ook\x18\x01 \x01(\x0b\x32\r.library.Book\"\x1c\n\x0eGetBookRequest\x12\n\n\x02id\x18\x01 \x01(\x05\".\n\x0fGetBookResponse\x12\x1b\n\x04\x62ook\x18\x01 \x01(\x0b\x32\r.library.Book\"0\n\x11UpdateBookRequest\x12\x1b\n\x04\x62ook\x18\x01 \x01(\x0b\x32\r.library.Book\"1\n\x12UpdateBookResponse\x12\x1b\n\x04\x62ook\x18\x01 \x01(\x0b\x32\r.library.Book\"\x1f\n\x11\x44\x65leteBookRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"%\n\x12\x44\x65leteBookResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x12\n\x10ListBooksRequest\"1\n\x11ListBooksResponse\x12\x1c\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\r.library.Book2\xe7\x02\n\x0eLibraryService\x12\x45\n\nCreateBook\x12\x1a.library.CreateBookRequest\x1a\x1b.library.CreateBookResponse\x12<\n\x07GetBook\x12\x17.library.GetBookRequest\x1a\x18.library.GetBookResponse\x12\x45\n\nUpdateBook\x12\x1a.library.UpdateBookRequest\x1a\x1b.library.UpdateBookResponse\x12\x45\n\nDeleteBook\x12\x1a.library.DeleteBookRequest\x1a\x1b.library.DeleteBookResponse\x12\x42\n\tListBooks\x12\x19.library.ListBooksRequest\x1a\x1a.library.ListBooksResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'library_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BOOK']._serialized_start=26
  _globals['_BOOK']._serialized_end=130
  _globals['_CREATEBOOKREQUEST']._serialized_start=132
  _globals['_CREATEBOOKREQUEST']._serialized_end=180
  _globals['_CREATEBOOKRESPONSE']._serialized_start=182
  _globals['_CREATEBOOKRESPONSE']._serialized_end=231
  _globals['_GETBOOKREQUEST']._serialized_start=233
  _globals['_GETBOOKREQUEST']._serialized_end=261
  _globals['_GETBOOKRESPONSE']._serialized_start=263
  _globals['_GETBOOKRESPONSE']._serialized_end=309
  _globals['_UPDATEBOOKREQUEST']._serialized_start=311
  _globals['_UPDATEBOOKREQUEST']._serialized_end=359
  _globals['_UPDATEBOOKRESPONSE']._serialized_start=361
  _globals['_UPDATEBOOKRESPONSE']._serialized_end=410
  _globals['_DELETEBOOKREQUEST']._serialized_start=412
  _globals['_DELETEBOOKREQUEST']._serialized_end=443
  _globals['_DELETEBOOKRESPONSE']._serialized_start=445
  _globals['_DELETEBOOKRESPONSE']._serialized_end=482
  _globals['_LISTBOOKSREQUEST']._serialized_start=484
  _globals['_LISTBOOKSREQUEST']._serialized_end=502
  _globals['_LISTBOOKSRESPONSE']._serialized_start=504
  _globals['_LISTBOOKSRESPONSE']._serialized_end=553
  _globals['_LIBRARYSERVICE']._serialized_start=556
  _globals['_LIBRARYSERVICE']._serialized_end=915
# @@protoc_insertion_point(module_scope)
