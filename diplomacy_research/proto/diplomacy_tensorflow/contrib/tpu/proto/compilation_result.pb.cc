// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: diplomacy_tensorflow/contrib/tpu/proto/compilation_result.proto

#include "diplomacy_tensorflow/contrib/tpu/proto/compilation_result.pb.h"

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

namespace protobuf_diplomacy_5ftensorflow_2fcompiler_2fxla_2fservice_2fhlo_2eproto {
extern PROTOBUF_INTERNAL_EXPORT_protobuf_diplomacy_5ftensorflow_2fcompiler_2fxla_2fservice_2fhlo_2eproto ::google::protobuf::internal::SCCInfo<2> scc_info_HloProto;
}  // namespace protobuf_diplomacy_5ftensorflow_2fcompiler_2fxla_2fservice_2fhlo_2eproto
namespace diplomacy {
namespace tensorflow {
namespace tpu {
class CompilationResultProtoDefaultTypeInternal {
 public:
  ::google::protobuf::internal::ExplicitlyConstructed<CompilationResultProto>
      _instance;
} _CompilationResultProto_default_instance_;
}  // namespace tpu
}  // namespace tensorflow
}  // namespace diplomacy
namespace protobuf_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2fcompilation_5fresult_2eproto {
static void InitDefaultsCompilationResultProto() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::diplomacy::tensorflow::tpu::_CompilationResultProto_default_instance_;
    new (ptr) ::diplomacy::tensorflow::tpu::CompilationResultProto();
    ::google::protobuf::internal::OnShutdownDestroyMessage(ptr);
  }
  ::diplomacy::tensorflow::tpu::CompilationResultProto::InitAsDefaultInstance();
}

::google::protobuf::internal::SCCInfo<1> scc_info_CompilationResultProto =
    {{ATOMIC_VAR_INIT(::google::protobuf::internal::SCCInfoBase::kUninitialized), 1, InitDefaultsCompilationResultProto}, {
      &protobuf_diplomacy_5ftensorflow_2fcompiler_2fxla_2fservice_2fhlo_2eproto::scc_info_HloProto.base,}};

void InitDefaults() {
  ::google::protobuf::internal::InitSCC(&scc_info_CompilationResultProto.base);
}

::google::protobuf::Metadata file_level_metadata[1];

const ::google::protobuf::uint32 TableStruct::offsets[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::diplomacy::tensorflow::tpu::CompilationResultProto, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::diplomacy::tensorflow::tpu::CompilationResultProto, status_code_),
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::diplomacy::tensorflow::tpu::CompilationResultProto, status_error_message_),
  GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(::diplomacy::tensorflow::tpu::CompilationResultProto, hlo_protos_),
};
static const ::google::protobuf::internal::MigrationSchema schemas[] GOOGLE_PROTOBUF_ATTRIBUTE_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, sizeof(::diplomacy::tensorflow::tpu::CompilationResultProto)},
};

static ::google::protobuf::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::google::protobuf::Message*>(&::diplomacy::tensorflow::tpu::_CompilationResultProto_default_instance_),
};

