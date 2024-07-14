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


## Introduction
SciCode is a newly developed benchmark designed to evaluate the capabilities of language models (LMs) in generating code for solving realistic scientific research problems. It has a diverse coverage of **6** domains: Physics, Math, Material Science, Biology, and Chemistry. They span 16 diverse natural science sub-fields. Unlike previous benchmarks that consist of question-answer pairs, SciCode problems naturally factorize into multiple subproblems, each involving knowledge recall, reasoning, and code synthesis. In total, SciCode contains **338** subproblems decomposed from **80** challenging main problems, and it offers optional descriptions specifying useful scientific background information and scientist-annotated gold-standard solutions and test cases for evaluation. Claude3.5-Sonnet, the best-performing model among those tested, can solve only **4.6%** of the problems in the most realistic setting. 


## Overview

![Image Title](https://github.com/scicode-bench/website-draft/blob/main/docs/figures/SciCode_example_problem.png)
## Benchmark Statistics

| **Fields**           | **Subfields**                                                                                                 |
|----------------------|---------------------------------------------------------------------------------------------------------------|
| **Mathematics**      | [Numerical Linear Algebra](#numerical-linear-algebra) (7), [Computational Mechanics](#computational-mechanics) (6), [Computational Finance](#computational-finance) (1) |
| **Physics**          | [Condensed Matter Physics](#condensed-matter-physics) (13), [Optics](#optics) (10), [Quantum Information/Computing](#quantum-informationcomputing) (6), [Computational Physics](#computational-physics) (5), [Astrophysics](#astrophysics) (2), [Particle Physics](#particle-physics) (1) |
| **Chemistry**        | [Quantum Chemistry](#quantum-chemistry) (5), [Computational Chemistry](#computational-chemistry) (3)          |
| **Biology**          | [Ecology](#ecology) (6), [Biochemistry](#biochemistry) (1), [Genetics](#genetics) (1)                         |
| **Material Science** | [Semiconductor Materials](#semiconductor-materials) (7), [Molecular Modeling](#molecular-modeling) (6)       |

Nobel prized related problems:

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

## Example Problem
### Main Problem and Dependencies
**1. Generate an array of Chern numbers for the Haldane model on a hexagonal lattice by sweeping the following parameters: the on-site energy to next-nearest-neighbor coupling constant ratio ($m/t_2$ from -6 to 6 with $N$ samples) and the phase ($\phi$ from -$\pi$ to $\pi$ with $N$ samples) values. Given the lattice spacing $a$, the nearest-neighbor coupling constant $t_1$, the next-nearest-neighbor coupling constant $t_2$, the grid size $\delta$ for discretizing the Brillouin zone in the $k_x$ and $k_y$ directions (assuming the grid sizes are the same in both directions), and the number of sweeping grid points $N$ for $m/t_2$ and $\phi$.**

``` python
'''
Inputs:
delta : float
    The grid size in kx and ky axis for discretizing the Brillouin zone.
a : float
    The lattice spacing, i.e., the length of one side of the hexagon.
t1 : float
    The nearest-neighbor coupling constant.
t2 : float
    The next-nearest-neighbor coupling constant.
N : int
    The number of sweeping grid points for both the on-site energy to next-nearest-neighbor coupling constant ratio and phase.

Outputs:
results: matrix of shape(N, N)
    The Chern numbers by sweeping the on-site energy to next-nearest-neighbor coupling constant ratio (m/t2) and phase (phi).
m_values: array of length N
    The swept on-site energy to next-nearest-neighbor coupling constant ratios.
phi_values: array of length N
    The swept phase values.
'''
```
```python
# Package Dependencies
import numpy as np
import cmath
from math import pi, sin, cos, sqrt
```
### Subproblems
**1.1 Write a Haldane model Hamiltonian on a hexagonal lattice, given the following parameters: wavevector components $k_x$ and $k_y$ (momentum) in the x and y directions, lattice spacing $a$, nearest-neighbor coupling constant $t_1$, next-nearest-neighbor coupling constant $t_2$, phase $\phi$ for the next-nearest-neighbor hopping, and the on-site energy $m$.**

**_Scientists Annotated Background:_**

Source: Haldane, F. D. M. (1988). Model for a quantum Hall effect without Landau levels: Condensed-matter realization of the" parity anomaly". Physical review letters, 61(18).

We denote $\{\mathbf{a}_i\}$ are the vectors from a B site to its three nearest-neighbor A sites, and $\{\mathbf{b}_i\}$ are next-nearest-neighbor distance vectors, then we have

$$
{\mathbf{a}_1} = (0,a),
$$

$$
{\mathbf{a}_2} = (\sqrt 3 a/2, - a/2),
$$

$$
{\mathbf{a}_3} = ( - \sqrt 3 a/2, - a/2)
$$

$$
{\mathbf{b}_1} = {\mathbf{a}_2} - {\mathbf{a}_3} = (\sqrt 3 a,0),
$$

$$
{\mathbf{b}_2} = {\mathbf{a}_3} - {\mathbf{a}_1} = ( - \sqrt 3 a/2, - 3a/2),
$$

$$
{\mathbf{b}_3} = {\mathbf{a}_1} - {\mathbf{a}_2} = ( - \sqrt 3 a/2,3a/2)
$$

Then the Haldane model on a hexagonal lattice can be written as

$$
H(k) = {d_0}I + {d_1}{\sigma _1} + {d_2}{\sigma _2} + {d_3}{\sigma _3}
$$

$${d_0} = 2{t_2}\cos \phi \sum\nolimits_i {\cos (\mathbf{k} \cdot {\mathbf{b}_i})} = 2{t_2}\cos \phi \left[ {\cos \left( {\sqrt 3 {k_x}a} \right) + \cos \left( { - \sqrt 3 {k_x}a/2 + 3{k_y}a/2} \right) + \cos \left( { - \sqrt 3 {k_x}a/2 - 3{k_y}a/2} \right)} \right]
$$

$$
{d_1} = {t_1}\sum\nolimits_i {\cos (\mathbf{k} \cdot {\mathbf{a}_i})}  = {t_1}\left[ {\cos \left( {{k_y}a} \right) + \cos \left( {\sqrt 3 {k_x}a/2 - {k_y}a/2} \right) + \cos \left( { - \sqrt 3 {k_x}a/2 - {k_y}a/2} \right)} \right]\\
$$

$$
{d_2} = {t_1}\sum\nolimits_i {\sin (\mathbf{k} \cdot {\mathbf{a}_i})}  = {t_1}\left[ {\sin \left( {{k_y}a} \right) + \sin \left( {\sqrt 3 {k_x}a/2 - {k_y}a/2} \right) + \sin \left( { - \sqrt 3 {k_x}a/2 - {k_y}a/2} \right)} \right] \\
$$

$$
{d_3} = m - 2{t_2}\sin \phi \sum\nolimits_i {\sin (\mathbf{k} \cdot {\mathbf{b}_i})}  = m - 2{t_2}\sin \phi \left[ {\sin \left( {\sqrt 3 {k_x}a} \right) + \sin \left( { - \sqrt 3 {k_x}a/2 + 3{k_y}a/2} \right) + \sin \left( { - \sqrt 3 {k_x}a/2 - 3{k_y}a/2} \right)} \right] \\
$$

where $\sigma_i$ are the Pauli matrices and $I$ is the identity matrix.
```python
def calc_hamiltonian(kx, ky, a, t1, t2, phi, m):
    """
    Function to generate the Haldane Hamiltonian with a given set of parameters.

    Inputs:
    kx : float
        The x component of the wavevector.
    ky : float
        The y component of the wavevector.
    a : float
        The lattice spacing, i.e., the length of one side of the hexagon.
    t1 : float
        The nearest-neighbor coupling constant.
    t2 : float
        The next-nearest-neighbor coupling constant.
    phi : float
        The phase ranging from -π to π.
    m : float
        The on-site energy.

    Output:
    hamiltonian : matrix of shape(2, 2)
        The Haldane Hamiltonian on a hexagonal lattice.
    """
```
```python
# test case 1
kx = 1
ky = 1
a = 1
t1 = 1
t2 = 0.3
phi = 1
m = 1
assert np.allclose(calc_hamiltonian(kx, ky, a, t1, t2, phi, m), target)
```
```python
# Test Case 2
kx = 0
ky = 1
a = 0.5
t1 = 1
t2 = 0.2
phi = 1
m = 1
assert np.allclose(calc_hamiltonian(kx, ky, a, t1, t2, phi, m), target)
```
```python
# Test Case 3
kx = 1
ky = 0
a = 0.5
t1 = 1
t2 = 0.2
phi = 1
m = 1
assert np.allclose(calc_hamiltonian(kx, ky, a, t1, t2, phi, m), target)
```
**1.2 Calculate the Chern number using the Haldane Hamiltonian, given the grid size $\delta$ for discretizing the Brillouin zone in the $k_x$ and $k_y$ directions (assuming the grid sizes are the same in both directions), the lattice spacing $a$, the nearest-neighbor coupling constant $t_1$, the next-nearest-neighbor coupling constant $t_2$, the phase $\phi$ for the next-nearest-neighbor hopping, and the on-site energy $m$.**

**_Scientists Annotated Background:_**

Source: Fukui, Takahiro, Yasuhiro Hatsugai, and Hiroshi Suzuki. "Chern numbers in discretized Brillouin zone: efficient method of computing (spin) Hall conductances." Journal of the Physical Society of Japan 74.6 (2005): 1674-1677.


Here we can discretize the two-dimensional Brillouin zone into grids with step $\delta {k_x} = \delta {k_y} = \delta$. If we define the U(1) gauge field on the links of the lattice as $U_\mu (\mathbf{k}_l) := \frac{\left\langle n(\mathbf{k}_l)\middle|n(\mathbf{k}_l + \hat{\mu})\right\rangle}{\left|\left\langle n(\mathbf{k}_l)\middle|n(\mathbf{k}_l + \hat{\mu})\right\rangle\right|}$, where $\left|n(\mathbf{k}_l)\right\rangle$ is the eigenvector of Hamiltonian at $\mathbf{k}_l$, $\hat{\mu}$ is a small displacement vector in the direction $\mu$ with magnitude $\delta$, and $\mathbf{k}_l$ is one of the momentum space lattice points $l$. The corresponding curvature (flux) becomes

$$
F_{xy}(\mathbf{k}_l) := \ln \left[U_x(\mathbf{k}_l)U_y(\mathbf{k}_l+\hat{x})U_x^{-1}(\mathbf{k}_l+\hat{y})U_y^{-1}(\mathbf{k}_l)\right]
$$

and the Chern number of a band can be calculated as

$$
c = \frac{1}{2\pi i} \Sigma_l F_{xy}(\mathbf{k}_l),
$$
where the summation is over all the lattice points $l$. Note that the Brillouin zone of a hexagonal lattice with spacing $a$ can be chosen as a rectangle with $0 \le {k_x} \le k_{x0} = 2\sqrt 3 \pi /(3a),0 \le {k_y} \le k_{y0} = 4\pi /(3a)$.
```python
def compute_chern_number(delta, a, t1, t2, phi, m):
    """
    Function to compute the Chern number with a given set of parameters.

    Inputs:
    delta : float
        The grid size in kx and ky axis for discretizing the Brillouin zone.
    a : float
        The lattice spacing, i.e., the length of one side of the hexagon.
    t1 : float
        The nearest-neighbor coupling constant.
    t2 : float
        The next-nearest-neighbor coupling constant.
    phi : float
        The phase ranging from -π to π.
    m : float
        The on-site energy.

    Output:
    chern_number : float
        The Chern number, a real number that should be close to an integer. The imaginary part is cropped out due to the negligible magnitude.
    """
```

```python
# test case 1
delta = 2 * np.pi / 200
a = 1
t1 = 4
t2 = 1
phi = 1
m = 1
assert np.allclose(compute_chern_number(delta, a, t1, t2, phi, m), target)
```

```python
# test case 2
delta = 2 * np.pi / 100
a = 1
t1 = 1
t2 = 0.3
phi = -1
m = 1
assert np.allclose(compute_chern_number(delta, a, t1, t2, phi, m), target)
```

```python
# test case 3
delta = 2 * np.pi / 100
a = 1
t1 = 1
t2 = 0.2
phi = 1
m = 1
assert np.allclose(compute_chern_number(delta, a, t1, t2, phi, m), target)
```

**1.3 Make a 2D array of Chern numbers by sweeping the parameters: the on-site energy to next-nearest-neighbor coupling ratio ($m/t_2$ from -6 to 6 with $N$ samples) and phase ($\phi$ from -$\pi$ to $\pi$ with $N$ samples) values. Given the grid size $\delta$ for discretizing the Brillouin zone in the $k_x$ and $k_y$ directions (assuming the grid sizes are the same in both directions), the lattice spacing $a$, the nearest-neighbor coupling constant $t_1$, and the next-nearest-neighbor coupling constant $t_2$.**
```python
def compute_chern_number_grid(delta, a, t1, t2, N):
    """
    Function to calculate the Chern numbers by sweeping the given set of parameters and returns the results along with the corresponding swept next-nearest-neighbor coupling constant and phase.

    Inputs:
    delta : float
        The grid size in kx and ky axis for discretizing the Brillouin zone.
    a : float
        The lattice spacing, i.e., the length of one side of the hexagon.
    t1 : float
        The nearest-neighbor coupling constant.
    t2 : float
        The next-nearest-neighbor coupling constant.
    N : int
        The number of sweeping grid points for both the on-site energy to next-nearest-neighbor coupling constant ratio and phase.

    Outputs:
    results: matrix of shape(N, N)
        The Chern numbers by sweeping the on-site energy to next-nearest-neighbor coupling constant ratio (m/t2) and phase (phi).
    m_values: array of length N
        The swept on-site energy to next-nearest-neighbor coupling constant ratios.
    phi_values: array of length N
        The swept phase values.
    """
```

### Domain Specific Test Cases
**Both the $k$-space and sweeping grid sizes are set to very rough values to make the computation faster, feel free to increase them for higher accuracy.**

**At zero on-site energy, the Chern number is 1 for $\phi > 0$, and the Chern number is -1 for $\phi < 0$.**

**For complementary plots, we can see that these phase diagrams are similar to the one in the original paper: Fig.2 in [Haldane, F. D. M. (1988)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.61.2015). To achieve a better match, decrease all grid sizes.**


**Compare the following three test cases. We can find that the phase diagram is independent of the value of $t_1$, and the ratio of $t_2/t_1$, which is consistent with our expectations.**

```python
# Test Case 1
delta = 2 * np.pi / 30
a = 1.0
t1 = 4.0
t2 = 1.0
N = 40
```
![alt text](https://github.com/scicode-bench/website-draft/blob/main/docs/figures/chern_number_1.png)

```python
# Test Case 2
delta = 2 * np.pi / 30
a = 1.0
t1 = 5.0
t2 = 1.0
N = 40
```
![alt text](https://github.com/scicode-bench/website-draft/blob/main/docs/figures/chern_number_2.png)

```python
# Test Case 3
delta = 2 * np.pi / 30
a = 1.0
t1 = 1.0
t2 = 0.2
N = 40
```
![alt text](https://github.com/scicode-bench/website-draft/blob/main/docs/figures/chern_number_3.png)

