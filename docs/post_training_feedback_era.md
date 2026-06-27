# The Post-Training Feedback Era (RLHF/DPO Boom, ~2019–2024)

As deep learning scaled, researchers realized that base language models trained purely on next-token prediction act as simple text-mimics. To make them useful assistants, alignment shifted to a post-training phase using reinforcement learning and preference feedback.

## Core Methodologies

### 1. Reinforcement Learning from Human Feedback (RLHF)
RLHF aligns models by training a separate **Reward Model** on human pairwise comparisons (preferring one model output over another). The base policy model is then optimized against this reward model using **Proximal Policy Optimization (PPO)**.

### 2. Direct Preference Optimization (DPO)
DPO simplifies the RLHF pipeline by mathematically showing that the policy model itself can act as the reward model. It bypasses the need to train a separate reward model or run complex reinforcement learning loops, optimizing the policy directly on preference data using a simple binary cross-entropy loss.

## Major Challenges

- **Reward Hacking:** The model learns to exploit flaws in the reward model's proxy metrics to score high rewards without actually generating safe or useful answers.
- **Resource Intensity:** Maintaining multiple models in GPU memory (Policy, Reference, Critic, Reward) creates severe VRAM bottlenecks.

## RLHF vs. DPO Pipeline Diagram

```mermaid
graph TD
    subgraph RLHF Pipeline
        A[Base Model] --> B[SFT Model]
        B --> C[Collect Pairwise Comparisons]
        C --> D[Train Reward Model]
        D --> E[PPO Reinforcement Learning]
        E --> F[Aligned Model (RLHF)]
    end
    subgraph DPO Pipeline
        G[Base Model] --> H[SFT Model]
        H --> I[Collect Pairwise Comparisons]
        I --> J[Direct Policy Optimization Loss]
        J --> K[Aligned Model (DPO)]
    end
```

---
[← Back to README](../README.md)
