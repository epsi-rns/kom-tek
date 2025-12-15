Point Load - Roller
-------------------

> Table Lookup Method

Determinant Static

A: Pinned
B: Point Load
B: No Support
C: Roller

--

# Lookup Table

## End slopes (rotation at supports)

-θ1 at x=0,  θ2 at x=L

\begin{align*}
    \theta_1 \quad \text{at} &\quad x=0,\\
    \theta_1 &= \frac{P b (l^2 - b^2)}{6 l E I}, \\
\\
    \theta_2 \quad \text{at} &\quad  x=l \\
    \theta_2 &= \frac{P a b (2l - b)}{6 l E I} \\
\end{align*}

## Deflection y(x) (piecewise)

\begin{align*}
    \text{For} \quad (0 < x < a): \\
    y(x) &= \frac{P b x}{6 E I l}
    \bigl(l^2 - x^2 - b^2\bigr) \\
\\
    \text{For} \quad (a < x < l): \\
    y(x) &= \frac{P b}{6 E I l}
    \Biggl[\frac{l}{b}(x-a)^3 + (l^2 - b^2),x - x^3\Biggr] \\
\end{align*}

## Maximum deflection

\begin{align*}
    & \delta_{\max} = \frac{P b \bigl(l^2 - b^2\bigr)^{3/2}}{9\sqrt{3}\,l\,E I} \\
    & \text{located at} \quad x = \sqrt{(l^2-b^2)}/3
\end{align*}

\text{(located at} \quad x = \sqrt{(l^2-b^2)}/3 \quad \text{per table)}

## Simplification at The Center

\begin{align*}
    & \delta_{\text{center}} = \frac{P b\,(3l^2 - 4b^2)}{48\,E I} \\
    & \text{(value at }x=l/2)
\end{align*}

--

# Equilibrium

## Sum of Forces

\begin{align*}
    \sum F_y = 0 & \implies R_A + R_C - P = 0 \\
                 & \Rightarrow R_A + R_C = P \tag{1} \\
\\
    \sum M_A = 0 & \implies R_C \cdot l - P \cdot a = 0 \\
                 & \Rightarrow R_C = \frac{P a}{l} \tag{2}
\end{align*}

## Substitutes

\begin{align*}
& R_A + \frac{P a}{l} = P \\
& \Rightarrow R_A = P - \frac{P a}{l} \\
& \Rightarrow R_A = P \left(1 - \frac{a}{l}\right) \\
& \Rightarrow R_A = \frac{P(l - a)}{l} \\
\end{align*}

## Considering (l−a=b)

\boxed{R_A = \frac{P b}{l}}, \qquad \boxed{R_C = \frac{P a}{l}}

--

# Equilibrium

## Support Reactions

R_A = \frac{P\,b}{l}, \qquad
R_C = \frac{P\,a}{l}

## Using Known Values

\begin{align*}
    P = 50   \,\text{N}, 
    l = 0.25 \,\text{m}, \\
    a = 0.20 \,\text{m}, 
    b = 0.05 \,\text{m}, \\
\end{align*}

\begin{align*}
R_A &= \frac{P\,b}{l} 
     = \frac{50\times0.05}{0.25} = 10 \, \text{N}, \\
R_C &= \frac{P\,a}{l}
     = \frac{50\times0.20}{0.25} = 40 \, \text{N}.
\end{align*}

## End slopes (θmax​)

\begin{align*}
    \theta_1 &= \frac{P b\,(l^2 - b^2)}{6\,l\,E I}
    = \underbrace{0.002}_{\text{(rad) per }P/(EI)} \frac{P}{E I}, \\  
    \theta_2 &= \frac{P a b (2l - b)}{6\,l\,E I}
    = \underbrace{0.003}_{\text{(rad) per }P/(EI)} \frac{P}{E I}. \\
\end{align*}


\boxed{\theta_{\max} = \theta_2 = 0.003;\frac{P}{E I}\ \text{(radians)}.}

## Deflection under The Load

