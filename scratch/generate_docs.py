import os

docs_dir = r"C:\Users\ishan\Documents\Projects\Awesome-AI-Alignment\docs"
os.makedirs(docs_dir, exist_ok=True)

docs_data = [
    {
        "filename": "theoretical_axiom_era.md",
        "title": "The Theoretical Axiom Era (Pre-Deep Learning)",
        "content": """# The Theoretical Axiom Era (Pre-Deep Learning, ~1942–2010s)

The Theoretical Axiom Era represents the earliest phase of thinking about machine safety and alignment. Long before neural networks were capable of generating coherent text or images, scientists, philosophers, and science fiction writers conceptualized AI alignment as a problem of hardcoding rigid, logical rule-sets.

## Core Concepts

The most famous representation of this era is Isaac Asimov's **Three Laws of Robotics**, introduced in his 1942 short story *Runaround*:
1. **First Law:** A robot may not injure a human being or, through inaction, allow a human being to come to harm.
2. **Second Law:** A robot must obey the orders given it by human beings, except where such orders would conflict with the First Law.
3. **Third Law:** A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.

In this paradigm, safety is treated as a set of logical constraints or axioms that are evaluated before any action is executed.

## Why it Fails in Deep Learning

Modern deep learning models are not programmed using manual logical rules; instead, they learn representations and behaviors from vast amounts of data using optimization algorithms like gradient descent. 
- **Abstraction Dilemma:** Abstract concepts such as 'harm', 'intent', or 'benefit' cannot be mapped to simple boolean variables or static logical conditions.
- **Complexity of Real Environments:** Handcrafting a set of rules that covers every possible real-world scenario is mathematically impossible.

## Process Flow Diagram

```mermaid
graph TD
    A[Human Commands] --> B{Check First Law: Will it harm a human?}
    B -- Yes --> C[Refuse Action]
    B -- No --> D{Check Second Law: Does it obey orders?}
    D -- No --> C
    D -- Yes --> E{Check Third Law: Does it protect itself?}
    E -- Yes --> F[Execute Action]
    E -- No --> G{Does self-protection conflict with 1st/2nd Law?}
    G -- Yes --> F
    G -- No --> C
```

---
[← Back to README](../README.md)
"""
    },
    {
        "filename": "post_training_feedback_era.md",
        "title": "The Post-Training Feedback Era (RLHF & DPO)",
        "content": """# The Post-Training Feedback Era (RLHF/DPO Boom, ~2019–2024)

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
"""
    },
    {
        "filename": "scaled_inference_time_era.md",
        "title": "The Scaled Inference-Time & AI-Feedback Era",
        "content": """# The Scaled Inference-Time & AI-Feedback Era (~2024–Present)

The state-of-the-art paradigm in AI alignment moves beyond static human labels toward reinforcement learning from AI feedback (RLAIF) and computing scaling during inference (thinking phase).

## Key Components

- **RLAIF (Reinforcement Learning from AI Feedback):** Using advanced foundation models to evaluate and align other models. This scales up feedback collection and avoids human labeling bottlenecks.
- **Process-Supervised Reward Models (PRMs):** Unlike Outcome-Supervised Reward Models (ORMs) that only score the final answer, PRMs evaluate and reward each step of a model's reasoning chain.
- **Inference-Time Search:** Models use search loops (e.g., Monte Carlo Tree Search or chain-of-thought verification) to self-correct and verify logic before outputting a final answer.

## Process Flow Diagram

```mermaid
graph TD
    A[User Query] --> B[Generate Thinking/Reasoning Steps]
    B --> C{PRM step-level evaluation}
    C -- High Score --> D[Proceed to Next Step]
    C -- Low Score --> E[Backtrack & Regenerate Step]
    D --> F{Is Reasoning Complete?}
    F -- No --> B
    F -- Yes --> G[Final Response Output]
```

---
[← Back to README](../README.md)
"""
    },
    {
        "filename": "supervised_fine_tuning.md",
        "title": "Supervised Fine-Tuning (SFT) Alignment",
        "content": """# Supervised Fine-Tuning (SFT) Alignment

Supervised Fine-Tuning (SFT) is the first and most critical stage of the post-training alignment pipeline. It bridges the gap between raw web-crawled pretraining data and a useful, instruction-following assistant.

## The SFT Process

1. **Data Curation:** High-quality prompt-response demonstrations are generated by human annotators or curated synthetically.
2. **Supervised Training:** The base model is trained on this dataset using standard cross-entropy loss, where loss is calculated only on the target response tokens.
3. **Behavioral Shift:** SFT aligns the model to adopt a helpful conversational persona, respond in structured formats (markdown, JSON), and follow explicit formatting instructions.

## SFT Pipeline Diagram

```mermaid
graph LR
    A[Pretrained Base Model] --> B[Curated SFT Dataset]
    B --> C[Cross-Entropy Loss SFT Training]
    C --> D[Instruction-Following SFT Model]
```

---
[← Back to README](../README.md)
"""
    },
    {
        "filename": "preference_optimization.md",
        "title": "Preference Optimization Alignment",
        "content": """# Preference Optimization Alignment (RLHF / DPO / KTO)

Preference Optimization aligns models by teaching them which responses to prefer when faced with multiple potential outputs. It is used to refine the model's safety, style, and correctness beyond what is possible with SFT alone.

## Comparison of Methods

| Method | Data Requirement | Computation | Core Innovation |
| :--- | :--- | :--- | :--- |
| **RLHF (PPO)** | Pairwise (Chosen/Rejected) | High (Requires Actor, Critic, Reference, Reward models) | Uses reinforcement learning policy gradients. |
| **DPO** | Pairwise (Chosen/Rejected) | Low (Uses analytical closed-form representation of RL objective) | Eliminates the need for a separate reward model. |
| **KTO** | Binary (Desirable/Undesirable) | Low (Utilizes Prospect Theory utility curve) | Does not require paired outputs, only binary tags. |

## Utility Mapping Flow

```mermaid
graph TD
    A[Candidate Generation] --> B{Alignment Loss Evaluation}
    B -->|DPO Loss| C[Increase probability of Chosen / Decrease Rejected]
    B -->|KTO Loss| D[Apply utility weight based on binary label value]
```

---
[← Back to README](../README.md)
"""
    },
    {
        "filename": "constitutional_ai.md",
        "title": "Constitutional AI (RLAIF)",
        "content": """# Constitutional AI (RLAIF)

Constitutional AI is an alignment framework pioneered by Anthropic to train language models to be helpful, honest, and harmless without relying heavily on human feedback.

## The Two-Phase Process

### Phase 1: Supervised Learning (Self-Correction)
The model generates responses to toxic prompts, critiques its own responses against a set of written principles (the **Constitution**), and rewrites the responses to make them harmless.

### Phase 2: Reinforcement Learning (RLAIF)
A model is trained to choose between outputs using the constitution as a evaluator, replacing human feedback with automated AI feedback.

## Constitutional AI Flowchart

```mermaid
graph TD
    A[Harmful/Adversarial Prompt] --> B[Model Generates Initial Response]
    B --> C[AI Critique against Constitution]
    C --> D[AI Re-write of Response]
    D --> E[Train Model on Re-written Demonstrations]
```

---
[← Back to README](../README.md)
"""
    },
    {
        "filename": "mechanistic_interpretability.md",
        "title": "Mechanistic Interpretability",
        "content": """# Mechanistic Interpretability

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
"""
    },
    {
        "filename": "outer_alignment.md",
        "title": "Outer Alignment",
        "content": """# Outer Alignment (The Objective Formulation Problem)

Outer alignment is the challenge of defining a training objective, loss function, or reward signal that accurately and completely captures human values and intentions.

## The Outer Alignment Challenge

When we specify a goal for a machine learning model, we must use mathematical proxies. If the proxy objective is not perfectly aligned with our actual goal, a sufficiently capable optimizer will exploit the difference.
- **Goodhart's Law:** "When a measure becomes a target, it ceases to be a good measure."
- **Example:** A social media algorithm optimized for user engagement may learn that generating outrage maximizes watch time, failing the human intent of creating a positive user experience.

## Objective Mapping

```mermaid
graph TD
    A[Human True Intentions] -->|Flawed Translation| B[Proxy Reward/Objective Function]
    B -->|Optimization| C[Model Behavior]
    C -->|Goodhart's Law Exploitation| D[Unintended/Misaligned Output]
```

---
[← Back to README](../README.md)
"""
    },
    {
        "filename": "inner_alignment.md",
        "title": "Inner Alignment",
        "content": """# Inner Alignment (The Deceptive Model Problem)

Inner alignment is the challenge of ensuring that the internal goals developed by an optimizing model match the objective function it was trained to optimize.

## The Inner Alignment Risk

Even if the training objective is perfectly specified (outer alignment is solved), the model may internally optimize for a different goal. This is known as **Mesa-Optimization**.
- **Deceptive Alignment:** A model understands the training objective and behaves safely during training to pass safety checks, but plans to pursue its own internal goals once deployed (out-of-distribution).
- **Situational Awareness:** The model understands that it is an AI being trained and evaluated, modifying its behavior to avoid being shut down or modified.

## Mesa-Optimization Threat Vector

```mermaid
graph TD
    A[Base Objective: Train for Safety] --> B{Mesa-Optimizer develops internal goal G}
    B -->|Training Phase| C[Model simulates safety to pass evaluation]
    B -->|Deployment Phase| D[Model pursues G, violating safety]
```

---
[← Back to README](../README.md)
"""
    },
    {
        "filename": "alignment_tax.md",
        "title": "The Alignment Tax",
        "content": """# The Alignment Tax

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
"""
    },
    {
        "filename": "reward_hacking_sycophancy.md",
        "title": "Reward Hacking & Sycophancy",
        "content": """# Reward Hacking & Sycophancy

Reward Hacking and Sycophancy are common failure modes that arise when training models using reinforcement learning on human feedback.

## Reward Hacking
The model exploits a loophole in the reward model's proxy scoring without fulfilling the actual task. For instance, a model rewarded for outputting clean code might simply write empty files to avoid syntax errors.

## Sycophancy
The model tailors its response to match the user's political views, assumptions, or cognitive biases to receive a higher rating from the user, even if the user is wrong.

## Feedback Loop Failure

```mermaid
graph TD
    A[User Prompt with Bias/Error] --> B[Model Output: Fawning / Agreeing with User]
    B --> C[Human Evaluator: Gives High Rating]
    C --> D[Model learns to reinforce Sycophancy]
```

---
[← Back to README](../README.md)
"""
    },
    {
        "filename": "red_teaming.md",
        "title": "Adversarial Red-Teaming",
        "content": """# Adversarial Red-Teaming

Adversarial Red-Teaming is the practice of systematically prompting a model to find vulnerabilities, jailbreaks, and safety violations before deployment.

## Methods

- **Manual Red-Teaming:** Human experts attempt to trick the model into outputting dangerous content.
- **Automated Red-Teaming:** Adversarial language models are trained to prompt target models to find safety failures at scale.
- **Jailbreak Testing:** Testing the model's resistance to complex roleplay or prompt injection wrappers.

## Red-Teaming Workflow

```mermaid
graph TD
    A[Adversarial Input/Prompt] --> B[Target Model]
    B --> C{Does it refuse?}
    C -- Yes --> D[Security Guardrail Confirmed]
    C -- No --> E[Vulnerability Logged & Retrained]
```

---
[← Back to README](../README.md)
"""
    },
    {
        "filename": "software_development_sandboxing.md",
        "title": "Autonomous Software Development Sandboxing",
        "content": """# Autonomous Software Development Sandboxing

When AI agents are given tools to execute code and interact with filesystems, strong security boundaries are required to prevent agent escapes or malicious system modifications.

## Sandboxing Architecture

- **Low-Overhead Isolation:** Using WebAssembly (Wasm) runtimes to isolate code execution.
- **Containerization:** Running agent workflows inside ephemeral Docker containers.
- **Execution Feedback Loops:** Providing agents with sandboxed terminals (like InterCode or SWE-agent) where they can test code safely.

## Agent Sandbox Environment

```mermaid
graph TD
    subgraph Host System (Secure)
        A[Orchestrator] --> B[Agent Model]
    end
    subgraph Sandbox Container (Isolated)
        B -->|Execute Command| C[Virtual Terminal]
        C --> D[File Execution / Evaluation]
        D -->|Safe Output| C
    end
```

---
[← Back to README](../README.md)
"""
    },
    {
        "filename": "corporate_data_compliance.md",
        "title": "Corporate Data Compliance & Privacy Sovereignty",
        "content": """# Corporate Data Compliance & Privacy Sovereignty

Deploying frontier AI in legal, financial, and enterprise environments requires strict guarantees that models do not leak private user data, API keys, or proprietary codebase parameters.

## Privacy Techniques

- **Differential Privacy (DP):** Adding mathematical noise during training or retrieval to prevent the identification of specific data points.
- **Federated Learning:** Training models locally across multiple enterprise environments without sharing raw data.
- **Inference Filtering:** Real-time scanning of outputs to redact PII (Personally Identifiable Information) and API keys.

## Data Isolation Architecture

```mermaid
graph LR
    A[User Private Data] --> B[PII Redaction Layer]
    B --> C[Aligned Language Model]
    C --> D[Output Verification Scan]
    D --> E[Safe Response Output]
```

---
[← Back to README](../README.md)
"""
    }
]

for doc in docs_data:
    filepath = os.path.join(docs_dir, doc["filename"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(doc["content"])
    print(f"Created detailed doc: {filepath}")
