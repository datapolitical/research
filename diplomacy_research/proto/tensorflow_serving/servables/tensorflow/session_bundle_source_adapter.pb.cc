// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: tensorflow_serving/servables/tensorflow/session_bundle_source_adapter.proto

#include "tensorflow_serving/servables/tensorflow/session_bundle_source_adapter.pb.h"

#include <algorithm>

#include <google/protobuf/stubs/common.h>
#include <google/protobuf/stubs/port.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/wire_format_lite_inl.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// This is a temporary google only hack
#ifdef GOOGLE_PROTOBUF_ENFORCE_UNIQUENESS
#include "third_party/protobuf/version.h"
#endif
// @@protoc_insertion_point(includes)

namespace protobuf_tensorflow_5fserving_2fservables_2ftensorflow_2fsession_5fbundle_5fconfig_2eproto {
extern PROTOBUF_INTERNAL_EXPORT_protobuf_tensorflow_5fserving_2fservables_2ftensorflow_2fsession_5fbundle_5fconfig_2eproto ::google::protobuf::internal::SCCInfo<4> scc_info_SessionBundleConfig;
}  // namespace protobuf_tensorflow_5fserving_2fservables_2ftensorflow_2fsession_5fbundle_5fconfig_2eproto
namespace tensorflow {
namespace serving {
class SessionBundleSourceAdapterConfigDefaultTypeInternal {
 public:
  ::google::protobuf::internal::ExplicitlyConstructed<SessionBundleSourceAdapterConfig>
      _instance;
} _SessionBundleSourceAdapterConfig_default_instance_;
}  // namespace serving
}  // namespace tensorflow
namespace protobuf_tensorflow_5fserving_2fservables_2ftensorflow_2fsession_5fbundle_5fsource_5fadapter_2eproto {
static void InitDefaultsSessionBundleSourceAdapterConfig() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::tensorflow::serving::_SessionBundleSourceAdapterConfig_default_instance_;
    new (ptr) ::tensorflow::serving::SessionBundleSourceAdapterConfig();
    ::google::protobuf::internal::OnShutdownDestroyMessage(ptr);
  }
  ::tensorflow::serving::SessionBundleSourceAdapterConfig::InitAsDefaultInstance();
}

::google::protobuf::internal::SCCInfo<1> scc_info_SessionBundleSourceAdapterConfig =
    {{ATOMIC_VAR_INIT(::google::protobuf::internal::SCCInfoBase::kUninitialized), 1, InitDefaultsSessionBundleSourceAdapterConfig}, {
      &protobuf_tensorflow_5fserving_2fservables_2ftensorflow_2fsession_5fbundle_5fconfig_2eproto::scc_info_SessionBundleConfig.base,}};

void InitDefaults() {
  ::google::protobuf::internal::InitSCC(&scc_info_SessionBundleSourceAdapterConfig.base);
}

::google::protobuf::Metadata file_level_metadata[1];

const ::google::protobuf::uint32 TableStruct::offsets[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::tensorflow::serving::SessionBundleSourceAdapterConfig, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::tensorflow::serving::SessionBundleSourceAdapterConfig, config_),
};
static const ::google::protobuf::internal::MigrationSchema schemas[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, sizeof(::tensorflow::serving::SessionBundleSourceAdapterConfig)},
};

static ::google::protobuf::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::google::protobuf::Message*>(&::tensorflow::serving::_SessionBundleSourceAdapterConfig_default_instance_),
};

void protobuf_AssignDescriptors() {
  AddDescriptors();
  AssignDescriptors(
      "tensorflow_serving/servables/tensorflow/session_bundle_source_adapter.proto", schemas, file_default_instances, TableStruct::offsets,
      file_level_metadata, NULL, NULL);
}

void protobuf_AssignDescriptorsOnce() {
  static ::google::protobuf::internal::once_flag once;
  ::google::protobuf::internal::call_once(once, protobuf_AssignDescriptors);
}

void protobuf_RegisterTypes(const ::std::string&) GOOGLE_PROTOBUF_ATTRIBUTE_COLD;
void protobuf_RegisterTypes(const ::std::string&) {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::internal::RegisterAllTypes(file_level_metadata, 1);
}

void AddDescriptorsImpl() {
  InitDefaults();
  static const char descriptor[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
      "\nKtensorflow_serving/servables/tensorflo"
      "w/session_bundle_source_adapter.proto\022\022t"
      "ensorflow.serving\032Ctensorflow_serving/se"
      "rvables/tensorflow/session_bundle_config"
      ".proto\"[\n SessionBundleSourceAdapterConf"
      "ig\0227\n\006config\030\001 \001(\0132\'.tensorflow.serving."
      "SessionBundleConfigb\006proto3"
  };
  ::google::protobuf::DescriptorPool::InternalAddGeneratedFile(
      descriptor, 267);
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedFile(
    "tensorflow_serving/servables/tensorflow/session_bundle_source_adapter.proto", &protobuf_RegisterTypes);
  ::protobuf_tensorflow_5fserving_2fservables_2ftensorflow_2fsession_5fbundle_5fconfig_2eproto::AddDescriptors();
}

