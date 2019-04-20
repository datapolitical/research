# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: diplomacy_tensorflow/contrib/mpi_collectives/mpi_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from diplomacy_tensorflow.core.framework import tensor_shape_pb2 as diplomacy__tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from diplomacy_tensorflow.core.framework import types_pb2 as diplomacy__tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='diplomacy_tensorflow/contrib/mpi_collectives/mpi_message.proto',
  package='diplomacy.tensorflow.contrib.mpi_collectives',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>diplomacy_tensorflow/contrib/mpi_collectives/mpi_message.proto\x12,diplomacy.tensorflow.contrib.mpi_collectives\x1a\x36\x64iplomacy_tensorflow/core/framework/tensor_shape.proto\x1a/diplomacy_tensorflow/core/framework/types.proto\"\xb3\x02\n\nMPIRequest\x12\x14\n\x0crequest_rank\x18\x01 \x01(\x05\x12Z\n\x0crequest_type\x18\x02 \x01(\x0e\x32\x44.diplomacy.tensorflow.contrib.mpi_collectives.MPIRequest.RequestType\x12\x33\n\x0btensor_type\x18\x03 \x01(\x0e\x32\x1e.diplomacy.tensorflow.DataType\x12\x13\n\x0btensor_name\x18\x04 \x01(\t\x12<\n\x0ctensor_shape\x18\x05 \x01(\x0b\x32&.diplomacy.tensorflow.TensorShapeProto\"+\n\x0bRequestType\x12\r\n\tALLREDUCE\x10\x00\x12\r\n\tALLGATHER\x10\x01\"\xe9\x01\n\x0bMPIResponse\x12]\n\rresponse_type\x18\x01 \x01(\x0e\x32\x46.diplomacy.tensorflow.contrib.mpi_collectives.MPIResponse.ResponseType\x12\x13\n\x0btensor_name\x18\x02 \x01(\t\x12\x15\n\rerror_message\x18\x03 \x01(\t\"O\n\x0cResponseType\x12\r\n\tALLREDUCE\x10\x00\x12\r\n\tALLGATHER\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x08\n\x04\x44ONE\x10\x03\x12\x0c\n\x08SHUTDOWN\x10\x04\x62\x06proto3')
  ,
  dependencies=[diplomacy__tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2.DESCRIPTOR,diplomacy__tensorflow_dot_core_dot_framework_dot_types__pb2.DESCRIPTOR,])



_MPIREQUEST_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='diplomacy.tensorflow.contrib.mpi_collectives.MPIRequest.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALLREDUCE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALLGATHER', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=482,
  serialized_end=525,
)
_sym_db.RegisterEnumDescriptor(_MPIREQUEST_REQUESTTYPE)

_MPIRESPONSE_RESPONSETYPE = _descriptor.EnumDescriptor(
  name='ResponseType',
  full_name='diplomacy.tensorflow.contrib.mpi_collectives.MPIResponse.ResponseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALLREDUCE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALLGATHER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHUTDOWN', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=682,
  serialized_end=761,
)
_sym_db.RegisterEnumDescriptor(_MPIRESPONSE_RESPONSETYPE)


_MPIREQUEST = _descriptor.Descriptor(
  name='MPIRequest',
  full_name='diplomacy.tensorflow.contrib.mpi_collectives.MPIRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_rank', full_name='diplomacy.tensorflow.contrib.mpi_collectives.MPIRequest.request_rank', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_type', full_name='diplomacy.tensorflow.contrib.mpi_collectives.MPIRequest.request_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor_type', full_name='diplomacy.tensorflow.contrib.mpi_collectives.MPIRequest.tensor_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor_name', full_name='diplomacy.tensorflow.contrib.mpi_collectives.MPIRequest.tensor_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor_shape', full_name='diplomacy.tensorflow.contrib.mpi_collectives.MPIRequest.tensor_shape', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MPIREQUEST_REQUESTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=525,
)


_MPIRESPONSE = _descriptor.Descriptor(
  name='MPIResponse',
  full_name='diplomacy.tensorflow.contrib.mpi_collectives.MPIResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_type', full_name='diplomacy.tensorflow.contrib.mpi_collectives.MPIResponse.response_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor_name', full_name='diplomacy.tensorflow.contrib.mpi_collectives.MPIResponse.tensor_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='diplomacy.tensorflow.contrib.mpi_collectives.MPIResponse.error_message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MPIRESPONSE_RESPONSETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=528,
  serialized_end=761,
)

_MPIREQUEST.fields_by_name['request_type'].enum_type = _MPIREQUEST_REQUESTTYPE
_MPIREQUEST.fields_by_name['tensor_type'].enum_type = diplomacy__tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_MPIREQUEST.fields_by_name['tensor_shape'].message_type = diplomacy__tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_MPIREQUEST_REQUESTTYPE.containing_type = _MPIREQUEST
_MPIRESPONSE.fields_by_name['response_type'].enum_type = _MPIRESPONSE_RESPONSETYPE
_MPIRESPONSE_RESPONSETYPE.containing_type = _MPIRESPONSE
DESCRIPTOR.message_types_by_name['MPIRequest'] = _MPIREQUEST
DESCRIPTOR.message_types_by_name['MPIResponse'] = _MPIRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MPIRequest = _reflection.GeneratedProtocolMessageType('MPIRequest', (_message.Message,), dict(
  DESCRIPTOR = _MPIREQUEST,
  __module__ = 'diplomacy_tensorflow.contrib.mpi_collectives.mpi_message_pb2'
  # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.contrib.mpi_collectives.MPIRequest)
  ))
_sym_db.RegisterMessage(MPIRequest)

MPIResponse = _reflection.GeneratedProtocolMessageType('MPIResponse', (_message.Message,), dict(
  DESCRIPTOR = _MPIRESPONSE,
  __module__ = 'diplomacy_tensorflow.contrib.mpi_collectives.mpi_message_pb2'
  # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.contrib.mpi_collectives.MPIResponse)
  ))
_sym_db.RegisterMessage(MPIResponse)


# @@protoc_insertion_point(module_scope)