void protobuf_AssignDescriptors() {
  AddDescriptors();
  AssignDescriptors(
      "diplomacy_tensorflow/contrib/tpu/proto/compilation_result.proto", schemas, file_default_instances, TableStruct::offsets,
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
      "\n\?diplomacy_tensorflow/contrib/tpu/proto"
      "/compilation_result.proto\022\030diplomacy.ten"
      "sorflow.tpu\0323diplomacy_tensorflow/compil"
      "er/xla/service/hlo.proto\0324diplomacy_tens"
      "orflow/core/lib/core/error_codes.proto\"\220"
      "\001\n\026CompilationResultProto\0225\n\013status_code"
      "\030\001 \001(\0162 .diplomacy.tensorflow.error.Code"
      "\022\034\n\024status_error_message\030\002 \001(\t\022!\n\nhlo_pr"
      "otos\030\003 \003(\0132\r.xla.HloProtoB\003\370\001\001b\006proto3"
  };
  ::google::protobuf::DescriptorPool::InternalAddGeneratedFile(
      descriptor, 358);
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedFile(
    "diplomacy_tensorflow/contrib/tpu/proto/compilation_result.proto", &protobuf_RegisterTypes);
  ::protobuf_diplomacy_5ftensorflow_2fcompiler_2fxla_2fservice_2fhlo_2eproto::AddDescriptors();
  ::protobuf_diplomacy_5ftensorflow_2fcore_2flib_2fcore_2ferror_5fcodes_2eproto::AddDescriptors();
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
}  // namespace protobuf_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2fcompilation_5fresult_2eproto
namespace diplomacy {
namespace tensorflow {
namespace tpu {

// ===================================================================

void CompilationResultProto::InitAsDefaultInstance() {
}
void CompilationResultProto::clear_hlo_protos() {
  hlo_protos_.Clear();
}
#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int CompilationResultProto::kStatusCodeFieldNumber;
const int CompilationResultProto::kStatusErrorMessageFieldNumber;
const int CompilationResultProto::kHloProtosFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

CompilationResultProto::CompilationResultProto()
  : ::google::protobuf::Message(), _internal_metadata_(NULL) {
  ::google::protobuf::internal::InitSCC(
      &protobuf_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2fcompilation_5fresult_2eproto::scc_info_CompilationResultProto.base);
  SharedCtor();
  // @@protoc_insertion_point(constructor:diplomacy.tensorflow.tpu.CompilationResultProto)
}
CompilationResultProto::CompilationResultProto(::google::protobuf::Arena* arena)
  : ::google::protobuf::Message(),
  _internal_metadata_(arena),
  hlo_protos_(arena) {
  ::google::protobuf::internal::InitSCC(&protobuf_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2fcompilation_5fresult_2eproto::scc_info_CompilationResultProto.base);
  SharedCtor();
  RegisterArenaDtor(arena);
  // @@protoc_insertion_point(arena_constructor:diplomacy.tensorflow.tpu.CompilationResultProto)
}
CompilationResultProto::CompilationResultProto(const CompilationResultProto& from)
  : ::google::protobuf::Message(),
      _internal_metadata_(NULL),
      hlo_protos_(from.hlo_protos_) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  status_error_message_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  if (from.status_error_message().size() > 0) {
    status_error_message_.Set(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.status_error_message(),
      GetArenaNoVirtual());
  }
  status_code_ = from.status_code_;
  // @@protoc_insertion_point(copy_constructor:diplomacy.tensorflow.tpu.CompilationResultProto)
}

void CompilationResultProto::SharedCtor() {
  status_error_message_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  status_code_ = 0;
}

CompilationResultProto::~CompilationResultProto() {
  // @@protoc_insertion_point(destructor:diplomacy.tensorflow.tpu.CompilationResultProto)
  SharedDtor();
}

void CompilationResultProto::SharedDtor() {
  GOOGLE_DCHECK(GetArenaNoVirtual() == NULL);
  status_error_message_.DestroyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}

void CompilationResultProto::ArenaDtor(void* object) {
  CompilationResultProto* _this = reinterpret_cast< CompilationResultProto* >(object);
  (void)_this;
}
void CompilationResultProto::RegisterArenaDtor(::google::protobuf::Arena* arena) {
}
void CompilationResultProto::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const ::google::protobuf::Descriptor* CompilationResultProto::descriptor() {
  ::protobuf_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2fcompilation_5fresult_2eproto::protobuf_AssignDescriptorsOnce();
  return ::protobuf_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2fcompilation_5fresult_2eproto::file_level_metadata[kIndexInFileMessages].descriptor;
}

const CompilationResultProto& CompilationResultProto::default_instance() {
  ::google::protobuf::internal::InitSCC(&protobuf_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2fcompilation_5fresult_2eproto::scc_info_CompilationResultProto.base);
  return *internal_default_instance();
}


void CompilationResultProto::Clear() {
// @@protoc_insertion_point(message_clear_start:diplomacy.tensorflow.tpu.CompilationResultProto)
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  hlo_protos_.Clear();
  status_error_message_.ClearToEmpty(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), GetArenaNoVirtual());
  status_code_ = 0;
  _internal_metadata_.Clear();
}

bool CompilationResultProto::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!GOOGLE_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:diplomacy.tensorflow.tpu.CompilationResultProto)
  for (;;) {
    ::std::pair<::google::protobuf::uint32, bool> p = input->ReadTagWithCutoffNoLastTag(127u);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // .diplomacy.tensorflow.error.Code status_code = 1;
      case 1: {
        if (static_cast< ::google::protobuf::uint8>(tag) ==
            static_cast< ::google::protobuf::uint8>(8u /* 8 & 0xFF */)) {
          int value;
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   int, ::google::protobuf::internal::WireFormatLite::TYPE_ENUM>(
                 input, &value)));
          set_status_code(static_cast< ::diplomacy::tensorflow::error::Code >(value));
        } else {
          goto handle_unusual;
        }
        break;
      }

      // string status_error_message = 2;
      case 2: {
        if (static_cast< ::google::protobuf::uint8>(tag) ==
            static_cast< ::google::protobuf::uint8>(18u /* 18 & 0xFF */)) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadString(
                input, this->mutable_status_error_message()));
          DO_(::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
            this->status_error_message().data(), static_cast<int>(this->status_error_message().length()),
            ::google::protobuf::internal::WireFormatLite::PARSE,
            "diplomacy.tensorflow.tpu.CompilationResultProto.status_error_message"));
        } else {
          goto handle_unusual;
        }
        break;
      }

      // repeated .xla.HloProto hlo_protos = 3;
      case 3: {
        if (static_cast< ::google::protobuf::uint8>(tag) ==
            static_cast< ::google::protobuf::uint8>(26u /* 26 & 0xFF */)) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessage(
                input, add_hlo_protos()));
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
  // @@protoc_insertion_point(parse_success:diplomacy.tensorflow.tpu.CompilationResultProto)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:diplomacy.tensorflow.tpu.CompilationResultProto)
  return false;
