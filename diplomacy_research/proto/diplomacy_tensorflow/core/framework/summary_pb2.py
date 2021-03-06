# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: diplomacy_tensorflow/core/framework/summary.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from diplomacy_tensorflow.core.framework import tensor_pb2 as diplomacy__tensorflow_dot_core_dot_framework_dot_tensor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='diplomacy_tensorflow/core/framework/summary.proto',
  package='diplomacy.tensorflow',
  syntax='proto3',
  serialized_options=_b('\n\030org.tensorflow.frameworkB\rSummaryProtosP\001Z=github.com/tensorflow/tensorflow/tensorflow/go/core/framework\370\001\001'),
  serialized_pb=_b('\n1diplomacy_tensorflow/core/framework/summary.proto\x12\x14\x64iplomacy.tensorflow\x1a\x30\x64iplomacy_tensorflow/core/framework/tensor.proto\"\'\n\x12SummaryDescription\x12\x11\n\ttype_hint\x18\x01 \x01(\t\"\x87\x01\n\x0eHistogramProto\x12\x0b\n\x03min\x18\x01 \x01(\x01\x12\x0b\n\x03max\x18\x02 \x01(\x01\x12\x0b\n\x03num\x18\x03 \x01(\x01\x12\x0b\n\x03sum\x18\x04 \x01(\x01\x12\x13\n\x0bsum_squares\x18\x05 \x01(\x01\x12\x18\n\x0c\x62ucket_limit\x18\x06 \x03(\x01\x42\x02\x10\x01\x12\x12\n\x06\x62ucket\x18\x07 \x03(\x01\x42\x02\x10\x01\"\xbf\x01\n\x0fSummaryMetadata\x12\x45\n\x0bplugin_data\x18\x01 \x01(\x0b\x32\x30.diplomacy.tensorflow.SummaryMetadata.PluginData\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x1b\n\x13summary_description\x18\x03 \x01(\t\x1a\x32\n\nPluginData\x12\x13\n\x0bplugin_name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"\x9a\x05\n\x07Summary\x12\x32\n\x05value\x18\x01 \x03(\x0b\x32#.diplomacy.tensorflow.Summary.Value\x1aX\n\x05Image\x12\x0e\n\x06height\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x12\n\ncolorspace\x18\x03 \x01(\x05\x12\x1c\n\x14\x65ncoded_image_string\x18\x04 \x01(\x0c\x1a}\n\x05\x41udio\x12\x13\n\x0bsample_rate\x18\x01 \x01(\x02\x12\x14\n\x0cnum_channels\x18\x02 \x01(\x03\x12\x15\n\rlength_frames\x18\x03 \x01(\x03\x12\x1c\n\x14\x65ncoded_audio_string\x18\x04 \x01(\x0c\x12\x14\n\x0c\x63ontent_type\x18\x05 \x01(\t\x1a\x81\x03\n\x05Value\x12\x11\n\tnode_name\x18\x07 \x01(\t\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x37\n\x08metadata\x18\t \x01(\x0b\x32%.diplomacy.tensorflow.SummaryMetadata\x12\x16\n\x0csimple_value\x18\x02 \x01(\x02H\x00\x12&\n\x1cobsolete_old_style_histogram\x18\x03 \x01(\x0cH\x00\x12\x34\n\x05image\x18\x04 \x01(\x0b\x32#.diplomacy.tensorflow.Summary.ImageH\x00\x12\x35\n\x05histo\x18\x05 \x01(\x0b\x32$.diplomacy.tensorflow.HistogramProtoH\x00\x12\x34\n\x05\x61udio\x18\x06 \x01(\x0b\x32#.diplomacy.tensorflow.Summary.AudioH\x00\x12\x33\n\x06tensor\x18\x08 \x01(\x0b\x32!.diplomacy.tensorflow.TensorProtoH\x00\x42\x07\n\x05valueBm\n\x18org.tensorflow.frameworkB\rSummaryProtosP\x01Z=github.com/tensorflow/tensorflow/tensorflow/go/core/framework\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[diplomacy__tensorflow_dot_core_dot_framework_dot_tensor__pb2.DESCRIPTOR,])




_SUMMARYDESCRIPTION = _descriptor.Descriptor(
  name='SummaryDescription',
  full_name='diplomacy.tensorflow.SummaryDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type_hint', full_name='diplomacy.tensorflow.SummaryDescription.type_hint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=125,
  serialized_end=164,
)


_HISTOGRAMPROTO = _descriptor.Descriptor(
  name='HistogramProto',
  full_name='diplomacy.tensorflow.HistogramProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='diplomacy.tensorflow.HistogramProto.min', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='diplomacy.tensorflow.HistogramProto.max', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num', full_name='diplomacy.tensorflow.HistogramProto.num', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sum', full_name='diplomacy.tensorflow.HistogramProto.sum', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sum_squares', full_name='diplomacy.tensorflow.HistogramProto.sum_squares', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucket_limit', full_name='diplomacy.tensorflow.HistogramProto.bucket_limit', index=5,
      number=6, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='diplomacy.tensorflow.HistogramProto.bucket', index=6,
      number=7, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
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
  serialized_start=167,
  serialized_end=302,
)


_SUMMARYMETADATA_PLUGINDATA = _descriptor.Descriptor(
  name='PluginData',
  full_name='diplomacy.tensorflow.SummaryMetadata.PluginData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plugin_name', full_name='diplomacy.tensorflow.SummaryMetadata.PluginData.plugin_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='diplomacy.tensorflow.SummaryMetadata.PluginData.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=446,
  serialized_end=496,
)

_SUMMARYMETADATA = _descriptor.Descriptor(
  name='SummaryMetadata',
  full_name='diplomacy.tensorflow.SummaryMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plugin_data', full_name='diplomacy.tensorflow.SummaryMetadata.plugin_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='diplomacy.tensorflow.SummaryMetadata.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='summary_description', full_name='diplomacy.tensorflow.SummaryMetadata.summary_description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SUMMARYMETADATA_PLUGINDATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=496,
)


_SUMMARY_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='diplomacy.tensorflow.Summary.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='diplomacy.tensorflow.Summary.Image.height', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='diplomacy.tensorflow.Summary.Image.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='colorspace', full_name='diplomacy.tensorflow.Summary.Image.colorspace', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoded_image_string', full_name='diplomacy.tensorflow.Summary.Image.encoded_image_string', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=562,
  serialized_end=650,
)

