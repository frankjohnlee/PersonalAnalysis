//
// Copyright (C) 2011-15 DyND Developers
// BSD 2-Clause License, see LICENSE.txt
//

#pragma once

#include <dynd/type.hpp>
#include <dynd/types/base_bytes_type.hpp>

namespace dynd {
namespace ndt {

  class DYNDT_API fixed_bytes_kind_type : public base_bytes_type {
  public:
    fixed_bytes_kind_type();

    size_t get_default_data_size() const;

    void print_data(std::ostream &o, const char *arrmeta, const char *data) const;

    void print_type(std::ostream &o) const;

    bool is_expression() const;
    bool is_unique_data_owner(const char *arrmeta) const;
    type get_canonical_type() const;

    bool is_lossless_assignment(const type &dst_tp, const type &src_tp) const;

    void get_bytes_range(const char **out_begin, const char **out_end, const char *arrmeta, const char *data) const;

    bool operator==(const base_type &rhs) const;

    void arrmeta_default_construct(char *arrmeta, bool blockref_alloc) const;
    void arrmeta_copy_construct(char *dst_arrmeta, const char *src_arrmeta,
                                const intrusive_ptr<memory_block_data> &embedded_reference) const;
    void arrmeta_reset_buffers(char *arrmeta) const;
    void arrmeta_finalize_buffers(char *arrmeta) const;
    void arrmeta_destruct(char *arrmeta) const;
    void arrmeta_debug_print(const char *arrmeta, std::ostream &o, const std::string &indent) const;

    void data_destruct(const char *arrmeta, char *data) const;
    void data_destruct_strided(const char *arrmeta, char *data, intptr_t stride, size_t count) const;

    bool match(const type &candidate_tp, std::map<std::string, type> &tp_vars) const;

    static type make() { return type(new fixed_bytes_kind_type(), false); }
  };

} // namespace dynd::ndt
} // namespace dynd