\begin{align*}
y(a) &= \frac{P b a}{6\,l\,E I}\bigl(l^2 - a^2 - b^2\bigr) \\
     &= \underbrace{0.0001333333333}_{\text{m per }P/(EI)} \, \frac{P}{E I} \\
     &= 0.0001333333 \, \frac{P}{E I}\ \text{(m)}
\end{align*}

-- -- --

Point Load - Roller
-------------------

> Double Integration Method

Determinant Static

A: Pinned
B: Point Load
B: No Support
C: Roller

--

# Governing Differential Equation

E I \,y''(x) = M(x)

# Boundary Conditions (BC)

## Deflection is zero:

y(0) = 0 \quad y(l) = 0

--

# Static Reactions

\begin{align*}
\sum F_y = 0 &: R_A + R_C - P = 0, \\
\sum M_A = 0 &: R_C \, l - P a = 0.
\end{align*}

\text{where} \quad (b = l - a)

$
M_1 = R_A \cdot x
$

--

# Moment M(x) (piecewise)

R_A = \dfrac{P b}{l}, \quad R_C = \dfrac{P a}{l}

$
M(x)=
\begin{cases}
    R_A\,x          , & 0\le x < a, \\
    R_A\,x - P(x-a) , & a\le x\le l.
\end{cases}
$

--

# Double Integration (left segment 0<x<a)

y(0) = 0, \quad 0<x<a \quad \Rightarrow C_2 = 0

\begin{align*}
    E I\,y''(x) &= R_A x. \\
    \\
    E I\,y'(x)  &= \frac{R_A x^2}{2} + C_1 \\
    y_L'(x)     &= \frac{R_A x^2}{2 E I} + \frac{C_1}{E I} \\
    \\
    E I\,y(x)   &= \frac{R_A x^3}{6} + C_1 x + C_2 \\
    y_L(x)      &= \frac{R_A x^3}{6 E I} + \frac{C_1}{E I} \, x \\
\end{align*}

--

# Boundary and Continuity Conditions

\begin{align*}
\text{At } A (x=0): & \quad y_1 = 0 \Rightarrow C_2 = 0, \\
\text{At } C (x=l): & \quad y_2 = 0, \\
\text{At } x=a:     & \quad y_1(a) = y_2(a), \\
                    & \quad y_1'(a) = y_2'(a).
\end{align*}

--

# Double Integration (right segment a<x<l)

\text{For}\, (a<x<l)

\begin{align*}
    E I\,y''(x) &= R_A x - P(x-a) \\
    \\
    E I\,y'(x)  &= \frac{R_A x^2}{2} - \frac{P x^2}{2} + P a x + C_3 \\
    &= \frac{(R_A-P)x^2}{2} + P a x + C_3 \\
    E I\,y(x)   &= \frac{(R_A-P)x^3}{6} + \frac{P a x^2}{2} + C_3 x + C_4 \\
    y_R(x)      &= \frac{(R_A-P)x^3}{6 E I} + \frac{P a x^2}{2 E I} + \frac{C_3}{E I}x + \frac{C_4}{E I} \\
\end{align*}

--

# Determine Integration Constants C1, C3, C4

1. Deflection Continuity at (x=a)

y_L(a) = y_R(a)

2. Slope Continuity at (x=a)

y_L'(a) = y_R'(a)

3. Right Support Deflection Zero

y_R(l) = 0

--

# Apply Continuity of Slope at (x=a)

\begin{align*}
E I\,y_1'(a) &= \frac{R_A a^2}{2} + C_1, \\
E I\,y_2'(a) &= \frac{(R_A - P)a^2}{2} + P a^2 + C_3.
\end{align*}

C_1 = C_3 + frac{P a^2}{2} 

--

# Apply Continuity of Deflection at (x=a)

\begin{align*}
  E I\,y_1(x) &= \frac{R_A x^3}{6} + C_1 x + C_2, \\
  E I\,y_2(x) &= \frac{(R_A - P)x^3}{6} + \frac{P a x^2}{2} + C_3 x + C_4.
\end{align*}

