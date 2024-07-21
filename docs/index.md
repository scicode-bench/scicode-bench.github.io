# SciCode: A Research Coding Benchmark Curated by Scientists

<p align="center">
<strong>Minyang Tian<sup>1,2*‡</sup>, Luyu Gao<sup>3*</sup>, Shizhuo Dylan Zhang<sup>1</sup>, Xinan Chen<sup>1†</sup>, Cunwei Fan<sup>1†</sup>, Xuefei Guo<sup>1†</sup>, Roland Haas<sup>1†</sup>, Pan Ji<sup>4†</sup>, Kittithat Krongchon<sup>1†</sup>, Yao Li<sup>1†</sup>, Shengyan Liu<sup>1†</sup>, Di Luo<sup>5,6,11†</sup>, Yutao Ma<sup>7†</sup>, Hao Tong<sup>1†</sup>, Kha Trinh<sup>7†</sup>, Chenyu Tian<sup>8†</sup>, Zihan Wang<sup>1†</sup>, Bohao Wu<sup>1†</sup>, Yanyu Xiong<sup>9†</sup>, Shengzhu Yin<sup>1†</sup>, Minhui Zhu<sup>1†</sup>, Kilian Lieret<sup>10</sup>, Yanxin Lu<sup>1</sup>, Genglin Liu<sup>1</sup>, Yufeng Du<sup>1</sup>, Tianhua Tao<sup>1</sup>, Ofir Press<sup>10</sup>, Jamie Callan<sup>3</sup>, Eliu Huerta<sup>1,2,7‡</sup>, Hao Peng<sup>1‡</sup></strong>
</p>

<p align="center">
<sup>1</sup>University of Illinois Urbana-Champaign  
<sup>2</sup>Argonne National Laboratory  
<sup>3</sup>Carnegie Mellon University  
<sup>4</sup>University of North Carolina at Chapel Hill  
<sup>5</sup>Massachusetts Institute of Technology  
<sup>6</sup>Harvard University  
<sup>7</sup>University of Chicago  
<sup>8</sup>University of Texas at Austin  
<sup>9</sup>Stanford University  
<sup>10</sup>Princeton University  
<sup>11</sup>The NSF AI Institute for Artificial Intelligence and Fundamental Interactions  
</p>

<p align="center">
* Equal contribution lead authors. † Data curation, alphabetical order.
‡ Corresponding to: {mtian8, haopeng}@illinois.edu, elihu@{anl.gov, uchicago.edu}
</p>


<div class="grid cards" markdown>