#undef DO_
}

void CompilationResultProto::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:diplomacy.tensorflow.tpu.CompilationResultProto)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // .diplomacy.tensorflow.error.Code status_code = 1;
  if (this->status_code() != 0) {
    ::google::protobuf::internal::WireFormatLite::WriteEnum(
      1, this->status_code(), output);
  }

  // string status_error_message = 2;
  if (this->status_error_message().size() > 0) {
    ::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
      this->status_error_message().data(), static_cast<int>(this->status_error_message().length()),
      ::google::protobuf::internal::WireFormatLite::SERIALIZE,
      "diplomacy.tensorflow.tpu.CompilationResultProto.status_error_message");
    ::google::protobuf::internal::WireFormatLite::WriteStringMaybeAliased(
      2, this->status_error_message(), output);
  }

  // repeated .xla.HloProto hlo_protos = 3;
  for (unsigned int i = 0,
      n = static_cast<unsigned int>(this->hlo_protos_size()); i < n; i++) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      3,
      this->hlo_protos(static_cast<int>(i)),
      output);
  }

  if ((_internal_metadata_.have_unknown_fields() &&  ::google::protobuf::internal::GetProto3PreserveUnknownsDefault())) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        (::google::protobuf::internal::GetProto3PreserveUnknownsDefault()   ? _internal_metadata_.unknown_fields()   : _internal_metadata_.default_instance()), output);
  }
  // @@protoc_insertion_point(serialize_end:diplomacy.tensorflow.tpu.CompilationResultProto)
}

::google::protobuf::uint8* CompilationResultProto::InternalSerializeWithCachedSizesToArray(
    bool deterministic, ::google::protobuf::uint8* target) const {
  (void)deterministic; // Unused
  // @@protoc_insertion_point(serialize_to_array_start:diplomacy.tensorflow.tpu.CompilationResultProto)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // .diplomacy.tensorflow.error.Code status_code = 1;
  if (this->status_code() != 0) {
    target = ::google::protobuf::internal::WireFormatLite::WriteEnumToArray(
      1, this->status_code(), target);
  }

  // string status_error_message = 2;
  if (this->status_error_message().size() > 0) {
    ::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
      this->status_error_message().data(), static_cast<int>(this->status_error_message().length()),
      ::google::protobuf::internal::WireFormatLite::SERIALIZE,
      "diplomacy.tensorflow.tpu.CompilationResultProto.status_error_message");
    target =
      ::google::protobuf::internal::WireFormatLite::WriteStringToArray(
        2, this->status_error_message(), target);
  }

  // repeated .xla.HloProto hlo_protos = 3;
  for (unsigned int i = 0,
      n = static_cast<unsigned int>(this->hlo_protos_size()); i < n; i++) {
    target = ::google::protobuf::internal::WireFormatLite::
      InternalWriteMessageToArray(
        3, this->hlo_protos(static_cast<int>(i)), deterministic, target);
  }

  if ((_internal_metadata_.have_unknown_fields() &&  ::google::protobuf::internal::GetProto3PreserveUnknownsDefault())) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        (::google::protobuf::internal::GetProto3PreserveUnknownsDefault()   ? _internal_metadata_.unknown_fields()   : _internal_metadata_.default_instance()), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:diplomacy.tensorflow.tpu.CompilationResultProto)
  return target;
}