\begin{align*}
   E I \,y_1(a) &= E I \,y_2(a) \\
   \frac{R_A a^3}{6} + C_1 a + C_2 &= \frac{(R_A - P)a^3}{6} + \frac{P a^3}{2} + C_3 a + C_4 \\
   \frac{R_A a^3}{6} + C_1 a + C_2 &= \frac{R_A a^3}{6} - \frac{P a^3}{6} + \frac{P a^3}{2} + C_3 a + C_4 \\
   -\frac{P a^3}{6} + \frac{P a^3}{2} &= +\frac{P a^3}{3} \\
   \frac{R_A a^3}{6} + C_1 a + C_2 &= \frac{R_A a^3}{6} + \frac{P a^3}{3} + C_3 a + C_4 \\
   C_1 a + C_2 =& C_3 a + C_4 + \frac{P a^3}{3}.
\end{align*}


--

# Substitute

C_1 = C_3 + \frac{P a^2}{2}

\begin{align*}
    (C_3 + \frac{P a^2}{2})a + C_2 &= C_3 a + C_4 + \frac{P a^3}{3} \\
    C_3 a + \frac{P a^3}{2} + C_2  &= C_3 a + C_4 + \frac{P a^3}{3} \\
    \frac{P a^3}{2} + C_2          &= C_4 + \frac{P a^3}{3} \\
\end{align*}


C_4 = C_2 + \frac{P a^3}{2} - \frac{P a^3}{3} = C_2 + \frac{P a^3}{6}

--

# Deflection (closed form)

> Final closed-form results (matching the lookup table)

## For (0<x<a):

y(x) = \frac{P b,x}{6 E I\, l} \bigl(l^2 - x^2 - b^2\bigr)

## For (a<x<l):

y(x) = \frac{P b}{6 E I\ l} \Biggl[\frac{l}{b}(x-a)^3 + (l^2-b^2) x - x^3\Biggr]

--

# End slopes (closed form)

> End slopes (from the first-integrals)

\begin{align*}
    \theta_1 &= y'(0) &= \frac{P b (l^2-b^2)}{6\,l\,E I}, \\
    \theta_2 &= y'(l) &= \frac{P a b (2l-b)}{6\,l\,E I}
\end{align*}

--

# Maximum Deflection (location and value)

y'(x)=0 \quad \text{in the interval} \quad (0<x<l)

\begin{align*}
    x_{max}      &= \frac{\sqrt{l^2 - b^2}}{\sqrt{3}}, \\
    \delta_{max} &= y(x_{max}) = \frac{P b (l^2 - b^2)^{3/2}}{9\sqrt{3}\,l\,E I}
\end{align*}

# The Three Constant

Thus the three constants are

\begin{align*}
    C_1 &= -\frac{P a l}{3} - \frac{P a^3}{6 l} + \frac{P a^2}{2} , \\
    \\
    C_3 &= -\frac{P a l}{3} - \frac{P a^3}{6 l} , \\
    \\
    C_4 &= C_2 + \frac{P a^3}{6} . \\
\end{align*}

\begin{flushleft}
\begin{align*}
    \boxed{C_1 = -\frac{P a l}{3} - \frac{P a^3}{6 l} + \frac{P a^2}{2}}, \\
    \boxed{C_3 = -\frac{P a l}{3} - \frac{P a^3}{6 l}}, \\
    \boxed{C_4 = \frac{P a^3}{6} }. \\
\end{align*}
\end{flushleft}

--

# Deflection at Left Support (x=0)

\begin{align*}
    E I\,y_1(x) &= \frac{R_A x^3}{6} + C_1 x + C_2 \\
    E I\,y_1(0) &= 0 = 0 + 0 + C_2 \implies C_2 = 0 \\
    C_4 &= C_2 + \frac{P a^3}{6} = \frac{P a^3}{6}
\end{align*}

# Deflection at Right Support  (x=l)

