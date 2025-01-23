---
description: Comprehensive guide for setting up and using NVIDIA CUDA with Python
  on Linux, focusing on deep learning and GPU acceleration
path: developer/frameworks/gpu/linux-nvidia-cuda-python-guide.md
prompt_type: Instruction-based prompting
tags:
- linux
- nvidia
- cuda
- python
- gpu
- deep-learning
title: Linux NVIDIA CUDA Python Development Guide
---

# Linux NVIDIA CUDA Python Development Guide

## Overview
This guide provides detailed instructions for setting up and using NVIDIA CUDA with Python on Linux systems, enabling GPU acceleration for deep learning and scientific computing applications.

## Prerequisites

### 1. System Requirements
```bash
# Check GPU compatibility
lspci | grep -i nvidia

# Check Linux distribution
cat /etc/os-release

# Check kernel version
uname -r
```

### 2. NVIDIA Driver Installation
```bash
# Add NVIDIA repository
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update

# Install NVIDIA driver
sudo apt install nvidia-driver-535  # Replace with latest version
sudo reboot

# Verify installation
nvidia-smi
```

## CUDA Installation

### 1. CUDA Toolkit
```bash
# Download CUDA installer
wget https://developer.download.nvidia.com/compute/cuda/12.3.0/local_installers/cuda_12.3.0_545.23.06_linux.run

# Make installer executable
chmod +x cuda_12.3.0_545.23.06_linux.run

# Run installer
sudo ./cuda_12.3.0_545.23.06_linux.run
```

### 2. Environment Setup
```bash
# Add CUDA paths to ~/.bashrc
echo 'export PATH=/usr/local/cuda/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc

# Verify CUDA installation
nvcc --version
```

## Python Environment Setup

### 1. Conda Environment
```bash
# Create conda environment
conda create -n cuda-env python=3.10
conda activate cuda-env

# Install CUDA toolkit
conda install cudatoolkit cudnn
```

### 2. PyTorch Installation
```bash
# Install PyTorch with CUDA support
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

## Basic CUDA Operations

### 1. CUDA Device Information
```python
import torch

def print_cuda_info():
    print(f"CUDA available: {torch.cuda.is_available()}")
    print(f"CUDA device count: {torch.cuda.device_count()}")
    print(f"Current CUDA device: {torch.cuda.current_device()}")
    print(f"CUDA device name: {torch.cuda.get_device_name(0)}")

print_cuda_info()
```

### 2. Basic Tensor Operations
```python
import torch

# Create tensor on GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.randn(1000, 1000).to(device)
y = torch.randn(1000, 1000).to(device)

# Perform operations
z = torch.matmul(x, y)
print(f"Result shape: {z.shape}")
print(f"Device: {z.device}")
```

## Deep Learning Example

### 1. Simple Neural Network
```python
import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 10)
        self.relu = nn.ReLU()
        
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Create model and move to GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SimpleNet().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters())

# Training loop example
def train(model, data, labels):
    model.train()
    data, labels = data.to(device), labels.to(device)
    
    optimizer.zero_grad()
    output = model(data)
    loss = criterion(output, labels)
    loss.backward()
    optimizer.step()
    
    return loss.item()
```

## Performance Optimization

### 1. Memory Management
```python
import torch

def optimize_memory():
    # Clear GPU cache
    torch.cuda.empty_cache()
    
    # Get memory statistics
    print(torch.cuda.memory_summary())
    
    # Use memory pinning for faster host-to-device transfer
    pinned_data = torch.tensor([1, 2, 3]).pin_memory()
    pinned_data = pinned_data.to(device, non_blocking=True)

# Example of batch processing
def process_in_batches(data, batch_size=32):
    for i in range(0, len(data), batch_size):
        batch = data[i:i+batch_size].to(device)
        # Process batch
        torch.cuda.empty_cache()
```

### 2. Multi-GPU Training
```python
import torch.nn as nn

class ParallelModel(nn.Module):
    def __init__(self):
        super(ParallelModel, self).__init__()
        self.model = SimpleNet()
        if torch.cuda.device_count() > 1:
            self.model = nn.DataParallel(self.model)
        self.model.to(device)
    
    def forward(self, x):
        return self.model(x)
```

## Debugging and Profiling

### 1. CUDA Error Handling
```python
import torch

def cuda_error_handling():
    try:
        # CUDA operation
        result = torch.cuda.FloatTensor(1000, 1000)
    except RuntimeError as e:
        print(f"CUDA error: {e}")
    finally:
        # Clean up
        torch.cuda.empty_cache()
```

### 2. Performance Profiling
```python
from torch.profiler import profile, record_function, ProfilerActivity

def profile_model(model, input_data):
    with profile(activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA],
                profile_memory=True, record_shapes=True) as prof:
        with record_function("model_inference"):
            model(input_data)
    
    print(prof.key_averages().table(sort_by="cuda_time_total"))
```

## Common Issues and Solutions

1. Out of Memory Errors
   - Reduce batch size
   - Use gradient checkpointing
   - Implement proper memory cleanup

2. CUDA Version Mismatch
   - Check compatibility matrix
   - Use correct PyTorch wheels
   - Verify driver versions

3. Performance Issues
   - Monitor GPU utilization
   - Optimize data transfers
   - Use appropriate batch sizes

## Best Practices

1. Development Guidelines
   - Always check CUDA availability
   - Use proper error handling
   - Implement memory management
   - Profile performance regularly

2. Production Deployment
   - Version control CUDA dependencies
   - Monitor GPU usage
   - Implement proper logging
   - Use appropriate container solutions

Remember to regularly update drivers and CUDA toolkit for optimal performance and compatibility. 