size_t CompilationResultProto::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:diplomacy.tensorflow.tpu.CompilationResultProto)
  size_t total_size = 0;

  if ((_internal_metadata_.have_unknown_fields() &&  ::google::protobuf::internal::GetProto3PreserveUnknownsDefault())) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        (::google::protobuf::internal::GetProto3PreserveUnknownsDefault()   ? _internal_metadata_.unknown_fields()   : _internal_metadata_.default_instance()));
  }
  // repeated .xla.HloProto hlo_protos = 3;
  {
    unsigned int count = static_cast<unsigned int>(this->hlo_protos_size());
    total_size += 1UL * count;
    for (unsigned int i = 0; i < count; i++) {
      total_size +=
        ::google::protobuf::internal::WireFormatLite::MessageSize(
          this->hlo_protos(static_cast<int>(i)));
    }
  }

  // string status_error_message = 2;
  if (this->status_error_message().size() > 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::StringSize(
        this->status_error_message());
  }

  // .diplomacy.tensorflow.error.Code status_code = 1;
  if (this->status_code() != 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::EnumSize(this->status_code());
  }

  int cached_size = ::google::protobuf::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void CompilationResultProto::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:diplomacy.tensorflow.tpu.CompilationResultProto)
  GOOGLE_DCHECK_NE(&from, this);
  const CompilationResultProto* source =
      ::google::protobuf::internal::DynamicCastToGenerated<const CompilationResultProto>(
          &from);
  if (source == NULL) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:diplomacy.tensorflow.tpu.CompilationResultProto)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:diplomacy.tensorflow.tpu.CompilationResultProto)
    MergeFrom(*source);
  }
}

void CompilationResultProto::MergeFrom(const CompilationResultProto& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:diplomacy.tensorflow.tpu.CompilationResultProto)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  hlo_protos_.MergeFrom(from.hlo_protos_);
  if (from.status_error_message().size() > 0) {
    set_status_error_message(from.status_error_message());
  }
  if (from.status_code() != 0) {
    set_status_code(from.status_code());
  }
}

void CompilationResultProto::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:diplomacy.tensorflow.tpu.CompilationResultProto)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void CompilationResultProto::CopyFrom(const CompilationResultProto& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:diplomacy.tensorflow.tpu.CompilationResultProto)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool CompilationResultProto::IsInitialized() const {
  return true;
}

void CompilationResultProto::Swap(CompilationResultProto* other) {
  if (other == this) return;
  if (GetArenaNoVirtual() == other->GetArenaNoVirtual()) {
    InternalSwap(other);
  } else {
    CompilationResultProto* temp = New(GetArenaNoVirtual());
    temp->MergeFrom(*other);
    other->CopyFrom(*this);
    InternalSwap(temp);
    if (GetArenaNoVirtual() == NULL) {
      delete temp;
    }
  }
}
void CompilationResultProto::UnsafeArenaSwap(CompilationResultProto* other) {
  if (other == this) return;
  GOOGLE_DCHECK(GetArenaNoVirtual() == other->GetArenaNoVirtual());
  InternalSwap(other);
}
void CompilationResultProto::InternalSwap(CompilationResultProto* other) {
  using std::swap;
  CastToBase(&hlo_protos_)->InternalSwap(CastToBase(&other->hlo_protos_));
  status_error_message_.Swap(&other->status_error_message_, &::google::protobuf::internal::GetEmptyStringAlreadyInited(),
    GetArenaNoVirtual());
  swap(status_code_, other->status_code_);
  _internal_metadata_.Swap(&other->_internal_metadata_);
}

::google::protobuf::Metadata CompilationResultProto::GetMetadata() const {
  protobuf_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2fcompilation_5fresult_2eproto::protobuf_AssignDescriptorsOnce();
  return ::protobuf_diplomacy_5ftensorflow_2fcontrib_2ftpu_2fproto_2fcompilation_5fresult_2eproto::file_level_metadata[kIndexInFileMessages];
}


// @@protoc_insertion_point(namespace_scope)
}  // namespace tpu
}  // namespace tensorflow
}  // namespace diplomacy
namespace google {
namespace protobuf {
template<> GOOGLE_PROTOBUF_ATTRIBUTE_NOINLINE ::diplomacy::tensorflow::tpu::CompilationResultProto* Arena::CreateMaybeMessage< ::diplomacy::tensorflow::tpu::CompilationResultProto >(Arena* arena) {
  return Arena::CreateMessageInternal< ::diplomacy::tensorflow::tpu::CompilationResultProto >(arena);
}
}  // namespace protobuf
}  // namespace google

// @@protoc_insertion_point(global_scope)