void AddDescriptors() {
  static ::google::protobuf::internal::once_flag once;
  ::google::protobuf::internal::call_once(once, AddDescriptorsImpl);
}
// Force AddDescriptors() to be called at dynamic initialization time.
struct StaticDescriptorInitializer {
  StaticDescriptorInitializer() {
    AddDescriptors();
  }
} static_descriptor_initializer;
}  // namespace protobuf_tensorflow_5fserving_2fservables_2ftensorflow_2fsession_5fbundle_5fsource_5fadapter_2eproto
namespace tensorflow {
namespace serving {

// ===================================================================

void SessionBundleSourceAdapterConfig::InitAsDefaultInstance() {
  ::tensorflow::serving::_SessionBundleSourceAdapterConfig_default_instance_._instance.get_mutable()->config_ = const_cast< ::tensorflow::serving::SessionBundleConfig*>(
      ::tensorflow::serving::SessionBundleConfig::internal_default_instance());
}
void SessionBundleSourceAdapterConfig::clear_config() {
  if (GetArenaNoVirtual() == NULL && config_ != NULL) {
    delete config_;
  }
  config_ = NULL;
}
#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int SessionBundleSourceAdapterConfig::kConfigFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

SessionBundleSourceAdapterConfig::SessionBundleSourceAdapterConfig()
  : ::google::protobuf::Message(), _internal_metadata_(NULL) {
  ::google::protobuf::internal::InitSCC(
      &protobuf_tensorflow_5fserving_2fservables_2ftensorflow_2fsession_5fbundle_5fsource_5fadapter_2eproto::scc_info_SessionBundleSourceAdapterConfig.base);
  SharedCtor();
  // @@protoc_insertion_point(constructor:tensorflow.serving.SessionBundleSourceAdapterConfig)
}
SessionBundleSourceAdapterConfig::SessionBundleSourceAdapterConfig(const SessionBundleSourceAdapterConfig& from)
  : ::google::protobuf::Message(),
      _internal_metadata_(NULL) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  if (from.has_config()) {
    config_ = new ::tensorflow::serving::SessionBundleConfig(*from.config_);
  } else {
    config_ = NULL;
  }
  // @@protoc_insertion_point(copy_constructor:tensorflow.serving.SessionBundleSourceAdapterConfig)
}

void SessionBundleSourceAdapterConfig::SharedCtor() {
  config_ = NULL;
}

SessionBundleSourceAdapterConfig::~SessionBundleSourceAdapterConfig() {
  // @@protoc_insertion_point(destructor:tensorflow.serving.SessionBundleSourceAdapterConfig)
  SharedDtor();
}

void SessionBundleSourceAdapterConfig::SharedDtor() {
  if (this != internal_default_instance()) delete config_;
}

void SessionBundleSourceAdapterConfig::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const ::google::protobuf::Descriptor* SessionBundleSourceAdapterConfig::descriptor() {
  ::protobuf_tensorflow_5fserving_2fservables_2ftensorflow_2fsession_5fbundle_5fsource_5fadapter_2eproto::protobuf_AssignDescriptorsOnce();
  return ::protobuf_tensorflow_5fserving_2fservables_2ftensorflow_2fsession_5fbundle_5fsource_5fadapter_2eproto::file_level_metadata[kIndexInFileMessages].descriptor;
}

const SessionBundleSourceAdapterConfig& SessionBundleSourceAdapterConfig::default_instance() {
  ::google::protobuf::internal::InitSCC(&protobuf_tensorflow_5fserving_2fservables_2ftensorflow_2fsession_5fbundle_5fsource_5fadapter_2eproto::scc_info_SessionBundleSourceAdapterConfig.base);
  return *internal_default_instance();
}


void SessionBundleSourceAdapterConfig::Clear() {
// @@protoc_insertion_point(message_clear_start:tensorflow.serving.SessionBundleSourceAdapterConfig)
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  if (GetArenaNoVirtual() == NULL && config_ != NULL) {
    delete config_;
  }
  config_ = NULL;
  _internal_metadata_.Clear();
}

bool SessionBundleSourceAdapterConfig::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!GOOGLE_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:tensorflow.serving.SessionBundleSourceAdapterConfig)
  for (;;) {
    ::std::pair<::google::protobuf::uint32, bool> p = input->ReadTagWithCutoffNoLastTag(127u);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // .tensorflow.serving.SessionBundleConfig config = 1;
      case 1: {
        if (static_cast< ::google::protobuf::uint8>(tag) ==
            static_cast< ::google::protobuf::uint8>(10u /* 10 & 0xFF */)) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessage(
               input, mutable_config()));
        } else {
          goto handle_unusual;
        }
        break;
      }

      default: {
      handle_unusual:
        if (tag == 0) {
          goto success;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, _internal_metadata_.mutable_unknown_fields()));
        break;
      }
    }
  }
success:
  // @@protoc_insertion_point(parse_success:tensorflow.serving.SessionBundleSourceAdapterConfig)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:tensorflow.serving.SessionBundleSourceAdapterConfig)
  return false;
#undef DO_
}

