# Architecture Design: Contrastive Learning for SNP Classification

## 1. Research Objective
The goal is to design a deep learning architecture that leverages **Contrastive Learning (CL)** to learn robust, high-dimensional representations of Single Nucleotide Polymorphisms (SNPs). These representations will then be used for downstream classification tasks (e.g., predicting pathogenicity, phenotypic association, or functional impact) where labeled data is often scarce compared to the abundance of unlabeled genomic sequences.

---

## 2. Data Representation & Augmentation Strategy
Contrastive learning relies heavily on the ability to create "positive" pairs through data augmentation. Since DNA is a discrete sequence, traditional image-based augmentations (rotation, cropping) are inapplicable.

### 2.1 Input Representation
*   **Primary Input:** A window of genomic sequence centered around the SNP site.
*   **Encoding:** One-hot encoding of nucleotides $\{A, C, G, T\}$ or k-mer embeddings to capture local motifs.
*   **Auxiliary Features:** Integration of conservation scores (e.g., PhyloP) and biochemical properties as additional channels.

### 2.2 Genomic Augmentation Suite ($\mathcal{T}$)
To create a positive pair $(x_i, x_j)$, we apply two different stochastic transformations:
1.  **Random Masking:** Randomly replacing $15\%$ of nucleotides in the flanking regions with a `[MASK]` token.
2.  **Synonymous Substitution (if coding):** Replacing bases with others that maintain the same amino acid, preserving functional semantics while changing the raw string.
3.  **Jittering Conservation Scores:** Adding Gaussian noise to continuous auxiliary features.
4.  **Sub-sequence Shuffling:** Randomly swapping small non-conserved blocks within the window.

---

## 3. Proposed Architecture: SNP-ContrastNet

### 3.1 High-Level Pipeline
The architecture follows a two-stage paradigm: **Self-Supervised Pre-training** followed by **Supervised Fine-tuning**.

#### Stage I: Contrastive Pre-training
*   **Encoder ($f_\theta$):** A Hybrid CNN-Transformer architecture. 
    *   *CNN Layers:* Extract local motifs and spatial correlations of the SNP site.
    *   *Transformer Blocks:* Capture long-range dependencies between the SNP and distant regulatory elements (enhancers/promoters).
*   **Projection Head ($g_\phi$):** A small MLP (Multi-Layer Perceptron) that maps the latent representation $h$ to a hypersphere where contrastive loss is calculated. This prevents the encoder from collapsing into a trivial solution.
*   **Loss Function:** **NT-Xent (Normalized Temperature-scaled Cross Entropy)**. It maximizes agreement between two augmented views of the same SNP while minimizing agreement with other SNPs in the batch.

#### Stage II: Downstream Classification
*   The projection head $g_\phi$ is discarded.
*   A **Classification Head** (Linear layer + Softmax) is attached to the encoder $f_\theta$.
*   The model is fine-tuned on a small labeled dataset of SNP classifications.

### 3.2 Architectural Diagram (Conceptual)
`Input x` $\rightarrow$ `Augmentation T1/T2` $\rightarrow$ `Encoder f(θ)` $\rightarrow$ `Projection g(φ)` $\rightarrow$ `Contrastive Loss`
`Fine-tuning:` `Input x` $\rightarrow$ `Encoder f(θ)` $\rightarrow$ `Classifier` $\rightarrow$ `Cross-Entropy Loss`

---

## 4. Comparison of Approaches

| Approach | Mechanism | Pros | Cons |
| :--- | :--- | :--- | :--- |
| **SimCLR Style** | Large batch size, symmetric augmentation. | Simple to implement; strong representations. | Requires massive memory for large batches of negative samples. |
| **MoCo Style** | Momentum encoder + Queue of negatives. | Memory efficient; decouples batch size from negative count. | More complex hyperparameters (momentum coefficient). |
| **BYOL Style** | No negative pairs; predicts one view from another. | Avoids "sampling bias" and the need for large batches. | Higher risk of representation collapse if not carefully regularized. |
| **Multi-View CL** | Contrast between DNA sequence $\leftrightarrow$ Protein structure. | Incorporates biological priors (cross-modal). | Requires paired data (DNA and 3D protein structures). |

**Selected Approach:** A **MoCo-inspired Hybrid Encoder**. Given the vastness of genomic data, a momentum queue allows us to contrast the target SNP against thousands of negative examples without requiring prohibitive GPU memory.

---

## 5. Trade-offs & Weaknesses

### 5.1 Trade-offs
*   **Model Complexity vs. Interpretability:** Using Transformers captures long-range interactions but makes it harder to identify exactly *which* base pair triggered the classification compared to a simple Random Forest on SNP features.
*   **Augmentation Strength:** Too much augmentation (e.g., excessive masking) destroys the biological signal of the SNP; too little leads to "shortcut learning" where the model memorizes noise rather than genomic patterns.

### 5.2 Potential Weaknesses
*   **The "Collapse" Problem:** In contrastive learning, the model may find a trivial solution where all inputs map to a single constant vector. This is mitigated by the projection head and temperature scaling in NT-Xent.
*   **Data Leakage:** If SNPs from the same gene or haplotype appear in both positive and negative sets, the model might learn "gene identity" rather than "functional impact."
*   **Computational Cost:** Pre-training on whole-genome SNP datasets is computationally expensive, requiring significant TFLOPS for the Transformer layers.

---

## 6. Summary of Design Decisions
1.  **Hybrid Architecture:** CNNs for motifs $\rightarrow$ Transformers for context.
2.  **Momentum Contrast (MoCo):** To handle large negative sample sets efficiently.
3.  **Biologically-Informed Augmentation:** Masking and synonymous substitutions to preserve semantic meaning.
4.  **Two-Phase Training:** Decoupling representation learning from label-dependent classification to combat data scarcity.