import torch
 
# 检查CUDA是否可用
cuda_available = torch.cuda.is_available()
 
if cuda_available:
    print("CUDA is available.")
else:
    print("CUDA is not available.")
 
# 检查CUDA版本
if cuda_available:
    cuda_version = torch.version.cuda
    print(f"CUDA version: {cuda_version}")


import torch.backends.cudnn as cudnn
print(cudnn.is_available())  # 检查是否可用CUDNN加速
print(cudnn.version())  # 获取CUDNN版本号
print(torch.cuda.is_available())  # 检查是否使用CUDA