_SUMMARY_AUDIO = _descriptor.Descriptor(
  name='Audio',
  full_name='diplomacy.tensorflow.Summary.Audio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sample_rate', full_name='diplomacy.tensorflow.Summary.Audio.sample_rate', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_channels', full_name='diplomacy.tensorflow.Summary.Audio.num_channels', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length_frames', full_name='diplomacy.tensorflow.Summary.Audio.length_frames', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoded_audio_string', full_name='diplomacy.tensorflow.Summary.Audio.encoded_audio_string', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='diplomacy.tensorflow.Summary.Audio.content_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=652,
  serialized_end=777,
)

_SUMMARY_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='diplomacy.tensorflow.Summary.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='diplomacy.tensorflow.Summary.Value.node_name', index=0,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='diplomacy.tensorflow.Summary.Value.tag', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='diplomacy.tensorflow.Summary.Value.metadata', index=2,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='simple_value', full_name='diplomacy.tensorflow.Summary.Value.simple_value', index=3,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obsolete_old_style_histogram', full_name='diplomacy.tensorflow.Summary.Value.obsolete_old_style_histogram', index=4,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='diplomacy.tensorflow.Summary.Value.image', index=5,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='histo', full_name='diplomacy.tensorflow.Summary.Value.histo', index=6,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audio', full_name='diplomacy.tensorflow.Summary.Value.audio', index=7,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor', full_name='diplomacy.tensorflow.Summary.Value.tensor', index=8,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
      name='value', full_name='diplomacy.tensorflow.Summary.Value.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=780,
  serialized_end=1165,
)

_SUMMARY = _descriptor.Descriptor(
  name='Summary',
  full_name='diplomacy.tensorflow.Summary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='diplomacy.tensorflow.Summary.value', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SUMMARY_IMAGE, _SUMMARY_AUDIO, _SUMMARY_VALUE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=499,
  serialized_end=1165,
)

_SUMMARYMETADATA_PLUGINDATA.containing_type = _SUMMARYMETADATA
_SUMMARYMETADATA.fields_by_name['plugin_data'].message_type = _SUMMARYMETADATA_PLUGINDATA
_SUMMARY_IMAGE.containing_type = _SUMMARY
_SUMMARY_AUDIO.containing_type = _SUMMARY
_SUMMARY_VALUE.fields_by_name['metadata'].message_type = _SUMMARYMETADATA
_SUMMARY_VALUE.fields_by_name['image'].message_type = _SUMMARY_IMAGE
_SUMMARY_VALUE.fields_by_name['histo'].message_type = _HISTOGRAMPROTO
_SUMMARY_VALUE.fields_by_name['audio'].message_type = _SUMMARY_AUDIO
_SUMMARY_VALUE.fields_by_name['tensor'].message_type = diplomacy__tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
_SUMMARY_VALUE.containing_type = _SUMMARY
_SUMMARY_VALUE.oneofs_by_name['value'].fields.append(
  _SUMMARY_VALUE.fields_by_name['simple_value'])
_SUMMARY_VALUE.fields_by_name['simple_value'].containing_oneof = _SUMMARY_VALUE.oneofs_by_name['value']
_SUMMARY_VALUE.oneofs_by_name['value'].fields.append(
  _SUMMARY_VALUE.fields_by_name['obsolete_old_style_histogram'])
