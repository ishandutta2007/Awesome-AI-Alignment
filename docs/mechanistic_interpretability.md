# Mechanistic Interpretability

Mechanistic Interpretability aims to open the "black box" of neural networks by reverse-engineering the weights and activations into understandable algorithms and circuits.

## Key Concepts

- **Features:** The fundamental concepts represented inside a network (e.g., a specific neuron or direction in activation space that fires for "deception").
- **Circuits:** Subgraphs of the network consisting of features and the weights connecting them that perform specific logical operations.
- **Superposition:** The phenomenon where a neural network represents more features than it has dimensions by coding them as non-orthogonal directions.

## Analysis Process Flow

```mermaid
graph LR
    A[Model Inputs] --> B[Examine Hidden Activations]
    B --> C[Sparse Autoencoders (SAEs) Feature Extraction]
    C --> D[Identify Inter-feature Circuits]
    D --> E[Verify & Audit Internal Logic]
```

---
[← Back to README](../README.md)