void SessionBundleSourceAdapterConfig::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:tensorflow.serving.SessionBundleSourceAdapterConfig)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // .tensorflow.serving.SessionBundleConfig config = 1;
  if (this->has_config()) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      1, this->_internal_config(), output);
  }

  if ((_internal_metadata_.have_unknown_fields() &&  ::google::protobuf::internal::GetProto3PreserveUnknownsDefault())) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        (::google::protobuf::internal::GetProto3PreserveUnknownsDefault()   ? _internal_metadata_.unknown_fields()   : _internal_metadata_.default_instance()), output);
  }
  // @@protoc_insertion_point(serialize_end:tensorflow.serving.SessionBundleSourceAdapterConfig)
}

::google::protobuf::uint8* SessionBundleSourceAdapterConfig::InternalSerializeWithCachedSizesToArray(
    bool deterministic, ::google::protobuf::uint8* target) const {
  (void)deterministic; // Unused
  // @@protoc_insertion_point(serialize_to_array_start:tensorflow.serving.SessionBundleSourceAdapterConfig)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // .tensorflow.serving.SessionBundleConfig config = 1;
  if (this->has_config()) {
    target = ::google::protobuf::internal::WireFormatLite::
      InternalWriteMessageToArray(
        1, this->_internal_config(), deterministic, target);
  }

  if ((_internal_metadata_.have_unknown_fields() &&  ::google::protobuf::internal::GetProto3PreserveUnknownsDefault())) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        (::google::protobuf::internal::GetProto3PreserveUnknownsDefault()   ? _internal_metadata_.unknown_fields()   : _internal_metadata_.default_instance()), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:tensorflow.serving.SessionBundleSourceAdapterConfig)
  return target;
}

size_t SessionBundleSourceAdapterConfig::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:tensorflow.serving.SessionBundleSourceAdapterConfig)
  size_t total_size = 0;

  if ((_internal_metadata_.have_unknown_fields() &&  ::google::protobuf::internal::GetProto3PreserveUnknownsDefault())) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        (::google::protobuf::internal::GetProto3PreserveUnknownsDefault()   ? _internal_metadata_.unknown_fields()   : _internal_metadata_.default_instance()));
  }
  // .tensorflow.serving.SessionBundleConfig config = 1;
  if (this->has_config()) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::MessageSize(
        *config_);
  }

  int cached_size = ::google::protobuf::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void SessionBundleSourceAdapterConfig::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:tensorflow.serving.SessionBundleSourceAdapterConfig)
  GOOGLE_DCHECK_NE(&from, this);
  const SessionBundleSourceAdapterConfig* source =
      ::google::protobuf::internal::DynamicCastToGenerated<const SessionBundleSourceAdapterConfig>(
          &from);
  if (source == NULL) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:tensorflow.serving.SessionBundleSourceAdapterConfig)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:tensorflow.serving.SessionBundleSourceAdapterConfig)
    MergeFrom(*source);
  }
}

void SessionBundleSourceAdapterConfig::MergeFrom(const SessionBundleSourceAdapterConfig& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:tensorflow.serving.SessionBundleSourceAdapterConfig)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from.has_config()) {
    mutable_config()->::tensorflow::serving::SessionBundleConfig::MergeFrom(from.config());
  }
}

void SessionBundleSourceAdapterConfig::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:tensorflow.serving.SessionBundleSourceAdapterConfig)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void SessionBundleSourceAdapterConfig::CopyFrom(const SessionBundleSourceAdapterConfig& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:tensorflow.serving.SessionBundleSourceAdapterConfig)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool SessionBundleSourceAdapterConfig::IsInitialized() const {
  return true;
}

void SessionBundleSourceAdapterConfig::Swap(SessionBundleSourceAdapterConfig* other) {
  if (other == this) return;
  InternalSwap(other);
}
void SessionBundleSourceAdapterConfig::InternalSwap(SessionBundleSourceAdapterConfig* other) {
  using std::swap;
  swap(config_, other->config_);
  _internal_metadata_.Swap(&other->_internal_metadata_);
}

::google::protobuf::Metadata SessionBundleSourceAdapterConfig::GetMetadata() const {
  protobuf_tensorflow_5fserving_2fservables_2ftensorflow_2fsession_5fbundle_5fsource_5fadapter_2eproto::protobuf_AssignDescriptorsOnce();
  return ::protobuf_tensorflow_5fserving_2fservables_2ftensorflow_2fsession_5fbundle_5fsource_5fadapter_2eproto::file_level_metadata[kIndexInFileMessages];
}


// @@protoc_insertion_point(namespace_scope)
}  // namespace serving
}  // namespace tensorflow
namespace google {
namespace protobuf {
template<> GOOGLE_PROTOBUF_ATTRIBUTE_NOINLINE ::tensorflow::serving::SessionBundleSourceAdapterConfig* Arena::CreateMaybeMessage< ::tensorflow::serving::SessionBundleSourceAdapterConfig >(Arena* arena) {
  return Arena::CreateInternal< ::tensorflow::serving::SessionBundleSourceAdapterConfig >(arena);
}
}  // namespace protobuf
}  // namespace google

// @@protoc_insertion_point(global_scope)
