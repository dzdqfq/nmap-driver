# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mgrpc/dom.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import msgs_pb2 as common_dot_msgs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mgrpc/dom.proto',
  package='rpc',
  syntax='proto3',
  serialized_options=b'\n\026net.skycloud.proto.rpcZ%github.com/sky-cloud-tec/proto/v1/rpc',
  serialized_pb=b'\n\x0fmgrpc/dom.proto\x12\x03rpc\x1a\x11\x63ommon/msgs.proto\"+\n\x1aWithNameIpPortTokenRequest\x12\r\n\x05token\x18\n \x01(\t2Y\n\x0c\x41gentService\x12I\n\rRegisterAgent\x12\x1f.rpc.WithNameIpPortTokenRequest\x1a\x15.common.EmptyResponse\"\x00\x42?\n\x16net.skycloud.proto.rpcZ%github.com/sky-cloud-tec/proto/v1/rpcb\x06proto3'
  ,
  dependencies=[common_dot_msgs__pb2.DESCRIPTOR,])




_WITHNAMEIPPORTTOKENREQUEST = _descriptor.Descriptor(
  name='WithNameIpPortTokenRequest',
  full_name='rpc.WithNameIpPortTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='rpc.WithNameIpPortTokenRequest.token', index=0,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=43,
  serialized_end=86,
)

DESCRIPTOR.message_types_by_name['WithNameIpPortTokenRequest'] = _WITHNAMEIPPORTTOKENREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WithNameIpPortTokenRequest = _reflection.GeneratedProtocolMessageType('WithNameIpPortTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _WITHNAMEIPPORTTOKENREQUEST,
  '__module__' : 'mgrpc.dom_pb2'
  # @@protoc_insertion_point(class_scope:rpc.WithNameIpPortTokenRequest)
  })
_sym_db.RegisterMessage(WithNameIpPortTokenRequest)


DESCRIPTOR._options = None

_AGENTSERVICE = _descriptor.ServiceDescriptor(
  name='AgentService',
  full_name='rpc.AgentService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=88,
  serialized_end=177,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterAgent',
    full_name='rpc.AgentService.RegisterAgent',
    index=0,
    containing_service=None,
    input_type=_WITHNAMEIPPORTTOKENREQUEST,
    output_type=common_dot_msgs__pb2._EMPTYRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AGENTSERVICE)

DESCRIPTOR.services_by_name['AgentService'] = _AGENTSERVICE

# @@protoc_insertion_point(module_scope)