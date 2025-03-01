// for google colab
// %%writefile naive_convolution.cu
// !nvcc -arch=sm_75 -o  naive_convolution naive_convolution.cu


#include <iostream>
#include <cuda_runtime.h>
#include <device_launch_parameters.h>



#define cudaCheckErrors(msg) \
    do { \
        cudaError_t __err = cudaGetLastError(); \
        if (__err != cudaSuccess) { \
            fprintf(stderr, "Fatal error: %s (%s at %s:%d)\n", \
                msg, cudaGetErrorString(__err), \
                __FILE__, __LINE__); \
            fprintf(stderr, "*** FAILED - ABORTING\n"); \
            exit(1); \
        } \
    } while (0)

__global__ void direct_convolution(
    const float* input, const float* kernel, float* output,
    int in_channels, int in_h, int in_w,
    int out_channels, int kernel_size, int stride, int pad
) {
    const int out_h = (in_h + 2 * pad - kernel_size) / stride + 1;
    const int out_w = (in_w + 2 * pad - kernel_size) / stride + 1;

    // Output coordinates (x, y) and output channel
    const int idx = blockIdx.x * blockDim.x + threadIdx.x;
    const int idy = blockIdx.y * blockDim.y + threadIdx.y;
    const int c_out = blockIdx.z;

    if (idx >= out_w || idy >= out_h || c_out >= out_channels) return;

    float sum = 0.0f;

    // Iterate over input channels
    for (int c_in = 0; c_in < in_channels; c_in++) {
        // Iterate over kernel elements
        for (int ky = 0; ky < kernel_size; ky++) {
            for (int kx = 0; kx < kernel_size; kx++) {
                // Input coordinates (adjusted for padding)
                const int in_y = idy * stride + ky - pad;
                const int in_x = idx * stride + kx - pad;

                if (in_y >= 0 && in_y < in_h && in_x >= 0 && in_x < in_w) {
                    const float input_val = input[(c_in * in_h + in_y) * in_w + in_x];
                    const float kernel_val = kernel[((c_out * in_channels + c_in) * kernel_size + ky) * kernel_size + kx];
                    sum += input_val * kernel_val;
                }
            }
        }
    }

    // Write output (add batch dimension)
    output[(c_out * out_h + idy) * out_w + idx] = sum;
}

int main() {
    // Configuration (example: 1024x1024 input, 3x3 kernel)
    const int batch = 1;
    const int in_channels = 3;
    const int in_h = 1024, in_w = 1024;
    const int out_channels = 64;
    const int kernel_size = 3;
    const int stride = 1;
    const int pad = 1;

    const int out_h = (in_h + 2 * pad - kernel_size) / stride + 1;
    const int out_w = (in_w + 2 * pad - kernel_size) / stride + 1;

    float *h_input = new float[batch * in_channels * in_h * in_w];
    float *h_kernel = new float[out_channels * in_channels * kernel_size * kernel_size];
    float *h_output = new float[batch * out_channels * out_h * out_w];

    std::fill(h_input, h_input + batch * in_channels * in_h * in_w, 1.0f);
    std::fill(h_kernel, h_kernel + out_channels * in_channels * kernel_size * kernel_size, 1.0f);

    float *d_input, *d_kernel, *d_output;
    cudaMalloc(&d_input, batch * in_channels * in_h * in_w * sizeof(float));
    cudaCheckErrors("cudaMalloc d_input failed");
    cudaMalloc(&d_kernel, out_channels * in_channels * kernel_size * kernel_size * sizeof(float));
    cudaCheckErrors("cudaMalloc d_kernel failed");
    cudaMalloc(&d_output, batch * out_channels * out_h * out_w * sizeof(float));
    cudaCheckErrors("cudaMalloc d_output failed");

    cudaMemcpy(d_input, h_input, batch * in_channels * in_h * in_w * sizeof(float), cudaMemcpyHostToDevice);
    cudaCheckErrors("cudaMemcpy H2D d_input failed");
    cudaMemcpy(d_kernel, h_kernel, out_channels * in_channels * kernel_size * kernel_size * sizeof(float), cudaMemcpyHostToDevice);
    cudaCheckErrors("cudaMemcpy H2D d_kernel failed");

    dim3 block(16, 16);
    dim3 grid(
        (out_w + block.x - 1) / block.x,
        (out_h + block.y - 1) / block.y,
        out_channels
    );

    cudaEvent_t start, stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    cudaCheckErrors("cudaEventCreate failed");

    direct_convolution<<<grid, block>>>(d_input, d_kernel, d_output, in_channels, in_h, in_w, out_channels, kernel_size, stride, pad);
    cudaCheckErrors("Warm-up kernel failed");

    cudaEventRecord(start);
    cudaCheckErrors("cudaEventRecord start failed");
    for (int i = 0; i < 10; ++i) { 
     // Running multiple times for stable measurement
        direct_convolution<<<grid, block>>>(d_input, d_kernel, d_output, in_channels, in_h, in_w, out_channels, kernel_size, stride, pad);
        cudaCheckErrors("Main convolution kernel failed");
    }
    cudaEventRecord(stop);
    cudaCheckErrors("cudaEventRecord stop failed");
    cudaEventSynchronize(stop);
    cudaCheckErrors("cudaEventSynchronize failed");

    float milliseconds = 0;
    cudaEventElapsedTime(&milliseconds, start, stop);
    cudaCheckErrors("cudaEventElapsedTime failed");
    std::cout << "Time per convolution: " << milliseconds / 10 << " ms\n";

    cudaMemcpy(h_output, d_output, batch * out_channels * out_h * out_w * sizeof(float), cudaMemcpyDeviceToHost);
    cudaCheckErrors("cudaMemcpy D2H failed");

    const float expected_value = in_channels * 4;
    std::cout << "First output value: " << h_output[0] << " (Expected: " << expected_value << ")\n";

    // Cleanup
    delete[] h_input;
    delete[] h_kernel;
    delete[] h_output;
    cudaFree(d_input);
    cudaFree(d_kernel);
    cudaFree(d_output);
    cudaEventDestroy(start);
    cudaEventDestroy(stop);

    return 0;
}