\begin{align*}
    E I,y_2(x) &= \frac{(R_A - P)x^3}{6} + \frac{P a x^2}{2} + C_3 x + C_4 \\
    0          &= \frac{(R_A - P)l^3}{6} + \frac{P a l^2}{2} + C_3 l + C_4 \\
    0          &= \frac{(\tfrac{P b}{l} - P)l^3}{6} + \frac{P a l^2}{2} + C_3 l + \frac{P a^3}{6} \\
    (\tfrac{P b}{l} - P)l^3 &= P(b - l)l^2 = -P a l^2 \\
    0          &= \frac{-P a l^2}{6} + \frac{P a l^2}{2} + C_3 l + \frac{P a^3}{6} \\
    \frac{-1}{6} + \frac{1}{2} &= \frac{1}{3} \\
    0          &= \frac{P a l^2}{3} + C_3 l + \frac{P a^3}{6} \\
    C_3        &= -\frac{P a l^2}{3l} - \frac{P a^3}{6l} = -\frac{P a}{l}\left(\frac{l^2}{3} + \frac{a^2}{6}\right) \\
    C_3        &= -\frac{P a}{6l}\bigl(2l^2 + a^2\bigr)
\end{align*}

# Back-substitute to find all constants

\begin{align*}
    C_1 &= C_3 + \frac{P a^2}{2} \\
        &= -\frac{P a}{6l}(2l^2 + a^2) + \frac{P a^2}{2} \\
        &= -\frac{P a}{6l}(2l^2 + a^2 - 3 a l), \\
    C_2 &= 0, \\
    C_3 &= -\frac{P a}{6l}(2l^2 + a^2), \\
    C_4 &= \frac{P a^3}{6}.
\end{align*}

--

# Left Segment: Substitution

\begin{align*}
    E I\,y_L(x) &= \frac{R_A x^3}{6} + C_1 x + C_2 \\
    C_1         &= -\frac{P a l}{3} - \frac{P a^3}{6 l} + \frac{P a^2}{2} \\
\end{align*}

\begin{align*}
    E I\,y_L(x)
        &= \frac{P b}{l}\cdot\frac{x^3}{6} 
        + \left(-\frac{P a l}{3} - \frac{P a^3}{6 l} + \frac{P a^2}{2}\right)x \\
        &= \frac{P}{6 l}\Bigl(b x^3 + \bigl(-2 a l^2 - a^3 + 3 a^2 l\bigr)\frac{x}{1}\Bigr)
\end{align*}

\begin{align*}
    b = l-a \\
    E I,y_L(x) = \frac{P b x}{6 l}\bigl(2 a l - a^2 - x^2\bigr) \\
\end{align*}

\begin{align*}
    b^2=(l-a)^2=l^2-2al+a^2 \\
    2 a l - a^2 - x^2 = l^2 - x^2 - b^2 \\
\end{align*}

\boxed{\,y_L(x) = -\,\dfrac{P b x}{6 E I\, l}\bigl(l^2 - x^2 - b^2\bigr)}

# Location of maximum deflection

\begin{align*}
    y_L(x) &= \frac{P b x}{6 E I l}\bigl(l^2 - x^2 - b^2\bigr) \\
    K      &= \dfrac{P b}{6 E I\, l} \\
    y_L(x) &= K \,x \,(l^2 - x^2 - b^2)
\end{align*}

\begin{align*}
    y_L'(x) &= K\bigl(l^2 - x^2 - b^2 + x(-2x)\bigr) \\
            &= K\bigl(l^2 - b^2 - 3x^2\bigr) \\
\end{align*}

\begin{align*}
    y_L'(x) &= 0 \\
    l^2 - b^2 - 3x^2 &= 0 \\
    \Longrightarrow\quad x^2 &= \frac{l^2 - b^2}{3}
\end{align*}

\boxed{\,x_{\max} = \frac{\sqrt{\,l^2 - b^2,}}{\sqrt{3}}}

## Maximum Deflection

y_L \, \text{at} \, x=x_{\max}

x_{\max}^2 = (l^2-b^2)/3

\begin{align*}
    l^2 - x_{\max}^2 - b^2 
        &= l^2 - b^2 - x_{\max}^2 \\
        &= l^2 - b^2 - \frac{l^2 - b^2}{3} \\
        &= \frac{2}{3}\bigl(l^2 - b^2\bigr)
\end{align*}