-   :material-book:{ .lg .middle } __Paper__

    ---

    Learn all the details

    [:octicons-arrow-right-24: Read the paper](https://github.com/scicode-bench/scicode-bench.github.io/blob/main/SciCode.pdf)

-   :material-download:{ .lg .middle } __Dataset__

    ---

    Browse all the problems

    [:octicons-arrow-right-24: Download Dataset](https://raw.githubusercontent.com/scicode-bench/scicode-bench.github.io/main/data/data.zip)


-   :material-github:{ .lg .middle } __Github Repo__

    ---

    Learn how to evaluate your model

    [:octicons-arrow-right-24: Installation & usage](https://github.com/scicode-bench/SciCode)

-   :material-trending-up:{ .lg .middle } __Leaderboard__

    ---

    How good are LMs at science, really?
    (Coming soon...)

    [:octicons-arrow-right-24: Browse the results](leaderboard.md)

</div>

    

## Introduction
<p align="justify">
SciCode is a challenging benchmark designed to evaluate the capabilities of language models (LMs) in generating code for solving realistic scientific research problems. It has a diverse coverage of <b>16</b> subdomains from <b>6</b> domains: Physics, Math, Material Science, Biology, and Chemistry. Unlike previous benchmarks that consist of exam-like question-answer pairs, SciCode is converted from real research problems. SciCode problems naturally factorize into multiple subproblems, each involving knowledge recall, reasoning, and code synthesis. In total, SciCode contains <b>338</b> subproblems decomposed from <b>80</b> challenging main problems, and it offers optional descriptions specifying useful scientific background information and scientist-annotated gold-standard solutions and test cases for evaluation. Claude3.5-Sonnet, the best-performing model among those tested, can solve only <b>4.6%</b> of the problems in the most realistic setting. Broadly, SciCode demonstrates a realistic and scientists' everyday workflow of identifying critical science concepts and facts and then transforming them into computation and simulation code. We believe SciCode not only helps demonstrate contemporary LLMs' progress towards helpful assistant for scientists but also helps shed light on future building and evaluation of scientific AI.
</p>


## Overview
<p align="justify">
SciCode sources challenging and realistic research-level coding problems across 6 natural science disciplines, covering a total of 16 subfields. This diverse selection ensures a comprehensive representation of the natural sciences, where extensive code development is essential. SciCode is mainly drawn from the scripts that scientists use in their everyday workflow. Many of these have been used in one or more publications, demonstrating their robustness and correctness.

Among various coding necessities, Scicode mainly focuses on: 1. Numerical methods. 2. Simulation of systems. 3. Scientific calculation. These are the tasks we believe require intense scientific knowledge and reasoning to optimally test LM’s science capability. The below figure is an example of the combination of 1 and 3.

In designing test cases for evaluation, we incorporate domain-specific test cases in addition to numerical cases. These tests are extracted from real scientific workflows: scientists must design domain-specific test cases to verify code accuracy by reproducing results published in papers or matching analytical solutions derived from theoretical models. Each problem goes through <b>3</b> rounds of validation (i.e. by in-domain scientists, out-of-domain scientists, GPT4) for quality control.
</p>
![Image Title](figures/SciCode_example_problem.png)
## Benchmark Statistics

| <b>Fields</b>           | <b>Subfields</b>                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------|
| <b>Mathematics</b>      | [Numerical Linear Algebra](problems.md#numerical-linear-algebra) (8), [Computational Mechanics](problems.md#computational-mechanics) (5), [Computational Finance](problems.md#computational-finance) (1) |
| <b>Physics</b>          | [Condensed Matter Physics](problems.md#condensed-matter-physics) (13), [Optics](problems.md#optics) (10), [Quantum Information/Computing](problems.md#quantum-informationcomputing) (6), [Computational Physics](problems.md#computational-physics) (5), [Astrophysics](problems.md#astrophysics) (2), [Particle Physics](problems.md#particle-physics) (1) |
| <b>Chemistry</b>        | [Quantum Chemistry](problems.md#quantum-chemistry) (5), [Computational Chemistry](problems.md#computational-chemistry) (3)          |
| <b>Biology</b>          | [Ecology](problems.md#ecology) (6), [Biochemistry](problems.md#biochemistry) (1), [Genetics](problems.md#genetics) (1)                         |
| <b>Material Science</b> | [Semiconductor Materials](problems.md#semiconductor-materials) (7), [Molecular Modeling](problems.md#molecular-modeling) (6)       |

![Image Title](figures/SciCode_chart.png)
<p style="text-align: center;">Left: Distribution of Main Problems   Right: Distribution of Subproblems</p>

<p align="justify">
We include several research problems that are built upon or reproduce methods used in Nobel Prize-winning studies to highlight current trends in scientific research: the self-consistent field (SCF) method for density functional theory (DFT) calculations (<b>The Nobel Prize in Chemistry 1998</b>), the PMNS matrix for neutrino oscillation in matter (<b>The Nobel Prize in Physics 2015</b>), the Haldane model for the anomalous quantum Hall effect (<b>The Nobel Prize in Physics 2016</b>), optical tweezer simulations for microscopic thermodynamics (<b>The Nobel Prize in Physics 2018</b>), and the replica method for spin glasses (<b>The Nobel Prize in Physics 2021</b>).
</p>

## Experiment Results
<p align="justify">
We evaluate our model using zero-shot prompts. We keep the prompts general and design different ones for different evaluation setups only to inform the model about the tasks. We keep prompts the same across models and fields, and they contain the model’s main and sub-problem instructions and code for previous subproblems. The standard setup means the model is tested without background knowledge and carrying over generated solutions to previous subproblems. The scientists' annotated background provides the necessary knowledge and reasoning steps to solve the problems, shifting the evaluation’s focus more towards the models’ coding and instruction-following capabilities.
</p>
![Image Title](figures/Standard_Setup.png)
![Image Title](figures/Standard_Background.png)
![Image Title](figures/Performance_Gain.png)

## Citation
```bibtex
@misc{tian2024scicode,
    title={SciCode: A Research Coding Benchmark Curated by Scientists},
    author={Minyang Tian and Luyu Gao and Shizhuo Dylan Zhang and Xinan Chen and Cunwei Fan and Xuefei Guo and Roland Haas and Pan Ji and Kittithat Krongchon and Yao Li and Shengyan Liu and Di Luo and Yutao Ma and Hao Tong and Kha Trinh and Chenyu Tian and Zihan Wang and Bohao Wu and Yanyu Xiong and Shengzhu Yin and Minhui Zhu and Kilian Lieret and Yanxin Lu and Genglin Liu and Yufeng Du and Tianhua Tao and Ofir Press and Jamie Callan and Eliu Huerta and Hao Peng},
    year={2024},
    eprint={2407.13168},
    archivePrefix={arXiv},
    primaryClass={cs.AI}
}
```
