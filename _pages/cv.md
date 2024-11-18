---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D Oceanography, University of Washington
* M.S. Oceanography, University of Washington
* B.A. Applied Mathematics, University of California San Diego
* B.S. Physics with Specialization in Computational Physics, University of California San Diego

Work experience
======

Hewlett Packard Enterprise, HPC, AI, and Compute | Cray Labs	
Principal HPC&AI Research Scientist	2022-Present
* Led scientific, weather and climate-related collaborations with NOAA/GFDL, IPSL, and M2LInES to explore novel AI and HPC simulation applications including: RNN and CNNs for mimicking high-CFL methods in circulation models, neural networks for physical parameterizations, and intelligent sampling methods for efficient, high-resolution surrogate training using PyTorch
* Created POCs combining AI and computational fluid dynamics applications with collaborators at national labs, in academia, and with a Formula 1 team using online learning/inference for mesh motion, reinforcement learning for active flow control, and Bayesian optimization for parameter tuning
* Achieved world-leading, AI and HPC demonstrations including the first realistic, global ocean simulation coupling ML inference online with the numerical solver and later proving the feasibility of large, CNN models for inference by scaling MOM6 to use 20,000 CPUs and 5,000 AMD GPUs on Frontier
* Set research directions with senior leadership and principal engineers across business units to inform AI and HPC strategy for multiple $200M+ proposals
* Authored and reviewed influential software architecture documents for HPE’s open-source SmartSim and SmartRedis libraries focusing on loosely-coupled workflows with AI and HPC components 
* Regularly briefed senior leadership (up to the EVP level) on the SmartSim team’s projects and ideated with high-profile customers on transformative applications of AI
* Derived technical requirements arising from at-scale research projects, oversaw implementation by small engineering teams, and guided SmartSim's overarching design as an advocate for the user
* Architected new build systems (CMake and Python) and CI/CD deployed on HPC platforms with Nvidia (P100 to GH200) and AMD (MI250x and MI300a) accelerators for SmartSim
* Received an external commendation from a national lab collaborator for developing an online, producer/consumer-based workflow for surrogate AI training from simulation data on Perlmutter; formally recognized for review excellence in service of an internal technology conference

Government of Canada, Environment and Climate Change Canada
Earth System Coupling Scientist (Permanent position),	2021-2022
Scientific Computing Contractor,	2020-2021
Earth System Coupling Scientist (Temporary position)	2020
* Co-led the tuning and development of the ocean model and atmosphere-ocean coupler for Canada’s coupled climate model (Fortran-based CanESM5)
* Directed three engineers to implement dynamically allocated arrays using modern Fortran allowing for runtime-adjustable simulation complexity, enabling the decoupling of configuration from compilation
* Containerized CanESM5 and deployed to Google Cloud Compute with Docker and on-premise, HPC platforms using Singularity to enable community uptake
* Owned the running and validation of official simulations for Canada’s contribution to the CMIP project and served as the organization’s primarily liaison to FAFMIP, OMIP, and OCMIP
* Implemented new build system for diagnostic and simulation codes to decrease compilation time by 10x
* Extended sequencing codes written in Perl, bash, and Python to enhance robustness when running 100+ member ensembles
* Replaced legacy Fortran analysis code with efficient xarray+dask libraries
* Created continuous-integration pipelines on HPC-based machines using Gitlab CI for efficient regression testing of coupled climate models saving senior developers and scientists O(100 hrs) of manual testing
* Developed the numerics and physics-based parameterizations for the NEMO and MOM6 ocean models

University of Victoria, School of Earth and Ocean Sciences	
Postdoctoral Research Fellow	2017-2020
* Architected the Fortran client for the open-source SmartSim library used to enable online ML inference in compiled-language models as a founding project engineer with Cray Inc.
* Predicted interior ocean changes from surface changes using Keras-based LSTMs and ocean model output
* Performed large-scale data analysis using dask, xarray, OpenMP, and MPI on large ensemble (100+) climate model output O(100TB)

