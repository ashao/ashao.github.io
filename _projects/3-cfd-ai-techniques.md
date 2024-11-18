---
title: "AI techniques applied to computational fluid dynamics"
excerpt: "OpenFOAM, a widely-used, open-source CFD solver, has a wide user base. With the Data-driven Modeling Special Interest group, we explored a variety of cases where we could inject AI (and related) techniques to classic CFD problems. To give others in the community a starting point, we developed three cases: 1) training a CNN online and then using it to predict the motion of the mesh in the case of a moving airfoil (see the image below, red indicates that the neural network results in better mesh quality than the default algorithm) 2) implementing an online, distributed, PCA algorithm to calculate turbulent eigenmodes for a turbulent cylinder in a box 3) using Bayesian optimization to tune turbulence parameters for the Pitz and Daily combustion case. <br/><img src='/images/openfoam_mesh.png'>"
collection: portfolio
---

This is an item in your portfolio. It can be have images or nice text. If you name the file .md, it will be parsed as markdown. If you name the file .html, it will be parsed as HTML. 