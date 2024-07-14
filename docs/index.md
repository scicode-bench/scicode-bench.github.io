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
‡ Corresponding to: {mtian8, haopeng}@illinois.edu, elihu@anl.gov
</p>

## Introduction
SciCode is a newly developed benchmark designed to evaluate the capabilities of language models (LMs) in generating code for solving realistic scientific research problems. It has a diverse coverage of **6** domains: Physics, Math, Material Science, Biology, and Chemistry. They span 16 diverse natural science sub-fields. Unlike previous benchmarks that consist of question-answer pairs, SciCode problems naturally factorize into multiple subproblems, each involving knowledge recall, reasoning, and code synthesis. In total, SciCode contains **338** subproblems decomposed from **80** challenging main problems, and it offers optional descriptions specifying useful scientific background information and scientist-annotated gold-standard solutions and test cases for evaluation. Claude3.5-Sonnet, the best-performing model among those tested, can solve only **4.6%** of the problems in the most realistic setting. 


## Overview

![alt text](https://github.com/scicode-bench/website-draft/blob/main/docs/figures/SciCode_example_problem.png)
## Benchmark Statistics

| **Fields**           | **Subfields**                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------|
| **Mathematics**      | [Numerical Linear Algebra](#numerical-linear-algebra) (7), [Computational Mechanics](#computational-mechanics) (6), [Computational Finance](#computational-finance) (1) |
| **Physics**          | [Condensed Matter Physics](#condensed-matter-physics) (13), [Optics](#optics) (10), [Quantum Information/Computing](#quantum-informationcomputing) (6), [Computational Physics](#computational-physics) (5), [Astrophysics](#astrophysics) (2), [Particle Physics](#particle-physics) (1) |
| **Chemistry**        | [Quantum Chemistry](#quantum-chemistry) (5), [Computational Chemistry](#computational-chemistry) (3)          |
| **Biology**          | [Ecology](#ecology) (6), [Biochemistry](#biochemistry) (1), [Genetics](#genetics) (1)                         |
| **Material Science** | [Semiconductor Materials](#semiconductor-materials) (7), [Molecular Modeling](#molecular-modeling) (6)       |

### Numerical Linear Algebra
1.
2.
3.
4.
5.
6.
7.

### Computational Mechanics
1.
2.
3.
4.
5.
6.

### Computational Finance
1.

### Condensed Matter Physics
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.

### Optics
1.
2.
3.
4.
5.
6.
7.
8.
9.
10.

### Quantum Information/Computing
1.
2.
3.
4.
5.
6.

### Computational Physics
1.
2.
3.
4.
5.

### Astrophysics
1.
2.

### Particle Physics
1.

### Quantum Chemistry
1.
2.
3.
4.
5.

### Computational Chemistry
1.
2.
3.

### Ecology
1.
2.
3.
4.
5.
6.

### Biochemistry
1.

### Genetics
1.

### Semiconductor Materials
1.
2.
3.
4.
5.
6.
7.

### Molecular Modeling
1.
2.
3.
4.
5.
6.



<div class="grid cards" markdown>

-   :material-book:{ .lg .middle } __Leaderboard__

    ---

    How good are LMs at science, really?

    [:octicons-arrow-right-24: Browse the results](leaderboard.md)

-   :material-book:{ .lg .middle } __Paper__

    ---

    Learn all the details

    [:octicons-arrow-right-24: Read the paper](https://arxiv.com)
</div>



<div class="grid cards" markdown>


-   :material-play:{ .lg .middle } __Installation & usage__

    ---

    Learn how to evaluate your model

    [:octicons-arrow-right-24: Read the docs](docs/index.md)

</div>