_SUMMARY_VALUE.fields_by_name['obsolete_old_style_histogram'].containing_oneof = _SUMMARY_VALUE.oneofs_by_name['value']
_SUMMARY_VALUE.oneofs_by_name['value'].fields.append(
  _SUMMARY_VALUE.fields_by_name['image'])
_SUMMARY_VALUE.fields_by_name['image'].containing_oneof = _SUMMARY_VALUE.oneofs_by_name['value']
_SUMMARY_VALUE.oneofs_by_name['value'].fields.append(
  _SUMMARY_VALUE.fields_by_name['histo'])
_SUMMARY_VALUE.fields_by_name['histo'].containing_oneof = _SUMMARY_VALUE.oneofs_by_name['value']
_SUMMARY_VALUE.oneofs_by_name['value'].fields.append(
  _SUMMARY_VALUE.fields_by_name['audio'])
_SUMMARY_VALUE.fields_by_name['audio'].containing_oneof = _SUMMARY_VALUE.oneofs_by_name['value']
_SUMMARY_VALUE.oneofs_by_name['value'].fields.append(
  _SUMMARY_VALUE.fields_by_name['tensor'])
_SUMMARY_VALUE.fields_by_name['tensor'].containing_oneof = _SUMMARY_VALUE.oneofs_by_name['value']
_SUMMARY.fields_by_name['value'].message_type = _SUMMARY_VALUE
DESCRIPTOR.message_types_by_name['SummaryDescription'] = _SUMMARYDESCRIPTION
DESCRIPTOR.message_types_by_name['HistogramProto'] = _HISTOGRAMPROTO
DESCRIPTOR.message_types_by_name['SummaryMetadata'] = _SUMMARYMETADATA
DESCRIPTOR.message_types_by_name['Summary'] = _SUMMARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SummaryDescription = _reflection.GeneratedProtocolMessageType('SummaryDescription', (_message.Message,), dict(
  DESCRIPTOR = _SUMMARYDESCRIPTION,
  __module__ = 'diplomacy_tensorflow.core.framework.summary_pb2'
  # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.SummaryDescription)
  ))
_sym_db.RegisterMessage(SummaryDescription)

HistogramProto = _reflection.GeneratedProtocolMessageType('HistogramProto', (_message.Message,), dict(
  DESCRIPTOR = _HISTOGRAMPROTO,
  __module__ = 'diplomacy_tensorflow.core.framework.summary_pb2'
  # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.HistogramProto)
  ))
_sym_db.RegisterMessage(HistogramProto)

SummaryMetadata = _reflection.GeneratedProtocolMessageType('SummaryMetadata', (_message.Message,), dict(

  PluginData = _reflection.GeneratedProtocolMessageType('PluginData', (_message.Message,), dict(
    DESCRIPTOR = _SUMMARYMETADATA_PLUGINDATA,
    __module__ = 'diplomacy_tensorflow.core.framework.summary_pb2'
    # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.SummaryMetadata.PluginData)
    ))
  ,
  DESCRIPTOR = _SUMMARYMETADATA,
  __module__ = 'diplomacy_tensorflow.core.framework.summary_pb2'
  # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.SummaryMetadata)
  ))
_sym_db.RegisterMessage(SummaryMetadata)
_sym_db.RegisterMessage(SummaryMetadata.PluginData)

Summary = _reflection.GeneratedProtocolMessageType('Summary', (_message.Message,), dict(

  Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), dict(
    DESCRIPTOR = _SUMMARY_IMAGE,
    __module__ = 'diplomacy_tensorflow.core.framework.summary_pb2'
    # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.Summary.Image)
    ))
  ,

  Audio = _reflection.GeneratedProtocolMessageType('Audio', (_message.Message,), dict(
    DESCRIPTOR = _SUMMARY_AUDIO,
    __module__ = 'diplomacy_tensorflow.core.framework.summary_pb2'
    # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.Summary.Audio)
    ))
  ,

  Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(
    DESCRIPTOR = _SUMMARY_VALUE,
    __module__ = 'diplomacy_tensorflow.core.framework.summary_pb2'
    # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.Summary.Value)
    ))
  ,
  DESCRIPTOR = _SUMMARY,
  __module__ = 'diplomacy_tensorflow.core.framework.summary_pb2'
  # @@protoc_insertion_point(class_scope:diplomacy.tensorflow.Summary)
  ))
_sym_db.RegisterMessage(Summary)
_sym_db.RegisterMessage(Summary.Image)
_sym_db.RegisterMessage(Summary.Audio)
_sym_db.RegisterMessage(Summary.Value)


DESCRIPTOR._options = None
_HISTOGRAMPROTO.fields_by_name['bucket_limit']._options = None
_HISTOGRAMPROTO.fields_by_name['bucket']._options = None
# @@protoc_insertion_point(module_scope)
