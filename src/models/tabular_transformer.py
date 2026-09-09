"""Compact Transformer encoder for numeric tabular residual regression."""

from __future__ import annotations

import torch
from torch import nn


class TabularTransformerRegressor(nn.Module):
    """Tokenize each numeric feature and predict one standardized residual."""

    def __init__(
        self,
        n_features: int,
        d_model: int = 128,
        n_heads: int = 8,
        n_layers: int = 3,
        feedforward_dim: int = 256,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()
        if d_model % n_heads:
            raise ValueError("d_model must be divisible by n_heads")

        self.n_features = n_features
        self.feature_projections = nn.ModuleList(
            nn.Linear(1, d_model) for _ in range(n_features)
        )
        self.feature_embeddings = nn.Parameter(
            torch.randn(1, n_features, d_model) * 0.02
        )
        layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=n_heads,
            dim_feedforward=feedforward_dim,
            dropout=dropout,
            activation="gelu",
            batch_first=True,
            norm_first=True,
        )
        self.encoder = nn.TransformerEncoder(layer, num_layers=n_layers)
        self.output = nn.Sequential(
            nn.LayerNorm(d_model),
            nn.Linear(d_model, d_model),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(d_model, 1),
        )

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        if inputs.ndim != 2 or inputs.shape[1] != self.n_features:
            raise ValueError(
                f"Expected shape (batch, {self.n_features}), got {tuple(inputs.shape)}"
            )

        tokens = torch.stack(
            [projection(inputs[:, index : index + 1]) for index, projection in enumerate(self.feature_projections)],
            dim=1,
        )
        encoded = self.encoder(tokens + self.feature_embeddings)
        return self.output(encoded.mean(dim=1))

