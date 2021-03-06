# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: diplomacy_tensorflow/stream_executor/dnn.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='diplomacy_tensorflow/stream_executor/dnn.proto',
  package='stream_executor.dnn',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n.diplomacy_tensorflow/stream_executor/dnn.proto\x12\x13stream_executor.dnn\"\xe1\x01\n\x15TensorDescriptorProto\x12\x12\n\ndimensions\x18\x01 \x03(\x03\x12\x30\n\tdata_type\x18\x02 \x01(\x0e\x32\x1d.stream_executor.dnn.DataType\x12\x36\n\x0b\x64\x61ta_layout\x18\x03 \x01(\x0e\x32\x1f.stream_executor.dnn.DataLayoutH\x00\x12:\n\rfilter_layout\x18\x04 \x01(\x0e\x32!.stream_executor.dnn.FilterLayoutH\x00\x42\x0e\n\x0clayout_oneof\"\x94\x01\n\x0e\x41lgorithmProto\x12\x0f\n\x07\x61lgo_id\x18\x01 \x01(\x03\x12?\n\tmath_type\x18\x02 \x01(\x0e\x32,.stream_executor.dnn.AlgorithmProto.MathType\"0\n\x08MathType\x12\x10\n\x0c\x44\x45\x46\x41ULT_MATH\x10\x00\x12\x12\n\x0eTENSOR_OP_MATH\x10\x01\"\xdc\x01\n\x1a\x43onvolutionDescriptorProto\x12\x10\n\x08paddings\x18\x01 \x03(\x03\x12\x0f\n\x07strides\x18\x02 \x03(\x03\x12\x11\n\tdilations\x18\x03 \x03(\x03\x12\x33\n\x0c\x63ompute_mode\x18\x04 \x01(\x0e\x32\x1d.stream_executor.dnn.DataType\x12\x13\n\x0bgroup_count\x18\x05 \x01(\x05\x12>\n\x10\x63onvolution_mode\x18\x06 \x01(\x0e\x32$.stream_executor.dnn.ConvolutionMode*E\n\x08\x44\x61taType\x12\n\n\x06kFloat\x10\x00\x12\x0b\n\x07kDouble\x10\x01\x12\t\n\x05kHalf\x10\x02\x12\t\n\x05kInt8\x10\x03\x12\n\n\x06kInt32\x10\x04*l\n\nDataLayout\x12\x11\n\rkYXDepthBatch\x10\x00\x12\x11\n\rkYXBatchDepth\x10\x01\x12\x11\n\rkBatchYXDepth\x10\x02\x12\x11\n\rkBatchDepthYX\x10\x03\x12\x12\n\x0ekBatchDepthYX4\x10\x04*s\n\x0c\x46ilterLayout\x12\x12\n\x0ekOutputInputYX\x10\x00\x12\x12\n\x0ekOutputYXInput\x10\x01\x12\x13\n\x0fkOutputInputYX4\x10\x02\x12\x12\n\x0ekInputYXOutput\x10\x03\x12\x12\n\x0ekYXInputOutput\x10\x04*f\n\x0e\x41\x63tivationMode\x12\t\n\x05kNone\x10\x00\x12\x0c\n\x08kSigmoid\x10\x01\x12\t\n\x05kRelu\x10\x02\x12\n\n\x06kRelu6\x10\x03\x12\n\n\x06kReluX\x10\x04\x12\t\n\x05kTanh\x10\x05\x12\r\n\tkBandPass\x10\x06*9\n\x0f\x43onvolutionMode\x12\x15\n\x11\x43ROSS_CORRELATION\x10\x00\x12\x0f\n\x0b\x43ONVOLUTION\x10\x01\x62\x06proto3')
)

_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='stream_executor.dnn.DataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kFloat', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kDouble', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kHalf', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kInt8', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kInt32', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=673,
  serialized_end=742,
)
_sym_db.RegisterEnumDescriptor(_DATATYPE)

DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
_DATALAYOUT = _descriptor.EnumDescriptor(
  name='DataLayout',
  full_name='stream_executor.dnn.DataLayout',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kYXDepthBatch', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kYXBatchDepth', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kBatchYXDepth', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kBatchDepthYX', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kBatchDepthYX4', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=744,
  serialized_end=852,
)
_sym_db.RegisterEnumDescriptor(_DATALAYOUT)

