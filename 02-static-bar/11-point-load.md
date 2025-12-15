Point Load - Free
-------------------

> Table Lookup Method

Determinant Static

A: Fixed End.
B: Point Load.
B: No Support (Free End)

# Lookup Table

\begin{align*}
\theta &= \frac{P L^2}{2 E I} \\
\\
\delta_{max} &= \frac{P L^3}{3 E I} \\
\\
y &= \frac{P x^2}{6 E I}(3L-x)
\end{align*}


# Equilibrium

\begin{flalign*}
& \sum F_x = 0, &
  \quad\ R_{Ax} = 0
\\
& \sum F_y = 0, &
  \quad R_{Ay} - P = 0 &
  \quad\Rightarrow\quad
  R_{Ay} = P = 50 \,\text{N} \,\text{(Downward)}
\\
& \sum M_A = 0, &
  \quad M_A - (P \cdot L) = 0 &
  \quad\Rightarrow\quad
   M_A = P \cdot L
\end{flalign*}

F = 50 \text{ N}, \quad 
L_1 = 25 \text{ cm}, \quad 
L_2 = 5 \text{ cm}

given values $F = 50 \text{ N}$ and $L = 25 \text{ cm} = 0.25 \text{ m}$:

R_{Ay} = 50\,\text{N}

M_A = (50\,\text{N}) \cdot (0.25\,\text{m}) 
    = 12.5\, \text{N} \cdot \text{m}
    \quad \text{(Counter-Clockwise)}

# Maximum Deflection (δmax​)

\begin{align*}
\delta_{max} &= \frac{(50 \,\text{N})(0.25 \,\text{m})^3}{3EI} \\
             &= \frac{50 \cdot (0.015625)}{3EI} \\
             &= \frac{0.78125}{3EI} \,\text{m}
\end{align*}


# Maximum Slope (θmax​)

\begin{align*}
\theta_{max} &= \frac{(50 \,\text{N})(0.25 \,\text{m})^2}{2EI} \\
             &= \frac{50 \cdot (0.0625)}{2EI} \\
             &= \frac{3.125}{2EI} \,\text{radian}
\end{align*}

-- -- --

Point Load - Free
-------------------

> Double Integration Method

# Governing Differential Equation

EI \frac{d^2v}{dx^2} = M(x)

# Boundary Conditions (BC)

Deflection is zero:
v(0) = 0

Slope is zero:
\frac{dv}{dx} (0) = 0

# Moment Equation

M(x) = -P(L - x) = -PL + Px

ask for sign later

# First Integration (Slope Equation)

## Substitute M(x)

\begin{align*}
        EI \frac{d^2v}{dx^2} &= -PL + Px \\
\\
\int EI \frac{d^2v}{dx^2} dx &= \int (-PL + Px) dx \\
\\
            EI \frac{dv}{dx} &= -PLx + \frac{Px^2}{2} + C_1 \\
\end{align*}

## Apply BC_A

\frac{dv}{dx} = 0 \quad \text{at} \quad x=0

\begin{align*}
EI(0) = -PL(0) + \frac{P(0)^2}{2} + C_1 \\
\quad \implies \quad C_1 = 0
\end{align*}

## Slope Equation

EI \frac{dv}{dx} = -PLx + \frac{Px^2}{2}

# Second Integration (Deflection Equation)

## Integrate Slope Equation

\begin{align*}
\int EI \frac{dv}{dx} dx &= \int \left(-PLx + \frac{Px^2}{2}\right) dx \\
\\
                 EI v(x) &= -\frac{PLx^2}{2} + \frac{Px^3}{6} + C_2 \\
\end{align*}

## Apply BC_A

v = 0 \quad \text{at} \quad $x=0$

\begin{align*}
EI(0) &= -\frac{PL(0)^2}{2} + \frac{P(0)^3}{6} + C_2 \\
      &\implies \quad C_2 = 0
\end{align*}

## Deflection Curve Equation

\begin{align*}
v(x) &= \frac{1}{EI} \left( -\frac{PLx^2}{2} + \frac{Px^3}{6} \right) \\
     &= \frac{PLx^2}{6EI} (x-3L)
\end{align*}

# Find the Maximum Deflection

## Free End (B), where x=L

\begin{align*}
v_{\text{max}} &= v(L) = \frac{1}{EI} \left( -\frac{PL(L)^2}{2} + \frac{P(L)^3}{6} \right) \\
\\
v_{\text{max}} &= \frac{1}{EI} \left( -\frac{PL^3}{2} + \frac{PL^3}{6} \right) \\
\\
&= \frac{1}{EI} \left( -\frac{3PL^3}{6} + \frac{PL^3}{6} \right) 
= \frac{1}{EI} \cdot -\frac{2PL^3}{6} \\
\\
v_{\text{max}} &= \frac{1}{EI} \left( -\frac{2PL^3}{6} \right) = -\frac{PL^3}{3EI}
\end{align*}

# Final Result

## Maximum Slope at (x=L)

\theta_{max} \quad \text{(at x=L)}

\fbox{$
\theta_{max} = \frac{PL^2}{2EI}
$}

## Maximum Deflection at (x=L)

\Delta_{max} \quad \text{(at x=L)}

\fbox{$
\Delta_{max} = \frac{PL^3}{3EI}
$}