\begin{align*}
    \delta_{max} &\equiv y_L(x_{max})
    = K x_{max} \frac{2}{3}\bigl(l^2 - b^2\bigr) \\
    &= \frac{P b}{6 E I, l} \cdot \frac{\sqrt{\,l^2-b^2\,}}{\sqrt{3}} \cdot \frac{2}{3}\bigl(l^2 - b^2\bigr) \\
    &= \frac{P b \,(l^2 - b^2)^{3/2}}{6 E I\, l}\cdot\frac{2}{3\sqrt{3}} \\
    &= \frac{P b \,(l^2 - b^2)^{3/2}}{9\sqrt{3}\, E I, l}
\end{align*}

\boxed{\,\delta_{\max} = \dfrac{P b \,(l^2 - b^2)^{3/2}}{9\sqrt{3}\, E I\, l},}

--

# Left end slope θ1 (at x=0)

\begin{align*}
    E \,y_L'(x)   &= \frac{R_A x^2}{2} + C_1 \\
    E I\,\theta_1 &= E I,y_L'(0) = C_1 \\
    E I\,y_L'(x)  &= \frac{P b}{6 l}\bigl(l^2 - b^2 - 3x^2\bigr) \\
    E I\,\theta_1 &= \frac{P b}{6 l}\bigl(l^2 - b^2\bigr) \\
\end{align*}


\boxed{\,\theta_1 = \dfrac{P b\,(l^2 - b^2)}{6 l E I}\,}

# Right end slope θ2 (at x=l)

E I\,y_2'(x) = \frac{(R_A-P)x^2}{2} + P a x + C_3

\boxed{\,\theta_2 = \dfrac{P a b (2l - b)}{6 l E I}\,}

-- -- --

Point Load - Roller
-------------------

> Segment by Segment Integration Method

Determinant Static

A: Pinned
B: Point Load
B: No Support
C: Roller

--

# Setup / knowns

## Reactions from statics

R_A = \frac{P b}{l} , \qquad R_C = \frac{P a}{l}

## Governing Differential Equation

E I,y''(x) = M(x)

## Piecewise moment

M(x)=
\begin{cases}
    R_A x,          & 0 \le x < a, \\
    R_A x - P(x-a), & a \le x \le l.
\end{cases}

--

# Left Segment (0 ≤ x ≤ a)

## Integration

\begin{align*}
    E I\,y_1''(x) &= R_A x \\
    E I\,y_1'(x)  &= \frac{R_A x^2}{2} + C_1 \\
    E I\,y_1(x)   &= \frac{R_A x^3}{6} + C_1 x + C_2 \\
\end{align*}

## Boundary Conditions (BC)

x = 0 \Rightarrow y_1(0) = 0, \quad \text{gives} \quad C_2=0

\boxed{\,E I\,y_1(x) = \frac{R_A x^3}{6} + C_1 x\, \quad 0\le x\le a}

# Evaluate at (x=a)

\begin{alignat*}{2}
    E I\,\theta_a^- &= E I\,y_1'(a) &&= \frac{R_A a^2}{2} + C_1, \\
    E I\,y_a^-       &= E I\,y_1(a)  &&= \frac{R_A a^3}{6} + C_1 a.
\end{alignat*}

--

# Right Segment (a ≤ x ≤ l)

## Integration

\begin{align*}
    E I\,y_2''(x) &= R_A x - P(x-a) = (R_A-P)x + P a \\
    E I\,y_2'(x)  &= \frac{(R_A-P)x^2}{2} + P a x + C_3 \\
    E I\,y_2(x)   &= \frac{(R_A-P)x^3}{6} + \frac{P a x^2}{2} + C_3 x + C_4 \\
\end{align*}

## Boundary Conditions (BC)

x = a \Rightarrow y_2(a) = y_1(a), \quad y_2'(a) = y_1'(a)

\begin{align*}
    E I\,y_2'(a) &= \frac{(R_A-P)a^2}{2} + P a^2 + C_3, \\
    E I\,y_2(a)  &= \frac{(R_A-P)a^3}{6} + \frac{P a^3}{2}+C_3 a + C_4.
\end{align*}

--

# Two Equations from Continuity

## Equality of slopes at (x=a)

\frac{R_A a^2}{2} + C_1 = \frac{(R_A-P)a^2}{2} + P a^2 + C_3