Princeton University/NOAA Geophysical Fluid Dynamics Laboratory	
Postdoctoral Research Associate	2016-2017
* Developed a new discretization technique for diffusion of scalars along arbitrary directions solving previous issues with non-monotonicity; now used in both MOM6 and BLOM
* Owned and validated key ocean model diagnostics published as part of the international CMIP project
* Validated high-order regridding/remapping techniques in MOM6 for use in online diagnostics

University of Washington, School of Oceanography	
Graduate Research Assistant	2010-2016
* Implemented and optimized biogeochemical models using a C-based code with OpenMP parallelization
* Added capability to existing codebase to create an adjoint model for the inverse modeling of 3d transport
* Ran MPI-based, large-scale simulations (100s of cores) on community HPC platforms 

Professional Service and Affiliations
=====================================
* NEMO Eddy Closure Working Group, Co-Chair	2021-Present
* NEMO Developers’ Committee, Member	2021-Present
* Affiliate Graduate Faculty, University of Victoria, School of Earth and Ocean Sciences	2023-Present
* OpenFOAM Special Interest Group on Data Driven Modelling, Member	2023-Present
* World Economic Forum, Working Group on AI for Climate Adaptation	2022-2023
* National Center for Atmospheric Research, Invited Research Scholar	Sept 2019
* Yale University, Visiting Research Scholar	2016-2017
* Reviewer for JGR Oceans, Environmental Data Science, Journal of Physical Oceanography, Journal of Advances in Modeling Earth Systems, National Science Foundation, and HPE internal technology conferences

Skills
======

* Programming: Fortran (expert), Python (advanced), C++ (competent), C (competent)
* ML and Analysis Libraries: numpy, xarray, dask, PyTorch, scikit-learn
* Subject Matter Expert: HPC, fluid dynamics, climate and weather, hybrid AI/simulation

Publications
============
[2126 Google Scholar citations, h-index 15]