DataLayout = enum_type_wrapper.EnumTypeWrapper(_DATALAYOUT)
_FILTERLAYOUT = _descriptor.EnumDescriptor(
  name='FilterLayout',
  full_name='stream_executor.dnn.FilterLayout',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kOutputInputYX', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kOutputYXInput', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kOutputInputYX4', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kInputYXOutput', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kYXInputOutput', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=854,
  serialized_end=969,
)
_sym_db.RegisterEnumDescriptor(_FILTERLAYOUT)

FilterLayout = enum_type_wrapper.EnumTypeWrapper(_FILTERLAYOUT)
_ACTIVATIONMODE = _descriptor.EnumDescriptor(
  name='ActivationMode',
  full_name='stream_executor.dnn.ActivationMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kNone', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kSigmoid', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kRelu', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kRelu6', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kReluX', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kTanh', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kBandPass', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=971,
  serialized_end=1073,
)
_sym_db.RegisterEnumDescriptor(_ACTIVATIONMODE)

ActivationMode = enum_type_wrapper.EnumTypeWrapper(_ACTIVATIONMODE)
_CONVOLUTIONMODE = _descriptor.EnumDescriptor(
  name='ConvolutionMode',
  full_name='stream_executor.dnn.ConvolutionMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CROSS_CORRELATION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONVOLUTION', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1075,
  serialized_end=1132,
)
_sym_db.RegisterEnumDescriptor(_CONVOLUTIONMODE)

ConvolutionMode = enum_type_wrapper.EnumTypeWrapper(_CONVOLUTIONMODE)
kFloat = 0
kDouble = 1
kHalf = 2
kInt8 = 3
kInt32 = 4
kYXDepthBatch = 0
kYXBatchDepth = 1
kBatchYXDepth = 2
kBatchDepthYX = 3
kBatchDepthYX4 = 4
kOutputInputYX = 0
kOutputYXInput = 1
kOutputInputYX4 = 2
kInputYXOutput = 3
kYXInputOutput = 4
kNone = 0
kSigmoid = 1
kRelu = 2
kRelu6 = 3
kReluX = 4
kTanh = 5
kBandPass = 6
CROSS_CORRELATION = 0
CONVOLUTION = 1


_ALGORITHMPROTO_MATHTYPE = _descriptor.EnumDescriptor(
  name='MathType',
  full_name='stream_executor.dnn.AlgorithmProto.MathType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT_MATH', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TENSOR_OP_MATH', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=400,
  serialized_end=448,
)
_sym_db.RegisterEnumDescriptor(_ALGORITHMPROTO_MATHTYPE)


