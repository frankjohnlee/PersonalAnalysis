//
// Copyright (C) 2011-15 DyND Developers
// BSD 2-Clause License, see LICENSE.txt
//

#pragma once

#include <dynd/callable.hpp>
#include <dynd/kernels/base_kernel.hpp>
#include <dynd/kernels/cuda_launch.hpp>

namespace dynd {
namespace kernels {

  template <int N, bool with_dst = true>
  struct permute_ck;

  template <int N>
  struct permute_ck<N, true> : nd::base_strided_kernel<permute_ck<N, true>, N> {
    typedef permute_ck self_type;

    intptr_t perm[N];

    permute_ck(const intptr_t *perm) { memcpy(this->perm, perm, sizeof(this->perm)); }

    void single(char *dst, char *const *src)
    {
      char *src_inv_perm[N];
      inv(src_inv_perm, dst, src);

      nd::kernel_prefix *child = this->get_child();
      kernel_single_t single = child->get_function<kernel_single_t>();
      single(child, NULL, src_inv_perm);
    }

    void strided(char *dst, intptr_t dst_stride, char *const *src, const intptr_t *src_stride, size_t count)
    {
      char *src_inv_perm[N];
      inv(src_inv_perm, dst, src);

      intptr_t src_stride_inv_perm[N];
      inv(src_stride_inv_perm, dst_stride, src_stride);

      nd::kernel_prefix *child = this->get_child();
      kernel_strided_t strided = child->get_function<kernel_strided_t>();
      strided(child, NULL, 0, src_inv_perm, src_stride_inv_perm, count);
    }

    static void instantiate(char *static_data, char *DYND_UNUSED(data), nd::kernel_builder *ckb,
                            const ndt::type &dst_tp, const char *dst_arrmeta, intptr_t nsrc, const ndt::type *src_tp,
                            const char *const *src_arrmeta, kernel_request_t kernreq, intptr_t nkwd,
                            const nd::array *kwds, const std::map<std::string, ndt::type> &tp_vars)
    {
      const std::pair<nd::callable, std::vector<intptr_t>> *data =
          reinterpret_cast<std::pair<nd::callable, std::vector<intptr_t>> *>(static_data);

      const nd::base_callable *child = data->first.get();

      const intptr_t *perm = data->second.data();

      ndt::type src_tp_inv[N];
      inv(src_tp_inv, dst_tp, src_tp, perm);

      const char *src_arrmeta_inv[N];
      inv(src_arrmeta_inv, dst_arrmeta, src_arrmeta, perm);

      ckb->emplace_back<self_type>(kernreq, detail::make_array_wrapper<N>(perm));
      child->instantiate(const_cast<char *>(child->static_data()), NULL, ckb, ndt::make_type<void>(), NULL, nsrc,
                         src_tp_inv, src_arrmeta_inv, kernreq | kernel_request_data_only, nkwd, kwds, tp_vars);
    }

  private:
    static void inv(ndt::type *src_inv, const ndt::type &dst, const ndt::type *src, const intptr_t *perm)
    {
      for (intptr_t i = 0; i < N; ++i) {
        intptr_t j = perm[i];
        if (j == -1) {
          src_inv[i] = dst;
        }
        else {
          src_inv[i] = src[j];
        }
      }
    }

    template <typename T>
    static void inv(T *src_inv, const T &dst, const T *src, const intptr_t *perm)
    {
      for (intptr_t i = 0; i < N; ++i) {
        intptr_t j = perm[i];
        if (j == -1) {
          src_inv[i] = dst;
        }
        else {
          src_inv[i] = src[j];
        }
      }
    }

    void inv(ndt::type *src_inv, const ndt::type &dst, const ndt::type *src) { return inv(src_inv, dst, src, perm); }

    template <typename T>
    void inv(T *src_inv, const T &dst, const T *src)
    {
      return inv(src_inv, dst, src, perm);
    }
  };

  template <int N>
  struct permute_ck<N, false> : nd::base_strided_kernel<permute_ck<N, false>, N> {
    typedef permute_ck self_type;

    intptr_t perm[N];

    permute_ck(const intptr_t *perm) { memcpy(this->perm, perm, sizeof(this->perm)); }

    void single(char *dst, char *const *src)
    {
      char *src_inv_perm[N];
      inv_permute(src_inv_perm, src, perm);

      nd::kernel_prefix *child = this->get_child();
      kernel_single_t single = child->get_function<kernel_single_t>();
      single(dst, src_inv_perm, child);
    }

    static void instantiate(char *static_data, char *DYND_UNUSED(data), nd::kernel_builder *ckb,
                            const ndt::type &dst_tp, const char *dst_arrmeta, intptr_t nsrc, const ndt::type *src_tp,
                            const char *const *src_arrmeta, kernel_request_t kernreq, intptr_t nkwd,
                            const nd::array *kwds, const std::map<std::string, ndt::type> &tp_vars)
    {
      const std::pair<nd::callable, std::vector<intptr_t>> *data =
          reinterpret_cast<std::pair<nd::callable, std::vector<intptr_t>> *>(static_data);

      const nd::base_callable *child = data->first.get();

      const intptr_t *perm = data->second.data();

      ndt::type src_tp_inv[N];
      inv_permute(src_tp_inv, src_tp, perm);

      const char *src_arrmeta_inv[N];
      inv_permute(src_arrmeta_inv, src_arrmeta, perm);

      ckb->emplace_back<self_type>(kernreq, detail::make_array_wrapper<N>(perm));
      child->instantiate(const_cast<char *>(child->static_data()), NULL, ckb, dst_tp, dst_arrmeta, nsrc, src_tp_inv,
                         src_arrmeta_inv, kernreq, nkwd, kwds, tp_vars);
    }

  private:
    template <typename T>
    static void inv_permute(T *src_inv, const T *src, const intptr_t *perm)
    {
      for (intptr_t i = 0; i < N; ++i) {
        src_inv[i] = src[perm[i]];
      }
    }
  };

} // dynd::kernels

namespace nd {
  namespace functional {

    DYND_API callable permute(const callable &child, const std::vector<intptr_t> &perm);

  } // namespace dynd::nd::functional
} // namespace dynd::nd
} // namespace dynd
