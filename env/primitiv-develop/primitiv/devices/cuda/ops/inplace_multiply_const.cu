#include <primitiv/config.h>

#include <primitiv/devices/cuda/device.h>
#include <primitiv/devices/cuda/ops/common.h>
#include <primitiv/internal/cuda/utils.h>

namespace {

__global__ void inplace_multiply_const_dev(
    float k, std::uint32_t size, float *px) {
  const std::uint32_t i = IDX;
  if (i < size) px[i] *= k;
}

}  // namespace

namespace primitiv {
namespace devices {

void CUDA::inplace_multiply_const_impl(float k, Tensor &x) {
  const std::uint32_t size = x.shape().size();
  const std::uint32_t g1 = GRID_SIZE(size, dim1_x_);
  CUDA_CALL(::cudaSetDevice(dev_id_));
  ::inplace_multiply_const_dev<<<g1, dim1_x_>>>(k, size, MDATA(x));
}

}  // namespace devices
}  // namespace primitiv