_TENSORDESCRIPTORPROTO = _descriptor.Descriptor(
  name='TensorDescriptorProto',
  full_name='stream_executor.dnn.TensorDescriptorProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='stream_executor.dnn.TensorDescriptorProto.dimensions', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='stream_executor.dnn.TensorDescriptorProto.data_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_layout', full_name='stream_executor.dnn.TensorDescriptorProto.data_layout', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter_layout', full_name='stream_executor.dnn.TensorDescriptorProto.filter_layout', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
    _descriptor.OneofDescriptor(
      name='layout_oneof', full_name='stream_executor.dnn.TensorDescriptorProto.layout_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=72,
  serialized_end=297,
)


_ALGORITHMPROTO = _descriptor.Descriptor(
  name='AlgorithmProto',
  full_name='stream_executor.dnn.AlgorithmProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='algo_id', full_name='stream_executor.dnn.AlgorithmProto.algo_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='math_type', full_name='stream_executor.dnn.AlgorithmProto.math_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ALGORITHMPROTO_MATHTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=448,
)


_CONVOLUTIONDESCRIPTORPROTO = _descriptor.Descriptor(
  name='ConvolutionDescriptorProto',
  full_name='stream_executor.dnn.ConvolutionDescriptorProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='paddings', full_name='stream_executor.dnn.ConvolutionDescriptorProto.paddings', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strides', full_name='stream_executor.dnn.ConvolutionDescriptorProto.strides', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dilations', full_name='stream_executor.dnn.ConvolutionDescriptorProto.dilations', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compute_mode', full_name='stream_executor.dnn.ConvolutionDescriptorProto.compute_mode', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_count', full_name='stream_executor.dnn.ConvolutionDescriptorProto.group_count', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='convolution_mode', full_name='stream_executor.dnn.ConvolutionDescriptorProto.convolution_mode', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=451,
  serialized_end=671,
)

_TENSORDESCRIPTORPROTO.fields_by_name['data_type'].enum_type = _DATATYPE
_TENSORDESCRIPTORPROTO.fields_by_name['data_layout'].enum_type = _DATALAYOUT
_TENSORDESCRIPTORPROTO.fields_by_name['filter_layout'].enum_type = _FILTERLAYOUT
_TENSORDESCRIPTORPROTO.oneofs_by_name['layout_oneof'].fields.append(
  _TENSORDESCRIPTORPROTO.fields_by_name['data_layout'])
_TENSORDESCRIPTORPROTO.fields_by_name['data_layout'].containing_oneof = _TENSORDESCRIPTORPROTO.oneofs_by_name['layout_oneof']
_TENSORDESCRIPTORPROTO.oneofs_by_name['layout_oneof'].fields.append(
  _TENSORDESCRIPTORPROTO.fields_by_name['filter_layout'])
_TENSORDESCRIPTORPROTO.fields_by_name['filter_layout'].containing_oneof = _TENSORDESCRIPTORPROTO.oneofs_by_name['layout_oneof']
_ALGORITHMPROTO.fields_by_name['math_type'].enum_type = _ALGORITHMPROTO_MATHTYPE
_ALGORITHMPROTO_MATHTYPE.containing_type = _ALGORITHMPROTO
_CONVOLUTIONDESCRIPTORPROTO.fields_by_name['compute_mode'].enum_type = _DATATYPE
_CONVOLUTIONDESCRIPTORPROTO.fields_by_name['convolution_mode'].enum_type = _CONVOLUTIONMODE
DESCRIPTOR.message_types_by_name['TensorDescriptorProto'] = _TENSORDESCRIPTORPROTO
DESCRIPTOR.message_types_by_name['AlgorithmProto'] = _ALGORITHMPROTO
DESCRIPTOR.message_types_by_name['ConvolutionDescriptorProto'] = _CONVOLUTIONDESCRIPTORPROTO
DESCRIPTOR.enum_types_by_name['DataType'] = _DATATYPE
DESCRIPTOR.enum_types_by_name['DataLayout'] = _DATALAYOUT
DESCRIPTOR.enum_types_by_name['FilterLayout'] = _FILTERLAYOUT
DESCRIPTOR.enum_types_by_name['ActivationMode'] = _ACTIVATIONMODE
DESCRIPTOR.enum_types_by_name['ConvolutionMode'] = _CONVOLUTIONMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TensorDescriptorProto = _reflection.GeneratedProtocolMessageType('TensorDescriptorProto', (_message.Message,), dict(
  DESCRIPTOR = _TENSORDESCRIPTORPROTO,
  __module__ = 'diplomacy_tensorflow.stream_executor.dnn_pb2'
  # @@protoc_insertion_point(class_scope:stream_executor.dnn.TensorDescriptorProto)
  ))
_sym_db.RegisterMessage(TensorDescriptorProto)

AlgorithmProto = _reflection.GeneratedProtocolMessageType('AlgorithmProto', (_message.Message,), dict(
  DESCRIPTOR = _ALGORITHMPROTO,
  __module__ = 'diplomacy_tensorflow.stream_executor.dnn_pb2'
  # @@protoc_insertion_point(class_scope:stream_executor.dnn.AlgorithmProto)
  ))
_sym_db.RegisterMessage(AlgorithmProto)

ConvolutionDescriptorProto = _reflection.GeneratedProtocolMessageType('ConvolutionDescriptorProto', (_message.Message,), dict(
  DESCRIPTOR = _CONVOLUTIONDESCRIPTORPROTO,
  __module__ = 'diplomacy_tensorflow.stream_executor.dnn_pb2'
  # @@protoc_insertion_point(class_scope:stream_executor.dnn.ConvolutionDescriptorProto)
  ))
_sym_db.RegisterMessage(ConvolutionDescriptorProto)


# @@protoc_insertion_point(module_scope)
