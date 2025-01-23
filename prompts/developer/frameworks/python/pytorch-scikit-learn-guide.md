---
description: A comprehensive guide for developing machine learning applications using
  PyTorch and scikit-learn, covering model development, training pipelines, and deployment
  strategies
path: developer/frameworks/python/pytorch-scikit-learn-guide
prompt_type: Instruction-based prompting
tags:
- python
- pytorch
- scikit-learn
- machine-learning
- deep-learning
title: PyTorch and Scikit-learn Development Guide
---

# PyTorch and Scikit-learn Development Guide

## Core Principles
- Model development
- Data preprocessing
- Training pipelines
- Model evaluation
- Deployment strategies

## Project Setup

### Directory Structure
```
ml_project/
├── src/
│   ├── data/
│   │   ├── __init__.py
│   │   ├── dataset.py
│   │   └── preprocessing.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── pytorch/
│   │   └── sklearn/
│   ├── training/
│   │   ├── __init__.py
│   │   ├── trainer.py
│   │   └── metrics.py
│   └── utils/
│       ├── __init__.py
│       └── visualization.py
├── notebooks/
│   ├── exploration.ipynb
│   └── evaluation.ipynb
├── tests/
│   ├── __init__.py
│   └── test_models.py
├── configs/
│   └── model_config.yaml
├── pyproject.toml
└── README.md
```

### Dependencies Setup
```toml
# pyproject.toml
[project]
name = "ml-project"
version = "0.1.0"
description = "Machine learning project"
requires-python = ">=3.12"

dependencies = [
    "torch>=2.1.0",
    "scikit-learn>=1.3.2",
    "numpy>=1.26.0",
    "pandas>=2.1.2",
    "matplotlib>=3.8.1",
    "seaborn>=0.13.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "black>=23.10.0",
    "ruff>=0.1.3",
    "jupyter>=1.0.0",
]
```

## Data Processing

### Dataset Implementation
```python
# src/data/dataset.py
from torch.utils.data import Dataset
import torch
import numpy as np
from typing import Tuple

class CustomDataset(Dataset):
    """Custom PyTorch dataset."""
    
    def __init__(
        self,
        data: np.ndarray,
        targets: np.ndarray,
        transform = None
    ) -> None:
        """Initialize dataset."""
        self.data = torch.FloatTensor(data)
        self.targets = torch.FloatTensor(targets)
        self.transform = transform
    
    def __len__(self) -> int:
        """Get dataset length."""
        return len(self.data)
    
    def __getitem__(
        self,
        idx: int
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """Get item by index."""
        x = self.data[idx]
        y = self.targets[idx]
        
        if self.transform:
            x = self.transform(x)
        
        return x, y
```

### Data Preprocessing
```python
# src/data/preprocessing.py
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
import numpy as np
from typing import Optional

class CustomPreprocessor(BaseEstimator, TransformerMixin):
    """Custom scikit-learn preprocessor."""
    
    def __init__(self, feature_range: Optional[tuple] = None):
        """Initialize preprocessor."""
        self.feature_range = feature_range
        self.scaler = StandardScaler()
    
    def fit(self, X: np.ndarray, y=None):
        """Fit preprocessor."""
        self.scaler.fit(X)
        return self
    
    def transform(self, X: np.ndarray) -> np.ndarray:
        """Transform data."""
        X_scaled = self.scaler.transform(X)
        
        if self.feature_range:
            min_val, max_val = self.feature_range
            X_scaled = (X_scaled - X_scaled.min()) / (
                X_scaled.max() - X_scaled.min()
            )
            X_scaled = X_scaled * (max_val - min_val) + min_val
        
        return X_scaled
```

## Model Development

### PyTorch Model
```python
# src/models/pytorch/model.py
import torch
import torch.nn as nn
from typing import List

class NeuralNetwork(nn.Module):
    """Neural network model."""
    
    def __init__(
        self,
        input_size: int,
        hidden_sizes: List[int],
        output_size: int,
        dropout: float = 0.2
    ) -> None:
        """Initialize model."""
        super().__init__()
        
        layers = []
        prev_size = input_size
        
        for hidden_size in hidden_sizes:
            layers.extend([
                nn.Linear(prev_size, hidden_size),
                nn.ReLU(),
                nn.BatchNorm1d(hidden_size),
                nn.Dropout(dropout)
            ])
            prev_size = hidden_size
        
        layers.append(nn.Linear(prev_size, output_size))
        self.model = nn.Sequential(*layers)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass."""
        return self.model(x)
```

### Scikit-learn Model
```python
# src/models/sklearn/model.py
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.preprocessing import LabelEncoder
import numpy as np
from typing import Optional

class CustomClassifier(BaseEstimator, ClassifierMixin):
    """Custom scikit-learn classifier."""
    
    def __init__(
        self,
        learning_rate: float = 0.01,
        n_iterations: int = 1000
    ) -> None:
        """Initialize classifier."""
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.label_encoder = LabelEncoder()
    
    def fit(
        self,
        X: np.ndarray,
        y: np.ndarray
    ) -> "CustomClassifier":
        """Fit classifier."""
        y_encoded = self.label_encoder.fit_transform(y)
        self.classes_ = self.label_encoder.classes_
        
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for _ in range(self.n_iterations):
            linear_model = np.dot(X, self.weights) + self.bias
            predictions = self._sigmoid(linear_model)
            
            dw = (1 / n_samples) * np.dot(X.T, (predictions - y_encoded))
            db = (1 / n_samples) * np.sum(predictions - y_encoded)
            
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
        
        return self
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict classes."""
        linear_model = np.dot(X, self.weights) + self.bias
        predictions = self._sigmoid(linear_model)
        return self.label_encoder.inverse_transform(
            (predictions >= 0.5).astype(int)
        )
    
    def _sigmoid(self, x: np.ndarray) -> np.ndarray:
        """Sigmoid activation function."""
        return 1 / (1 + np.exp(-x))
```

