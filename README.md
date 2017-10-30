# capow

Introduction
CAPOW is a graphical user interface to operate two programs; one to produce normal probability plots and another to calculate the optimal a and b parameters for a SHELXL weighting scheme. The SHELXL weighting scheme has six variables which can be defined by the user (a-f). For a refinement on F2:
(w=  q/(σ_(F^2)^2+(ap)^2+bp+d+e sin⁡θ ))
where p=f×F_o^2+(1-f)×F_c^2 and q varies depending on the sign of parameter c: q=1.0 when c = 0, q=exp⁡〖(c〗 (sin⁡θ/λ)^2)  when c > 0, and q=〖1 - exp〗⁡〖(c〗 (sin⁡θ/λ)^2)  when c > 0.

Optimal a and b parameters are routinely calculated for data refined in a variety of refinement programs, with the other parameters (c, d, e = 0 and f = 1/3) remaining fixed.

