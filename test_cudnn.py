import torch.backends.cudnn as cudnn
print(cudnn.is_available())  # 检查是否可用CUDNN加速
print(cudnn.version())  # 获取CUDNN版本号
print(torch.cuda.is_available())  # 检查是否使用CUDA