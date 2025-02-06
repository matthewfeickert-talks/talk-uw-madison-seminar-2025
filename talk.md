class: middle, center, title-slide
count: false

# Towards Differentiable Physics Analysis at the
# High-Luminosity Large Hadron Collider
# and Beyond

.huge.blue[Matthew Feickert]<br>
.huge[(University of Wisconsin-Madison)]
<br><br>
[matthew.feickert@cern.ch](mailto:matthew.feickert@cern.ch)

[UC Berkeley Neyman](https://events.berkeley.edu/neyman-seminar/event/236154-neyman-seminar-matthew-feickert) [Seminar](https://matthewfeickert-talks.github.io/talk-uc-berkeley-research-seminar-2024/)

January 31st, 2024

<!-- ---
# Notes

* .bold[Time]: 45 minutes .bold[talk] + 5-10 minutes .bold[questions]
* .bold[Prompt]: Research seminar focusing on past work. It will be open to faculty, students, other departments and a broader audience.
* .bold[Abstract:] With the High-Luminosity Large Hadron Collider (HL-LHC) era on the horizon for physics analysis at the LHC experiments, there are multiple computing and data challenges to be overcome to efficiently analyze and extract the most scientific value from the unique and valuable data collected. In this seminar I will present a high-level overview of how applications of data science tools from the modern scientific open source community, techniques and applications from the field of automatic differentiation, and strategies for enabling analysis reuse can be leveraged to tackle scientific analysis at the HL-LHC scale and beyond. -->

---
# Introduction

.kol-2-3[
.huge[
* As a "data physicist" have privileged opportunity to work among multiple scientific communities
* Care about .bold[reusable] open science to be able to push the physical sciences forward at the .bold[community scale]
   - The challenges of the next decade provide wonderful research environments that will require interdisciplinary knowledge exchange to fully engage
* Today I'll share .bold[high level] views of deeply .bold[technical problems]
]
]
.kol-1-3[
.center.width-65[[![logo_IRIS-HEP](assets/logos/logo_institution.png)](https://datascience.wisc.edu/institute/)]

.center.width-40[[![logo_ATLAS](assets/logos/logo_ATLAS.png)](https://atlas.cern/)]

.center.width-40[[![logo_IRIS-HEP](assets/logos/logo_IRIS-HEP.png)](https://iris-hep.org/)]

.center.width-30[[![logo_Scikit-HEP](figures/scikit-hep-logo.svg)](https://scikit-hep.org/)]

.center.width-30[[![logo_joss](figures/joss_logo.png)](https://joss.theoj.org/)]
]

---
# High Energy Physics at the LHC

.kol-1-2.center[
<p style="text-align:center;">
   <a href="https://home.cern/science/accelerators/large-hadron-collider/">
      <img src="figures/LHC.jpg"; width=100%>
   </a>
</p>
.caption[LHC]
]
.kol-1-2.center[
<p style="text-align:center;">
   <a href="https://atlas.cern/">
      <img src="figures/ATLAS_TRex.png"; width=100%>
   </a>
</p>
.caption[ATLAS]
]
.kol-1-1[
.kol-1-2.center[
<p style="text-align:center;">
   <a href="https://twitter.com/HEPfeickert/status/1269406145858469891?s=20">
      <img src="figures/SM_mug.jpg"; width=45%>
   </a>
</p>
]
.kol-1-2.center[
.kol-1-2.center[
<p style="text-align:center;">
   <a href="https://twitter.com/HEPfeickert/status/1269406145858469891?s=20">
      <img src="figures/ParticleZoo_Higgs.jpg"; width=100%>
   </a>
</p>
]
.kol-1-2.center[
<p style="text-align:center;">
   <a href="https://twitter.com/HEPfeickert/status/1269406145858469891?s=20">
      <img src="figures/ParticleZoo_DarkMatter.jpg"; width=85%>
   </a>
</p>
]
]
]

---
# High Energy Physics at the LHC

.kol-1-2.center[
<p style="text-align:center;">
   <a href="https://howlargeisthelhc.com/">
      <img src="figures/how-large-is-the-lhc.png"; width=60%>
   </a>
</p>
.caption[LHC]
]
.kol-1-2.center[
<p style="text-align:center;">
   <a href="https://atlas.cern/">
      <img src="figures/ATLAS_TRex.png"; width=100%>
   </a>
</p>
.caption[ATLAS]
]
.kol-1-1[
.kol-1-2.center[
<p style="text-align:center;">
   <a href="https://twitter.com/HEPfeickert/status/1269406145858469891?s=20">
      <img src="figures/SM_mug.jpg"; width=45%>
   </a>
</p>
]
.kol-1-2.center[
.kol-1-2.center[
<p style="text-align:center;">
   <a href="https://twitter.com/HEPfeickert/status/1269406145858469891?s=20">
      <img src="figures/ParticleZoo_Higgs.jpg"; width=100%>
   </a>
</p>
]
.kol-1-2.center[
<p style="text-align:center;">
   <a href="https://twitter.com/HEPfeickert/status/1269406145858469891?s=20">
      <img src="figures/ParticleZoo_DarkMatter.jpg"; width=85%>
   </a>
</p>
]
]
]

---
# High Energy Physics at the LHC

<p style="text-align:center;">
   <!-- original dimensions: https://videos.cern.ch/record/2298073
   width = 560, height-315  -->
   <iframe scrolling="no"  src="https://videos.cern.ch/video/ATLAS-VIDEO-2023-013-001?autoplay=1&loop=1" width="840" height="473" frameborder="0" allowfullscreen></iframe>
</p>
.center[[Animated ATLAS event display of simulated new physics (.italic[Phys. Lett. B 848 (2024) 138324])](https://atlaspo.cern.ch/public/event_display/)]

---
# High Energy Physics at the LHC

.kol-3-5[
.large[
* LHC beam crossing at experiments every .bold[25 ns] <br>(.bold[40 MHz] collisions)
   - Would translate to around 100 terabytes per second ⚠️
   - Use real time data processing ("trigger") system to only keep potentially interesting collisions
   - Use further physics specific selections before writing to disk to reduce data stream even more
* Translates to roughly .bold[90 petabytes] of collision data recorded per year
<!-- * LHC Run 2 produced data set 5x that used for the 2012 Higgs discovery -->
* LHC data taking scheduled to continue for another roughly .bold[20 years]
   - Majority of data is yet to come!
   - The roughly 10% taken already challenging
]
]
.kol-2-5[
<p style="text-align:center;">
   <img src="figures/lhc_lumi.png"; width=90%>
.center[Planned (HL-)LHC lifetime data collection]
</p>
]

---
# Opportunities and Challenges of the HL-LHC
<!--  -->
<p style="text-align:center;">
   <a href="https://hilumilhc.web.cern.ch/content/hl-lhc-project">
      <img src="figures/HL-LHC_schedule.png"; width=69%>
   </a>
   <img src="figures/lhc_lumi.png"; width=30%>
</p>
<!--  -->
.large[
* Increase in data generating collision rate ("luminosity") of roughly order of magnitude
   - Factor of .bold[20-25] times the amount of collisions delivered from Run-2 of the LHC
* Boon for measurements constrained by statistical uncertainties, searches for rare processes
]

---
# Opportunities and Challenges of the HL-LHC

.center.large[Challenge to be able to .bold[record, store, and analyze] the data]

<p style="text-align:center;">
   <a href="https://cds.cern.ch/record/2802918">
      <img src="figures/HL-LHC-cpu-projections-atlas.png"; width=50%>
   </a>
.center[[ATLAS software and computing review](https://cds.cern.ch/record/2802918)]
</p>

.center.large[Projected .bold[required compute usage] for HL-LHC (want .blue[R]&.red[D] below .black[budget] line)]

---
# IRIS-HEP

.large[.bold[Execute R&D activities] required to close the HL-LHC software and computing gaps and serve as .bold[intellectual hub for larger community]]

.kol-3-5[
.huge.bold[[HL-LHC Software and Computing Gaps](https://inspirehep.net/literature/2628983)]
.huge[
1. Raw resource gaps

2. Scalability of the distributed computing cyberinfrastructure

3. Analysis at scale

4. Sustainability
]
]
.kol-2-5[
<p style="text-align:center;">
   <a href="https://iris-hep.org/">
      <img src="assets/logos/logo_IRIS-HEP.png"; width=100%>
   </a>
</p>
.center.large[Institute for Research and Innovation in Software for High Energy Physics (IRIS-HEP)]

.center[Supported by the National Science Foundation Cooperative Agreements <br>[OAC-1836650](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1836650) and [PHY-2323298](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2323298)
]
]

---
# IRIS-HEP

<p style="text-align:center;">
   <a href="https://iris-hep.org/about/team">
      <img src="figures/iris-hep-full-team.png"; width=90%>
   </a>
.center.large[Distributed team of professional physicists, computer scientists, software developers, <br>research software engineers, professors, and Ph.D. students from 20 institutions!]
</p>

---
# IRIS-HEP

.kol-1-1[
.kol-1-2[
.huge[
Designed around [focus areas](https://inspirehep.net/literature/2628983)
]
.large[
* Intellectual Hub
* Analysis Systems
* Data Organization, Management, and Access (DOMA)
* Innovative Algorithms
* Translational Research for AI
* Scalable Systems Laboratory (SSL)
* OSG Services for LHC (OSG-LHC)
]
]
.kol-1-2[
<br>
<p style="text-align:center;">
   <a href="https://iris-hep.org/">
      <img src="figures/IRIS-HEP-executive-board.png"; width=100%>
   </a>
</p>
.caption[IRIS-HEP Institute Structure]
]
]

.large[
community engagement with .bold[training, education, and outreach] and .bold[institute grand challenges]
]

<!-- https://github.com/iris-hep/analysis-grand-challenge/blob/382e512d39e9b62fc4d9da2c69e454dfc718c5f6/docs/index.rst#more-details-what-is-being-investigated-in-the-agc-context -->
---
# IRIS-HEP Analysis Systems

<p style="text-align:center;">
   <a href="https://iris-hep.org/as.html">
      <img src="figures/cabinetry-vertical-slice.png"; width=75%>
   </a>
</p>

.huge[
* Deployable analysis pipelines that reduces physicist time-to-insight
   - Tools integrate into the broader scientific Python computing ecosystem
* Analysis reuse as deployment feature
]

---
# IRIS-HEP Analysis Systems

<p style="text-align:center;">
   <a href="https://github.com/iris-hep/analysis-grand-challenge/blob/382e512d39e9b62fc4d9da2c69e454dfc718c5f6/docs/taskbackground.rst">
      <img src="figures/iris-hep_agc_ml_pipeline.png"; width=90%>
   </a>
</p>

.huge.center[
Integrating [machine learning training and inference](https://indico.jlab.org/event/459/contributions/11692/) into analysis workflows
]

---
# Ecosystems

<p style="text-align:center;">
   <a href="https://coiled.io/blog/pydata-dask/">
      <img src="figures/pydata-ecosystem-pycon-2017.png"; width=55%>
   </a>
</p>

.center.large[
In his [PyCon 2017 keynote](https://youtu.be/ZyjCqQEUa8o), Jake VanderPlas gave us the iconic "PyData ecosystem" image
]

---
# PyHEP ecosystem

<p style="text-align:center;">
   <a href="https://indico.cern.ch/event/1140031/">
      <img src="figures/pyhep-ecosystem.svg"; width=55%>
   </a>
</p>

.center.large[
In [2022](https://indico.cern.ch/event/1140031/) we created a view for the PyHEP ecosystem
]

---
# Community adoption ...

<p style="text-align:center;">
   <a href="https://github.com/matthewfeickert/talk-analysis-ecosystems-workshop-2022/issues/1">
      <img src="figures/pip-installs-summary.svg"; width=85%>
   </a>
</p>
.center.large["pip install XYZ" download rate for MacOS/Windows (no batch jobs) in aggregate]

.footnote[[Modern Python analysis ecosystem for High Energy Physics](https://matthewfeickert.github.io/talk-doepy-python-exchange-2022/2022-06-29.pdf), Jim Pivarski, Matthew Feickert, Gordon Watts]

---
# Community adoption with ecosystem growth

<p style="text-align:center;">
   <a href="https://github.com/matthewfeickert/talk-analysis-ecosystems-workshop-2022/issues/1">
      <img src="figures/pip-installs-by-package.svg"; width=85%>
   </a>
</p>
.center.large["pip install XYZ" download rate for MacOS/Windows (no batch jobs) by package]
.caption[Aided by interoperable design]

.footnote[[Modern Python analysis ecosystem for High Energy Physics](https://matthewfeickert.github.io/talk-doepy-python-exchange-2022/2022-06-29.pdf), Jim Pivarski, Matthew Feickert, Gordon Watts]

---
# Broader scientific open source collaborations

<br>

.kol-1-1[
.kol-1-3[
<p style="text-align:center;">
   <a href="https://github.com/dask-contrib/dask-awkward">
      <img src="figures/dask-horizontal.svg"; width=100%>
   </a>
</p>
]
.kol-1-3[
<p style="text-align:center;">
   <a href="https://scikit-build-core.readthedocs.io/">
      <img src="figures/scikit_build_logo.svg"; width=100%>
   </a>
</p>
]
.kol-1-3[
<p style="text-align:center;">
   <a href="https://numfocus.org/">
      <img src="figures/numfocus-logo.png"; width=100%>
   </a>
</p>
]
]
<!--  -->
.kol-1-3[
.center.huge[[dask-awkward](https://github.com/dask-contrib/dask-awkward)]

.center[Native Dask collection for partioned Awkward arrays for analysis at scale]
]
.kol-1-3[
.center.huge[[scikit-build-core](https://scikit-build-core.readthedocs.io/)]

.center[Next generation of build tools for scientific packaging]
]
.kol-1-3[
.center.huge[[NumFOCUS](https://numfocus.org/)]

.center[Organizing and supporting scientific open source]
]

---
# Automatic differentiation as tool for science

<!-- .footnote[Taking a [slide](https://indico.ph.tum.de/event/7113/contributions/7705/) from Lukas Heinrich] -->

.kol-1-2[
<p style="text-align:center;">
   <img src="figures/freeman-dyson.png"; width=65%>
</p>
]
.kol-1-2.huge[
<br><br>
.bold[New directions in science are launched by new tools much more often than by new concepts.]<br>&mdash; .italic[Imagined Worlds], 1997, Freeman Dyson
]

---
# Gradients as Computational Tools

- As we'll see later, having access to the gradient while performing minimization is .bold[highly beneficial]!
- Can imagine multiple ways of arriving at gradients for computational functions
   <!-- - But want them to be both .bold[exact] and .bold[flexible] -->

.center.width-30[![carbon_f_x](figures/carbon_f_x.png)]
.kol-6-8[
.bold.center[Symbolic]
.center.width-100[![carbon_fprime_symbolic](figures/carbon_fprime_symbolic.png)]
]
.kol-2-8.huge[
<br>
- Exact: .blue[Yes]
- Flexible: .red[No]
]

---
# Gradients as Computational Tools

- As we'll see later, having access to the gradient while performing minimization is .bold[highly beneficial]!
- Can imagine multiple ways of arriving at gradients for computational functions

.center.width-30[![carbon_f_x](figures/carbon_f_x.png)]
.kol-6-8[
.bold.center[Numeric]
.center.width-70[![carbon_fprime_numeric](figures/carbon_fprime_numeric.png)]
]
.kol-2-8.huge[
<br>
- Exact: .red[No]
- Flexible: .blue[Yes]
]

---
# Gradients as Computational Tools

- As we'll see later, having access to the gradient while performing minimization is .bold[highly beneficial]!
- Can imagine multiple ways of arriving at gradients for computational functions

.center.width-30[![carbon_f_x](figures/carbon_f_x.png)]
.kol-6-8[
.bold.center[Automatic]
.center.width-80[![carbon_fprime_automatic](figures/carbon_fprime_automatic.png)]
]
.kol-2-8.huge[
<br>
- Exact: .blue[Yes]
- Flexible: .blue[Yes]
]

---
# Automatic Differentiation

.kol-3-5[
- Automatic differentiation (autodiff) provides gradients of numerical functions to machine precision
- Build computational graph of the calculation
- Nodes represent operations, edges represent flow of gradients
- Apply the chain rule to operations
   - Can traverse the graph in forward or reverse modes depending on the relative dimensions of input and output for efficient computation

$$
f(a,b) = a^{2} \sin(ab)
$$
<br>
$$
\frac{df}{da} = \frac{\partial c}{\partial a} \frac{\partial f}{\partial c} + \frac{\partial d}{\partial a} \frac{\partial e}{\partial d} \frac{\partial f}{\partial e}
$$
$$
= 2a \sin(ab) + a^{2}b \cos(ab)
$$

<!-- TODO: Revise example with graphviz -->
]
.kol-2-5.center[
.width-100[[![autodiff_graph](figures/autodiff_graph.png)](https://indico.cern.ch/event/941278/contributions/4084835/)]
]

---
# Differentiable Programming

.grid[
.kol-1-2.large[
- Allows writing fully differentiable programs that are .bold[efficient and accurate]
- Resulting system can be optimized end-to-end using efficient gradient-based optimization algorithms
   - Exploit advances in deep learning
- Enables .italic[efficient] computation of gradients and Jacobians
   - Large benefit to statistical inference
- Replace non-differentiable operations with differentiable analogues
   - Binning, sorting, cuts
]
.kol-1-2[
<br><br>
.center.width-100[[![Snowmass_LOI](figures/Snowmass_LOI.png)](https://www.snowmass21.org/docs/files/summaries/CompF/SNOWMASS21-CompF5_CompF3_Gordon_Watts-046.pdf)]
.center.large[[Snowmass Community Planning Process <br>2021 Letter of Interest](https://www.snowmass21.org/docs/files/summaries/CompF/SNOWMASS21-CompF5_CompF3_Gordon_Watts-046.pdf)]
]
]


---
class: focus-slide, center
# Case study:<br> Automatic differentiation improving analyses

.huge.bold.center[Application of automatic differentiation in `pyhf`]

---
# Goals of physics analysis at the LHC

.kol-1-1[
.kol-1-3.center[
.width-100[[![ATLAS_Higgs_discovery](figures/ATLAS_Higgs_discovery.png)](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/HIGG-2012-27/)]
Search for new physics
]
.kol-1-3.center[
<br>
.width-100[[![CMS-PAS-HIG-19-004](figures/CMS-PAS-HIG-19-004.png)](http://cms-results.web.cern.ch/cms-results/public-results/superseded/HIG-19-004/index.html)]

<br>
Make precision measurements
]
.kol-1-3.center[
.width-110[[![SUSY-2018-31_limit](figures/SUSY-2018-31_limit.png)](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-31/)]

Provide constraints on models through setting best limits
]
]

- All require .bold[building statistical models] and .bold[fitting models] to data to perform statistical inference
- Model complexity can be huge for complicated searches
- **Problem:** Time to fit can be .bold[many hours]
- .blue[Goal:] Empower analysts with fast fits and expressive models

---
# HistFactory Model

$$
f\left(\mathrm{data}\middle|\mathrm{parameters}\right) =  f\left(\textcolor{#00a620}{\vec{n}}, \textcolor{#a3130f}{\vec{a}}\middle|\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}}\right) = \prod\_{c \\,\in\\, \textrm{channels}} \prod\_{b \\,\in\\, \textrm{bins}\_c} \textrm{Pois} \left(\textcolor{#00a620}{n\_{cb}} \middle| \nu\_{cb}\left(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}}\right)\right) \prod\_{\chi \\,\in\\, \vec{\chi}} c\_{\chi} \left(\textcolor{#a3130f}{a\_{\chi}}\middle|\textcolor{#9c2cfc}{\chi}\right)
$$

.center[$\textcolor{#00a620}{\vec{n}}$: .obsdata[events], $\textcolor{#a3130f}{\vec{a}}$: .auxdata[auxiliary data], $\textcolor{#0495fc}{\vec{\eta}}$: .freepars[unconstrained pars], $\textcolor{#9c2cfc}{\vec{\chi}}$: .conpars[constrained pars]]

$$
\nu\_{cb}(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}}) = \sum\_{s \\,\in\\, \textrm{samples}} \underbrace{\left(\sum\_{\kappa \\,\in\\, \vec{\kappa}} \kappa\_{scb}(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}})\right)}\_{\textrm{multiplicative}} \Bigg(\nu\_{scb}^{0}(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}}) + \underbrace{\sum\_{\Delta \\,\in\\, \vec{\Delta}} \Delta\_{scb}(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}})}\_{\textrm{additive}}\Bigg)
$$

Mathematical grammar for a simultaneous fit with multiple disjoint _channels_ (or regions) of binned distributions with multiple _samples_ contributing to each with additional (possibly shared) systematics between sample estimates

<!-- .center[.bold[This is a _mathematical_ representation!] Nowhere is any software spec defined] -->
.center[.bold[Until 2018] the only implementation of HistFactory was in `C++` framework for physics analysis ([`ROOT`](https://root.cern.ch/))]

<p style="text-align:center;">
   <a href="https://root.cern/doc/v628/group__HistFactory.html">
      <img src="figures/ROOT_HistFactory.png"; width=55%>
   </a>
</p>

---
# `pyhf`: HistFactory in pure Python

.kol-1-1[
.kol-1-2.large[
- First non-`C++`/ROOT implementation of the HistFactory p.d.f. template
.width-40[[![DOI](figures/zenodo.1169739.svg)](https://doi.org/10.5281/zenodo.1169739)] .width-40[[![DOI](https://joss.theoj.org/papers/10.21105/joss.02823/status.svg)](https://doi.org/10.21105/joss.02823)]
- pure-Python library as second implementation of HistFactory
  - [`$ python -m pip install pyhf`](https://scikit-hep.org/pyhf/installation.html#install-from-pypi)
  <!-- - [`$ micromamba install -c conda-forge pyhf`](https://prefix.dev/channels/conda-forge/packages/pyhf) -->
  - No dependence on large `C++` ROOT framework!
]
.kol-1-2.large[
- Open source tool for all of HEP
   - [IRIS-HEP](https://iris-hep.org/projects/pyhf.html) supported Scikit-HEP project
   - Used in ATLAS SUSY, Exotics, and Top physics groups in [28 published analyses](https://scikit-hep.org/pyhf/citations.html#published-statistical-models)
   - [Used by](https://scikit-hep.org/pyhf/citations.html#use-citations) flavor physics ([Belle II](https://inspirehep.net/literature/1860766)), neutrino physics ([MicroBooNE](https://arxiv.org/abs/2310.07660)), phenomenology community ([`SModelS`](https://inspirehep.net/literature/1814793)), future collider studies ([EIC](https://inspirehep.net/literature/1846026), [MuC](https://inspirehep.net/literature/2743639))
   <!-- ([`SModelS`](https://inspirehep.net/literature/1814793), [`MadAnalysis 5`](https://inspirehep.net/literature/2103971)) -->
   <!-- - Expanding to future experiments too! -->
   - [![NumFOCUS Affiliated Project](https://img.shields.io/badge/NumFOCUS-Affiliated%20Project-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org/sponsored-projects/affiliated-projects)
]
]
<!--  -->
.kol-1-1[
.kol-1-3.center[
<p style="text-align:center;">
   <a href="https://pypi.org/project/pyhf/">
      <img src="figures/pyhf_PyPI.png"; width=100%>
   </a>
</p>
]
.kol-2-3[
.grid[
.kol-1-3.center[
.circle.width-70[![Lukas](figures/collaborators/heinrich.png)]

[Lukas Heinrich](https://github.com/lukasheinrich)
]
.kol-1-3.center[
.circle.width-70[![Matthew](https://avatars2.githubusercontent.com/u/5142394)]

[Matthew Feickert](https://www.matthewfeickert.com/)
]
.kol-1-3.center[
.circle.width-65[![Giordon](figures/collaborators/stark.jpg)]

[Giordon Stark](https://github.com/kratsg)
]
]
]
]

---
# `pyhf`: HistFactory in pure Python

.kol-1-1[
.kol-1-2.large[
- First non-`C++`/ROOT implementation of the HistFactory p.d.f. template
.width-40[[![DOI](figures/zenodo.1169739.svg)](https://doi.org/10.5281/zenodo.1169739)] .width-40[[![DOI](https://joss.theoj.org/papers/10.21105/joss.02823/status.svg)](https://doi.org/10.21105/joss.02823)]
- pure-Python library as second implementation of HistFactory
  - [`$ python -m pip install pyhf`](https://scikit-hep.org/pyhf/installation.html#install-from-pypi)
  <!-- - [`$ micromamba install -c conda-forge pyhf`](https://prefix.dev/channels/conda-forge/packages/pyhf) -->
  - No dependence on large `C++` ROOT framework!
]
.kol-1-2.large[
- Open source tool for all of HEP
   - [IRIS-HEP](https://iris-hep.org/projects/pyhf.html) supported Scikit-HEP project
   - Used in ATLAS SUSY, Exotics, and Top physics groups in [28 published analyses](https://scikit-hep.org/pyhf/citations.html#published-statistical-models)
   - [Used by](https://scikit-hep.org/pyhf/citations.html#use-citations) flavor physics ([Belle II](https://inspirehep.net/literature/1860766)), neutrino physics ([MicroBooNE](https://arxiv.org/abs/2310.07660)), phenomenology community ([`SModelS`](https://inspirehep.net/literature/1814793)), future collider studies ([EIC](https://inspirehep.net/literature/1846026), [MuC](https://inspirehep.net/literature/2743639))
   <!-- ([`SModelS`](https://inspirehep.net/literature/1814793), [`MadAnalysis 5`](https://inspirehep.net/literature/2103971)) -->
   <!-- - Expanding to future experiments too! -->
   - [![NumFOCUS Affiliated Project](https://img.shields.io/badge/NumFOCUS-Affiliated%20Project-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org/sponsored-projects/affiliated-projects)
]
]
<!--  -->
.kol-1-1[
.kol-1-3.center[
<p style="text-align:center;">
   <a href="https://pypi.org/project/pyhf/">
      <img src="figures/pyhf_PyPI.png"; width=100%>
   </a>
</p>
]
<!--  -->
.kol-1-3.center[
<p style="text-align:center;">
   <a href="https://joss.theoj.org/papers/10.21105/joss.02823">
      <img src="figures/pyhf-joss-paper.png"; width=75%>
   </a>
</p>
]
<!--  -->
.kol-1-3.center[
<p style="text-align:center;">
   <a href="https://inspirehep.net/literature/1845084">
      <img src="figures/inspire-citations.png"; width=82%>
   </a>
</p>
]
]

---
# Machine Learning Frameworks for Computation

.grid[
.kol-2-3[
- All numerical operations implemented in .bold[tensor backends] through an API of $n$-dimensional array operations
- Using deep learning frameworks as computational backends allows for .bold[exploitation of automatic differentiation and GPU acceleration]
- As huge buy in from industry we benefit for free as these frameworks are .bold[continually improved] by professional software engineers (physicists are not)

.kol-1-2.center[
.width-80[![scaling_hardware](figures/scaling_hardware_annotated.png)]
]
.kol-1-2[
- Hardware acceleration giving .bold[order of magnitude speedup] in interpolation for systematics!
   - does suffer some overhead
- Noticeable impact for large and complex models
   - hours to minutes for fits
]
]
.kol-1-4.center[
.width-85[![NumPy](figures/logos/NumPy_logo.svg)]
.width-85[![PyTorch](figures/logos/Pytorch_logo.svg)]
.width-85[![Tensorflow](figures/logos/TensorFlow_logo.svg)]

<br>
.width-50[![JAX](figures/logos/JAX_logo.png)]
]
]

---
# Automatic differentiation

With tensor library backends gain access to _exact (higher order) derivatives_ &mdash; accuracy is only limited by floating point precision

$$
\frac{\partial L}{\partial \mu}, \frac{\partial L}{\partial \theta_{i}}
$$

.grid[
.kol-1-2[
.large[Exploit .bold[full gradient of the likelihood] with .bold[modern optimizers] to help speedup fit!]

<br><br>
.large[Gain this through the frameworks creating _computational directed acyclic graphs_ and then applying the chain rule (to the operations)]
]
.kol-1-2[
<p style="text-align:center;">
   <img src="figures/computational_graph.png"; width=85%>
</p>
]
]

---
# HEP Example: Likelihood Gradients

.kol-1-2.center[
<p style="text-align:center;">
   <a href="https://indico.cern.ch/event/882824/timetable/#45-introduction-to-automatic-d">
      <img src="figures/carbon_plot_MLE_grads.png"; width=85%>
   </a>
</p>
]
.kol-1-2.center[
<p style="text-align:center;">
   <img src="figures/MLE_grad_map.png"; width=90%>
</p>
]

.bold.center[Having access to the gradients can make the fit orders of magnitude faster than finite difference]

---
# New Art: Analysis as a Differentiable Program

<p style="text-align:center;">
   <a href="https://inspirehep.net/literature/2050088">
      <img src="figures/neos-pipeline.png"; width=95%>
   </a>
</p>
.caption[[neos: End-to-End-Optimised Summary Statistics for High Energy Physics](https://inspirehep.net/literature/2050088), Nathan Simpson, Lukas Heinrich]

1. From data $d$ train a neural net with parameters $\varphi$ that produces an observable, $f_{\varphi}(d)$
2. Bin the observable to construct a histogram $h$
3. Build a HistFactory binned statistical model, $p$, from the histograms
4. Perform statistical inference and construct a test statistic, $q$, from hypothesis test
5. Construct monotonic test statistic, $\mathrm{CL}_{s}$, to summarize analysis sensitivity

---
# New Art: Analysis as a Differentiable Program

<p style="text-align:center;">
   <a href="https://inspirehep.net/literature/2050088">
      <img src="figures/neos-pipeline.png"; width=95%>
   </a>
</p>
.caption[[neos: End-to-End-Optimised Summary Statistics for High Energy Physics](https://inspirehep.net/literature/2050088), Nathan Simpson, Lukas Heinrich]

.large[
.bold[Goal]: Express final summary statistic as a function of the input data $\mathcal{D}$ and observable parameters $\varphi$ and then optimize analysis sensitivity through back propagating $\partial \,\mathrm{CL_s} / \partial \varphi$ to update $\varphi$
]

$$
\mathrm{CL}_{s} = f(\mathcal{D},\varphi) = (f\textrm{sensitivity} \circ f\textrm{test stat} \circ f \textrm{probability model}  \circ f \textrm{histogram}  \circ f \textrm{observable})(\mathcal{D},\varphi)
$$

<!-- $\mathrm{CL_s} = f(\mathcal{D},\varphi) = (f_{\mathrm{sensitivity}} \circ f_{\mathrm{test\,stat}} \circ f_{\mathrm{likelihood}}  \circ f_{\mathrm{histogram}}  \circ f_{\mathrm{observable}})(\mathcal{D},\varphi)$ -->

.large.bold[
Requires all operations to be differentiable
]


---
# New Art: Analysis as a Differentiable Program

<p style="text-align:center;">
   <a href="https://inspirehep.net/literature/2050088">
      <img src="figures/neos-pipeline.png"; width=95%>
   </a>
</p>
.caption[[neos: End-to-End-Optimised Summary Statistics for High Energy Physics](https://inspirehep.net/literature/2050088), Nathan Simpson, Lukas Heinrich]

.kol-3-5[
* Histograms are non-differentiable, so use kernel density estimation (KDE) to provide differentiable analouge
   - Accumulate distribution mass in bounds of histogram to construct "binned KDE"
* pyhf is used as able to differentiate constructed likelihood function
   - neos extends pyhf with differentiation of optimization routines
]
.kol-2-5[
<p style="text-align:center;">
   <a href="https://indico.cern.ch/event/882824/timetable/#46-neos-physics-analysis-as-a">
      <img src="figures/kde_bins.gif"; width=70%>
   </a>
</p>
]

---
# New Art: Analysis as a Differentiable Program

<p style="text-align:center;">
   <a href="https://inspirehep.net/literature/2050088">
      <img src="figures/neos-pipeline.png"; width=95%>
   </a>
</p>
.caption[[neos: End-to-End-Optimised Summary Statistics for High Energy Physics](https://inspirehep.net/literature/2050088), Nathan Simpson, Lukas Heinrich]

1. From data $d$ train a neural net with parameters $\varphi$ that produces an observable, $f_{\varphi}(d)$
2. .bold[Construct KDE of observable to construct histogram analouge, $h$]
3. Build a HistFactory binned statistical model, $p$, from the histograms .bold[with pyhf]
4. Perform statistical inference and construct a test statistic, $q$, from hypothesis test .bold[with pyhf + neos]
5. Construct monotonic test statistic, $\mathrm{CL}_{s}$, to summarize analysis sensitivity

---
# New Art: Analysis as a Differentiable Program

<p style="text-align:center;">
   <a href="https://github.com/gradhep/neos">
      <img src="https://raw.githubusercontent.com/gradhep/neos/master/nbs/assets/pyhf_3.gif"; width=93%>
   </a>
</p>
.caption[`neos` 3 bin KDE transformed observable (NN output) optimized with systematics w.r.t. $\mathrm{CL}_{s}$]

.kol-1-3[
- .neos-orange[Background] and .neos-blue[signal] samples
   - Same colors for dist. / hist.
- NN output observable
   - $0$: Background-like
   - $1$: Signal-like
]
.kol-1-3[
- Build `pyhf` model (1 channel, 2 samples, 3 bins) from KDE of NN outputs
- Decision regions mappings of NN output
   - $[0.67, 1.0]$ bin $\to$ top left region
]
.kol-1-3[
- $\mathrm{CL}_{s}$ value minimized with loss of NN
- Analysis end-to-end optimized directly on physics sensitivity
]

---
# Scaling and Analysis Reuse

<p style="text-align:center;">
   <a href="https://iris-hep.org/as.html">
      <img src="figures/cabinetry-vertical-slice.png"; width=90%>
   </a>
</p>

.center[Revisiting .bold[IRIS-HEP Analysis Systems] in the context of distributed scaling (HL-LHC) and analysis reuse]

---
# Scaling is reasonable

From the 2023 MIAPbP Workshop on on Differentiable and Probabilistic Programming for physics engagement with the broader community showed multiple large scale workflows

.center[.bold[If] things are differentiable, shouldn't be scared of .bold[large-scale codebases and applications]]

.kol-1-2[
<p style="text-align:center;">
   <a href="https://www.munich-iapbp.de/probabilistic-programming/">
      <img src="figures/MIAPbP-workshop-poster.png"; width=90%>
   </a>
</p>
]
.kol-1-2[
<p style="text-align:center;">
   <a href="https://indico.ph.tum.de/event/7314/contributions/7432/">
      <img src="figures/miapbp-workshop-scaling-ad.png"; width=90%>
   </a>
</p>
.center[[Nicolas Gauger, MIAPbP Workshop 2023](https://indico.ph.tum.de/event/7314/contributions/7432/)]
]

---
# Analysis Reuse

.large[
* Data and analyses done at the LHC are .bold[scientific opportunities performed under unique experimental conditions]
* Workflow language based [RECAST](https://github.com/recast-hep/recast-atlas) .bold[reinterpretation and analysis preservation] framework (Cranmer, Heinrich, Feickert) has been implemented in ATLAS as an enabling technology
* Results leading to ATLAS public notes extending the physics reach of original publications
]

.kol-1-3[
<p style="text-align:center;">
   <a href="https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PUBNOTES/ATL-PHYS-PUB-2020-007/">
      <!-- <img src="figures/recasted-analysis.png"; width=100%> -->
      <img src="figures/recasted-analysis-dark-matter-particlezoo.png"; width=100%>
   </a>
</p>
]
.kol-2-3[
<p style="text-align:center;">
   <img src="figures/recast-workflow-goal.png"; width=100%>
</p>
]

---
# Analysis Reuse enabling new physics analysis

.kol-2-3[
.large[
* RECAST is designed to work with the CERN [REANA](https://reana.io/) open source reproducible research data analysis platform to .bold[perform analysis at scale]
* RECAST + REANA enabled the recent (2023) ATLAS LHC Run-2 Phenomenological Minimal Supersymmetric Standard Model (pMSSM) scan analysis
   - Theory model .bold[reduced] down to 19-dimensional parameter space
   - Analysis of combination of published ATLAS LHC Run-2 analyses uses .bold[tens of thousands] of parameter space models (each a full analysis evaluation)
* Analysis .bold[would be intractable] without existing full analysis preservation from RECAST scaled to thousands of cores with REANA
]
]
.kol-1-3[
<p style="text-align:center;">
   <a href="https://reana.io/">
      <img src="figures/logo-reana.svg"; width=70%>
   </a>
</p>
<p style="text-align:center;">
   <a href="https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2023-055/">
      <img src="figures/ATLAS-CONF-2023-055.png"; width=95%>
   </a>
</p>
]

---
# Full statistical model publication...

.center[...making good on [19 year old agreement to publish likelihoods](https://indico.cern.ch/event/746178/contributions/3396797/)]

.center.width-90[
[![likelihood_publishing_agreement](figures/likelihood_publishing_agreement.png)](https://cds.cern.ch/record/411537)
]

.center[([1st Workshop on Confidence Limits, CERN, 2000](http://inspirehep.net/record/534129))]

.bold[This hadn't been done in HEP until `pyhf` in 2019]
- A "open world" of statistical models gives a difficult domain problem to solve
- What to preserve and how? All of the ROOT `C++` framework and binary model files?
- Idea: Focus on a single more tractable binned model first

---
# JSON spec fully describes the HistFactory model

.kol-1-4.width-100[
- Human & machine readable .bold[declarative] statistical models
- Industry standard
   - Will be with us forever
- Parsable by every language
   - Highly portable
   - Bidirectional translation <br>with `C++` ROOT
- Versionable and easily preserved
   - JSON Schema [describing<br> HistFactory specification](https://scikit-hep.org/pyhf/likelihood.html#bibliography)
   - Attractive for analysis preservation
   - Highly compressible
]
.kol-3-4[
<p style="text-align:center;">
   <img src="figures/carbon_JSON_spec_annotated.png"; width=98%>
</p>

.center[[`JSON` defining a single channel, two bin counting experiment with systematics](https://scikit-hep.org/pyhf/likelihood.html#toy-example)]
]

---
# ATLAS validation and publication of full models

.kol-1-2[
.center.width-100[[![ATLAS_PUB_Note_title](figures/ATLAS_PUB_Note_title.png)](https://cds.cern.ch/record/2684863)]

.center.width-90[[![overlay_multiplex_contour](figures/overlay_multiplex_contour.png)](https://cds.cern.ch/record/2684863)]

<br>
.center[(ATLAS, 2019)]
]
.kol-1-2[
.center.width-100[[![CERN_news_story](figures/CERN_news_story.png)](https://home.cern/news/news/knowledge-sharing/new-open-release-allows-theorists-explore-lhc-data-new-way)]
.center[(CERN, 2020)]
]

---
# Large community adoption followed
<!-- .center.large.bold[Placeholder slide] -->
.center[
.width-95[[![community-adoption](figures/community-adoption.svg)](https://scikit-hep.org/pyhf/citations.html)]
]

---
# Extending model portability with HS3

.kol-3-5.large[
* [High Energy Physics Statistics Serialization Standard](https://github.com/hep-statistics-serialization-standard/hep-fit-serialization) (HS3)
   - Make statistical models: persistent, interchangeable, modifiable, readable
* Goal: Generalize the pyhf JSON model spec to a feature complete specification for particle physics
   - Ongoing work across the HS3 team and adopting tool teams
   - Tackle supporting more of the "open world" of statistical modeling
* HS3 spec will support statistical libraries RooFit (`C++`/`ROOT`), pyhf (Python), BAT (Julia), and others
   - Write once, run anywhere
   - Draft v0.2 currently in alpha (first deployment in `ROOTFit`)
]
.kol-2-5[
<br>
<br>
<p style="text-align:center;">
   <a href="https://github.com/hep-statistics-serialization-standard/hep-fit-serialization">
      <img src="figures/HS3-paper-title-page.png"; width=110%>
   </a>
</p>
]

---
# Dedicated investment for the next decades

.bold.center.large[Exciting future for all these areas in particle physics with large scale investment!]

.kol-1-3[
<p style="text-align:center;">
   <a href="https://www.usparticlephysics.org/2023-p5-report/">
      <img src="figures/p5-theme.jpg"; width=100%>
   </a>
</p>

.center[[Report of the 2023 Particle Physics Project Prioritization Panel](https://www.usparticlephysics.org/2023-p5-report/)]

Once a decade formal recommendations from US particle physics community to .bold[US Congress and funding agencies]

Serve on Formation Task Force for the Coordinating Panel for Software and Computing
]
.kol-2-3[
<p style="text-align:center;">
   <a href="https://www.usparticlephysics.org/2023-p5-report/">
      <img src="figures/p5-charge.png"; width=90%>
   </a>
</p>
<p style="text-align:center;">
   <a href="https://www.usparticlephysics.org/2023-p5-report/">
      <img src="figures/p5-software-computing-chapter.png"; width=90%>
   </a>
</p>
<p style="text-align:center;">
   <a href="https://www.usparticlephysics.org/2023-p5-report/">
      <img src="figures/p5-area-recommendation-18.png"; width=90%>
   </a>
</p>
]

---
# Applications beyond HEP

.huge[Today we've discussed .bold[general techniques and technologies] applied to HEP problems, but not constrained to them]

.large[
* Automatic differentiation is a rich field of research unto itself
   - [Machine-learning Optimized Design of Experiments (MODE) collaboration](https://mode-collaboration.github.io/) working towards detector design optimization using automatic differentiation
   - [Fully differentiable branching programs](https://inspirehep.net/literature/2692444) (novel!) can attack problems across fields
* Engagement with the broader scientific open source community
   - Scikit-HEP and IRIS-HEP have strong involvement in Scientific Python project, NumFOCUS, and SciPy Conference, JuliaHEP being fostered now
* Planning for analysis reuse brings flexibility to leverage tooling
   - Adopting standards and workflows allows for tooling to change with opportunity
]

---
# Summary

.large[
* Many challenges and opportunities ahead at the HL-LHC
* Engaging the broader scientific open source community has been a boon for particle physics tooling
* Automatic differentiation gives a powerful tool in the form of differentiable programming
* Scalable and reusable analysis workflows allow leveraging our tools
* Exciting future with full investment in these research areas is happening now!
]

.kol-1-3[
<p style="text-align:center;">
   <img src="figures/lhc_lumi.png"; width=60%>
</p>
]
.kol-1-3[
<p style="text-align:center;">
   <a href="https://iris-hep.org/as.html">
      <img src="figures/cabinetry-vertical-slice.png"; width=110%>
   </a>
</p>
]
.kol-1-3[
<p style="text-align:center;">
   <img src="figures/MLE_grad_map.png"; width=75%>
</p>
]

---
class: end-slide, center

.large[Backup]

---
# Opportunities and Challenges of the HL-LHC

.center.large[Challenge to be able to .bold[record, store, and analyze] the data]

.kol-1-2[
<p style="text-align:center;">
   <a href="https://cds.cern.ch/record/2802918">
      <img src="figures/HL-LHC-disk-projections-atlas.png"; width=95%>
   </a>
</p>
]
.kol-1-2[
<br>
<p style="text-align:center;">
   <a href="https://cds.cern.ch/record/2815292?ln=en">
      <img src="figures/HL-LHC-disk-projections-cms.png"; width=100%>
   </a>
</p>
]

.center.large[Projected .bold[required disk usage] for HL-LHC (want R&D below budget line)]

.center[[ATLAS](https://cds.cern.ch/record/2803119?ln=en) and [CMS](https://cds.cern.ch/record/2815292?ln=en) software and computing reviews]

---
# Rapid rise of Python for analysis in HEP

<p style="text-align:center;">
   <a href="https://matthewfeickert.github.io/talk-doepy-python-exchange-2022/2022-06-29.pdf">
      <img src="figures/github-language-fullstudy-for-review.svg"; width=85%>
   </a>
</p>
.center.large["import XYZ" matches in GitHub repos for users who fork [CMSSW](https://github.com/cms-sw/cmssw) by file]

.footnote[[Modern Python analysis ecosystem for High Energy Physics](https://matthewfeickert.github.io/talk-doepy-python-exchange-2022/2022-06-29.pdf), Jim Pivarski, Matthew Feickert, Gordon Watts]

---
# Explosion of Scientific Python (NumPy, etc.)

<p style="text-align:center;">
   <a href="https://matthewfeickert.github.io/talk-doepy-python-exchange-2022/2022-06-29.pdf">
      <img src="figures/github-package-fullstudy-for-review.svg"; width=85%>
   </a>
</p>
.center.large["import XYZ" matches in GitHub repos for users who fork [CMSSW](https://github.com/cms-sw/cmssw) by library/tool]

.footnote[[Modern Python analysis ecosystem for High Energy Physics](https://matthewfeickert.github.io/talk-doepy-python-exchange-2022/2022-06-29.pdf), Jim Pivarski, Matthew Feickert, Gordon Watts]

---
# Automatic Differentiation: Forward and Reverse

.center[Performing maps $f: \mathbb{R}^{m} \to \mathbb{R}^{n}$]
<br>
.center[aka, "wide" vs. "tall" transformations]
<br>
.kol-1-2[
- .bold[Forward] mode
- Column wise evaluation of Jacobian
   - Jacobian-vector products
   - Execution time scales with input parameters
   - Example: few variables into very high dimensional spaces $\mathbb{R} \to \mathbb{R}^{100}$
]
.kol-1-2[
- .bold[Reverse] mode
- Row wise evaluation of Jacobian
   - vector-Jacobian products
   - Execution time scales with output parameters
   - Example: scalar maps from very high-dimensional spaces $\mathbb{R}^{100} \to \mathbb{R}$
]

<br>
.center[Allows for efficient computation depending on dimensionality]

---
# HistFactory Model

- A flexible probability density function (p.d.f.) template to build statistical models in high energy physics
- Developed in 2011 during work that lead to the Higgs discovery [[CERN-OPEN-2012-016](http://inspirehep.net/record/1236448)]
- Widely used by ATLAS for .bold[measurements of known physics] (Standard Model) and .bold[searches for new physics] (beyond the Standard Model)

.kol-2-5.center[
.width-90[[![HIGG-2016-25](figures/HIGG-2016-25.png)](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/HIGG-2016-25/)]
.bold[Standard Model]
]
.kol-3-5.center[
.width-100[[![SUSY-2016-16](figures/SUSY-2016-16.png)](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-16/)]
.bold[Beyond the Standard Model]
]

---
# HistFactory Template: at a glance

<!-- \definecolor{data}{HTML}{00a620}
\definecolor{auxdata}{HTML}{a3130f}
\definecolor{freepars}{HTML}{0495fc}
\definecolor{conpars}{HTML}{9c2cfc} -->
$$
f\left(\mathrm{data}\middle|\mathrm{parameters}\right) =  f\left(\textcolor{#00a620}{\vec{n}}, \textcolor{#a3130f}{\vec{a}}\middle|\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}}\right) = \textcolor{blue}{\prod\_{c \\,\in\\, \textrm{channels}} \prod\_{b \\,\in\\, \textrm{bins}\_c} \textrm{Pois} \left(n\_{cb} \middle| \nu\_{cb}\left(\vec{\eta}, \vec{\chi}\right)\right)} \\,\textcolor{red}{\prod\_{\chi \\,\in\\, \vec{\chi}} c\_{\chi} \left(a\_{\chi}\middle|\chi\right)}
$$

.center[$\textcolor{#00a620}{\vec{n}}$: .obsdata[events], $\textcolor{#a3130f}{\vec{a}}$: .auxdata[auxiliary data], $\textcolor{#0495fc}{\vec{\eta}}$: .freepars[unconstrained pars], $\textcolor{#9c2cfc}{\vec{\chi}}$: .conpars[constrained pars]]

$$
\nu\_{cb}(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}}) = \sum\_{s \\,\in\\, \textrm{samples}} \underbrace{\left(\sum\_{\kappa \\,\in\\, \vec{\kappa}} \kappa\_{scb}(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}})\right)}\_{\textrm{multiplicative}} \Bigg(\nu\_{scb}^{0}(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}}) + \underbrace{\sum\_{\Delta \\,\in\\, \vec{\Delta}} \Delta\_{scb}(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}})}\_{\textrm{additive}}\Bigg)
$$

.bold[Use:] Multiple disjoint _channels_ (or regions) of binned distributions with multiple _samples_ contributing to each with additional (possibly shared) systematics between sample estimates

.bold[Main pieces:]
- .blue[Main Poisson p.d.f. for simultaneous measurement of multiple channels]
- .katex[Event rates] $\nu\_{cb}(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}})$ (nominal rate $\nu\_{scb}^{0}$ with rate modifiers)
   - encode systematic uncertainties (e.g. normalization, shape)
- .red[Constraint p.d.f. (+ data) for "auxiliary measurements"]

---
# HistFactory Template: at a second glance

<!-- \definecolor{data}{HTML}{00a620}
\definecolor{auxdata}{HTML}{a3130f}
\definecolor{freepars}{HTML}{0495fc}
\definecolor{conpars}{HTML}{9c2cfc} -->
$$
f\left(\mathrm{data}\middle|\mathrm{parameters}\right) =  f\left(\textcolor{#00a620}{\vec{n}}, \textcolor{#a3130f}{\vec{a}}\middle|\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}}\right) = \prod\_{c \\,\in\\, \textrm{channels}} \prod\_{b \\,\in\\, \textrm{bins}\_c} \textrm{Pois} \left(\textcolor{#00a620}{n\_{cb}} \middle| \nu\_{cb}\left(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}}\right)\right) \\,\prod\_{\chi \\,\in\\, \vec{\chi}} c\_{\chi} \left(\textcolor{#a3130f}{a\_{\chi}}\middle|\textcolor{#9c2cfc}{\chi}\right)
$$

.center[$\textcolor{#00a620}{\vec{n}}$: .obsdata[events], $\textcolor{#a3130f}{\vec{a}}$: .auxdata[auxiliary data], $\textcolor{#0495fc}{\vec{\eta}}$: .freepars[unconstrained pars], $\textcolor{#9c2cfc}{\vec{\chi}}$: .conpars[constrained pars]]

$$
\nu\_{cb}(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}}) = \sum\_{s \\,\in\\, \textrm{samples}} \underbrace{\left(\sum\_{\kappa \\,\in\\, \vec{\kappa}} \kappa\_{scb}(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}})\right)}\_{\textrm{multiplicative}} \Bigg(\nu\_{scb}^{0}(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}}) + \underbrace{\sum\_{\Delta \\,\in\\, \vec{\Delta}} \Delta\_{scb}(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}})}\_{\textrm{additive}}\Bigg)
$$

.bold[Use:] Multiple disjoint _channels_ (or regions) of binned distributions with multiple _samples_ contributing to each with additional (possibly shared) systematics between sample estimates

.bold[Main pieces:]
- .blue[Main Poisson p.d.f. for simultaneous measurement of multiple channels]
- .katex[Event rates] $\nu\_{cb}(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}})$ (nominal rate $\nu\_{scb}^{0}$ with rate modifiers)
   - encode systematic uncertainties (e.g. normalization, shape)
- .red[Constraint p.d.f. (+ data) for "auxiliary measurements"]

---
# HistFactory Template: grammar

$$
f\left(\mathrm{data}\middle|\mathrm{parameters}\right) =  f\left(\textcolor{#00a620}{\vec{n}}, \textcolor{#a3130f}{\vec{a}}\middle|\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}}\right) = \color{blue}{\prod\_{c \\,\in\\, \textrm{channels}} \prod\_{b \\,\in\\, \textrm{bins}\_c} \textrm{Pois} \left(n\_{cb} \middle| \nu\_{cb}\left(\vec{\eta}, \vec{\chi}\right)\right)} \\,\color{red}{\prod\_{\chi \\,\in\\, \vec{\chi}} c\_{\chi} \left(a\_{\chi}\middle|\chi\right)}
$$

Mathematical grammar for a simultaneous fit with multiple disjoint _channels_ (or regions) of binned distributions with multiple _samples_ contributing to each with additional (possibly shared) systematics between sample estimates

.kol-1-2[
.bold[Main pieces:]
- .blue[Main Poisson p.d.f. for simultaneous measurement of multiple channels]
- .katex[Event rates] $\nu\_{cb}(\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}})$ (nominal rate $\nu\_{scb}^{0}$ with rate modifiers)
- .red[Constraint p.d.f. (+ data) for "auxiliary measurements"]
   - encode systematic uncertainties (e.g. normalization, shape)
<!-- - $\vec{n}$: events, $\vec{a}$: auxiliary data, $\vec{\eta}$: unconstrained pars, $\vec{\chi}$: constrained pars -->
- $\textcolor{#00a620}{\vec{n}}$: .obsdata[events], $\textcolor{#a3130f}{\vec{a}}$: .auxdata[auxiliary data], $\textcolor{#0495fc}{\vec{\eta}}$: .freepars[unconstrained pars], $\textcolor{#9c2cfc}{\vec{\chi}}$: .conpars[constrained pars]
]
.kol-1-2[
.center.width-100[[![SUSY-2016-16_annotated](figures/SUSY-2016-16.png)](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-16/)]
.center[Example: .bold[Each bin] is separate (1-bin) _channel_,<br> each .bold[histogram] (color) is a _sample_ and share<br> a .bold[normalization systematic] uncertainty]
]

---
# HistFactory Template: systematic uncertainties

.kol-4-7[
- In HEP common for systematic uncertainties to be specified with two template histograms: "up" and "down" variation for parameter $\theta \in \\{\textcolor{#0495fc}{\vec{\eta}}, \textcolor{#9c2cfc}{\vec{\chi}} \\}$
   - "up" variation: model prediction for $\theta = +1$
   - "down" variation: model prediction for $\theta = -1$
   - Interpolation and extrapolation choices provide .bold[model predictions $\nu(\vec{\theta}\,)$ for any $\vec{\theta}$]
<!--  -->
- [Constraint terms](https://pyhf.readthedocs.io/en/v0.6.3/intro.html#id25) $c\_{j} \left(\textcolor{#a3130f}{a\_{j}}\middle|\textcolor{#9c2cfc}{\theta_{j}}\right)$ used to model auxiliary measurements. Example for Normal (most common case):
   - Mean of nuisance parameter $\textcolor{#9c2cfc}{\theta_{j}}$ with normalized width ($\sigma=1$)
   - Normal: auxiliary data $\textcolor{#a3130f}{a\_{j} = 0}$ (aux data function of modifier type)
   - Constraint term produces penalty in likelihood for pulling $\textcolor{#9c2cfc}{\theta_{j}}$ away from auxiliary measurement value
   - As $\nu(\vec{\theta}\,)$ constraint terms inform rate modifiers (.bold[systematic uncertainties]) during simultaneous fit
   - Example: Correlated shape `histosys` modifier could represent part of the uncertainty associated with a jet energy scale
]
.kol-3-7[
.center.width-70[[![systematics](figures/systematics.png)](https://indico.cern.ch/event/1076231/contributions/4560405/)]
.center[Image credit: [Alex Held](https://indico.cern.ch/event/1076231/contributions/4560405/)]
]

---
# Moving towards differentiable workflows

.kol-1-3[
<p style="text-align:center;">
   <img src="figures/signal_background_stacked.png"; width=100%>
</p>
* Counting experiment for presence of signal process
* Place discriminate selection ("cut") on observable $x$ to maximize significance $S(x)$
* Step along cut values in $x$ and calculate significance
]
.kol-1-3[
<p style="text-align:center;">
   <img src="figures/significance_scan_compare.png"; width=100%>
</p>
* Need differentiable analogue to non-differentiable cut
* Weight events using activation function of sigmoid

.center[$w=\left(1 + e^{-\alpha(x-c)}\right)^{-1}$]

* Event far .italic[below] cut: $w \to 0$
* Event far .italic[above] cut: $w \to 1$
]
.kol-1-3[
<p style="text-align:center;">
   <img src="figures/automated_optimization.png"; width=95%>
</p>
* With a simple gradient descent algorithm can easily automate the significance optimization
* Allows for the "cut" to become a parameter that can be differentiated through for the larger analysis
]

---
# Discriminate Signal and Background
<!--  -->
* Counting experiment for presence of signal process
* Place discriminate selection cut on observable $x$ to maximize significance
   - Significance: $\sqrt{2 (S+B) \log(1 + \frac{S}{B})-2S}$ (for small $S/B$: significance $\to S/\sqrt{B}$)

.footnote[Example inspired by Alexander Held's [example of a differentiable analysis](https://github.com/alexander-held/differentiable-analysis-example/)]

.kol-1-2.center[
<p style="text-align:center;">
   <img src="figures/signal_background_shapes.png"; width=100%>
</p>
]
.kol-1-2.center[
<p style="text-align:center;">
   <img src="figures/signal_background_stacked.png"; width=100%>
</p>
]

---
# Traditionally: Scan across cut values
<!--  -->
- Set baseline cut at $x=0$ (accept everything)
- Step along cut values in $x$ and calculate significance at each cut. Keep maximum.
<!--  -->
.kol-1-2.center[
.width-100[![signal_background_stacked](figures/signal_background_stacked.png)]
]
.kol-1-2[
.width-100[![significance_cut_scan](figures/significance_cut_scan.png)]
]

.center[Significance: $\sqrt{2 (S+B) \log(1 + \frac{S}{B})-2S}$]

---
# Differentiable Approach

.kol-1-2.large[
- Need differentiable analogue to non-differentiable cut
- Weight events using activation function of sigmoid

.center[$w=\left(1 + e^{-\alpha(x-c)}\right)^{-1}$]

- Event far .italic[below] cut: $w \to 0$
- Event far .italic[above] cut: $w \to 1$
- $\alpha$ tunable parameter for steepness
   - Larger $\alpha$ more cut-like
]
.kol-1-2[
<br>
.width-100[![sigmoid_event_weights](figures/sigmoid_event_weights.png)]
]

---
# Compare Hard Cuts vs. Differentiable

.kol-1-2.large[
- For hard cuts the significance was calculated by applying the cut and than using the remaining $S$ and $B$ events
- But for the differentiable model there aren't cuts, so approximate cuts with the sigmoid approach and weights
- Comparing the two methods shows good agreement
- Can see that the approximation to the hard cuts improves with larger $\alpha$
   - But can become unstable, so tunable
]
.kol-1-2.center[
<br>
.width-100[![significance_scan_compare](figures/significance_scan_compare.png)]
]

---
# Compare Hard Cuts vs. Differentiable

.kol-1-2.large[
- For hard cuts the significance was calculated by applying the cut and then using the remaining $S$ and $B$ events
- But for the differentiable model there aren't cuts, so approximate cuts with the sigmoid approach and weights
- Comparing the two methods shows good agreement
- Can see that the approximation to the hard cuts improves with larger $\alpha$
   - But can become unstable, so tunable
]
.kol-1-2.center[
<br>
.width-100[![significance_scan_compare_high_alpha](figures/significance_scan_compare_high_alpha.png)]
]

---
# Accessing the Gradient

.kol-2-5.large[
* Most importantly though, with the differentiable model we have access to the gradient
   - $\partial_{x} f(x)$
* So can find the maximum significance at the point where the gradient of the significance is zero
   - $\partial_{x} f(x) = 0$
* With the gradient in hand this cries out for automated optimization!
]
.kol-3-5.center[
<p style="text-align:center;">
   <img src="figures/significance_gradient.png"; width=90%>
</p>
]

---
# Automated Optimization

.kol-2-5.large[
* With a simple gradient descent algorithm can easily automate the significance optimization
* For this toy example, obviously less efficient then cut and count scan
* Gradient methods apply well in higher dimensional problems
* Allows for the "cut" to become a parameter that can be differentiated through for the larger analysis
]
.kol-3-5.center[
.width-100[![automated_optimization](figures/automated_optimization.png)]

<!-- TODO: Make this an animated GIF -->
]

---
# What is `pyhf`?

Please checkout the many resources we have starting with the [website](https://scikit-hep.org/pyhf/) and the [SciPy 2020 talk](https://youtu.be/FrH9s3eB6fU)!

<!-- [![SciPy 2020 talk YouTube](http://i3.ytimg.com/vi/FrH9s3eB6fU/maxresdefault.jpg)](https://youtu.be/FrH9s3eB6fU) -->
<p align="center">
<a href="https://youtu.be/FrH9s3eB6fU"><img src="http://i3.ytimg.com/vi/FrH9s3eB6fU/maxresdefault.jpg" width="480" height="270"></a>
</p>
.grid[
.kol-1-3.center[
.width-60[[![scikit-hep_logo](https://scikit-hep.org/assets/images/logo.png)](https://scikit-hep.org/)]
]
.kol-1-3.center[
<br>
.width-60[[![pyhf_logo](https://iris-hep.org/assets/logos/pyhf-logo.png)](https://github.com/scikit-hep/pyhf)]
]
.kol-1-3.center[
<br>
.width-70[[![iris-hep_logo](assets/logos/logo_IRIS-HEP.png)](https://iris-hep.org/)]
]
]

---
# Differentiable Ecosystem

.kol-1-3.center[
.width-100[[![gradhep](https://avatars1.githubusercontent.com/u/65067820)](https://hepsoftwarefoundation.org/activities/differentiablecomputing.html)]

[gradhep](https://hepsoftwarefoundation.org/activities/differentiablecomputing.html)
]
.kol-1-3.center[
.width-100[[![neos_logo](https://raw.githubusercontent.com/gradhep/neos/master/nbs/assets/neos_logo.png)](https://github.com/gradhep/neos)]

[neos](https://github.com/gradhep/neos), [INFERNO](https://inspirehep.net/literature/1677673)
]
.kol-1-3.center[
<br><br>
.width-100[[![MLE_grad_map_full](figures/Acts_autodiff_talk.png)](https://indico.cern.ch/event/941278/contributions/4084835/)]

<br><br><br>
[ACTS](https://iris-hep.org/projects/acts.html)
]

<br>
.kol-1-1[
.bold.center[Groups, libraries, and applications growing rapidly]
]

---
# Gradient Passing

.kol-2-5.code-large[
- Real world high energy physics analyses have various challenges:
   - Computations highly complex chains
   - Not implementable in a single framework
   - Asynchronous multi-step procedures
   - Strong need for distributed computing
- Passing of gradients .bold[between] different implementations and services
   - Large scale machine learning in industry needs to do this to train models
- Possible solution to allow for distributed computations at scale exploiting gradients
]
.kol-3-5.center[
<br>
.width-100[[![metadiff](figures/metadiff.png)](https://indico.cern.ch/event/960587/contributions/4070325/)]
.caption[[Differentiating through PyTorch, JAX, and TensorFlow using FaaS](https://indico.cern.ch/event/960587/contributions/4070325/)]
]

---
# ML + reinterpretation: Active learning

.kol-1-2[
.huge[
Leveraging [REANA](https://www.reana.io/) reproducible research data analysis platform possible to run distributed ML and analysis workflows at scale
]
<p style="text-align:center;">
   <a href="https://conference.ippp.dur.ac.uk/event/1178/contributions/6449/">
      <img src="figures/exclusion-learning.png"; width=90%>
   </a>
</p>
.caption[[ Christian Weber, Reinterpretation Forum 2023](https://conference.ippp.dur.ac.uk/event/1178/contributions/6449/)]
]
.kol-1-2[
<p style="text-align:center;">
   <a href="https://conference.ippp.dur.ac.uk/event/1178/contributions/6449/">
      <img src="figures/active-learning-workflow.png"; width=100%>
   </a>
</p>
.caption[[ATL-PHYS-PUB-2023-010](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PUBNOTES/ATL-PHYS-PUB-2023-010/)]
]

---
# Active Learning

.kol-1-2.large[
* Iterative procedure to actively collect new labelled data for an optimisation task
* One or more new BSM parameter space points are selected and for each the upper limit on the BSM signal strength is evaluated
* Regression on the signal strength upper limit in the multidimensional space
* A new set of parameter space points are suggested for further analysis such that a sufficiently accurate exclusion contour may be obtained subject to some sampling budget constraints
]
.kol-1-2[
<p style="text-align:center;">
   <a href="https://indico.cern.ch/event/708041/contributions/3269754/">
      <img src="figures/excursion-ACAT-2019.png"; width=100%>
   </a>
</p>
.caption[[Active Learning for Excursion Set Estimation, ACAT 2019](https://indico.cern.ch/event/708041/contributions/3269754/)]
]

---
# References

1. Lukas Heinrich, .italic[[Distributed Gradients for Differentiable Analysis](https://indico.cern.ch/event/960587/contributions/4070325/)], [Future Analysis Systems and Facilities Workshop](https://indico.cern.ch/event/960587/), 2020.
2. Jim Pivarski, .italic[[History and Adoption of Programming Languages in NHEP](https://github.com/jpivarski-talks/2022-02-08-jlab-roundtable-language-history)], [Software & Computing Round Table](https://indico.jlab.org/event/505/#day-2022-02-08), 2022.

---

class: end-slide, center
count: false

The end.
