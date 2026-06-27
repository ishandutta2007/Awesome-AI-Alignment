# The Alignment Tax

The **Alignment Tax** refers to the trade-off in performance, capability, or resources that occurs when a model is constrained to be safe and aligned with human values.

## Manifestations of the Tax

1. **Refusal Underfitting:** The model over-generalizes safety rules and refuses benign requests (e.g., refusing to explain how to kill a command line process because it contains the word "kill").
2. **Capability Degradation:** Strongly aligned models sometimes perform worse on coding, reasoning, or creative writing benchmarks compared to their unaligned counterparts.
3. **Compute and VRAM Tax:** Collecting human feedback and running RL pipelines requires massive additional training time and infrastructure.

## Balancing Trade-offs

```mermaid
graph LR
    A[Raw Capability] <--> B[Safety Constraints (Alignment Tax)]
    B --> C{Optimization Target}
    C --> D[Optimal Frontier: Highly Safe & Highly Capable]
```

---
[← Back to README](../README.md)