Refereed
--------
* von Laszewski, Gregor; Brewer, Wesley; Shao, Andrew; Kirkpatrick, Christine R.; Fleischer, J.P.; Pitkar, Harshad; Fox, Geoffrey. C., Experiment Execution in Support of Community Benchmark Workflows for HPC, Frontiers in High Performance Computing [in review]
* Holdsworth, Amber M; Shao, Andrew; Christian, James R; Clustering to characterize extreme marine conditions for the benthic region of the Northeastern Pacific continental margin, Geophysical Research Letters [in review]
* Khatri, Hemant; Griffies, Stephen M; […], Shao, Andrew, A scale‐dependent analysis of the barotropic vorticity budget in a global ocean simulation, Journal of Advances in Modeling Earth Systems [2024]
* Maric, Tomislav; Fadeli, Mohammed Elwardi; Rigazzi, Alessandro; Shao, Andrew; Weiner, Andre, Combining machine learning with computational fluid dynamics using OpenFOAM and SmartSim, Meccanica [2024]
* Marques, Gustavo M; Shao, Andrew E; Bachman, Scott D; Danabasoglu, Gokhan; Bryan, Frank O, Representing eddy diffusion in the surface boundary layer of ocean models with general vertical coordinates, Journal of Advances in Modeling Earth Systems, [2023]
* Sigmond, Michael; Anstey, James; […]; Shao, Andrew; et al., Improvements in the Canadian Earth system model (CanESM) through systematic model analysis: CanESM5.0 and CanESM5, Geoscientific Model Development [2023]
* Jackson, Laura Claire; Alastrué de Asenjo, Eduardo; […]; Saenko, Oleg, Shao, Andrew, et al., Understanding AMOC stability: the North Atlantic hosing model intercomparison project, Geoscientific Model Development [2022]
* Jarníková, Tereza; Ianson, Debby; Allen, Susan E; Shao, Andrew E; Olson, Elise M, Anthropogenic carbon increase has caused critical shifts in aragonite saturation across a sensitive coastal system, Global Biogeochemical Cycles [2022]
* Ragen, Sarah; Armour, Kyle C; Thompson, LuAnne; Shao, Andrew; Darr, David, The role of Atlantic basin geometry in meridional overturning circulation, Journal of Physical Oceanography [2022]
* Christian, James R; Denman, Kenneth L; […] ; Shao, Andrew E; et al., Ocean biogeochemistry in the canadian earth system model version 5.0. 3: CanESM5 and CanESM5-CanOE, Geoscientific Model Development Discussions [2021]
* Partee, Sam; Ellis, Matthew; Rigazzi, Alessandro; Shao, Andrew E; Bachman, Scott; Marques, Gustavo; Robbins, Benjamin, Using machine learning at scale in numerical simulations with SmartSim: An application to ocean climate modeling, Journal of Computational Science [2022]
* Couldrey, Matthew P; Gregory, Jonathan M; […]; Shao, Andrew E; et al., What causes the spread of model projections of ocean dynamic sea-level change in response to greenhouse gas forcing?, Climate Dynamics [2021]
* Shao, Andrew E; Adcroft, Alistair; Hallberg, Robert; Griffies, Stephen M, A general‐coordinate, nonlocal neutral diffusion operator, Journal of Advances in Modeling Earth [2020]
* Mortenson, Eric; Steiner, Nadja; Monahan, Adam H; Hayashida, Hakase; Sou, Tessa; Shao, Andrew, Modeled impacts of sea ice exchange processes on Arctic Ocean carbon uptake and acidification (1980–2015),Journal of Geophysical Research: Oceans,125,7,e2019JC015782,2020,
* Swart, Neil C; Cole, Jason NS; […]; Shao, Andrew E; et al., The Canadian Earth System Model version 5, Geoscientific Model Development, [2019]
* Adcroft, Alistair; Anderson, Whit; […]; Shao, Andrew E; et al., The GFDL global ocean and sea ice model OM4. 0: Model description and simulation features, Journal of Advances in Modeling Earth Systems [2019]
* Shao, Andrew E; Mecking, Sabine; Thompson, LuAnne; Sonnerup, Rolf E, Evaluating the use of 1‐D transit time distributions to infer the mean state and variability of oceanic ventilation, Journal of Geophysical Research: Oceans [2016]
* Shao, Andrew E; Gille, Sarah T; Mecking, Sabine; Thompson, LuAnne, Properties of the Subantarctic Front and Polar Front from the skewness of sea level anomaly, Journal of Geophysical Research: Oceans [2015]
* Shao, Andrew E; Mecking, Sabine; Thompson, LuAnne; Sonnerup, Rolf E, Mixed layer saturations of CFC‐11, CFC‐12, and SF6 in a global isopycnal model, Journal of Geophysical Research: Oceans [2013]

Non-Refereed
------------

* Wegener et al. [contributor and expert reviewer], Innovation and Adaptation in the Climate Crisis: Technology for the New Normal, World Economic Forum [2024]
* Golovtchenko, Valentin; Maher, Hamid; Shao, Andrew, 7 ways to harness technology for climate adaptation, World Economic Forum Annual Meeting [2024]
* Newton, J.A., M. Jimenez Urias, L. Li, L. Li, K. O’Brien Beaumont, A.E. Shao, and H.B. Stone, Summary and Recommendations of the Second Pacific Anomalies Workshop Seattle, WA [2016]

Selected Talks
==============

* Invited Talk: Using AI for the greater good by advancing science, Society-Engaged AI and Robotics Research Cluster, University of Victoria [2024] 
* Workshop: Combining scientific simulations and AI with SmartSim, NERSC/OLCF [2024]
* Panel: Two Worlds Collide: Forging Sustainable Coupled HPC Simulation/Deep Learning Applications from Hardware to Algorithm, Supercomputing Conference [2023]
* Panel: Understanding the Performance, Reproducibility, Validation, Portability, and Sustainability of Coupled HPC Simulation and Deep Learning Calculations, Supercomputing Conference [2023]
* Invited Talk: Enhancing high-resolution simulations of the global ocean with machine learning using SmartSim, Extreme Scale Computing Training, Argonne National Laboratory [2021]