

#THE LANDAU GAUGE NON-COMMUTATIVE DIRAC QW
#local on Coord0, delocalized on Coord1.

#OVERALL CONCLUSIONS

#HARPERS BEHAVIOURS


# PREFIX
q=128
l=1 # Tunes hbar
r=0 # Free phase convention
walk = QW2D(q, eps=0.01, m=1.0,
xX0=1, xZ1=1, 
yX1=1, 
pxX0=1, pxZ0=-l, pxZ1=r, 
pyX1=1, pyZ0=r, pyZ1=-l) 






# POSTFIX

t=0
walk.plot_complete(psi0,t)
t=40
psiT = walk.evolve(psi0, n_steps=t)
walk.plot_complete(psiT,t)