C_1 - C_3 = \frac{P a^2}{2}
\qquad\Longrightarrow\qquad
\boxed{\,C_3 = C_1 - \frac{P a^2}{2}\,}

## Equality of deflections at (x=a)

\frac{R_A a^3}{6} + C_1 a = \frac{(R_A-P)a^3}{6} + \frac{P a^3}{2} + C_3 a + C_4.

\begin{align*}
    C_1 a - C_3 a - C_4 &= \frac{P a^3}{3} \\
    C_1 a - \bigl(C_1 - \tfrac{P a^2}{2}\bigr)a - C_4 &= \frac{P a^3}{3} \\
    \frac{P a^3}{2} - C_4 &= \frac{P a^3}{3} \\
\end{align*}

\Rightarrow \boxed{\,C_4 = \frac{P a^3}{6}\,}

--

# Apply Right-Support Boundary

y_2(l) =0 \quad \text{to solve for} \quad C_1

\begin{align*}
    0 &= \frac{(R_A-P)l^3}{6} + \frac{P a l^2}{2} + C_3 l + C_4 \\
    0 &= \frac{(R_A-P)l^3}{6} + \frac{P a l^2}{2} + \Bigl(C_1-\frac{P a^2}{2}\Bigr)l + \frac{P a^3}{6} \\
    C_1 l &= -\frac{(R_A-P)l^3}{6} - \frac{P a l^2}{2} + \frac{P a^2}{2}\,l - \frac{P a^3}{6} \\
\end{align*}

(R_A-P)l^3 = \Bigl(\frac{P b}{l}-P\Bigr)l^3 = P(b-l)l^2 = -P a l^2 \\

\begin{align*}
    C_1 l &= -\frac{(-P a l^2)}{6} - \frac{P a l^2}{2} + \frac{P a^2 l}{2} - \frac{P a^3}{6} \\
    C_1 l &= \frac{P a l^2}{6} - \frac{P a l^2}{2} + \frac{P a^2 l}{2} - \frac{P a^3}{6} \\
    C_1 l &= -\frac{P a l^2}{3} + \frac{P a^2 l}{2} - \frac{P a^3}{6}. \\
\end{align*}

\boxed{\,C_1 = \frac{P a}{6 l}\bigl(-2 l^2 + 3 a l - a^2\bigr)\,} 

--

# Back-Substitute to Find (C_3, C_4)

\boxed{\,C_3 = C_1 - \frac{P a^2}{2} = -\frac{P a}{6 l}\bigl(2 l^2 + a^2\bigr)\,}

\boxed{\,C_4 = \frac{P a^3}{6}\,}

--

# Final Piecewise Deflection Functions

## Left Segment (0 ≤ x ≤ a)

\begin{align*}
    E I\,y_1(x) = \frac{R_A x^3}{6} + C_1 x \\
    \quad \Longrightarrow \quad
    \boxed{\,y_1(x) = \frac{P b\,x}{6 E I\, l}\bigl(l^2 - x^2 - b^2\bigr)\,}
\end{align*}

## Right Segment (a ≤ x ≤ l)

\begin{align*}
    E I\,y_2(x) = \frac{(R_A-P)x^3}{6} + \frac{P a x^2}{2} + C_3 x + C_4 \\
    \boxed{\,y_2(x) = \frac{P b}{6 E I\, l}\Bigl[\frac{l}{b}(x-a)^3 + (l^2-b^2)\,x - x^3\Bigr]\,}
\end{align*}

--

# Stationary Point

y_1(x) = K \,x(l^2-x^2-b^2)\, \quad K = \frac{P b}{6 E I\, l}

\text{Set} \quad y_1'(x)=0

\begin{align*}
    l^2-b^2-3x^2=0 \\
    \Rightarrow\quad x_{\max} = \frac{\sqrt{\,l^2-b^2,}}{\sqrt{3}}
\end{align*}

# Maximum Deflection

\boxed{\,\delta_{\max} = \frac{P b\,(l^2-b^2)^{3/2}}{9\sqrt{3}\,E I\,l}\,}

-- -- --
