# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msgs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msgs.proto',
  package='common',
  syntax='proto3',
  serialized_options=b'\n\031net.skycloud.proto.commonZ(github.com/sky-cloud-tec/proto/v1/common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nmsgs.proto\x12\x06\x63ommon\"%\n\x11SimpleJsonRequest\x12\x10\n\x08json_str\x18\n \x01(\t\"&\n\x12SimpleJsonResponse\x12\x10\n\x08json_str\x18\n \x01(\t\"\x0e\n\x0c\x45mptyRequest\"\x0f\n\rEmptyResponseBE\n\x19net.skycloud.proto.commonZ(github.com/sky-cloud-tec/proto/v1/commonb\x06proto3'
)




_SIMPLEJSONREQUEST = _descriptor.Descriptor(
  name='SimpleJsonRequest',
  full_name='common.SimpleJsonRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='json_str', full_name='common.SimpleJsonRequest.json_str', index=0,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=59,
)


_SIMPLEJSONRESPONSE = _descriptor.Descriptor(
  name='SimpleJsonResponse',
  full_name='common.SimpleJsonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='json_str', full_name='common.SimpleJsonResponse.json_str', index=0,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=99,
)


_EMPTYREQUEST = _descriptor.Descriptor(
  name='EmptyRequest',
  full_name='common.EmptyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=115,
)


_EMPTYRESPONSE = _descriptor.Descriptor(
  name='EmptyResponse',
  full_name='common.EmptyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=132,
)

DESCRIPTOR.message_types_by_name['SimpleJsonRequest'] = _SIMPLEJSONREQUEST
DESCRIPTOR.message_types_by_name['SimpleJsonResponse'] = _SIMPLEJSONRESPONSE
DESCRIPTOR.message_types_by_name['EmptyRequest'] = _EMPTYREQUEST
DESCRIPTOR.message_types_by_name['EmptyResponse'] = _EMPTYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleJsonRequest = _reflection.GeneratedProtocolMessageType('SimpleJsonRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLEJSONREQUEST,
  '__module__' : 'msgs_pb2'
  # @@protoc_insertion_point(class_scope:common.SimpleJsonRequest)
  })
_sym_db.RegisterMessage(SimpleJsonRequest)

SimpleJsonResponse = _reflection.GeneratedProtocolMessageType('SimpleJsonResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLEJSONRESPONSE,
  '__module__' : 'msgs_pb2'
  # @@protoc_insertion_point(class_scope:common.SimpleJsonResponse)
  })
_sym_db.RegisterMessage(SimpleJsonResponse)

EmptyRequest = _reflection.GeneratedProtocolMessageType('EmptyRequest', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYREQUEST,
  '__module__' : 'msgs_pb2'
  # @@protoc_insertion_point(class_scope:common.EmptyRequest)
  })
_sym_db.RegisterMessage(EmptyRequest)

EmptyResponse = _reflection.GeneratedProtocolMessageType('EmptyResponse', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYRESPONSE,
  '__module__' : 'msgs_pb2'
  # @@protoc_insertion_point(class_scope:common.EmptyResponse)
  })
_sym_db.RegisterMessage(EmptyResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