## Training Pipeline

### PyTorch Trainer
```python
# src/training/trainer.py
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from typing import Optional, Callable
import numpy as np
from tqdm import tqdm

class PyTorchTrainer:
    """PyTorch model trainer."""
    
    def __init__(
        self,
        model: nn.Module,
        criterion: nn.Module,
        optimizer: torch.optim.Optimizer,
        device: str = "cuda" if torch.cuda.is_available() else "cpu"
    ) -> None:
        """Initialize trainer."""
        self.model = model.to(device)
        self.criterion = criterion
        self.optimizer = optimizer
        self.device = device
    
    def train_epoch(
        self,
        train_loader: DataLoader,
        epoch: int,
        scheduler: Optional[torch.optim.lr_scheduler._LRScheduler] = None
    ) -> float:
        """Train one epoch."""
        self.model.train()
        total_loss = 0
        
        with tqdm(train_loader, desc=f"Epoch {epoch}") as pbar:
            for batch_idx, (data, target) in enumerate(pbar):
                data, target = data.to(self.device), target.to(self.device)
                
                self.optimizer.zero_grad()
                output = self.model(data)
                loss = self.criterion(output, target)
                
                loss.backward()
                self.optimizer.step()
                
                if scheduler is not None:
                    scheduler.step()
                
                total_loss += loss.item()
                pbar.set_postfix({"loss": loss.item()})
        
        return total_loss / len(train_loader)
    
    @torch.no_grad()
    def evaluate(
        self,
        val_loader: DataLoader,
        metric_fn: Optional[Callable] = None
    ) -> tuple[float, Optional[float]]:
        """Evaluate model."""
        self.model.eval()
        total_loss = 0
        predictions = []
        targets = []
        
        for data, target in val_loader:
            data, target = data.to(self.device), target.to(self.device)
            output = self.model(data)
            loss = self.criterion(output, target)
            
            total_loss += loss.item()
            predictions.append(output.cpu().numpy())
            targets.append(target.cpu().numpy())
        
        avg_loss = total_loss / len(val_loader)
        metric = None
        
        if metric_fn is not None:
            predictions = np.concatenate(predictions)
            targets = np.concatenate(targets)
            metric = metric_fn(targets, predictions)
        
        return avg_loss, metric
```

### Training Metrics
```python
# src/training/metrics.py
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)
from typing import Dict, Any

def calculate_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray
) -> Dict[str, float]:
    """Calculate classification metrics."""
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, average="weighted"),
        "recall": recall_score(y_true, y_pred, average="weighted"),
        "f1": f1_score(y_true, y_pred, average="weighted")
    }

def calculate_regression_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray
) -> Dict[str, float]:
    """Calculate regression metrics."""
    return {
        "mse": np.mean((y_true - y_pred) ** 2),
        "rmse": np.sqrt(np.mean((y_true - y_pred) ** 2)),
        "mae": np.mean(np.abs(y_true - y_pred)),
        "r2": 1 - (
            np.sum((y_true - y_pred) ** 2) /
            np.sum((y_true - np.mean(y_true)) ** 2)
        )
    }
```

## Model Evaluation

### Visualization
```python
# src/utils/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict, Any

def plot_training_history(
    history: Dict[str, List[float]],
    figsize: tuple = (10, 6)
) -> None:
    """Plot training history."""
    plt.figure(figsize=figsize)
    
    for metric, values in history.items():
        plt.plot(values, label=metric)
    
    plt.title("Training History")
    plt.xlabel("Epoch")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_confusion_matrix(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    labels: List[str],
    figsize: tuple = (8, 6)
) -> None:
    """Plot confusion matrix."""
    cm = confusion_matrix(y_true, y_pred)
    
    plt.figure(figsize=figsize)
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=labels,
        yticklabels=labels
    )
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.show()
```

## Model Deployment

### Model Export
```python
# src/models/export.py
import torch
import pickle
from pathlib import Path
from typing import Any

def save_pytorch_model(
    model: torch.nn.Module,
    path: str | Path,
    save_jit: bool = True
) -> None:
    """Save PyTorch model."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    if save_jit:
        model.eval()
        traced_model = torch.jit.script(model)
        torch.jit.save(traced_model, str(path))
    else:
        torch.save(model.state_dict(), path)

def save_sklearn_model(
    model: Any,
    path: str | Path
) -> None:
    """Save scikit-learn model."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, "wb") as f:
        pickle.dump(model, f)
```

## Best Practices

### Development
1. Use version control
2. Write unit tests
3. Document code
4. Profile performance
5. Monitor training

### Model Development
- Data validation
- Cross-validation
- Hyperparameter tuning
- Model evaluation
- Error analysis

### Training
1. Use GPU when available
2. Implement early stopping
3. Monitor metrics
4. Save checkpoints
5. Log experiments

### Deployment
- Model versioning
- Environment management
- Performance monitoring
- Error handling
- Scalability

## Resources
- PyTorch documentation
- Scikit-learn guides
- ML best practices
- Deployment strategies
- Performance optimization 