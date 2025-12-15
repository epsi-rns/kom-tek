### Preface

> Goal: A practical overview of trends,
> from modeling data in Excel to scripting it in Python.

_I can read the data._ \
_I know what it means._

Once, I had this eureka moment. \
I want you to experience it too.

Data is nowadays language, a new form of communication. \
The way we perceive data shaping how we think. \
In this way, insight becomes natural outcome.

-- -- --

### Beyond the Books: A Hands-On Revival

> For those left behind.

A statistics handbook that I read make me realize. \
They are relics from a pre-code era.

No cheatsheets, no worksheets, \
And not a single line of usable code.

That's when somehow, my conscience stirred with a **calling**, loud and clear:
"_To bridge the gap for those left behind_."
My inner activist side found my objective.

#### When Curiosity Meets Data

> A Second Chance

Learning should never expire.
I've always wanted to learn statistics,
but I never quite knew where to begin.
The breakthrough came when I was challenged
to fit a curve to a data series.
That one task opened the door to regression,
correlation, and a whole new perspective.

Back in college, I never skipped a single statistics class.
But even then, what we learned barely
scratched the surface, just the basics.
Meanwhile, I heard that other universities were
diving into things like ANOVA.

Sure my office task doesn't demand intermediate statistics.
But the fact that I know nothing about it,
makes me an unprepared employee,
who can't solve things with further tools.
Or worse, **_I feel so uneducated_**.
Now, two decades later, I find myself learning everything from scratch.
No formal class. No course. Just curiosity.

I started seriously exploring statistics around 2017.
A book helped me lay the foundation, and since then,
I've seen tons of content, concepts in videos,
fancy online calculators, and summaries in articles.

#### Data, Math, and the Code Behind It

> Built for belonging.

But here's the problem: very few of them come with real,
practical Excel examples for everyday use.
And without doing the calculations manually,
how can I be sure my results are even correct?
I want to see how the math works,
not just get the answer.

Even the online tools fall short.
If they don't explain the math equation behind the scenes,
how am I supposed to learn from them?
Books help, sure. But even if I understand the theory,
how do I turn that into a script?
How do I actually use this knowledge?
How do I automate my job with scripting?

Most handbooks reveal their age.
Not by their theories, but by their absence of practical tools,
like cheatsheets, interactive worksheets,
or coding examples that reflect today's data-driven workflows.

That's why I've decided to take
a new approach on learning statistics.
One that's hands-on, grounded, and script-friendly:

* Understand the math behind the method
* Reproduce it manually using Excel
* Implement it programmatically using Python
* Go further with automation, nice visualization,
  and combine with other technologies

My goal is to speed up the learning process, for anyone wishing to learn.
This is not for my personal achievement, nor targeting academics.

_This article series is not built for brilliance,_ \
_but for belonging._

#### Reality Bites

> I passed the exam, but I failed in the real world.

I've been away from the university for more than two decades.
And I heard they have a good program nowadays.
But how about most people?

Matching skill with market demands is,
not just about career planning.

Trust me. _When all you got is rice,_
_cheap vegetables and a pile of debts,_
_this is going to affect your body shape soon._

Now those days are gone.
Nothing can stop Tom Cruise from running.
Nothing can stop me from writing and sharing.

#### Approachable Statistics

> Down to Earth

I want to bring statistics down from the ivory tower,
and into the kitchen table,
where real people make real decisions.

Let's make statistics less of a scary math monster,
and more of a friendly tool.
Something we can use even before our morning coffee kicks in.

-- -- --

### Habit Change

_How do we start solving math problem?_

Back in my college days, it was simple:
Grab a sheet of paper, scribble down the equation,
and work it through by hand.
Line by line. Thought by thought.
Derive this. Simplify that. Pure muscle memory.

But times have changed. Paper is rare. Pens are even rarer.
These days, I don't even carry one in my bag.
No more old-school notes on napkins.
So naturally, the way I "_write things down_" has evolved.

_What tools do we used these days?_

How do we approach it now?
We've had spreadsheets for more than
two decades (since about 25 years ago),
and they've become second nature.
When intuition kicks in, I reach straight for Excel
 It's quick, visual, and everywhere.
Need to show someone your data model? Screenshot it.
Paste the result into WhatsApp.
Or better yet, just attach the whole spreadsheet file.

_How do you communicate the equation itself?_

Sure, Excel can display equations nicely.
But if I want to share the math behind the scenes,
especially in a clean, readable format, I'll use LaTeX.
LaTeX gives me both beauty and precision:
equations that are easy to read by humans,
and still machine-readable.

_What is the final form?_

It depends, on the audience, the purpose, and the medium.
For something like a polynomial fit, I usually want a visual chart.
One that compares the raw data to the fitted curve.
So anyone can instantly see what's going on.

This chart could be made in Excel, sure.
But for more control and automation,
I use Python's matplotlib.
That way, I can export an image,
ready to drop into any chat app or social feed.
You could use R, or any language that speaks data.
The tool doesn't matter. The insight does.

-- -- --

### How do We Start?

> Hands-on walkthrough!

We kick things off with something familiar: **polynomial curve fitting**.



From there, we'll level up.
Venturing into **least squares**, **regression**, and **correlation**.
And it all starts with a good old-fashioned cheatsheet.

Here's a breakdown of the equation flow for basic **linear regression**:



But we're not stopping at linear. 
we also tackle **polynomial regression** too.
This is where we lay the real groundwork.



To make this journey easier,
I've put together a beginner-friendly worksheet.
Aa step-by-step guide to solving linear regression by hand,
with full statistical context.

Once we've done the math manually
(because we should understand it before automating it),
we'll switch gears and use built-in spreadsheet formulas,
in Excel or LibreOffice Calc.



Then comes Python.
We'll walk through manual calculations in code,
followed by Python's built-in helpers.
`numpy`, `scipy`, and other statistics libraries.
Then we'll move on to **visualizing** results with `matplotlib`.

For example: here is a confidence interval shaded around a regression line.



We'll also cover **distribution analysis**,
plotting density curves to understand how our data behaves.
We need to learn the basic of plotting the distribution curve.



Eventually, we'll be able to overlay
**statistical markers** on **histograms**, like this:



Want a little more elegance?you’ve laid real groundwork
We'll enhance our plots using **Seaborn**,
And yes, there's a **JupyterLab** version of every script on GitHub.



We'll even verify our manual work using **PSPPire**,
the open-source cousin of **SPSS**.



Eventually, we'll see how this entire workflow can be replicated in other languages:
such as `R`, `Julia`, and maybe later I will continue with `Typescript`, and `Golang`.



That's all.
For further information, please contact your nearest statistician.

#### How do We Continue?

> Build our own diagnostic kit.

With a solid grasp of **polynomial regression**,
stepping into multivariate regression becomes much easier.
Like swapping our socket wrench for a full torque-calibrated toolkit
From here, we can smoothly move on to ANOVA, ANAREG, MANOVA, and beyond.

The underlying math principles stay familiar,.
The workflows in spreadsheets is similar,
We can build our own tabular data, just more columns to tune.
Python stays approachable, still the same workbench.
And PSPP? Built for everyday end-users like us,
great for routine jobs.

Now, let’s apply this to a real, highly scientific case:
comparing the average cuteness scores of cats, dogs, and rabbits.
Since we have more than two contenders in the adorable Olympics,
we bring out ANOVA, the referee that checks if any group is truly cuter than the rest.
If the p-value is small enough to raise eyebrows,
it means at least one furry faction stands out in cuteness.

And once we've nailed this case,
we're ready to judge any cute contest that comes our way.
From kittens to bunnies to, who knows,
maybe even our favorite coffee mug

Once we understand the **principles**,
we become a builder, not just a user.
When we know how the system works under the hood,
we're no longer tied to:

* One brand of tools (e.g., Excel, Python, R, PSPP)
* One repair manual (e.g., ANOVA vs regression)
* One model of car (tidy vs. messy datasets)

_When we understand the **logic** of the engine._ \
_We don’t just follow the manual._ \
_We tweak. We upgrade. We invent._

-- -- --

### Table of Content

> Polynomial Article Series

I divide this polynomial articles series into subseries:

1. Trend: Prediction

   * **Trend - Overview**
   * **Trend - Built-in Intro**
   * **Trend - Polynomial Interpolation**
   * **Trend - Polynomial Algebra**
   * **Trend - Polynomial in Worksheet**
   * **Trend - Polynomial in Python**
   * **Trend - Polynomial Examples**
   * **Trend - Least Square**

2. Trend: Regression

   * **Trend - Properties - Cheatsheet**
   * **Trend - Properties - Formula**
   * **Trend - Properties - Python Tools**
   * **Trend - Properties - Visualization**
   * **Trend - Polynomial Regression - Theory**
   * **Trend - Polynomial Regression - Spreadsheet**
   * **Trend - Polynomial Regression - Python**

3. Trend: Enhanced

   * **Trend - Visualization - Distribution**
   * **Trend - Properties - Additional**
   * **Trend - Visualization - Seaborn**
   * **Trend - Properties - PSPPire**

4. Trend: Language

   * **Trend - Language - R - Part One**
   * **Trend - Language - R - Part Two**
   * **Trend - Language - R - Part Three**
   * **Trend - Language - Julia - Part One**
   * **Trend - Language - Julia - Part Two**
   * **Trend - Language - Julia - Part Three**

-- -- --

### Understanding Data

> Do you speak data?

The way we understand data isn't just about numbers.
It's how we speak to the world, how we connect ideas.
It's more than interpretation.
It's a new language, a shared space where insight emerges naturally,
like words forming a story.
And once we start seeing it, there's no going back.

_It's not about mastery, it's about becoming fluent._

-- -- --

### Data Jokes

Philosopical thought could be hard.
So, let's lower our frequency.
Relax, and here is a joke for data nerds.

A model strikes up a conversation with a mathematician and proudly says:

"_Hey, I'm a model, you know!_"

The mathematician replies, deadpan:

"_Oh? What kind? Polynomial, Chebyshev, Legendre, or Hermite?_"

She meant runway. He meant regression. Neither apologized.

-- -- --

### What Comes Next 🤔?

The journey begins with the built-in `LINEST `formula in spreadsheets,
and the `Polynomial` library method in Python's numpy.

So if you're ready, let's dive deeper: **Trend - Built-in Method**.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Solving trend with built-in method available in excel and python,
> without reinventing the wheel.

Before we dive into the stone-age ritual of manual curve fitting,
armed with nothing but grid cells and existential dread,
let's appreciate the magic of built-in tools.

Think of them as the microwave ovens of data analysis:
press a button, get results. No firewood. No tears.
Why make life harder when your spreadsheet can do algebra for you?

Here's the cast of characters:

1. Excel/Calc: The `LINEST`
   (statistically smarter than your boss).

2. Python: The `Polynomial` library
   (because polyfit is so last decade).

This saves time: no more manual sums, squares, or swearing at your screen,
and also reduces errors.

"_Work smarter, not harder, unless you enjoy unnecessary suffering._"

#### Worksheet Source

> Playsheet Artefact

A single workbook to rule them all 
(or at least trend-fit them all).



Feel free to poke around or break it lovingly:

* **github.com/.../math/trend/10-curve-fitting.xlsx**

-- -- --

### 1: Linest

Need a trendline? `LINEST` is the statistical butler of Excel.
It serves you linear, quadratic, and cubic fits on a silver platter.

* Linear: `y = a + bx `
  (the classic "straight line through chaos").

* Quadratic: `y = a + bx + cx²`
  (for when life gets curvy).

* Cubic: `y = a + bx + cx² + dx³`
  (because sometimes data has drama).

The easiest way to get curve fitting coefficient,
in spreadsheet in Excel or Calc is by using `LINEST` formula.
`LINEST` handles regression calculations for us,
including slope, intercept, and more.

#### Order Matters

> Unlike in Some Meetings

The equation complexity scales with the polynomial degree.
Here's the cheat sheet:

$$
\begin{array}{|c|c|}
\hline
order = 1 & y = a + b{x}  \\
\hline
order = 2 & y = a + b{x} + c{x}^2 \\
\hline
order = 3 & y = a + b{x} + c{x}^2 + d{x}^3  \\
\hline
\end{array}
$$

#### Linear Linest

> The Straightforward One

Start simple,
consider this linear equation:

$$
y = a + bx
$$



The `LINEST` formula follows the format.
Be aware that the first argument is `y` column first,
then `x` column.

```excel
=LINEST(y_observed, x_observed)
=LINEST(C6:C18;B6:B18)
```

Just don't get the order reversed,
or you'll end up modeling chaos.

To save space (and your sanity), use `TRANSPOSE`:

```excel
=TRANSPOSE(LINEST(y_observed, x_observed))
=TRANSPOSE(LINEST(C6:C18;B6:B18))
```

With this result, we get the linear equation as

$$
y = 5 + 4x
$$

This gives you the coefficients directly.
No matrix math required.

#### Quadratic Linest

> When Life Isn't Linear

The curve deepens,
consider this quadratic equation:

$$
y = a + bx + cx^2
$$

The formula is as below:

```excel
=LINEST(y_observed, x_observed^{1.2})
=LINEST(F6:F18;E6:E18^{1.2})
```

And the transposed version is:

```excel
=TRANSPOSE(LINEST(y_observed, x_observed^{1.2}))
=TRANSPOSE(LINEST(F6:F18;E6:E18^{1.2}))
```

With this result, we get the quadratic equation as

$$
y = 5 + 4x + 3x^2
$$

Quadratic models help when your data has inflection points.

**Pro tip**:
Use Ctrl+Shift+Enter because this is an array formula.
Excel wants you to really mean it.

#### Cubic Linest

> For Extra Spice

With the same method we can get cubic equation:

$$
y = a + bx + cx^2 + dx^3
$$

The formula is as below:

```excel
=LINEST(y_observed, x_observed^{1.2.3})
=LINEST(I6:I18;H6:H18^{1.2.3})
```

And the transposed version is:

```excel
=TRANSPOSE(LINEST(y_observed, x_observed^{1.2.3}))
=TRANSPOSE(LINEST(I6:I18;H6:H18^{1.2.3}))
```

With this result, we get the quadratic equation as

$$
y = 5 + 4x + 3x^2 + 2x^3
$$

Again, Ctrl+Shift+Enter, since the formula contain array such as `{1.2.3}`,
Excel insists. Like a parent checking your homework.

#### Array Operation

So what is this `x_observed^{1.2.3}` after all?

This is arrays of variables: [`xs₁`, `xs₂`, or `xs₃`].
Yo can try yourself in Excel/Calc with something like:

```excel
{=H6:H18^{1.2.3}}
```

Don't forget to `ctrl+shift+enter`.



We will need this to built _gram matrix_ later to solve [`ys₁`, `ys₂`, or `ys₃`].
We can also compare to PSPP variable later.

#### Comparing Linest

> Let's Judge Them All.

Same series. Three different models.
Let's compare, shall we?



Fit all three models to the same data and ask ourself:

* Does it look right? (Eyeball test) Which one fits the best?
* Does it feel right? (Stats test. But we'll get to that later.)
* Do I really need that third-degree polynomial or am I just overfitting my ego?
  Is the extra complexity worth it?

"_If your cubic curve has more twists than your thesis, simplify._"

-- -- --

### 2: Polyfit

Want curve-fitting in Python without summoning the ghost of Gauss?
Say hello to `polyfit`, NumPy's built-in function,
that takes your scattered data,
and slaps a line (or curve) through it like it means business.

The library that we need is just `numpy` and `matplotlib.`
Two imports. Infinite possibilities. And zero manual calculations.

```python
import numpy as np
import matplotlib.pyplot as plt
```

The easiest way to get curve fitting coefficient,
in python script is by using `polyfit` method in `numpy`,
or the new `Polynomial` library in `numpy`.

Instead of wrestling with matrix math,
`polyfit` or `Polynomial` library,
gives us instant coefficients,
like a vending machine for regression models.

#### Linear Polyfit

You can obtain the source code in below:

* **11-polyfit-line.py**

```python
import numpy as np
import matplotlib.pyplot as plt

# Given data
x_values = np.array([
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y_values = np.array([
  5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53])

# Curve Fitting Order
order = 1

# Perform linear regression using polyfit
mC = np.polyfit(x_values, y_values, deg=order)
print('Using polyfit')
print(f'Coefficients (a, b):\n\t{np.flip(mC)}\n')

# Draw Plot
[a, b] = np.flip(mC)
x_plot = np.linspace(min(x_values), max(x_values), 100)
y_plot = a + b * x_plot

plt.scatter(x_values, y_values, label='Data points')
plt.plot(x_plot, y_plot, color='red',
  label='Linear Equation')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.suptitle(
  'Straight line fitting')

subfmt = "a = %.2f, b = %.2f"
plt.title(subfmt % (a, b), y=-0.01)

plt.show()

```

We can start with given **data series** and **order**.

```python
x_values = np.array([
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y_values = np.array([
  5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53])
```

Then getting the `polynomial` coefficient using `polyfit` method:

```python
# Curve Fitting Order
order = 1

# Perform linear regression using polyfit
mC = np.polyfit(x_values, y_values, deg=order)
print('Using polyfit')
print(f'Coefficients (a, b):\n\t{np.flip(mC)}\n')
```

With the result as below coefficient:

```output
Using polyfit
Coefficients (a, b):
        [5. 4.]
```

With this result, we get the linear equation as

$$
y = 5.0 + 4.0 x
$$

Perfect for trendlines, forecasting,
or pretending we're a data wizard at meetings.

#### Matplotlib

> Seeing is Believing

We can plot the result with matplotlib.
First calculate the `x_plot` and `y_plot`:

```python
# Draw Plot
[a, b] = np.flip(mC)
x_plot = np.linspace(min(x_values), max(x_values), 100)
y_plot = a + b * x_plot
```

Then draw two chart in the same `plt` object.
Add the scatterplot and the fitted line:

```python
plt.scatter(x_values, y_values, label='Data points')
plt.plot(x_plot, y_plot, color='red',
  label='Linear Equation')
```

Add some accesories: labels, legends, and title:

```python
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.suptitle(
  'Straight line fitting')
```

And finally show the plot.

```python
subfmt = "a = %.2f, b = %.2f"
plt.title(subfmt % (a, b), y=-0.01)

plt.show()
```

Visual feedback helps catch errors fast,
or show off to your boss with colorful graphs.

#### Quadratic Polyfit

> Now With Curves™

You can obtain the source code in below code:

* **12-polyfit-quadratic.py**

```python
import numpy as np
import matplotlib.pyplot as plt

# Given data
x_values = np.array([
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y_values = np.array([
  5, 12, 25, 44, 69, 100, 137,
  180, 229, 284, 345, 412, 485])

# Curve Fitting Order
order = 2

# Perform quadratic regression using polyfit
mC = np.polyfit(x_values, y_values, deg=order)
print('Using polyfit')
print(f'Coefficients (a, b, c):\n\t{np.flip(mC)}\n')

# Draw Plot
[a, b, c] = np.flip(mC)
x_plot = np.linspace(min(x_values), max(x_values), 100)
y_plot = a + b * x_plot + c * x_plot**2

plt.scatter(x_values, y_values, label='Data points')
plt.plot(x_plot, y_plot, color='red',
  label='Fitted second-order polynomial')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.suptitle(
  'Second-order polynomial curve fitting')

subfmt = "a = %.2f, b = %.2f, c = %.2f"
plt.title(subfmt % (a, b, c), y=-0.01)

plt.show()
```

Here's a dataset that's clearly living its best parabolic life:

```python
x_values = np.array([
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y_values = np.array([
  5, 12, 25, 44, 69, 100, 137,
  180, 229, 284, 345, 412, 485])
```

Just set `order = 2`, and let `polyfit` do its polynomial sorcery
with the result as below:

```output
Using polyfit
Coefficients (a, b, c):
        [5. 4. 3.]
```

That result gives us quadratic equation as

$$
y = 5 + 4x + 3x^2
$$

And the plot? With data series above,
a perfect fit for our data.

Quadratic models are great when our data bends.

#### Cubic Polyfit

We can start with given **data series** and **order**.

```python
x_values = np.array([
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y_values = np.array([
  5, 14, 41, 98, 197, 350, 569, 866, 
  1253, 1742, 2345, 3074, 3941])
```

You can obtain the source code in below link:

* **13-polyfit-cubic.py**

```python
import numpy as np
import matplotlib.pyplot as plt

# Given data
x_values = np.array([
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y_values = np.array([
  5, 14, 41, 98, 197, 350, 569, 866, 
  1253, 1742, 2345, 3074, 3941])

# Curve Fitting Order
order = 3

# Perform cubic regression using polyfit
mC = np.polyfit(x_values, y_values, deg=order)
print('Using polyfit')
print(f'Coefficients (a, b, c, d):\n\t{np.flip(mC)}\n')

# Draw Plot
[a, b, c, d] = np.flip(mC)
x_plot = np.linspace(min(x_values), max(x_values), 100)
y_plot = a + b * x_plot + \
         c * x_plot**2 + d * x_plot**3

plt.scatter(x_values, y_values, label='Data points')
plt.plot(x_plot, y_plot, color='red',
  label='Fitted third-order polynomial')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.suptitle(
  'Third-order polynomial curve fitting')

subfmt = "a = %.2f, b = %.2f, c = %.2f, d = %.2f"
plt.title(subfmt % (a, b, c, d), y=-0.01)

plt.show()
```

Set `order = 3`, and we're in business.
Using similar script we can get the coefficient of cubic equation,
with the result as below:

```output
Using polyfit
Coefficients (a, b, c):
        [5. 4. 3.]
```

With this result, we get the cubic equation as

$$
y = 5 + 4x + 3x^2 + 2x^3
$$

Cubic fits handle complex curves,
ideal for growth trends, fancy predictions,
or data that's just a little extra.

-- -- --

### 3: Playing with data

Once you've tamed the basics of `polyfit`,
it's time to have some fun.
We're now mixing and matching polynomial orders (1st, 2nd, 3rd)
with different custom data series, aka ys1, ys2, and ys3.

Think of it as speed dating for polynomials:
_which model will be your perfect match_?

You can try this at home (or the office, we won't judge):

* **15-polyfit-examples.py**

```python
import numpy as np
import matplotlib.pyplot as plt

from typing import List

class CurveFitting:
  def __init__(self, order: int,
      xs, ys : List[int]) -> None:

    # Curve Fitting Order
    self.order = order

    # Given data
    self.xs = np.array(xs)
    self.ys = np.array(ys)

  def calc_coeff(self) -> None:
    # Perform regression using polyfit,
    mC = np.polyfit(self.xs, self.ys, deg=self.order)

    # Get coefficient matrix
    self.mCoeff = np.flip(mC)

    # Display
    coeff_text = {
      1: '(a, b)', 2: '(a, b, c)', 3: '(a, b, c, d)'}
    print('Using polyfit')
    print(f'Coefficients {coeff_text[self.order]}:'
      + f'\n\t{self.mCoeff}\n')

  def calc_plot_1st(self) -> None:
    [a, b] = self.mCoeff    
    xp = self.x_plot
    self.y_plot = a + b * xp

  def calc_plot_2nd(self) -> None:
    [a, b, c] = self.mCoeff    
    xp = self.x_plot
    self.y_plot = a + b * xp + c * xp**2

  def calc_plot_3rd(self) -> None:
    [a, b, c, d] = self.mCoeff
    xp = self.x_plot
    self.y_plot = a + b * xp + c * xp**2 + d * xp**3

  def draw_plot(self) -> None:
    label = {
      1: 'Linear Equation',
      2: 'Fitted second-order polynomial',
      3: 'Fitted third-order polynomial' }

    plt.scatter(self.xs, self.ys, label='Data points')
    plt.plot(self.x_plot, self.y_plot, color='red',
      label=label[self.order])

    suptitle = {
      1: 'Straight line fitting',
      2: 'Second-order polynomial curve fitting',
      3: 'Third-order polynomial curve fitting' }

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.suptitle(suptitle[self.order])

    subfmt = {
      1: 'a = %.2f, b = %.2f',
      2: 'a = %.2f, b = %.2f, c = %.2f',
      3: 'a = %.2f, b = %.2f, c = %.2f, d = %.2f' }

    title = subfmt[self.order] % tuple(self.mCoeff)
    plt.title(title, y=-0.01)

    plt.show()

  def process(self) -> None:
    self.calc_coeff()

    self.x_plot = np.linspace(
      min(self.xs), max(self.xs), 100)

    order_functions = {
      1: self.calc_plot_1st,
      2: self.calc_plot_2nd,
      3: self.calc_plot_3rd }
 
    if self.order in order_functions:
      order_functions[self.order]()

    self.draw_plot()

def main() -> int:
  order = 2

  xs = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  ys1 = [ 5, 9, 13, 17, 21, 25, 29,
    33, 37, 41, 45, 49, 53]
  ys2 = [ 5, 12, 25, 44, 69, 100, 137,
    180, 229, 284, 345, 412, 485]
  ys3 = [ 5, 14, 41, 98, 197, 350, 569,
    866, 1253, 1742, 2345, 3074, 3941]

  example = CurveFitting(order, xs, ys3)
  example.process()
  
  return 0

if __name__ == "__main__":
  raise SystemExit(main())
```

#### Custom Series

> Choose your own adventure: Linear, Parabolic, or “Whoa, that escalated quickly.”

We've defined three data series with increasing levels of drama:

* `ys₁`: Calm, consistent, linear.
  (your accountant would love it).

* `ys₂`: A gentle parabola.
  (slightly dramatic but manageable).

* `ys₃`: A full-blown polynomial soap opera.

No need for `ys₄`, and `ys₅`.

```python
def main() -> int:
  order = 2

  xs = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  ys1 = [ 5, 9, 13, 17, 21, 25, 29,
    33, 37, 41, 45, 49, 53]
  ys2 = [ 5, 12, 25, 44, 69, 100, 137,
    180, 229, 284, 345, 412, 485]
  ys3 = [ 5, 14, 41, 98, 197, 350, 569,
    866, 1253, 1742, 2345, 3074, 3941]

  example = CurveFitting(xs, ys3)
  example.process()
  
  return 0

if __name__ == "__main__":
  raise SystemExit(main())
```

Real-world data rarely follows a perfect line.
Testing different series and polynomial degrees helps us
choose the model that best fits the story our data is telling.

#### Class Skeleton

> Where object-oriented design meets polynomial destiny.

All of this curve-fitting goodness is wrapped neatly in a `CurveFitting` class.
Oour one-stop shop for modeling, plotting, and feeling like a software architect.

Skeleton methods include:

* `calc_coeff()`  : Finds our precious coefficients.
* `calc_plot_*()` : Generates points for plotting (based on the polynomial order).
* `draw_plot()`   : Unleashes matplotlib to draw your masterpiece.
* `process()`     : Glues it all together so you don't have to.

This utilized custom `CurveFitting` class with skeleton as below:

```python
class CurveFitting:
  def __init__(self, order: int,
  def calc_coeff(self) -> None:
  def calc_plot_1st(self) -> None:
  def calc_plot_2nd(self) -> None:
  def calc_plot_3rd(self) -> None:
  def draw_plot(self) -> None:
  def process(self) -> None:

def main() -> int:
```

_Encapsulation keeps things clean and reusable._
_Plus, we'll impress our coworkers with phrases like "modular polynomial architecture"._

#### Example Curve Fitting

> Statistically speaking, this is where the magic happens.

For example let's try the third series ys₃,
with polyfit of second order polynomial:

```python
  ys3 = [ 5, 14, 41, 98, 197, 350, 569,
    866, 1253, 1742, 2345, 3074, 3941]
```

Which gives us the result as below coefficient:

```output
Using polyfit
Coefficients (a, b, c):
        [ 137. -162.   39.]
```

We get the quadratic equation .
A bold, expressive curve that fits our data like a glove made of quadratic velvet.

$$
y = 137 - 162x + 39x^2
$$

Let's get the visual confirmation from ys₃ data series.



This isn't just number-crunching. It's pattern-finding.
Whether we're modeling sales trends, rocket trajectories,
or rice prices at south Jakarta,
curve fitting reveals the underlying shape of our data.

-- -- --

### 4: Comparing Plot

> Why choose one curve when you can have them all?

Sometimes, choosing just one model feels like picking a favorite child.
Impossible and politically dangerous.
So why not plot everything and let the visuals
speak louder than our analysis?

Here's how we throw all our polynomial fits,
into one glorious plot for easy comparation.

* **17-polyfit-merge.py**

```python
import numpy as np
import matplotlib.pyplot as plt

from typing import List

class CurveFitting:
  def __init__(self, xs, ys : List[int]) -> None:

    # Given data
    self.xs = np.array(xs)
    self.ys = np.array(ys)

  def calc_coeff(self, order) -> np.ndarray:
    # Perform regression using polyfit,
    mC = np.polyfit(self.xs, self.ys, deg=order)

    # Display
    coeff_text = {
      1: '(a, b)', 2: '(a, b, c)', 3: '(a, b, c, d)'}

    print('Using polyfit')
    print(f'Coefficients {coeff_text[order]}:'
      + f'\n\t{np.flip(mC)}\n')

    # Get coefficient matrix
    return np.flip(mC)

  def calc_plot_all(self) -> None:
    self.x_plot = xp = np.linspace(
      min(self.xs), max(self.xs), 100)

    [a1, b1] = self.mCoeff_1st
    self.y1_plot = a1 + b1 * xp

    [a2, b2, c2] = self.mCoeff_2nd
    self.y2_plot = a2 + b2 * xp + c2 * xp**2

    [a3, b3, c3, d3] = self.mCoeff_3rd
    self.y3_plot = a3 + b3 * xp + c3 * xp**2 + d3 * xp**3

  def draw_plot(self) -> None:
    plt.scatter(self.xs, self.ys, color='teal',
      label='Data points', )
    plt.plot(self.x_plot, self.y1_plot, color='red',
      label='Linear Equation')
    plt.plot(self.x_plot, self.y2_plot, color='green',
      label='Fitted second-order polynomial')
    plt.plot(self.x_plot, self.y3_plot, color='blue',
      label='Fitted third-order polynomial')

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Polynomial Curve Fitting')

    plt.show()

  def process(self) -> None:
    self.mCoeff_1st = self.calc_coeff(1)
    self.mCoeff_2nd = self.calc_coeff(2)
    self.mCoeff_3rd = self.calc_coeff(3)

    self.calc_plot_all()
    self.draw_plot()

def main() -> int:
  xs = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  ys1 = [ 5, 9, 13, 17, 21, 25, 29,
    33, 37, 41, 45, 49, 53]
  ys2 = [ 5, 12, 25, 44, 69, 100, 137,
    180, 229, 284, 345, 412, 485]
  ys3 = [ 5, 14, 41, 98, 197, 350, 569,
    866, 1253, 1742, 2345, 3074, 3941]

  example = CurveFitting(xs, ys3)
  example.process()
  
  return 0

if __name__ == "__main__":
  raise SystemExit(main())
```

#### Data Series

> tale of three ys: The Linear, the Parabolic, and the Polynomial That Went Too Far.

We're working with three pre-cooked series.
You may choose `ys₁`, `ys₂`, or `ys₃`:

* **series.csv**

```csv
xs, ys1, ys2, ys3
0,  5,   5,   5
1,  9,   12,  14
2,  13,  25,  41
3,  17,  44,  98
4,  21,  69,  197
5,  25,  100, 350
6,  29,  137, 569
7,  33,  180, 866
8,  37,  229, 1253
9,  41,  284, 1742
10, 45,  345, 2345
11, 49,  412, 3074
12, 53,  485, 3941
```

Comparing all three helps us see which model best matches reality.
Or at least fakes it convincingly.

#### Code Logic

> Polyfit Party

We manage the main method.
We start with the `main()`,
store array in `numpy`.

We read the CSV, transpose it (because numpy likes it that way),
and run our custom CurveFitting class using one of the series.
Say, `ys₃` for maximum curve drama.

```python
def main() -> int:
  # Getting Matrix Values
  mCSV = np.genfromtxt("series.csv",
    skip_header=1, delimiter=",", dtype=float)
  mCSVt   = np.transpose(mCSV)

  example = CurveFitting(mCSVt[0], mCSVt[3])
  example.process()
  
  return 0
```

Let's say that we pick `ys₃`,
then we choose `mCSVt[3]` as curve fitting parameter.

#### Class Skeleton

Let's peek into the skeleton of our `CurveFitting` class.
Think of it as the statistical wardrobe,
where all our polynomial fits hang out,
neatly labeled and ready to go.

```python
class CurveFitting:
  def __init__(self, xs, ys : List[int]) -> None:
  def calc_coeff(self, order) -> np.ndarray:
  def calc_plot_all(self) -> None:
  def draw_plot(self) -> None:
  def process(self) -> None:

def main() -> int:
```

The link to the source code is given above.



A clear class structure means our code won't descend
into chaos when degrees of polynomials start multiplying like rabbits.

#### Class

> Setting Up the Stats Lab

Our class kicks off with some basic data preparation.
Turning our poor, innocent lists into mighty numpy arrays.

```python
class CurveFitting:
  def __init__(self, xs, ys : List[int]) -> None:

    # Given data
    self.xs = np.array(xs)
    self.ys = np.array(ys)
```

_Converting to numpy arrays enables fast numerical operations._
_Iterating with plain lists is so last century_.

#### Calculate Coefficient

> The Shape of Things to Come

Time to fit our equations!
We use `np.polyfit` to find the best-fitting coefficients
for 1st, 2nd, and 3rd-degree polynomials.
Or, as statisticians call them: the polite, the dramatic,\
and the "are you sure this isn't overfitting?"

Why it matters: 

```python
  def calc_coeff(self, order) -> np.ndarray:
    # Perform regression using polyfit,
    mC = np.polyfit(self.xs, self.ys, deg=order)

    # Display
    coeff_text = {
      1: '(a, b)', 2: '(a, b, c)', 3: '(a, b, c, d)'}
    order_text = {
      1: 'Linear',  2: 'Quadratic ', 3: 'Cubic'}

    print(f'Using polyfit : {order_text[order]}')
    print(f'Coefficients  : {coeff_text[order]}:'
      + f'\n\t{np.flip(mC)}\n')

    # Get coefficient matrix
    return np.flip(mC)
```

Fitting curves lets us model trends, make predictions,
and impress friends at data parties.

Get all the coefficient:

```python
  def process(self) -> None:
    self.mCoeff_1st = self.calc_coeff(1)
    self.mCoeff_2nd = self.calc_coeff(2)
    self.mCoeff_3rd = self.calc_coeff(3)
```



With the coefficient result as:

```output
❯ python 17-polyfit-merge.py
Using polyfit : Linear
Coefficients  : (a, b):
	[-721.  306.]

Using polyfit : Quadratic 
Coefficients  : (a, b, c):
	[ 137. -162.   39.]

Using polyfit : Cubic
Coefficients  : (a, b, c, d):
	[5. 4. 3. 2.]
```



Now we have all the equations:

$$
\begin{align*}
y_1 &= -721 - 306x \\
y_2 &= 137 - 162x + 39x^2 \\
y_3 &= 5 - 4x + 3x^2 + 2x^3
\end{align*}
$$

_A linear model walks into a bar._
_The bartender says, "We don't serve your kind."_
_The model replies, "That's OK, I'm just passing through."_

#### Calculate All the Plot Values

> Drawing Data Like a Pro

Armed with coefficients,
we can now compute our predicted values.
This is the part where theory meets pixels.
With that coefficient above,
we can calculate all the `x_plot` and `y_plot` values.

```python
  def calc_plot_all(self) -> None:
    self.x_plot = xp = np.linspace(
      min(self.xs), max(self.xs), 100)

    [a1, b1] = self.mCoeff_1st
    self.y1_plot = a1 + b1 * xp

    [a2, b2, c2] = self.mCoeff_2nd
    self.y2_plot = a2 + b2 * xp + c2 * xp**2

    [a3, b3, c3, d3] = self.mCoeff_3rd
    self.y3_plot = a3 + b3 * xp + c3 * xp**2 + d3 * xp**3
```

Or better, without flipping the mC,
just use the `polyval`.

Also, for the lazy but efficient (i.e. every good data scientist),
`np.polyval` saves us from having to write out the full equation manually.
Less typing, more plotting.

```python
  def calc_plot_all(self) -> None:
    self.x_plot = xp = np.linspace(
      min(self.xs), max(self.xs), 100)

    self.y1_plot = np.polyval(self.calc_coeff(1), xp)
    self.y2_plot = np.polyval(self.calc_coeff(2), xp)
    self.y3_plot = np.polyval(self.calc_coeff(3), xp)
```

Plotting without computing is like trying to draw a sine wave from memory.
You'll end up with something that looks more like spaghetti than science.

#### Draw Plot

> From Math to Masterpiece

Raw numbers are great, but visualizing the fit
helps us (and our audience) see the story behind the data.

Now we bring it all together in one glorious matplotlib plot.
Scatter the real data, paint the fitted curves, and voilà: statistical art.
Let's plot all the different `y_plot` series in one `plt` object.

```python
  def draw_plot(self) -> None:
    plt.scatter(self.xs, self.ys, label='Data points', color='teal')
    plt.plot(self.x_plot, self.y1_plot, color='red',
      label='Linear Equation')
    plt.plot(self.x_plot, self.y2_plot, color='green',
      label='Fitted second-order polynomial')
    plt.plot(self.x_plot, self.y3_plot, color='blue',
      label='Fitted third-order polynomial')

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Polynomial Curve Fitting')

    plt.show()
```

Use different colors.
Even statisticians deserve a little joy.



A good plot is worth a thousand equations.
Chance are, our professor won't read your regression output,
if our plot already tells the story.

#### Execute Process

> Final Act of Curve Theatre

The `process()` method is our conductor.
Orchestrating coefficient calculation, plot preparation,
and the final rendering of all curves.
It's like conducting Beethoven or Gamelan,
but with more `numpy`.

```python
  def process(self) -> None:
    self.mCoeff_1st = self.calc_coeff(1)
    self.mCoeff_2nd = self.calc_coeff(2)
    self.mCoeff_3rd = self.calc_coeff(3)

    self.calc_plot_all()
    self.draw_plot()
```

Behold the curve-fitting magic in action.

_Keeping our workflow in one place makes the logic clear,_
_reproducible, and less likely to cause future-us,_
_a mental breakdown._

#### Polynomial Library

> Curve Fitting, Now with Extra Fancy

Tired of the same old `polyfit`?
Spice it up with `Polynomial.fit`,
the modern twist that brings style (and stability)
to our regression.

And why not throw in Seaborn styling,
while we're at it?
Even equations deserve to be pretty.

```python
    def calc_plot_all(self) -> None:
        self.x_plot = xp = np.linspace(
            min(self.xs), max(self.xs), 100)

        # Calculate coefficients directly
        self.y1_plot = Polynomial.fit(self.xs, self.ys, deg=1)(xp)
        self.y2_plot = Polynomial.fit(self.xs, self.ys, deg=2)(xp)
        self.y3_plot = Polynomial.fit(self.xs, self.ys, deg=3)(xp)
```

Plot result? Identical. But cooler. Statistically approved.



Get the polished Jupyter notebook here.
And may your R²s always be close to 1.

* **18-polynomial.py**

```python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from numpy.polynomial import Polynomial
from typing import List

class CurveFitting:
    def __init__(self, xs, ys : List[int]) -> None:
        # Given data
        self.xs = np.array(xs)
        self.ys = np.array(ys)

        # Display
        self.coeff_text = {
            1: '(a, b)', 2: '(a, b, c)', 3: '(a, b, c, d)'}
        self.order_text = {
            1: 'Linear',  2: 'Quadratic ', 3: 'Cubic'}

        # Seaborn styling setup
        sns.set_theme(style="whitegrid")
        self.colors = sns.color_palette("husl", 4)

    def print_props(self, order) -> np.ndarray:  
        # Perform regression using polyfit,
        poly = Polynomial.fit(self.xs, self.ys, deg=order)

        # Convert to standard form and get coefficients
        mC = poly.convert().coef

        print(f'Using Polynomial.fit : {self.order_text[order]}')
        print(f'Coefficients  : {self.coeff_text[order]}:'
            + f'\n\t{mC}\n')

    def calc_plot_all(self) -> None:
        self.x_plot = xp = np.linspace(
            min(self.xs), max(self.xs), 100)

        # Calculate coefficients directly
        self.y1_plot = Polynomial.fit(self.xs, self.ys, deg=1)(xp)
        self.y2_plot = Polynomial.fit(self.xs, self.ys, deg=2)(xp)
        self.y3_plot = Polynomial.fit(self.xs, self.ys, deg=3)(xp)

    def draw_plot(self) -> None:
        plt.figure(figsize=(10, 6))
        
        # Scatter plot with Seaborn color
        sns.scatterplot(
            x=self.xs, y=self.ys, color=self.colors[0], 
            s=100, label='Data points', edgecolor='w', linewidth=0.5)
        
        # Polynomial curves with Seaborn colors
        plt.plot(self.x_plot, self.y1_plot, color=self.colors[1], 
                linewidth=2.5, label='Linear fit')
        plt.plot(self.x_plot, self.y2_plot, color=self.colors[2], 
                linewidth=2.5, label='Quadratic fit')
        plt.plot(self.x_plot, self.y3_plot, color=self.colors[3], 
                linewidth=2.5, label='Cubic fit')

        # Styling
        plt.title('Polynomial Curve Fitting', pad=20)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        
        # Legend and grid
        plt.legend(fontsize=10, framealpha=0.9)

        plt.tight_layout()
        plt.show()

    def process(self) -> None:
        self.calc_plot_all()
        self.draw_plot()

        for order in [1, 2, 3]:
            self.print_props(order)

def main() -> int:
    # Getting Matrix Values
    mCSV = np.genfromtxt("series.csv",
      skip_header=1, delimiter=",", dtype=float)
    mCSVt   = np.transpose(mCSV)

    example = CurveFitting(mCSVt[0], mCSVt[3])
    example.process()

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

_Using newer libraries helps write more concise, readable code._
_And makes our GitHub repo look like it's from this decade._

-- -- --

### What's the Next Exciting Step 🤔?

Fitting a curve is like getting a tailored suit.
It looks great, but it doesn't tell you how the tailor did it.
If we want to build real understanding
(and maybe even brag at math parties),
we need to look under the hood.

Okay, so we've been talking about curves, models, math, and code.
And if you're wondering whether this is turning into a full-blown math lecture... 
You're not wrong. But hang in there.
It's about to get even nerdier, and that's a good thing!

Now that we've explored built-in formulas and fitting methods
(thank you, `numpy.polyfit` and friends), it's time to up the ante.

So what's next?
We'll be diving into solving equations.
Not just any equations, but the kind that show up when you actually try to construct those curves yourself:

* A system of linear equations
  (our classic y = mx + b gang),

* Then things escalate to quadratic and cubic systems
  (yes, bring our imaginary friends, roots, that is).

> Ready for the next leap?

Continue your journey with:
**Trend - Polynomial Interpolation**.

Let's go from following the curve to building it from scratch.
And who knows, we might start enjoying solving systems of equations.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Connect the dots perfectly with interpolation.

So far, we've seen curve fitting,
the art of finding a line that kind of fits the data.
But what if you're a perfectionist?
What if "close enough" makes your inner statistician twitch?

Enter **interpolation**: instead of approximating the data,
we draw a curve that passes exactly through all given points.
No curve gets left behind.

Interpolation is our go-to when we cannot afford to guess.
Like reconstructing sensor readings, pricing points in finance,
or trying to explain to our boss why our data model doesn't miss a single dot.

#### Polynomial Interpolation

> Interpolation ≠ Curve Fitting

Curve fitting is not the only target that you want to achieve.
We might just want to connect the dots perfectly.
This is called interpolation.

Unlike curve fitting, interpolation require the curve to pass through all the given data points.
We can use polynomial method to connect a few data points.
This method use minimal required point to calculate the equation for example:

1. Two points for linear equation.
2. Three points for quadratic equation.
3. Four points for cubic equation.

$$
\begin{aligned}
& \scriptstyle \text{1st order} && y = a + b{x} \\
& \scriptstyle \text{2nd order} && y = a + b{x} + c{x}^2 \\
& \scriptstyle \text{3rd order} && y = a + b{x} + c{x}^2 + d{x}^3 \\
& && \scriptstyle \text{(Order = polynomial degree, letters = coefficients)}
\end{aligned}
$$

If you're just connecting two points,
you don't even need a polynomial.
Just calculate the slope.
It's the statistical equivalent of,
using a butter knife instead of a chainsaw.

#### Piecewise

Please note that when conducting
interpolation in practical applications,
curve fitting isn't the sole method available.
There are also the option to utilize multiple straight lines,
connecting points from one to another,
without necessitating of curve fitting at all.

Interpolation insists on perfection,
while curve fitting allows for a little statistical flexibility
(i.e., it's okay to be "a bit off" sometimes, just like real life).
You can also use a piecewise approach.
connect the dots with straight lines.
It's low effort, but still respectable.
Like wearing sweatpants to a Zoom meeting.

#### Worksheet Source

> Playsheet Artefact

Although this sounds fancy.
It's really just a handy spreadsheet.



Need options?
We've got options.
Jump between sheets like a data ninja,
and choose the one that works best for your problem:



And yes, you can download the whole file,
tweak it, break it, or build your own polynomial empire:

* **github.com/.../math/trend/10-curve-fitting.xlsx**

This isn't just theory.
You'll get your hands dirty (in Excel).
The workbook is packed with sheets for various interpolation techniques,
including matrix-based polynomial solving.

-- -- --

### 1: Straight Line from Two Points

> Calculating Slope

If you only need to connect two data points,
skip the high-drama polynomial gymnastics.
Just use the humble, glorious straight line.
It's fast, and accurate.
You should use simple method instead of the complex one.
Stay away from polynomial method, and just use this slope equation.

_When you've only got two points to worry about, don't bring a bazooka to a dart game._

#### Visualization

> The Classic "Two-Dot Problem"

We've got two points,
and our goal is to predict what lies between them.
(Think of it as statistically dignified guesswork.)



#### The Math Behind It

> Fear Not

The equation of linear trend for straight line is,
as friendly as math gets:

$$
y = mx + a
$$

Where:

* `m` is the slope
  (how steep the line is),

* `a` is the intercept
  (where the line crosses the y-axis).

To calculate the slope we take the difference for both y and x, then divide.

$$
m = \frac{{\Delta y}}{{\Delta x}}
$$

For two points, the slope become `y2-y1`, and `x2-x1`.

$$
m = \frac{{y_2 - y_1}}{{x_2 - x_1}}
$$

Then we plug that slope into the formula to find the `a` variable.

$$
a = y_1 - mx_1
$$

_Slope-based interpolation is the Swiss army knife of modeling._
_It's lightweight, perfect for quick predictions,_
_and easily done in your head (or Excel)._

#### Other Equation Forms

> Different Ways to Say the Same Thing

Textbooks and papers like to change outfits.

The variable names above is named as:

$$
y = a + bx
$$

* `m`: slope, and
* `a`: intercept.

The notation can be different from book to book.
But they have the same meaning.
Such this below example:

$$
y = b + mx
$$

The standard notation for statistics is sound intimidating,
with the cryptic form as below,
for curve fitting with many samples data.

$$
y_i = \bar{\beta}_0 + \bar{\beta}_1 x_i
$$

They are all serve simple straight lines.

#### Getting Coefficient

>  In Practice

Supposed you have two pairs of point

* `p1` = (11, 49), and
* `p2` = (12, 53)

Throw them into a spreadsheet (or calculate manually if you're feeling bold):



We'll find the coefficient as

* `m` = 5, and
* `a` = 4

Our line is now:

$$
y = 4x + 5
$$

Simple. Elegant. Statistically satisfying.

#### Predicting Values

Now that you have your equation,
try interpolating values for example [x=0, x=5, x=12]



This will get this pairs of point:

* (`x` = 0, `y` = 5),
* (`x` = 5, `y` = 25),
* (`x` = 12, `y` = 53),

And so on.

And just like that, we're doing predictive modeling.
With two points and some good old-fashioned algebra.

-- -- --

### Polynomial Interpolation: Linear

> Minimum Two Points

When you only have two points to connect,
you could use slope-intercept form.
Sure. But if you're feeling a bit extra,
you can go full matrix mode.

#### Matrix Equation

> Getting unknown Coefficient value

Let's say you want to connect these two noble data points:

$$
\begin{align*}
p_0 &= (x_0, y_0) &= (11, 49) \\
p_1 &= (x_1, y_1) &= (12, 53) \\
\end{align*}
$$

Instead of calculating slope and intercept the classic way,
let's dress it up in a matrix suit.
A system of linear equations can be represented as a matrix equation.

$$
\begin{array}{cc}
\begin{bmatrix}
    y_0 \\
    y_1 \\
\end{bmatrix}
=
\begin{bmatrix}
    1 & x_0 \\
    1 & x_1 \\
\end{bmatrix}
\begin{bmatrix}
    a \\
    b \\
\end{bmatrix}
& \Rightarrow &
\begin{bmatrix}
    49 \\
    53 \\
\end{bmatrix}
=
\begin{bmatrix}
    1 & 11 \\
    1 & 12 \\
\end{bmatrix}
\begin{bmatrix}
    a \\
    b \\
\end{bmatrix}
\end{array}
$$

This matrix can be represented as variable below:

$$
A\mathbf{C} = \mathbf{B}
$$

#### Solving the Coefficients

We are going to solve the formula above using this equation

$$
\begin{aligned}
              && A \times \mathbf{C} &= \mathbf{B} \\
  \Rightarrow && \mathbf{C}  &= A^{-1}  \times \mathbf{B} \\
\end{aligned}
$$

_Matrix form generalizes nicely._
_Add more points, and it still works._
_It's basically the scalable, professional version of solving for `y`._

In Excel/Calc, we can calculate the inverse of matrix A.
Let's turn this into a matrix using `MINVERSE` formula.
When in doubt, pivot to linear algebra:

$$
A^{-1} =
\begin{bmatrix}
    12 & -11 \\
    -1 & 1 \\
\end{bmatrix}
$$

And solve this matrix equation and get below coefficient result:

$$
\mathbf{C} = A^{-1} \times \mathbf{B} =
\begin{bmatrix}
    5 \\
    4 \\
\end{bmatrix}
$$

In case you're wondering,
here's the gritty detail:

$$
\begin{aligned}
\begin{bmatrix}
    12 & -11 \\
    -1 & 1 \\
\end{bmatrix}
\times
\begin{bmatrix}
    49 \\
    53 \\
\end{bmatrix}
&=
\begin{bmatrix}
    12\times49 - 11\times53 \\
    -1\times49 + 1\times53 \\
\end{bmatrix} \\
&=
\begin{bmatrix}
    588 - 583 \\
    -49 + 53 \\
\end{bmatrix} \\
&=
\begin{bmatrix}
    5 \\
    4 \\
\end{bmatrix}
\end{aligned}
$$

With coefficient above we can write the linear equation as below:

$$
y = 5 + 4x
$$

A beautiful, linear masterpiece, brought to you by matrices.

_The Matrix Has You_

#### Worksheet

> Getting unknown Y-Value

_Jerry Maguire said: Show Me the Spreadsheet!_

Here's how we'd set it up in Excel.
Write down the equation as below, to get the coefficient:



Use the formula:

```excel
=MMULT(MINVERSE(E9:F10);J9:J10)
```

Now we can easily get the predicted value using interpolation above,
by applying it to new `x` values and start predicting like a regression wizard:



_Whether you're coding, calculating by hand, or using spreadsheets,_
_this method scales beautifully into quadratic, cubic, and higher-order interpolation. _

-- -- --

### Polynomial Interpolation: Quadratic

> Minimum Three Points

So you've conquered the straight line. Bravo!
But what if life isn't linear? (Spoiler: It usually isn't.)
That's where quadratic interpolation comes in:
the elegant art of connecting three points with a single curve,
that says, "_Yes, I pass through all of you._"

With the same method as linear equation,
we can do the the quadratic equation.

#### Visualization

Here's the scenario: three points, one mission.
To predict the rest.



#### Matrix Equation

> Getting unknown Coefficient value

We're given three precious data points:

$$
\begin{align*}
p_0 &= (x_0, y_0) &= (10, 345) \\
p_1 &= (x_1, y_1) &= (11, 412) \\
p_2 &= (x_2, y_2) &= (12, 485) \\
\end{align*}
$$

Let's turn this into a matrix.
Because, as any statistician will tell you,
when in doubt, pivot to linear algebra:
A system of quadratic equations
can also be represented as a matrix equation

$$
\begin{array}{cc}
\begin{bmatrix}
    y_0 \\
    y_1 \\
    y_2 \\
\end{bmatrix}
=
\begin{bmatrix}
    1 & x_0 & {x_0}^2 \\
    1 & x_1 & {x_1}^2 \\
    1 & x_2 & {x_2}^2 \\
\end{bmatrix}
\begin{bmatrix}
    a \\
    b \\
    c \\
\end{bmatrix}
& \Rightarrow &
\begin{bmatrix}
    345 \\
    412 \\
    485 \\
\end{bmatrix}
=
\begin{bmatrix}
    1 & 10 & 100 \\
    1 & 11 & 121 \\
    1 & 12 & 144 \\
\end{bmatrix}
\begin{bmatrix}
    a \\
    b \\
    c \\
\end{bmatrix}
\end{array}
$$

Quadratic interpolation gives you curvature.
It's great for modeling real-world trends like growth,
decay, or the mood swings of your coffee consumption.

#### Solving the Coefficients

We are going to solve the formula above using this equation

$$
\begin{aligned}
              && A\mathbf{C} &= \mathbf{B} \\
  \Rightarrow && \mathbf{C}  &= A^{-1} \mathbf{B} \\
\end{aligned}
$$

We can use spreadsheet using `MINVERSE` formula.
Break out Excel and plug in that matrix.
Here's the inverse matrix:

$$
A^{-1} =
\begin{bmatrix}
    66    & -20 &  55 \\
    -11.5 &  22 & -10.5 \\
      0.5 &  -1 &   0.5 \\
\end{bmatrix}
$$

Solve this matrix equation by multiply it by the output vector,
to reveal below coefficient result:

$$
\mathbf{C} = A^{-1} \mathbf{B} =
\begin{bmatrix}
    5 \\
    4 \\
    3 \\
\end{bmatrix}
$$

Which means we now have our equation:

$$
y = 5 + 4x + 3x^2
$$

#### Worksheet

> Getting unknown Y-Value

Here's how it looks in the spreadsheet realm:



Just plug in this magical incantation:

```excel
=MMULT(MINVERSE(E9:G11);K9:K11)
```

And voilà, predictions pour in like coffee on a Monday.
We can easily get the predicted value using interpolation above.



-- -- --

### Polynomial Interpolation: Cubic

> Minimum Four Points

Congratulations!
You've made it past linear and quadratic interpolation.
Now it's time for cubic.

#### Visualization

You've got four points. You want a curve.
Not just any curve, but one that hugs all your data like a well-fit model should.



Real-world data often bends.
Think population growth, depreciation curves,
or coffee consumption over deadlines.
Cubic interpolation gives you that sweet third-degree bend.

#### Matrix Equation

> Getting unknown Coefficient value

Let's connect four points with a cubic equation.
That's just enough info to model a curve with a twist.
Here's our cast of data:

$$
\begin{align*}
p_0 &= (x_0, y_0) &= &(9, 1742) \\
p_1 &= (x_1, y_1) &= &(10, 2345) \\
p_2 &= (x_2, y_2) &= &(11, 3074) \\
p_3 &= (x_3, y_3) &= &(12, 3941) \\
\end{align*}
$$

Let's express this using matrix form.
A system of cubic equations can be represented as a matrix equation

$$
\begin{array}{cc}
&
\begin{bmatrix}
    y_0 \\
    y_1 \\
    y_2 \\
    y_3 \\
\end{bmatrix}
=
\begin{bmatrix}
    1 & x_0 & {x_0}^2 & {x_0}^3 \\
    1 & x_1 & {x_1}^2 & {x_0}^3 \\
    1 & x_2 & {x_2}^2 & {x_0}^3 \\
    1 & x_3 & {x_3}^2 & {x_0}^3 \\
\end{bmatrix}
\begin{bmatrix}
    a \\
    b \\
    c \\
    d \\
\end{bmatrix} \\
\Rightarrow &
\begin{bmatrix}
    1742 \\
    2345 \\
    3074 \\
    3941 \\
\end{bmatrix}
=
\begin{bmatrix}
    1 &  9 &  81 &  729 \\
    1 & 10 & 100 & 1000 \\
    1 & 11 & 121 & 1331 \\
    1 & 12 & 144 & 1728 \\
\end{bmatrix}
\begin{bmatrix}
    a \\
    b \\
    c \\
    d \\
\end{bmatrix}
\end{array}
$$

Notice how that third column escalates things quickly.
Welcome to the power of cubes.

#### Solving the Coefficients

Time to solve it like a boss.
This matrix also can be represented as variable.
Again, we are going to solve the formula above using this equation

$$
\begin{aligned}
              && A\mathbf{C} &= \mathbf{B} \\
  \Rightarrow && \mathbf{C}  &= A^{-1} \mathbf{B} \\
\end{aligned}
$$

Yep, you can still use Excel like a total matrix whisperer with `MINVERSE`.
to solve this matrix equation and get coefficient result.
Here's below what we get:

$$
\mathbf{C} = A^{-1} \mathbf{B} =
\begin{bmatrix}
    5 \\
    4 \\
    3 \\
    2 \\
\end{bmatrix}
$$

And this coefficient above  gives us our mighty cubic equation:

$$
y = 5 + 4x + 3x^2 + 2x^3
$$

More coefficients mean more flexibility.
But beware, like a third espresso, cubic power is potent.
Great for smooth curves. Terrible for noisy overfits.

#### Worksheet

> Getting unknown Y-Value

With spreadsheet, we can write down the equation,
as below to get the coefficient:



Your Excel/Calc formula incantation:

```excel
=MMULT(MINVERSE(E9:H12);L9:L12)
```

From here, calculating predictions is a breeze. Or at least a gentle curve.
Now we can easily get the predicted value using interpolation above.



Just because we can fit a higher-order polynomial doesn't mean we should.
Use cubic with care. It's powerful, but a bad fit will bend the truth,
faster than a misquoted correlation.

So what's next? quartic? quintic?
Maybe we should stop before we enter overfitting territory.

-- -- --

### What's Our Next Endeavor 🤔?

> Real-world scenario

Where do we go after fitting a curve through perfection?
Answer: _Real life, where data is messy and points don't always hold hands._

So far, we've been living in a mathematical utopia.
Where points align, curves obey, and interpolations are smooth
as your favorite regression line.
But now... things get real. 😅

Welcome to the next step: **Polynomial curve fitting**.
Instead of demanding a perfect fit through every point
(because life is rarely that cooperative),
we fit a curve that approximates the trend,
through noisy, scattered, and very human data.

In real-world scenarios, whether it's predicting sales, climate trends,
or how many gorengan (or doughnuts) our team consumes before 10 AM
perfect fits are rare.
Curve fitting lets us model the general pattern,
without sweating the small stuff (or the outliers).

> Algebra with a Twist

The structure is the same as before, matrix equations, inverse operations,
and just the right sprinkle of Excel wizardry.
But instead of connecting exactly through every point,
we use more points than the polynomial's degree and solve for a best-fit curve.

And yes, we still use the same `polyfit` (or build it manually using matrix magic),
only now we let it do what statisticians love best: minimize errors like a boss.

Ready to move from interpolation to fitting? 
Then brace ourself, polish our matrix skills, and head over to:
**Trend - Polynomial Algebra**.

It's like interpolation,
but with lower expectations and better coffee.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Understanding how the polynmial internally works.
  Gently explanation from each form to generalization.

To ease you into the world of equations,
here's a visual roadmap of where we're heading
that outlines the flow of polynomial calculations:



Don't worry about the equations.
Ignore the symbols for now,
unless you're fluent in Matrices. 
I will start gently, step by step.
We'll walk through it all.
No calculus-induced trauma required.

_Don't panic. This is math, not a mystery novel._

-- -- --

### 1: Equation Breakdown

> So, you're still here? Excellent.

That means you're either really into math,
or you're procrastinating on something else.

Now for the curious.
Let's peel back the curtain and look at the structure behind polynomial regression.
Think of this as opening the hood of your regression model.
Sure, it runs, but don't you want to know why it runs?

We'll eventually tie this into how Excel and Python handle polynomial fitting.
For now, let's admire some good old-fashioned matrix wizardry.

Let's have a look again to this equation.
We are going to connect polynomial equation to regression equation later.

$$
\begin{aligned}
              &&    A \cdot \mathbf{C} &= \mathbf{B} \\
  \Rightarrow &&    A^\top \cdot A \cdot \mathbf{C} &= A^\top \cdot \mathbf{B} \\
  \Rightarrow &&    \mathbf{C}  &= (A^\top A)^{-1} \cdot (A^\top \mathbf{B})
\end{aligned}
$$

This is the canonical form of least squares regression. 
Then what is this (Aᵗ x A) x C = Aᵗ x B looks like in the matrix?
We are going to show the gram matrix (Aᵗ.A) of the system.

This equation helps us find the regression coefficients,
that **minimize the sum of squared errors**.
The holy grail of fitting.

#### Linear Regression

Let's start with the first polynomial boss: the line.

1. Generic Matrix

$$
A
=
\begin{bmatrix}
1 & x_1 \\
1 & x_2 \\
1 & x_3 \\
\vdots & \vdots \\
1 & x_n \\
\end{bmatrix}
$$

This matrix A is what we call a design matrix.
Yes, statisticians get to "_design_" things too.
Mostly equations and sleep schedules.

2. Normal Equation

$$
\begin{aligned}
  (\mathbf{A}^T \cdot \mathbf{A}) \cdot 
  \begin{bmatrix}
    a \\
    b \\
  \end{bmatrix}
  = \mathbf{A}^T \cdot \mathbf{B}
\end{aligned}
$$

3. Expanded

   * This equation relate to least square.
   * Now you have alternative way to simplify the matrix calculation in Excel.

$$
\begin{bmatrix}
n & \sum x_i \\
\sum x_i & \sum x_i^2
\end{bmatrix}
\begin{bmatrix}
a \\
b
\end{bmatrix}
=
\begin{bmatrix}
\sum y_i \\
\sum x_i y_i
\end{bmatrix}
$$

This gives us a system of two equations in two unknowns.
Very solvable. Very spreadsheet-friendly.

4. Inverse (Aᵗ.A)ˉ¹

   * We can cheat the computation for the inverse using this formula.

$$
(A^T A)^{-1} =
\frac{1}{n \sum x_i^2 - (\sum x_i)^2}
\begin{bmatrix}
\sum x_i^2 & -\sum x_i \\
-\sum x_i & n
\end{bmatrix}
$$

No regression article is complete without the classic "look, Ma, I inverted a matrix" moment.
Butctually, the inverse equation is not really useful to simplify current tabular calculation,
except for curiosity purpose.
I'd rather use current excel formula or python.

While you can compute this by hand,
I recommend doing it only when your Excel crashes,
and you need to impress a statistician at a party.

#### Quadratic Regression

Welcome to degree two.
This is where our nice straight line puts on a little flair.

1. Generic Matrix

$$
A
=
\begin{bmatrix}
1 & x_1 & x_1^2 \\
1 & x_2 & x_2^2 \\
1 & x_3 & x_3^2 \\
\vdots & \vdots & \vdots \\
1 & x_n & x_n^2 \\
\end{bmatrix}
$$

2. Normal Equation

$$
\begin{aligned}
  (\mathbf{A}^T \cdot \mathbf{A}) \cdot 
  \begin{bmatrix}
    a \\
    b \\
    c \\
  \end{bmatrix}
  = \mathbf{A}^T \cdot \mathbf{B}
\end{aligned}
$$

3. Expanded

   * Now you have alternative way to simplify the matrix calculation in Excel.

$$
\begin{bmatrix}
n & \sum x_i & \sum x_i^2 \\
\sum x_i & \sum x_i^2 & \sum x_i^3 \\
\sum x_i^2 & \sum x_i^3 & \sum x_i^4
\end{bmatrix}
\begin{bmatrix}
a \\
b \\
c
\end{bmatrix}
=
\begin{bmatrix}
\sum y_i \\
\sum x_i y_i \\
\sum x_i^2 y_i
\end{bmatrix}
$$

4. Inverse

   * No easy cheat, we need to compute.

$$
(A^T A)^{-1} =
\begin{bmatrix}
* & * & * \\
* & * & * \\
* & * & *
\end{bmatrix}
$$

No closed-form shortcut here.
Time to break out `NumPy` or let Excel's `LINEST` handle it.
Or pray. Both work.

#### Cubic Regression

Polynomials of degree three: when your line just has to loop.

1. Generic Matrix

$$
A
=
\begin{bmatrix}
1 & x_1 & x_1^2 & x_1^3 \\
1 & x_2 & x_2^2 & x_2^3 \\
1 & x_3 & x_3^2 & x_3^3 \\
\vdots & \vdots & \vdots & \vdots \\
1 & x_n & x_n^2 & x_n^3 \\
\end{bmatrix}
$$

2. Normal Equation

$$
\begin{aligned}
  (\mathbf{A}^T \cdot \mathbf{A}) \cdot 
  \begin{bmatrix}
    a \\
    b \\
    c \\
    d \\
  \end{bmatrix}
  = \mathbf{A}^T \cdot \mathbf{B}
\end{aligned}
$$

3. Expanded

   * Now you have alternative way to simplify the matrix calculation in Excel.

$$
\begin{bmatrix}
n & \sum x_i & \sum x_i^2 & \sum x_i^3 \\
\sum x_i & \sum x_i^2 & \sum x_i^3 & \sum x_i^4 \\
\sum x_i^2 & \sum x_i^3 & \sum x_i^4 & \sum x_i^5 \\
\sum x_i^3 & \sum x_i^4 & \sum x_i^5 & \sum x_i^6
\end{bmatrix}
\begin{bmatrix}
a \\
b \\
c \\
d
\end{bmatrix}
=
\begin{bmatrix}
\sum y_i \\
\sum x_i y_i \\
\sum x_i^2 y_i \\
\sum x_i^3 y_i
\end{bmatrix}
$$

4. Inverse

   * No easy cheat, we need to compute.

$$
(A^T A)^{-1} =
\begin{bmatrix}
* & * & * & * \\
* & * & * & * \\
* & * & * & * \\
* & * & * & *
\end{bmatrix}
$$

At this point, we're better off trusting the robots.
Let Python do the math, and we focus on making the plots look pretty.

#### Cheatsheet

> Vandermonde

If you remember one thing, remember this:
_polynomial regression is just linear regression in disguise_,
wearing powers of `x` like a fashionable scarf.

Finally summarized in just one table.

$$
\begin{equation*}
\scriptsize

\begin{array}{|c|c|c|}
\hline
    \textbf{Linear} & \textbf{Quadratic} & \textbf{Cubic} \\
\hline

\hline
    \mathbf{A}
    =
    \begin{bmatrix}
        1 & x_1 \\
        1 & x_2 \\
        \vdots & \vdots \\
        1 & x_n \\
    \end{bmatrix}, \,
    \mathbf{B}
    =
    \begin{bmatrix}
        y_1 \\
        y_2 \\
        \vdots \\
        y_n \\
    \end{bmatrix} &

    \mathbf{A}
    =
    \begin{bmatrix}
        1 & x_1 & x_1^2 \\
        1 & x_2 & x_2^2 \\
        \vdots & \vdots & \vdots \\
        1 & x_n & x_n^2 \\
    \end{bmatrix}, \,
    \mathbf{B}
    =
    \begin{bmatrix}
        y_1 \\
        y_2 \\
        \vdots \\
        y_n \\
    \end{bmatrix} &

    \mathbf{A}
    =
    \begin{bmatrix}
        1 & x_1 & x_1^2 & x_1^3 \\
        1 & x_2 & x_2^2 & x_2^3 \\
        \vdots & \vdots & \vdots & \vdots \\
        1 & x_n & x_n^2 & x_n^3 \\
    \end{bmatrix}, \,
    \mathbf{B}
    =
    \begin{bmatrix}
        y_1 \\
        y_2 \\
        \vdots \\
        y_n \\
    \end{bmatrix} \\
\hline

\hline
    \left(\mathbf{A}^T \mathbf{A}\right)
    \begin{bmatrix}
        a \\ b \\
    \end{bmatrix} 
    = \mathbf{A}^T \mathbf{B} &

    \left(\mathbf{A}^T \mathbf{A}\right)
    \begin{bmatrix}
        a \\ b \\ c \\
    \end{bmatrix} 
    = \mathbf{A}^T \mathbf{B} &

    \left(\mathbf{A}^T \mathbf{A}\right)
    \begin{bmatrix}
        a \\ b \\ c \\ d \\
    \end{bmatrix} 
    = \mathbf{A}^T \mathbf{B} \\
\hline

\hline
    \begin{bmatrix}
        n & \sum x_i \\
        \sum x_i & \sum x_i^2 \\
    \end{bmatrix}
    \begin{bmatrix}
        a \\ b \\
    \end{bmatrix}
    =
    \begin{bmatrix}
        \sum y_i \\
        \sum x_i y_i \\
    \end{bmatrix} &

    \begin{bmatrix}
        n & \sum x_i & \sum x_i^2 \\
        \sum x_i & \sum x_i^2 & \sum x_i^3 \\
        \sum x_i^2 & \sum x_i^3 & \sum x_i^4 \\
    \end{bmatrix}
    \begin{bmatrix}
        a \\ b \\ c \\
    \end{bmatrix}
    =
    \begin{bmatrix}
        \sum y_i \\
        \sum x_i y_i \\
        \sum x_i^2 y_i \\
    \end{bmatrix} &

    \begin{bmatrix}
        n & \sum x_i & \sum x_i^2 & \sum x_i^3 \\
        \sum x_i & \sum x_i^2 & \sum x_i^3 & \sum x_i^4 \\
        \sum x_i^2 & \sum x_i^3 & \sum x_i^4 & \sum x_i^5 \\
        \sum x_i^3 & \sum x_i^4 & \sum x_i^5 & \sum x_i^6 \\
    \end{bmatrix}
    \begin{bmatrix}
        a \\ b \\ c \\ d \\
    \end{bmatrix}
    =
    \begin{bmatrix}
        \sum y_i \\
        \sum x_i y_i \\
        \sum x_i^2 y_i \\
        \sum x_i^3 y_i \\
    \end{bmatrix} \\
\hline

\end{array}
\end{equation*}
$$

Check out the handy table above for quick reference.
If this looks intimidating, just remember,
It's all just a bunch of sums and products.
Like grocery shopping, but with less walking.

Excel, Python, R,
they all use versions of this math under the hood.
Understanding it helps us trust the output...
and debug when things go sideways.

You can see the detail in Wiki with topic of Vandermonde and Least Square.

$$
\boxed{
  \begin{array}{c}
  \text{Vandermonde-based least squares} \\
  \scriptstyle\text{(Ref: Wikipedia, 2020)}
  \end{array}
}
$$

That's all how the expanded matrix looks like.

-- -- --

### 2: Generalization

Form practical examples, we goes back to conceptual.
using standard statistical notation, to avoid confusion.

#### Statistical Notation

We've wandered through the world of polynomial fitting.
Linear, quadratic, cubic,
and now it's time to climb the final hill: generalization.
Don't worry, this is the part where everything gets suspiciously neat
and the math starts wearing a tuxedo.

Let's dress up our formulas using standard statistical notation.
Why? Because eventually someone will ask you
about "β coefficients" at a conference,
and you don't want to just smile and nod.

#### Explicit Form

This is the classic polynomial regression model.
Fancy, formal, and ready for publication.

$$
y = \beta_0 + \beta_1 x + \beta_2 x^2 + \cdots + \beta_k x^k
$$

This is the function we're trying to fit.
It's your best guess of how `x` and `y` are dancing together.
Now with choreography up to degree `k`.

#### Matrix Form

Ah, matrices. 
The universal language of statisticians and robots.

$$
    \begin{bmatrix}
        1 & x_1 & x_1^2 & \cdots & x_1^k \\
        1 & x_2 & x_2^2 & \cdots & x_2^k \\
        \vdots & \vdots & \vdots & \ddots & \vdots \\
        1 & x_n & x_n^2 & \cdots & x_n^k \\
    \end{bmatrix}
    \begin{bmatrix}
        \beta_0 \\
        \beta_1 \\
        \beta_2 \\
        \vdots \\
        \beta_k \\
    \end{bmatrix} 
    =
    \begin{bmatrix}
        y_1 \\
        y_2 \\
        \vdots \\
        y_n \\
    \end{bmatrix} \\
$$

Where 

* n: Number of observations (rows in X)
* k: Degree of the polynomial

This matrix setup allows us to plug the problem
into Excel, Python, or our favorite statistical black box,
and let the algorithms do the heavy lifting.

#### Solution

The mythical "_closed-form solution_"
that statisticians talk about at parties (yes, those exist),
where `X` is the predictor variables,
and `y` is dependent variables.

$$
\begin{aligned}
              &&    X \mathbf{\beta} &= \mathbf{y} \\
  \Rightarrow &&    X^\top X \mathbf{\beta} &= X^\top \mathbf{y} \\
  \Rightarrow &&    \mathbf{\beta} &= (X^\top X)^{-1} X^\top \mathbf{y}
\end{aligned}
$$

This is the formula behind y\our Excel `LINEST`,
our Python `np.linalg.lstsq()`,
and our professor's final exam.

#### Explicit Gram Matrix

> The matrix is always symmetric.

We can also generalized the gram matrix (Xᵗ.X).
Here's what (Xᵗ.X) looks like when you stare at it long enough.
No, it's not a magic square, though it sometimes feels like one.

$$
X^\top X = 
\begin{bmatrix}
n                        & \sum x_m       & \sum x_m^2     & \cdots & \sum x_m^k \\
\sum x_m                 & \sum x_m^2     & \sum x_m^3     & \cdots & \sum x_m^{k+1} \\
\sum x_m^2               & \sum x_m^3     & \sum x_m^4     & \cdots & \sum x_m^{k+2} \\
\vdots                   & \vdots         & \vdots         & \ddots & \vdots \\
\sum x_m^k               & \sum x_m^{k+1} & \sum x_m^{k+2} & \cdots & \sum x_m^{2k}
\end{bmatrix}
$$

Where 

* m: Index used for summation for (Xᵗ.X) entries

This matrix captures all the information needed to estimate our model.
It's symmetric, and like most symmetric things in math,
that's both beautiful and useful.

#### Inverse Gram Matrix

> Generalization? Yes. Closed-form inverse? Not so much.

We now enter the realm where algebra shrugs and hands the baton to numerical methods.
There is no simple closed-form expression for inverse gram matrix (Xᵗ.X)ˉ¹.
I accept the reality of life. And welcome using Excel computation instead.

$$
(X^\top X)^{-1}
$$

There's no simple cheat here.
Just let Excel or Python do their magic.
Actually it is pretty easy to map these equation into Excel tabular calculation.

Trying to invert a high-degree polynomial's Gram matrix by hand,
is a great way to delay finishing your thesis.
Use a computer!

#### Fit Prediction

> The theoretical model 

The theoretical truth (Unobservable), platonic ideal.
This is how the world probably works.

$$
\mathbf{y} = X \boldsymbol{\beta} + \boldsymbol{\varepsilon}
$$

Where εε is the error term.
A polite way of saying,
"_we have no clue what caused that noise._"

> The practical estimate

For Estimated Coefficients (Calculated from Data),
we minimize the residual and get the following fit:

$$
  \boldsymbol{\hat{\beta}} = (X^\top X)^{-1} X^\top \mathbf{y}
$$

This is how we estimate it from data.
This is how we go from _some dots on a chart_,
to _a model we can use to make decisions_.
This is what we pragmatically compute from noisy data.
It's the bridge from data to insight.

-- -- --

### What's Our Next Move 🤔?

> That was fun, wasn't it?

Equations, matrices, and just a pinch of existential dread.
But let's not stop at algebraic elegance.
We're here to use this stuff.

Now, it's time to translate those mathematical expressions,
into something wonderfully clicky and copy-pasteable.
Let's see how to implement these equations in a spreadsheet,
row by glorious row.

Start here: **Trend - Polynomial in Worksheet**.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Implement polynomial equation in worksheet.
> From theory to data modelling in Excel/Calc.
> Solving third order polynomial equation.

Welcome to the world where algebra meets the almighty spreadsheet.

Here, we take our polynomial equations out of their theoretical ivory tower,
and drop them right into Excel or LibreOffice Calc,
where real-world data lives (and occasionally misbehaves).

This isn't abstract math for fun.
Okay, also for fun, but it's primarily about learning,
how to actually do polynomial regression,
in the software many people already use every day. 

We'll walk through the special case of cubic equations.
Why cubic? Because it's the perfect mix of complexity and practicality.
Also, it sounds cooler than quadratic.

Tabular layout helps build intuition:
you see the powers of `x`, the sums, the coefficients.
It's like watching a matrix do interpretive dance,
surprisingly insightful.

#### Shorter

> But Wait... There's a Shortcut!

Spreadsheets have a magical formula called `LINEST`,
which can solve everything in one go.

> But we're not using it.

Why? Because the goal here is understanding,
not just button-mashing.
Plus, `LINEST` feels like cheating...
and we're classy statisticians.

Instead, we will derive the solution by hand
(well, by Excel and Python).
We are going to calculate the solution manually.
The step by step approach is 
required to get deeper understanding, of how things works.
So the next time someone casually mentions
"_least squares regression_" we will nod confidently,
and not just hope they change the subject.

#### Shifting from Interpolation

> From Interpolation to Approximation

Here's the twist, in previous articles,
we connected exact points with a polynomial (interpolation).
Now, we're entering the realm of curve fitting.
Modeling data that doesn't play nice.

The math shifts slightly,
because we now have more data points than coefficients.
So, we need a clever workaround to make our matrix solvable.

> Enter the transpose trick

The difference with previous interpolation is,
the approach of getting the matrix solution.
Since inverse can only work with square `nxn` matrix.
We need to alter the equation a bit with transpose.

$$
\begin{aligned}
              &&    A\mathbf{C}     &= \mathbf{B} \\
  \Rightarrow &&    A^T A\mathbf{C} &= A^T \mathbf{B} \\
  \Rightarrow &&    \mathbf{C}      &= (A^T A)^{-1} A^T \mathbf{B}
\end{aligned}
$$

This technique (also known as the normal equation) is,
the foundation of least squares regression,
which is the backbone of many machine learning models,
economic forecasts, and awkwardly plotted trendlines in presentations.

#### Manual Labor

> But Make It Fun

We're skipping the spreadsheet autopilot and doing things manually.
Because reverse-engineering builds true understanding.

Here's a preview of the spreadsheet we'll build:



Later, we'll recreate the same logic in Python,
not because we dislike `polyfit`,
but because we like knowing what it`s doing behind the scenes.

After all, any statistician can click a button,
but a real statistician knows why that button works.

#### Step by Step

We'll focus on a third-order polynomial
(a + bx + cx² + x³) and walk through each step methodically:

We would pick third order polynomial as a case.
Then we would explain in systematic way.

* Start with cubic equation with know coefficient,
  to produce Y-value, using spreadsheet.

* Solve the Y-Value, using spreadsheet,
  but this time with the help of matrix
  (reverse-engineer the coefficients).

* Inverse using spreadsheet,
  find the coefficient, with know Y-Value.
  (Yes, Excel can do it. No, it's not sorcery)

* Translate the entire matrix process into Python code.

We will leave this with more than just answers.
We will understand the process,
which is exactly what separates a spreadsheet user from a spreadsheet wizard.

#### Worksheet Source

> A little Excel playground for the mathematically curious.

You can grab the Excel file, explore, and even break things.
It's encouraged, in a safe, learning sort of way.

* **github.com/.../math/polynomial/basic-polynomial.xlsx**

-- -- --

### 1: Polynomial Case

> Task: Find the coefficient.

This is where math meets detective work.
We're using **numerical methods** to solve a statistical puzzle:
Find the coefficients of a cubic polynomial,
that best explains a set of known values.

#### Polynomial Expression

Let's start with the usual suspect: a third-degree (cubic) polynomial.

$$
y = a + b{x} + c{x}^2 + d{x}^3
$$

Here, `a`, `b`, `c` and `d` are the coefficients we're after.
You could say they're the polynomial's DNA.
If we know them, we know everything.

#### Known Data

In the real world, you rarely get handed perfect equations.
Instead, you're given data, and expected to find the pattern.
Our mission is to find the coeffient, based on known data.

For example, here's our mystery dataset, 13 pairs of (x, y) values:

|  X | Y-Value |
| -- | ------- |
|  0 |       5 |
|  1 |      10 |
|  2 |     410 |
|  3 |      90 |
|  4 |     190 |
|  5 |     350 |
|  6 |     460 |
|  7 |     960 |
|  8 |    1050 |
|  9 |    1740 |
| 10 |    1340 |
| 11 |    3270 |
| 12 |    3540 |

This is the kind of messiness you get in actual data science or forecasting work.
The goal is to find a polynomial model that fits the trend,
even if it doesn't hit every point.

-- -- --

### 2: Cubic Equation

Let's warm up by flipping the problem around:
What if we already know the coefficients?

| Coeff. | Value |
| ------ | ----- |
|    a   |   5   |
|    b   |   4   |
|    c   |   3   |
|    d   |   2   |

Consider reverse our task,
find the data for known coefficient.

#### Equation

Plug those in and you get the equation:

$$
y = 5 + 4{x} + 3{x}^2 + 2{x}^3
$$

For the LaTeX crowd, here's your moment of glory:

```latex
y = 5 + 4{x} + 3{x}^2 + 2{x}^3
```

#### Applying Equation

Applying equation for each pairs can be written as below:



#### Spreadsheet

Here's how we bring this math into Excel/Calc.



In the same sheet, we can also visualize the XY line,
in a tidy chart as below figure:



We've built the equation forward,
_from coefficients to values_.
Next, we'll crank things in reverse and solve,
_from values to coefficients_, using matrix methods.

Stay tuned, we're about to make Excel do linear algebra,
and live to tell the tale.

-- -- --

### 3: Matrix Equation

> Getting unknown Y-Value

Our objective is to reverse-engineer the coefficients.
Like CSI: Polynomial Edition.

Now that we've seen how a polynomial generates values,
let's flip the problem: We know the outputs (the Y-values),
and we want to deduce the equation that made them.

Time to bring in matrices,
the Swiss Army knife of numerical methods.

#### Spreadsheet Setup

Let's roll out the big guns:
a `13×4` matrix to represent our polynomial basis.



Multiply this with a `4×1` column matrix of coefficients `[a, b, c, d]`,
and voilà — you get a `13×1` column matrix of Y-values.

$$
A\mathbf{C} = \mathbf{B}
$$

Where:

* A is our Vandermonde matrix
* C is our coefficient mystery box
* B is our known Y-values



In Excel, use the `MMULT` function for matrix multiplication.
Just remember: this isn't your typical lazy formula,
it needs array calculation.
Use Ctrl+Shift+Enter to activate array mode. 
for example for this `{=MMULT(F6:I18;K6:K9)}` formula.



Now we are ready to solve our real problem.
Reverse back to unknown coefficient for known `Y-Value`.

This process forms the backbone of many modern statistical and machine learning algorithms.
From linear regression to curve fitting.
Understanding this helps you move beyond "click-and-hope" analytics.

#### Our Equation

> Vandermonde Matrix

Tthe Vandermonde Matrix sounds fancy,
but it's just powers of X arranged in rows.

Here's the mathematical form of our `13×4` matrix setup:

$$
\begin{bmatrix}
    1 & x_0 & {x_0}^2 & {x_0}^3 \\
    1 & x_1 & {x_1}^2 & {x_1}^3 \\
    1 & x_2 & {x_2}^2 & {x_2}^3 \\
    1 & x_3 & {x_3}^2 & {x_3}^3 \\
    1 & x_4 & {x_4}^2 & {x_4}^3 \\
    1 & x_5 & {x_5}^2 & {x_5}^3 \\
    1 & x_6 & {x_6}^2 & {x_6}^3 \\
    1 & x_7 & {x_7}^2 & {x_7}^3 \\
    1 & x_8 & {x_8}^2 & {x_8}^3 \\
    1 & x_9 & {x_9}^2 & {x_9}^3 \\
    1 & x_{10} & {x_{10}}^2 & {x_{10}}^3 \\
    1 & x_{11} & {x_{11}}^2 & {x_{11}}^3 \\
    1 & x_{12} & {x_{12}}^2 & {x_{12}}^3 \\
\end{bmatrix}
\begin{bmatrix}
    a \\
    b \\
    c \\
    d \\
\end{bmatrix}
=
\begin{bmatrix}
    y_0 \\
    y_1 \\
    y_2 \\
    y_3 \\
    y_4 \\
    y_5 \\
    y_6 \\
    y_7 \\
    y_8 \\
    y_9 \\
    y_{10} \\
    y_{11} \\
    y_{12} \\
\end{bmatrix}
$$

The `13x4` size matrix can be described as:
* 13 number of data.
* 4 coefficient, for third order.

For our fellow LaTeX nerds (no judgment, only respect),
you can get the equation by right click the equation above,
and copy the `TeX Commands` to clipboard from the menu.

This layout, a Vandermonde matrix,
is the foundation for polynomial regression and interpolation.
It's how machines (and humans with Excel) learn trends from raw numbers.

-- -- --

### 4: Inverse Matrix

> Getting unknown coefficient

We've assembled our matrix.
We've multiplied it, transposed it,
maybe even stared at it until it blinked first.
Now, it's time for the final boss of matrix operations: **inversion**.

Let's find those coefficients,
the statistical Rosetta Stones that connect Xₛ to Yₛ.

#### Problem Domain

Here's how our equation looks in the land of spreadsheets:



You might think this looks intense.
But to a statistician, this is just Tuesday.

#### Equation

Let's start with the basic setup.
We are going to solve the formula above using this equation

$$
\begin{aligned}
              && A\mathbf{C} &= \mathbf{B} \\
  \Rightarrow && \mathbf{C}  &= A^{-1} \mathbf{B} \\
\end{aligned}
$$

Now here's the catch: you can't invert a non-square matrix.
Trying to do that is like asking your toaster to make ice cubes,
mathematically forbidden.

Inverse can only work with square `nxn` matrix.
Since our `13x4` matrix is definitely not a square matrix.
We need to alter the equation a bit with transpose.

$$
\begin{aligned}
              &&    A\mathbf{C}     &= \mathbf{B} \\
  \Rightarrow &&    A^T A\mathbf{C} &= A^T \mathbf{B} \\
  \Rightarrow &&    \mathbf{C}      &= (A^T A)^{-1} A^T \mathbf{B}
\end{aligned}
$$

This technique is called the Normal Equation.
It's used in linear regression, machine learning, and even AI training.
It's the statistical equivalent of a Swiss watch mechanism.
Elegant, precise, and quietly powerful.

#### LaTeX

If you are curious,
the LaTeX code can be obtained by right click the equation.
A menu will be shown-up, then you can copy to clipboard.

Want to copy that juicy equation into your own LaTeX editor?
Here you go:

```latex
\begin{align*}
              &&    A\mathbf{C}     &= \mathbf{B} \\
  \Rightarrow &&    A^T A\mathbf{C} &= A^T \mathbf{B} \\
  \Rightarrow &&    \mathbf{C}      &= (A^T A)^{-1} A^T \mathbf{B}
\end{align*}
```

Or use the friendly folks at quicklatex for instant render magic.

* [quicklatex.com/](https://www.quicklatex.com/)



#### Transpose

With `transpose` formula such as: `=TRANSPOSE(E9:H21)`,
we can have the matrix transposed as below:



Suddenly, rows become columns.
It's matrix yoga.

#### Multiply Like a Pro

Again, we can cross multiply both, with `MMULT`.

You've done this before. `MMULT` is back. First, let's do:

* Aᵀ × A



* Aᵀ × B



Statisticians call this the setup for the **Normal Equation**.
Normal in name, but not in workload.

#### Inverse

To invert the matrix,
we unleash Excel's `MINVERSE` formula,
such as `{=MINVERSE(E32:H35)}`.

Curly brackets mean it's an array formula.
Yes, the ones that need Ctrl+Shift+Enter.



You can examine the excel formula here.



#### Coeffecient

Multiply the inverse matrix with Aᵀ × B using `MMULT`, and behold.
The hidden polynomial coefficients rise from the spreadsheet.



You can examine the excel formula here.



Yes, we have our result. It's official.
Our spreadsheet just did algebra.

#### Big Picture

Here's how it all connects, spreadsheet-style:



This matrix inversion trick,
especially when used with AᵀA,
is the backbone of least squares regression,
the statistical bread-and-butter of modern data analysis.
Whether you're building a machine learning model,
or fitting a curve to cat weight vs. lasagna intake,
this method is everywhere.

-- -- --

### What's Our Next Endeavor 🤔?

We've done it,
We've summoned the power of matrix algebra inside a spreadsheet.
That alone earns use nerd points redeemable in most academic circles.

But what if our data grows... and our spreadsheet crashes? 😱
That's where Python enters the scene, cape fluttering, `NumPy` blazing.

Let's take those same polynomial calculations,
and power them with less-clicking tools called Python,
more scaling, and bonus: prettier plots.

Continue here: **Trend - Polynomial in Python**.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Implement polynomial equation in python.
> From data modelling in spreadsheet to programming language.
> Solving third order polynomial equation.

Spreadsheets are great.
They've helped humanity track budgets, analyze experiments, and so on.
But when it comes to scaling our analysis,
Python steps in like a caffeinated intern with `NumPy`.

In this article, we take the cubic polynomial work,
we carefully built in a spreadsheet and translate it into a Python script.
You'll see how the matrix math maps one-to-one between Excel and code.
And you'll start to appreciate Python not just as a language,
but as a force multiplier.

Why Python? Because it's readable, powerful,
and probably already installed on your laptop.
Plus, it lets us handle large datasets,
run simulations, and plot things with colors,
which is really all a statistician wants.

Along the way,
we'll confirm spreadsheet values, visualize fitted curves,
and maybe even have a brief existential crisis about overfitting.
Fun times.

-- -- --

### 1: Matrix in Python

> Where Code Meets Coefficients

Consider represent above equation into python code.
We are going to turning algebra into automation,
Doing matrix math by hand is a cry for help.

#### Source Code

If you'd rather see this in action,
and possibly make fewer typos,
here are the full scripts:

* **21-poly.py**

```python
import numpy as np

order = 3
mx  = np.array([
        0, 1, 2, 3,
        4, 5, 6, 7,
        8, 9, 10, 11, 12])

mA = np.array([ 
       [(x ** i) for i in range(order+1)]
         for x in mx])

print(mA)
```

* **22-poly.py**

```python
import numpy as np

order = 3
mx  = np.array([
        0, 1, 2, 3,
        4, 5, 6, 7,
        8, 9, 10, 11, 12])
mB  = np.array([
         5,   14,   41,   98,
       197,  350,  569,  866,
      1253, 1742, 2345, 3074, 3941])

mA = np.array([ 
       [(x ** i) for i in range(order+1)]
         for x in mx])

mAt   = np.transpose(mA)
mAt_A = np.matmul(mAt, mA)
mAt_B = np.matmul(mAt, mB)

# First Method
mAt_A_i = np.linalg.inv(mAt_A)
mC      = np.matmul(mAt_A_i, mAt_B)
print("Coefficients (a, b, c, d):", mC)

# Second Method
mC      = np.linalg.solve(mAt_A, mAt_B)
print("Coefficients (a, b, c, d):", mC)
```

They contain the full setup and matrix solution process.

#### Setup Matrix A

We begin by channeling the power of `numpy`,
the Swiss Army knife of numerical Python.
First, define the polynomial order and your x-values:

```python
import numpy as np

order = 3
mx  = np.array([
        0, 1, 2, 3,
        4, 5, 6, 7,
        8, 9, 10, 11, 12])
```

Now generate the design matrix using list comprehension,
because you're not just a coder.
You're an artist with loops:

```python
mA = np.array([ 
       [(x ** i) for i in range(order+1)]
         for x in mx])

print(mA)
```

With `numpy`, the matrix result is nicer,
compared with regular array.
Which gives us:

```output
$ python 01-poly.py
[[   1    0    0    0]
 [   1    1    1    1]
 [   1    2    4    8]
 [   1    3    9   27]
 [   1    4   16   64]
 [   1    5   25  125]
 [   1    6   36  216]
 [   1    7   49  343]
 [   1    8   64  512]
 [   1    9   81  729]
 [   1   10  100 1000]
 [   1   11  121 1331]
 [   1   12  144 1728]]
 ```

 You can see the result here:



This is the foundation of the model.
Each row is a data point.
Each column is a power of x.
Together, they form our design matrix.
The DNA of our polynomial regression.

#### Alternatives: Column Stack

If you want the clean version without loops,
to build design matrix using list comprehension,
here's a cheat code:

```python
mA = np.column_stack([np.ones_like(mx), mx, mx**2, mx**3])
```

But hardcoding powers is like naming your kids
"Child1", "Child2", "Child3"...
not scalable. So we go dynamic:

```python
mA = np.column_stack([mx**j for j in range(order+1)])
```

#### Numpy's Vander

> The Fancy Option

Feeling lazy?
`numpy.vander` lets you generate a Vandermonde matrix with one line:

```python
mV = np.vander(mx, 4)
```

But note: vander assumes the classic polynomial form arrangement:

$$
y = a{x}^3 + b{x}^2 + c{x} + d
$$

While our version reads left-to-right:

$$
y = a + b{x} + c{x}^2 + d{x}^3
$$

No worries, just `np.flip` the matrix horizontally:
We can replace our list comprehension with vander.

```python
mV = np.flip(np.vander(mx, 4), axis=1)
```

Same math, different notation.
Always check whether your library prefers
"mathematical elegance" or "computational chaos."

#### Matrix Operation

> Solving for Coefficients

Matrix operation in python is incredibly simple.
Let's say we have this setup.
A know XY value pairs.

Let's define our known values x and y:

```python
import numpy as np

order = 3
mx  = np.array([
        0, 1, 2, 3,
        4, 5, 6, 7,
        8, 9, 10, 11, 12])
mB  = np.array([
         5,   14,   41,   98,
       197,  350,  569,  866,
      1253, 1742, 2345, 3074, 3941])

mA = np.array([ 
       [(x ** i) for i in range(order+1)]
         for x in mx])
```



We can prepare to compute the previous matrix equation.
Now apply the matrix formula:

$$
  A^T A\mathbf{C} = A^T \mathbf{B} \\
$$

```python
mAt   = np.transpose(mA)
mAt_A = np.matmul(mAt, mA)
mAt_B = np.matmul(mAt, mB)
```

Finally, solve for C, get the result:

$$
\mathbf{C} = (A^T A)^{-1} A^T
$$

Method 1: The long way:

```python
mAt_A_i = np.linalg.inv(mAt_A)
mC      = np.matmul(mAt_A_i, mAt_B)
print("Coefficients (a, b, c, d):", mC)
```

Method 2: The smarter way:

```python
mC      = np.linalg.solve(mAt_A, mAt_B)
print("Coefficients (a, b, c, d):", mC)
```



This is the core of polynomial regression.
It turns your data into a formula.
That formula predicts.

_Predicting is good._
_Predicting while looking smart in Python?_
_Even better._

#### @ (at) Operator

Want a cleaner syntax? Use the `@` (at) operator.
It's like `MMULT`, but cooler.

```python
# Calculated Matrix Variable

mA    = np.flip(np.vander(mx, 4), axis=1)
mAt   = np.transpose(mA)
mAt_A = mAt @ mA
mAt_B = mAt @ mB

# First Method
mAt_A_i = np.linalg.inv(mAt_A)
mC      = mAt_A_i @ mAt_B
print("Coefficients (a, b, c, d):", mC)

# Second Method
mC      = np.linalg.solve(mAt_A, mAt_B)
print("Coefficients (a, b, c, d):", mC)

# Draw Plot
[a, b, c, d] = mC
```

This Python matrix operation mirrors what we did in Excel earlier.
But now it's scalable, automatable,
and doesn't require you to wrestle with Ctrl+Shift+Enter.

Whether you're modeling data trends or building a machine learning model,
this is your algebraic skeleton key.

-- -- --

### 2: Alternative Coefficient Solution

> Along with Prediction Solution

Sometimes it feels like Python libraries are multiplying faster
than a grad student's coffee intake during finals.
Just when you master one method, a newer, shinier one pops up,
Complete with better docs and an example in TensorFlow.

But fear not, here's a guided tour through the jungle of coefficient-solving methods.
We'll take the same design matrix `mA` and vector `mB`,
and find our coefficient vector `mC` (then predict `yp`),
using various tools in the Python ecosystem.

Why so many options?
Because one size fits all only works for socks.
And even then, not really.

> Pick Your Solver, Pick Your Style

_In Python, there are at least six ways to solve any problem._
_And seven ways to feel bad about not knowing all of them._

However, this is what I know so far to solve the coefficient.
From the known design matrix `mA`, how do we find the coefficient `mC`,
and what is the final `yp` prediction result?

$$
\begin{aligned}
              &&    A\mathbf{C}     &= \mathbf{B} \\
  \Rightarrow &&    A^T A\mathbf{C} &= A^T \mathbf{B} \\
  \Rightarrow &&    \mathbf{C}      &= (A^T A)^{-1} A^T \mathbf{B}
\end{aligned}
$$

#### 1. Using `linalg` library

Solving gram matrix.

First up, the direct linear algebra approach.
Think of this as the textbook method.
You know, the one they put on the midterm.

```python
mAt_A = mA.T @ mA # gram matrix
mAt_B = mA.T @ mB 
mC = np.linalg.solve(mAt_A, mAt_B)
yp = mA @ mC
```

Using inverse of gram matrix.
When you're feeling bold and rebellious.

This is the foundation of OLS regression.
Also a good way to make your linear algebra professor proud,
or at least not sigh loudly.

```python
mC = np.linalg.inv(mA.T @ mA) @ (mA.T @ mB)
yp = a + b * mx + c * mx**2 + d * mx**3
```

Using least square.
Note that `np.linalg.lstsq` works for any polynomial degree
(linear, quadratic, cubic, etc.)
Bbecause it works even if your matrix is being dramatic:

```python
mC = np.linalg.lstsq(mA, mB, rcond=None)[0]
```

#### 2. Using the deprecated `polyfit`

Despite being labeled "deprecated" more times than Fortran,
this still works like a charm.

```python
mC = np.polyfit(mx, my, deg=order)
yp = np.polyval(mC, self.xs) 
```

It's quick and easy.
But like using a fax machine in 2025,
it's time to move on if you're building serious models.

#### 3. Using numpy `Polynomial` library

`Polynomial.fit` is `polyfit`'s well-behaved younger sibling.
It's object-oriented and much more polite.
We can use this instead of `polyfit`.

```python
from numpy.polynomial import Polynomial
poly = Polynomial.fit(mx, my, deg=order)
mC = poly.convert().coef
yp = poly(mx)
```

Want to feel fancy?
Swap in `Polynomial` for `Chebyshev`, `Legendre`,
or `Hermite` for different basis functions
Great for impressing your math friends,
or confusing your coworkers.

#### 4. Using stats `linregress'

This one-trick Pony is strictly for linear regression (degree = 1),
focuses on hypothesis testing, not regression.
It's less flexible but great for t-tests and p-values.

```python
from scipy import stats
m, b, _, _, _ = stats.linregress(mx, my)
```

Use this when your professor asks you to "_test a hypothesis_",
and you pretend to know what that means.

#### 5. Using statsmodels `OLS' (ordinary least square)

If you're looking to get serious with confidence intervals,
t-values, and beautiful `.summary()` outputs, this is the one.
Linear regression only, because scipy.stats focuses on
hypothesis testing, not regression.

```python
import statsmodels.api as sm

x = sm.add_constant(mx)
model = sm.OLS(y_values, x).fit()
a, b, c = model.params
```

This method is for people who enjoy linear regression reports,
with more footnotes than a PhD thesis.

#### 6. Using sklearn `PolynomialFeatures` library

Let's go simple machine learning mode.
Here's how to use `PolynomialFeatures` with `LinearRegression`.
This is for a more complex case.
Let's rewrite in complete code.

```python
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

order = 3
mx  = np.array([
        0, 1, 2, 3,
        4, 5, 6, 7,
        8, 9, 10, 11, 12])
my  = np.array([
         5,   14,   41,   98,
       197,  350,  569,  866,
      1253, 1742, 2345, 3074, 3941])

mx = mx.reshape(-1, 1)
```

Then transform and fit:

```python
# design matrix mA
poly   = PolynomialFeatures(degree=order)
mA = poly.fit_transform(mx) 

model  = LinearRegression().fit(mA, my)
y_pred = model.predict(mA)

# Default: does NOT adjust for Degree of Freedom
mse_sklearn = mean_squared_error(my, y_pred)  
print(f"Scikit-learn MSE (unadjusted): {mse_sklearn:.3f}")
```

Ideal when we're building models with cross-validation,
pipelines, and trying to sound impressive during coffee breaks.

Cool right!

#### A Random Note: FOMO is Real

> So many libraries, so little certainty.

Fear of missing out yet?
Sometimes, python is amazingly making us so incompetence,
worst than social media.

And then, have you ever have this feeling,
when you should decide whether using `np.linalg.solve`, or using `np.polyfit`,
or sacrifice a goat to the stats gods and hope `Polynomial.fit` gives the right curve?

Python's data ecosystem can feel like statistical imposter syndrome on steroids.
One moment we're solving a system with `np.linalg.solve`,
and the next we're 12 tabs deep into `Chebyshev` polynomials for time series forecasting.

But the good news?
They all get you to the same coefficients (eventually).
Use what fits your problem, your data,
and your current level of caffeination.

-- -- --

### 3: Matplotlib

> Visual confirmation

_If you can't plot it, did it even happen?_

After crunching all those numbers
and doing your best impersonation of Gauss with a keyboard,
It's time to actually see if your curve makes sense.
Enter: `matplotlib`, the data scientist's favorite excuse to avoid writing reports.

#### Source Code

Need the full code? We've got you:

* **24-poly.py**

```python
import numpy as np
import matplotlib.pyplot as plt

# Initial Matrix Value

order = 3
mx  = np.array([
        0, 1, 2, 3,
        4, 5, 6, 7,
        8, 9, 10, 11, 12])
mB  = np.array([
         5,   10,  410,   90,
       190,  350,  460,  960,
      1050, 1740, 1340, 3270, 3540])

# Calculated Matrix Variable
mA    = np.flip(np.vander(mx, 4), axis=1)
mAt   = np.transpose(mA)
mAt_A = mAt @ mA
mAt_B = mAt @ mB
mC    = np.linalg.solve(mAt_A, mAt_B)
[a, b, c, d] = mC
print("Coefficients (a, b, c, d):", mC)

# Draw Plot
x_plot = np.linspace(min(mx), max(mx), 100)
y_plot = a + b * x_plot + \
         c * x_plot**2 + d * x_plot**3

plt.scatter(mx, mB, label='Data points')
plt.plot(x_plot, y_plot, color='red',
  label='Fitted third-order polynomial')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.suptitle(
  'Third-order polynomial curve fitting')

subfmt = "a = %.2f, b = %.2f c = %.2f, d = %.2f"
plt.title(subfmt % (a, b, c, d), y=-0.01)

plt.show()
```

#### Basic Plot

Let's revisit our polynomial-fitted coefficients,
toss them into a pretty plot,
and bask in the satisfaction
of seeing math and reality shake hands.



Here's how to bring the curve to life:

```python
x_plot = np.linspace(min(mx), max(mx), 100)
y_plot = a + b * x_plot + \
         c * x_plot**2 + d * x_plot**3

plt.scatter(mx, mB, label='Data points')
plt.plot(x_plot, y_plot, color='red',
  label='Fitted third-order polynomial')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title(
  'Third-order polynomial curve fitting')

plt.show()
```

Visualization helps verify that
our model isn't just spitting out plausible numbers.
It's actually following the data trend.
It also helps when our boss asks.
So... what does this mean?



With the result as.



Congratulations!
We've plotted something fancier than a straight line.
The ghost of `Legendre` nods approvingly.

#### Test Other Data

> Chaos Mode

Let's mix things up.
Change the `mB` values and see how the polynomial tries to keep up.
Sometimes you learn more when the math starts sweating.

```python
mB  = np.array([
         5,   10,  410,   90,
       190,  350,  460,  960,
      1050, 1740, 1340, 3270, 3540])
```

This tests the robustness of our model.
Does it gracefully adjust to new patterns?
Or does it panic like a student on exam day?

The matrix equation should remain the same.



Add a title to show the actual fitted coefficients:

```python
# Draw Plot
[a, b, c, d] = mC

...

plt.suptitle(
  'Third-order polynomial curve fitting')

subfmt = "a = %.2f, b = %.2f c = %.2f, d = %.2f"
plt.title(subfmt % (a, b, c, d), y=-0.01)

plt.show()
```

That's right.
We're labeling the curve with the actual math behind it.
Because we're fancy like that.



And the final result.
Now we can see,
how the line fit the dots.

If our plot starts to look like modern art, double-check the data.
Or say it's non-linear heteroscedasticity and walk away confidently.



_You can do it yourself._

Here we can see whether our elegant third-degree curve is,
actually capturing the chaos,
or awkwardly missing the mark like
a first-year undergrad estimating Pi with a ruler.

-- -- --

### 4: Enhance Script

> Polynomial Polish: Scripting Like a Pro

Ah yes, Enhancing our script.
Let's add some polish (the scripting kind, not the Eastern European kind),
to make your polynomial workflow smoother than a cubic curve at an inflection point.

You can make your life easier with these few tricks.

#### Source Code

Want the full script? Grab it here:

* **25-poly.py**

```python
import numpy as np
import matplotlib.pyplot as plt

# Initial Matrix Value
order = 3

# Setup numpy
np.set_printoptions(
  precision=2,
  formatter={
    'int':   '{:30,d}'.format,
    'float': '{:10,.8f}'.format
  },
  linewidth=np.inf,
  suppress=True)

# Getting Matrix Values
mCSV = np.genfromtxt("poly.csv",
  skip_header=1, delimiter=",", dtype=float)

mCSVt   = np.transpose(mCSV)
x_values = mx = mCSVt[0]
y_values = mB = mCSVt[1]

# Perform cubic regression using polyfit
mC = np.polyfit(x_values, y_values, deg=order)
print('Using polyfit')
print(f'Coefficients (a, b, c, d):\n\t{np.flip(mC)}\n')

# Calculated Matrix Variable
mA    = np.flip(np.vander(mx, order+1), axis=1)
mAt   = np.transpose(mA)
mAt_A = mAt @ mA
mAt_B = mAt @ mB
mC    = np.linalg.solve(mAt_A, mAt_B)

[a, b, c, d] = mC
print('Calculate manually')
print(f'Coefficients (a, b, c, d):\n\t{mC}\n')

for x in mx:
  y = a + b*x + c*x**2 + d*x**3
  print(f'x = {x:5}  =>  y = {y:10,.2f} ')

# Draw Plot
x_plot = np.linspace(min(mx), max(mx), 100)
y_plot = a + b * x_plot + \
         c * x_plot**2 + d * x_plot**3

plt.scatter(mx, mB, label='Data points')
plt.plot(x_plot, y_plot, color='red',
  label='Fitted third-order polynomial')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.suptitle(
  'Third-order polynomial curve fitting')

subfmt = "a = %.2f, b = %.2f c = %.2f, d = %.2f"
plt.title(subfmt % (a, b, c, d), y=-0.01)

plt.show()
```

#### Setup Numpy

Tired of Numpy arrays printing like an accountant in panic mode?
Clean up the formatting globally with one line.
It won't do your taxes, but it will make debugging less of an optical illusion.

Instead of formatting data all the time,
we can set the `numpy` output globally.

```python
# Setup numpy
np.set_printoptions(
  precision=2,
  formatter={
    'int':   '{:30,d}'.format,
    'float': '{:10,.8f}'.format
  },
  linewidth=np.inf,
  suppress=True)
```



Readable output helps avoid mistaking 1e3 for a rounding error or a rogue exponential.

#### Data Source with CSV

Hardcoding arrays is for amateurs and tutorial screenshots.
Real data scientists live dangerously, with CSVs.

Instead of array, you can have your data source from anywhere,
from database, spreadsheet, or simple CSV.

```python
# Getting Matrix Values
mCSV = np.genfromtxt("poly.csv",
  skip_header=1, delimiter=",", dtype=float)

mCSVt   = np.transpose(mCSV)
mx = mCSVt[0]
mB = mCSVt[1]
```

Real-world data often comes in files,
not copy-pasteable arrays from Stack Overflow.
Welcome to adulthood.



You can get the example CSV here.

* **poly.csv**

Here's how the CSV looks:

```csv
x,y
0,5
1,14
2,41
3,98
4,197
5,350
6,569
7,866
8,1253
9,1742
10,2345
11,3074
12,3941
```

Yes, this file is more polite than some coworkers,
it even has headers.

#### Polyfit

Rather than reenact matrix algebra by hand every time,
let `polyfit` do the number crunching.
It's fast, flexible, and doesn't require caffeine.

```python
# Initial Matrix Value
order = 3

mCSVt   = np.transpose(mCSV)
x_values = mx = mCSVt[0]
y_values = mB = mCSVt[1]

# Perform cubic regression using polyfit
mC = np.polyfit(x_values, y_values, deg=order)
print('Using polyfit')
print(f'Coefficients (a, b, c, d):\n\t{np.flip(mC)}\n')
```

You can try different polynomial degrees like a buffet.
No matrix multiplication hangovers required.



Statistically speaking,
that's a beautiful curve if we've ever seen one.

```output
$ python 05-poly.py
Using polyfit
Coefficients (a, b, c, d):
	[5.00000000 4.00000000 3.00000000 2.00000000]
```

#### Output Result

For debugging purpose you can show each prediction value line by line.

```python
for x in mx:
  y = a + b*x + c*x**2 + d*x**3
  print(f'x = {x:5}  =>  y = {y:10,.2f} ')
```

```output
$ python 05-poly.py
x =   0.0  =>  y =       5.00 
x =   1.0  =>  y =      14.00 
x =   2.0  =>  y =      41.00 
x =   3.0  =>  y =      98.00 
x =   4.0  =>  y =     197.00 
x =   5.0  =>  y =     350.00 
x =   6.0  =>  y =     569.00 
x =   7.0  =>  y =     866.00 
x =   8.0  =>  y =   1,253.00 
x =   9.0  =>  y =   1,742.00 
x =  10.0  =>  y =   2,345.00 
x =  11.0  =>  y =   3,074.00 
x =  12.0  =>  y =   3,941.00 
```

Does our model actually work, or is it just faking it?
Print predicted values alongside input.
Great for testing and smug satisfaction.



Verifying model output one row at a time is
the data scientist's version of reading poetry aloud.
Cathartic.

#### Editable Output

Want to edit your plot in Illustrator or Inkscape without recreating it?
Export as `.svg`, not `.png`.

This not enhanced script, but rather a trick.
Instead of exporting `.png` from matplotlib,
you can export to `.svg`.
Sometimes you need to alter the result for further processing,
such as report, or removing annoying lines quickly.



You can have the SVG source from here

* **SVG Source**

SVG is vector-based, editable, and doesn't pixelate
when our manager asks for it "slightly bigger."

#### Choosing Order

In my experience, higher order tend to have further precision.
If you have issue with precision, you might consider lower order.

```python
# Initial Matrix Value
order = 2
```

Higher order = more precision,
until it becomes overfitting's evil twin.
Sometimes, less is more.
And sometimes more is... still too much.

#### Interactive JupyterLab

Want sliders, instant feedback, and markdown magic?
Open the `Jupyter Notebook`.

Jupyter is where ideas come to life.
Or crash in real time.
Either way, it's interactive.

-- -- --

### 5: Variants Beyond polynomial

`Polynomials` are like vanilla ice cream:
reliable, smooth, and always a crowd-pleaser.
But sometimes, your dataset deserves rocky road.
Enter `numpy`'s other regression flavors:
`Chebyshev`, `Legendre`, and `Hermite`.
All fancy, all orthogonal, and all with names
that sound like 19th-century mathematicians
who probably owned monocles.

Numpy offers four built-in regression bases:

* `Polynomial`
* `Chebyshev`
* `Legendre`
* `Hermite`

The same series points (xₛ, yₛ) will produce different coefficients for each kind of variants.
But the prediction result is the same, you can check that in matplotlib.



On the other hand, the same coefficient would produce different prediction, for each variants.

* **29-variants.py**

```python
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import (
    Polynomial, Chebyshev, Legendre, Hermite)

# Create x values
x = np.linspace(-1.1, 1.1, 400)

# Degree 3 polynomials with simple coefficients for comparison
coeffs = [5, 4, 3, 2]

# Generate polynomial curves
y_poly = Polynomial(coeffs)(x)
y_cheb = Chebyshev(coeffs)(x)
y_legendre = Legendre(coeffs)(x)
y_hermite = Hermite(coeffs)(x)

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(x, y_poly, label="Regular Polynomial", linewidth=2)
plt.plot(x, y_cheb, label="Chebyshev Series", linestyle='--')
plt.plot(x, y_legendre, label="Legendre Series", linestyle='-.')
plt.plot(x, y_hermite, label="Hermite Series", linestyle=':')

plt.title("Comparison of Polynomial Series (Degree 3)")
plt.xlabel("x")
plt.ylabel("y")

plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
```

-- -- --

### What's Our Next Endeavor 🤔?

> That was fun, wasn't it?

Math that compiles and runs? Truly, we live in the future.

We've built polynomial models in spreadsheets,
coded them in Python, and we've survived both.
But now it's time to bring this knowledge down to Earth,
with real, practical examples.

Not just equations, but tools we can plug into daily analysis.
Linear, quadratic, cubic... in Excel and Python,
with scripts we'll actually use.
Because a good theory is only as valuable,
as its copy-pasteable implementation.

What do you think?

Continue here: **Trend - Polynomial Examples**.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Curve fitting examples for daily basis,
> using vandermonde matrix.

Let's be honest: on a typical Tuesday,
nobody wakes up excited to derive polynomial equations by hand.
Fortunately, we don't have to.
I've got ready-made spreadsheets and Python scripts,
so we can focus on the fun part, like fitting curves
to wildly unpredictable real-world data
(or impressing friends with our Excel wizardry).

To make things digestible,
I've cooked up a spreadsheet with three themed tabs:

1. Linear Equation (first order polynomial)
2. Quadratic Equation (second order polynomial)
3. Cubic Equation (third order polynomial)



Each sheet follows a familiar recipe,
as seen in the last article:

1. From the known coefficient,
   find the points (x, y).

2. Building the matrix visually,
   based on equation of the system.

3. From the points (x, y),
   find the coefficient.
   Inverse the matrix, solving the equation.

Understanding how equations morph from abstract coefficients
to real-world points, and back again,
is the statistical equivalent of learning how the sausage is made.
You don't have to do it daily,
but knowing how gives you control,
when the auto-tools misbehave.

#### Practical

For daily basis, all you need is just
the last sheet (matrix inverse) of selected case (order).
The real data for daily basis is dispersed,
unlike given data in this example sheet.

The worksheet is pretty explanatory.
Assuming that you have read previous article,
The first and the second sheet is,
already well explained in previous article,
so we are going to skip these sheets.
I do not think that I should explain each worksheet in detail.

The python script also has been explained in previous article,
the purpose of this exampale is just giving a ready to use script.
So I won't go into detail either.

#### Other Method

Of course, the Vandermonde matrix isn't the only player in town.
Later, we'll look at the Least Squares Method.
A powerful technique when our data points refuse to play nice
(which they always do).

Multiple tools mean more flexibility.
When one method makes your data look like a confused doodle,
another might give you a Mona Lisa.

#### Worksheet Source

> Playsheet Artefact

Here's the Excel file.
Tinker, explore, and maybe even break it.
The best way to understand something is
to make it crash gloriously.

* **github.com/.../math/trend/examples-polynomial.xlsx**

-- -- --

### 1: Linear Equation

> First Order Polynomial Method

#### Curve Fitting

Since real data matrix is definitely not a square matrix,
and matrix inverse can only work with square `nxn` matrix.
We need to alter the equation with transpose.

Our real-world data shows up in a less-than-cooperative format
(read: a tall, skinny matrix), things get interesting.
Since we can't invert a non-square matrix,
we apply a little matrix magic: the transpose trick.

$$
\begin{aligned}
              &&    A \times \mathbf{C} &= \mathbf{B} \\
  \Rightarrow &&    A^T \times A \times \mathbf{C} &= A^T \times \mathbf{B} \\
  \Rightarrow &&    \mathbf{C}  &= (A^T \times A)^{-1} \times (A^T \times \mathbf{B})
\end{aligned}
$$

Here's how that looks in spreadsheet reality:



To recap the formula:

First, calculate Aᵀ × A:

$$
A^T \times A
$$

```excel
=MMULT(TRANSPOSE(E9:F21);E9:F21)
```

Then take the inverse:

$$
(A^T \times A)^{-1}
$$

```excel
=MINVERSE(E27:F28)
```

Multiply Aᵀ × B:

$$
A^T \times \mathbf{B}
$$

```excel
=MMULT(TRANSPOSE(E9:F21);J9:J21)
```

And finally, the crown jewel:
calculate the coefficient vector CC

$$
\mathbf{C}  = (A^T \times A)^{-1} \times (A^T \times \mathbf{B})
$$

```excel
=MMULT(E30:F31;E33:E34)
```

Tidy it all up, and your spreadsheet transforms from chaos to clarity:



With our shiny new coefficients:

$$
\begin{aligned}
a &= 5 \\
b &= 4 \\
\end{aligned}
$$

And known `x` for this equatio,
this gives us

$$
\begin{aligned}
x_i &= [0, 1, 2, \ldots, 10, 11, 12] \\
y_i &= a + bx_i
\end{aligned}
$$
`
Now plug in values of `x` (from 0 to 12),
and we can calculate the predicted yy values using.
We can calculate `y` by using spreadsheet formula.

```excel
=$C$43+$C$44*B47
```

The prediction value can be shown as spreadsheet below:



#### Python Scripts

Instead of hardcoded data, we can setup the source data in CSV.

If Excel isn't your thing,
or if you just enjoy wrangling matrices in code,
here's a Python script to do the same thing.

* **31-linear-equation.csv**

The CSV looks like this file below:

```csv
x,y
0,5
1,9
2,13
3,17
4,21
5,25
6,29
7,33
8,37
9,41
10,45
11,49
12,53
```

The python source can be obtained from below link

* **31-linear-equation.py**

```python
x,y
0,5
1,9
2,13
3,17
4,21
5,25
6,29
7,33
8,37
9,41
10,45
11,49
12,53
```

It's almost identical to the one from our earlier article,
except that it is tuned for linear equations.
So I don't think that I should explain into the detail.

```python
# Initial Matrix Value
order = 1

# Getting Matrix Values
mCSV = np.genfromtxt("31-linear-equation.csv",
  skip_header=1, delimiter=",", dtype=float)
...
```

The result, courtesy of Matplotlib,
is a beautiful straight line that says,
"_Yep, the trend is real._"

Reproducing spreadsheet results in code,
makes our analysis reproducible, scalable, and automatable

#### Interactive JupyterLab

Want to poke around interactively?
Here's a `JupyterLab` notebook so you can tweak,
rerun, and experiment to your heart's content:

* **31-linear-equation.py**

```python
import numpy as np
import matplotlib.pyplot as plt

# Initial Matrix Value
order = 1

# Setup numpy
np.set_printoptions(
  precision=2,
  formatter={
    'int':   '{:30,d}'.format,
    'float': '{:10,.8f}'.format
  },
  linewidth=np.inf,
  suppress=True)

# Getting Matrix Values
mCSV = np.genfromtxt("31-linear-equation.csv",
  skip_header=1, delimiter=",", dtype=float)

mCSVt   = np.transpose(mCSV)
x_values = mx = mCSVt[0]
y_values = mB = mCSVt[1]

# Perform linear regression using polyfit
mC = np.polyfit(x_values, y_values, deg=order)
print('Using polyfit')
print(f'Coefficients (a, b):\n\t{np.flip(mC)}\n')

# Calculated Matrix Variable
mA    = np.flip(np.vander(mx, order+1), axis=1)
mAt   = np.transpose(mA)
mAt_A = mAt @ mA
mAt_B = mAt @ mB
mC    = np.linalg.solve(mAt_A, mAt_B)

[a, b] = mC
print('Calculate manually')
print(f'Coefficients (a, b):\n\t{mC}\n')


# Draw Plot
x_plot = np.linspace(min(mx), max(mx), 100)
y_plot = a + b * x_plot

plt.scatter(mx, mB, label='Data points')
plt.plot(x_plot, y_plot, color='red',
  label='Linear Equation')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.suptitle(
  'Straight line fitting')

subfmt = "a = %.2f, b = %.2f"
plt.title(subfmt % (a, b), y=-0.01)

plt.show()
```

It's like Excel, but with less clicking and more satisfaction.

-- -- --

### 2: Quadratic Equation

> Second Order Polynomial Method

When straight lines just won't cut it.

#### Curve Fitting

Using the same matrix-based steps as before
(transpose, multiply, invert, survive),
we can visualize the quadratic system equation,
straight in the spreadsheet:



Our spreadsheet spits out the coefficients:

$$
\begin{aligned}
a &= 5, & b &= 4, & c &= 3
\end{aligned}
$$

With known `x` for this equation,
we can calculate `y` by using spreadsheet formula.

$$
\begin{aligned}
x_i &= [0, 1, 2, \ldots, 10, 11, 12] \\
y_i &= a + bx_i + cx_i^2
\end{aligned}
$$

Which means our prediction model is now flexing some curvature.
Here's the spreadsheet result in all its second-degree glory:



Not all relationships in data are linear. A quadratic fit lets you model acceleration, parabolic trends, or just the kind of weird behavior Excel charts love to dramatize.

#### Python Scripts

As before, we can ditch the manual entry (aka hardcoded data),
and bring in our data via CSV like a civilized data analyst.

* **32-data-second-order.csv**

Here's what it looks like:

```csv
x,y
0,5
1,12
2,25
3,44
4,69
5,100
6,137
7,180
8,229
9,284
10,345
11,412
12,485
```

The python source can be obtained from below link

* **32-poly-second-order.py**

```python
import numpy as np
import matplotlib.pyplot as plt

# Initial Matrix Value
order = 2

# Setup numpy
np.set_printoptions(
  precision=2,
  formatter={
    'int':   '{:30,d}'.format,
    'float': '{:10,.8f}'.format
  },
  linewidth=np.inf,
  suppress=True)

# Getting Matrix Values
mCSV = np.genfromtxt("32-data-second-order.csv",
  skip_header=1, delimiter=",", dtype=float)

mCSVt   = np.transpose(mCSV)
x_values = mx = mCSVt[0]
y_values = mB = mCSVt[1]

# Perform quadratic regression using polyfit
mC = np.polyfit(x_values, y_values, deg=order)
print('Using polyfit')
print(f'Coefficients (a, b, c):\n\t{np.flip(mC)}\n')

# Calculated Matrix Variable
mA    = np.flip(np.vander(mx, order+1), axis=1)
mAt   = np.transpose(mA)
mAt_A = mAt @ mA
mAt_B = mAt @ mB
mC    = np.linalg.solve(mAt_A, mAt_B)

[a, b, c] = mC
print('Calculate manually')
print(f'Coefficients (a, b, c):\n\t{mC}\n')


# Draw Plot
x_plot = np.linspace(min(mx), max(mx), 100)
y_plot = a + b * x_plot + c * x_plot**2

plt.scatter(mx, mB, label='Data points')
plt.plot(x_plot, y_plot, color='red',
  label='Fitted second-order polynomial')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.suptitle(
  'Second-order polynomial curve fitting')

subfmt = "a = %.2f, b = %.2f, c = %.2f"
plt.title(subfmt % (a, b, c), y=-0.01)

plt.show()
```

The Python version, once again,
sticks close to our earlier structure,
just tuned up for second-order fitting.
So again, I don't think that I should explain into the detail.

```python
# Initial Matrix Value
order = 2

# Getting Matrix Values
mCSV = np.genfromtxt("32-data-second-order.csv",
  skip_header=1, delimiter=",", dtype=float)

...
```

With that in place, Python does its matrix dance and gives us this satisfying curve:

With data series in CSV above in place,
Python does its matrix dance and gives us this satisfying curve fitting as below:



#### Interactive JupyterLab

For those who prefer mixing code and results in real time
(a.k.a. data sorcery), grab the interactive notebook:

Bend it, break it, rerun it.
Jupyter makes experimenting with trends feel like play, not work.

-- -- --

### 3: Cubic Equation

> Third Order Polynomial Method

When our trendline has mood swings.

#### Curve Fitting

As with the previous cases,
we follow our usual matrix three-step:
transpose, multiply, and invert.
Now with more dimensions and potential for confusion!

Here's how that plays out visually in a spreadsheet:



We wrangle the matrix,
and out pop these coefficients:

$$
\begin{aligned}
a &= 5, & b &= 4, & c &= 3, & d &= 4.
\end{aligned}
$$

With known `x` for this equation,
we can calculate `y` by using spreadsheet formula.

$$
\begin{aligned}
x_i &= [0, 1, 2, \ldots, 10, 11, 12] \\
y_i &= a + bx_i + cx_i^2 + dx_i^3
\end{aligned}
$$

Apply it down our sheet,
and we get a plot that would make even a rollercoaster designer proud:



Cubic fits are ideal when our data does the statistical equivalent of jazz,
unexpected turns, dramatic rises, and inflection points galore.

#### Python Scripts

As always, ditching hardcoded values and feeding your script with a CSV,
is the way to go, let our computer do the heavy lifting,
while we sip coffee and pretend it's magic.

* **33-data-third-order.csv**

Here's what the data looks like:

```csv
x,y
0,5
1,14
2,41
3,98
4,197
5,350
6,569
7,866
8,1253
9,1742
10,2345
11,3074
12,3941
```

And the Python source (familiar, yet now powered for cubic glory):

* **33-poly-third-order.py**

```python
import numpy as np
import matplotlib.pyplot as plt

# Initial Matrix Value
order = 3

# Setup numpy
np.set_printoptions(
  precision=2,
  formatter={
    'int':   '{:30,d}'.format,
    'float': '{:10,.8f}'.format
  },
  linewidth=np.inf,
  suppress=True)

# Getting Matrix Values
mCSV = np.genfromtxt("33-data-third-order.csv",
  skip_header=1, delimiter=",", dtype=float)

mCSVt   = np.transpose(mCSV)
x_values = mx = mCSVt[0]
y_values = mB = mCSVt[1]

# Perform cubic regression using polyfit
mC = np.polyfit(x_values, y_values, deg=order)
print('Using polyfit')
print(f'Coefficients (a, b, c, d):\n\t{np.flip(mC)}\n')

# Calculated Matrix Variable
mA    = np.flip(np.vander(mx, order+1), axis=1)
mAt   = np.transpose(mA)
mAt_A = mAt @ mA
mAt_B = mAt @ mB
mC    = np.linalg.solve(mAt_A, mAt_B)

[a, b, c, d] = mC
print('Calculate manually')
print(f'Coefficients (a, b, c, d):\n\t{mC}\n')

# Draw Plot
x_plot = np.linspace(min(mx), max(mx), 100)
y_plot = a + b * x_plot + \
         c * x_plot**2 + d * x_plot**3

plt.scatter(mx, mB, label='Data points')
plt.plot(x_plot, y_plot, color='red',
  label='Fitted third-order polynomial')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.suptitle(
  'Third-order polynomial curve fitting')

subfmt = "a = %.2f, b = %.2f, c = %.2f, d = %.2f"
plt.title(subfmt % (a, b, c, d), y=-0.01)

plt.show()
```

It is very similar with source code in previous article,
except that it is for quadratic equation.
So again, I don't think that I should explain into the detail.

```python
# Initial Matrix Value
order = 3

# Getting Matrix Values
mCSV = np.genfromtxt("33-data-third-order.csv",
  skip_header=1, delimiter=",", dtype=float)

...
```

Python digs through the data and returns a beautiful curve:



Whether we're modeling stock prices, scientific measurements,
or the emotional arc of your last project,
cubic curves are the sweet spot for capturing complexity,
without going full math meltdown.

#### Interactive JupyterLab

For the tinkerers and the curious, here's our playground:

* **33-poly-third-order.py**

Fire it up, tweak a coefficient,
rerun the cell, and instantly see how the curve morphs.
Like magic, but statistically sound.

-- -- --

### 4: Optimizing Spreadsheet

> How I Learned to Stop Worrying and Love the Gram Matrix

Let's be honest.
Real-world data isn't just a neat set of five numbers,
you can eyeball in one coffee break.
Once you've got rows upon rows of data,
it is simply doesn't make any sense,
to write the whole long column of matrix transpose of A.
Manually writing out matrix A
(and its beautiful but exhausting transpose) becomes...
Well, statistically unsustainable.

We can simplifiy this by writing the formula of (Aᵗ.A) at once.
In fact we do not even need to write A matrix in physical cell at all.

#### Worksheet Source

> A spreadsheet so efficient it should be peer-reviewed

Don't reinvent the pivot table.
Download the Excel file, play with it,
and bask in the automation:

* **github.com/.../math/trend/31-gram-matrix.xlsx**

#### Formula Step by Step

Let's break it down.
Here's the pipeline of spreadsheet matrix algebra:

As a concept we can describe the process as:

* Transpose of A: (Aᵗ)

```excel
=TRANSPOSE(A)
```

* Gram Matrix (Aᵗ·A)

```excel
=MMULT(TRANSPOSE(A), A)
```

Inverse of Gram Matrix: (Aᵗ.A)ˉ¹

```excel
=MINVERSE(Aᵗ.A)
```

Moment Vector (Aᵗ.B):

```excel
=MMULT(TRANSPOSE(A), B)
```

C = Coefficient Vector = (Aᵗ.A)ˉ¹(Aᵗ.B)

This is the actual fit: the line/curve we're modeling.

```excel
=MMULT((Aᵗ.A)ˉ¹, (Aᵗ.B))
```

This workflow automates the fitting process,
scales with our data, and most importantly,
saves us from dragging formulas down 300 rows,
like a spreadsheet peasant.

#### Generic Matrix

Now, what is matrix A anyway?

We can generalized the matrix in equation to:

$$
\begin{align}
    \begin{aligned}
        &\begin{array}{|c|c|c|}
            \hline
            \textbf{Linear} & 
            \textbf{Quadratic} & 
            \textbf{Cubic} \\
            \hline
            A = 
            \begin{bmatrix}
                1 & x_1 \\
                1 & x_2 \\
                1 & x_3 \\
                \vdots & \vdots \\
                1 & x_n \\
            \end{bmatrix}
            &
            A = 
            \begin{bmatrix}
                1 & x_1 & x_1^2 \\
                1 & x_2 & x_2^2 \\
                1 & x_3 & x_3^2 \\
                \vdots & \vdots & \vdots \\
                1 & x_n & x_n^2 \\
            \end{bmatrix}
            &
            A = 
            \begin{bmatrix}
                1 & x_1 & x_1^2 & x_1^3 \\
                1 & x_2 & x_2^2 & x_2^3 \\
                1 & x_3 & x_3^2 & x_3^3 \\
                \vdots & \vdots & \vdots & \vdots \\
                1 & x_n & x_n^2 & x_n^3 \\
            \end{bmatrix}
            \\
            \hline
        \end{array}
    \end{aligned}
\end{align}
$$

Matrix A is like a trend-fitting chameleon.
It changes shape based on your polynomial order:

#### Apply to Spreadsheet

Suppose we have this data series containing pair observed values,
in range `B37:C49`:

* x: B37:B49
* y: C37:C49



Let's build the model without ever writing out matrix A.

#### Temporary Matrix

We can utilize `CHOOSE` formula as as replacement of matrix A.
No visual clutter, no risk of accidental edits.

```excel
=CHOOSE({1,2}, 1, B37:B49)
```

Transpose it with:

```excel
=TRANSPOSE(CHOOSE({1,2}, 1, B37:B49))
```

Matrix `B` is just our y-values:
And for the matrix `B`, we use range `C37:C49`, the same with y series.

Now we can write gram matrix (Aᵗ.A) in range `B12:C13` using this formula:

```excel
=MMULT(TRANSPOSE(CHOOSE({1,2}, 1, B37:B49)),
       CHOOSE({1,2}, 1, B37:B49))
```

Now we can continue writing inverse of gram matrix (Aᵗ.A)ˉ¹,
in range `B18:C19` using this formula:

```excel
=MINVERSE(B12:C13)
```

Let's continue to RHS (right hand side) of the equation,
containing the moment vector (Aᵗ.B),
in range `B24:B25` using this formula:

```excel
=MMULT(TRANSPOSE(CHOOSE({1,2}, 1, B37:B49)), C37:C49)
```

Finally, calculate the C matrix containing coefficient (Aᵗ.A)ˉ¹.(Aᵗ.B) using this formula:

```excel
=MMULT(B18:C19, B24:B25)
```



We are done with trend without even writing A matrix in any cells.
This setup gives us clean, dynamic, and scalable modeling,
without cluttering our sheet with every power of every x.
It's like wearing noise-cancelling headphones in a crowded matrix.

#### Gram Matrix: Quadratic

ime to upgrade to second-order polynomial.
We can continue writing gram matrix (Aᵗ.A) for quadratic polynomial:
Here's your cheat sheet:

```excel
A 
=CHOOSE({1,2,3},
 1, B37:B49, B37:B49^2)

B: Range: C37:C49

Aᵗ
=TRANSPOSE(A)
=TRANSPOSE(CHOOSE({1,2,3},
           1, B37:B49, B37:B49^2))

(Aᵗ.A)
Range: E12:G14
=MMULT(TRANSPOSE(A), A)
=MMULT(TRANSPOSE(CHOOSE({1,2,3},
           1, B37:B49, B37:B49^2)),
       CHOOSE({1,2,3},
       1, B37:B49, B37:B49^2))

(Aᵗ.A)ˉ¹
Range: E18:G20
=MINVERSE(E12:G14)

(Aᵗ.B)
Range: E24:E26
=MMULT(TRANSPOSE(A), B)
=MMULT(TRANSPOSE(CHOOSE({1,2,3},
           1, B37:B49, B37:B49^2)),
       C37:C49)

C: Coefficients (Aᵗ.A)ˉ¹.(Aᵗ.B)
=MMULT(E18:G20, E24:E26)
```

#### Gram Matrix: Quadratic

Feeling brave? Welcome to cubic.
Also continue writing gram matrix (Aᵗ.A):

```excel
A 
=CHOOSE({1,2,3,4},
 1, B37:B49, B37:B49^2, B37:B49^3)

B: Range: C37:C49

Aᵗ
=TRANSPOSE(A)
=TRANSPOSE(CHOOSE({1,2,3,4},
           1, B37:B49, B37:B49^2, B37:B49^3))

(Aᵗ.A)
Range: I12:L15
=MMULT(TRANSPOSE(A), A)
=MMULT(TRANSPOSE(CHOOSE({1,2,3,4},
           1, B37:B49, B37:B49^2, B37:B49^3)),
       CHOOSE({1,2,3,4},
       1, B37:B49, B37:B49^2, B37:B49^3))

(Aᵗ.A)ˉ¹
Range: I18:L21
=MINVERSE(I12:L15)

(Aᵗ.B)
Range: I24:I27
=MMULT(TRANSPOSE(A), B)
=MMULT(TRANSPOSE(CHOOSE({1,2,3,4},
           1, B37:B49, B37:B49^2, B37:B49^3)),
       C37:C49)

C: Coefficients (Aᵗ.A)ˉ¹.(Aᵗ.B)
=MMULT(I18:L21, I24:I27)
```

The spreadsheet with all coefficients looks something like this:



#### Predicted Series

Now that you've got all your coefficients,
use them to generate predicted values for:
linear, quadratic, and cubic models,
side by side.



It's like a polynomial bake-off.
Same kitchen (data), different recipes (models),
and now you can taste, test the results.

Note that we can enhance the prediction formula further with this form:

```excel
=SUMPRODUCT(TRANSPOSE(coeff_3),B37^{3,2,1,0})
```

We are going to use this form later,
while using spreadsheet with named range in polynomial regression.

#### Completed Worksheet

You can imagine how your life can be easier now.
You can even compare different result at once,
since all written side by side in the same worksheet.

The final form of our spreadsheet,
the statistical equivalent of achieving Excel enlightenment:



With this setup, we're now free to model, compare,
and update without breaking a sweat, or a formula.
Just change the data, and the rest updates like clockwork.

We are going to use this matrix calculation later,
while doing polynomial regressions.

-- -- --

### What's the Next Chapter 🤔?

We've played with trendlines,
climbed the polynomial curve up to degree three,
and survived matrix math with dignity mostly intact.
But guess what?
There's an even sharper tool in the shed: **Least Squares**.

This technique isn't just a way to draw the best squiggly line through our data points.
It's a foundational approach that underpins most of modern regression analysis.
And like all good thrillers, it starts simple: linear least squares.

Least squares isn't just a method. It's the method.
Mastering it means we're not just throwing curves at our data.
We're actually understanding the forces behind the fit.
Plus, it opens doors to correlation analysis,
inference, and all sorts of future fun.

Ready to shift from trendlines to simple regression?
Check out the next adventure: **Trend - Least Square**.

(Bring your data. And maybe a cup of coffee.)

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Curve fitting examples for daily basis,
> using least squares method.

I'm not a statistician,
though I do occasionally dress like one (corduroy optional).
That's why when I do talk about statistics, I tread carefully.

We will start by laying out the math,
because math doesn't lie, only people misinterpret it.
Then move to spreadsheet implementation
using Calc (which plays nicely with Excel).
And finally round things off with a bit of Python scripting.
All practical, all grounded, and no asymptotic nonsense (yet).

From here, we will gracefully tiptoe,
into regression analysis and correlation

-- -- --

### 1: Statistic Notation

Before we hurl ourselves at least squares,
we need to brush up on the two pillars of statistical awkwardness:
populations (theoretical utopia) vs. samples (your messy spreadsheet data).

#### Population and Samples

> Statistical Properties

Statistic differ between population and samples.
For least squares, the calculation is the same,
even though the notation is different. 
For example the `Mean` notation.

Here's how statisticians distinguish between perfection and reality:

$$
\begin{align}
\begin{aligned}
&\text{Mean (Average):} \\
&\begin{array}{|c|c|}
\hline
\mathrm{\textbf{Population}} & \mathrm{\textbf{Sample}} \\
\hline
\mu = \frac{1}{N}\sum\limits_{i=1}^{N} x_i &
\bar{x} = \frac{1}{n}\sum\limits_{i=1}^{n} x_i \\
\hline
\end{array}
\end{aligned}
\end{align}
$$

Where

* μ (mu): The true average, as seen by an all, knowing statistical deity.
* x̄ (x-bar): Your best guess, based on whatever you scraped off a CSV file.

Notation impacts formulas,
especially when calculating things like variance, 
regression coefficients, and correlation.
Where degrees of freedom lurk,
like surprise plot twists in a statistics textbook.

For correlation and regression,
the equation has different degree of freedom.
This means, the equation is different.
We will talk about this later.

-- -- --

### 2: The Math Behind

> Which Least Square

Even least squares come in multiple flavors.
Like yogurt, but for math.

When it comes to solving least squares,
statisticians have options.
And by _options_, we mean slightly different ways,
to arrive at exactly the same answer.
Because math, like bureaucracy, loves redundancy.

Here are three friendly paths to the truth:

1. Direct Equation Derivation:
   algebra straight from calculus.

2. Equation Using Means:
   tidy, intuitive, and easier on the eyes.

3. Matrix Method:
   for when you're feeling fancy
   (or lazy, thanks to Excel and Python).



All three have the same result,
and with spreadsheet we can calculate with any method easily.
You can choose what equation suitable for your case.

Whichever method you pick,
they'll all walk you to the same solution.
That's the beauty of math.
Everyone disagrees on the path,
but we all end up at the same sad residuals.

#### Worksheet Source

> Playsheet Artefact

Yes, the spreadsheet exists.
And yes, it's editable.
Because what good is math if you can't poke at it?

* **github.com/.../math/trend/least-square.xlsx**

Go wild. Or at least, copy-paste responsibly.

#### Slope and Intercept

Let's say you've got a bunch of data points (x, y).
You want to find the best straight line that captures their general vibe.

$$
y = mx + b
$$

With the same x, from observed value (x,y), we can get the prediction value of y.
Now we have two kind of y, the observed value as the calculation source,
and the predicted value as the result of the curve fitting equation.

$$
\begin{array}{|c|c|}
\hline
x_i & \textbf{observed x} \\
\hline
y_i & \textbf{observed y} \\
\hline
\hat{y}_i & \textbf{predicted y}  \\
\hline
\end{array}
$$

Where:
* xᵢ: observed x-values (a.k.a. your independent variable)
* yᵢ: observed y-values (the thing you care about)
* ŷᵢ: predicted y-values from the fitted line

The fit equation for the predicted y value (ŷᵢ):

$$
\hat{y}_i = mx_i + b
$$

#### Residual

> Because data is never fully obedient.

Real-world data never falls perfectly on your line,
unless you're cheating.
The residual is the amount by which each point rebels:

The formula for the slope (m) and intercept (b) of the least squares regression line,
can be derived from the principle of minimizing the sum of squared errors (residuals) ,
etween the observed values of y and the values predicted by the regression line.

The residual for each observation is,
the difference between the observed value of y and the predicted value of y:

$$
e_i = y_i - \hat{y}_i
$$

The sum of squared residuals (SSE) is defined as:

$$
SSE = \sum\limits_{i=1}^{n} (e_i)^2 = \sum\limits_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

Our goal is to minimize SSE by choosing appropriate values of m and b
To find the values of m and b that minimize SSE,
we take the derivatives of SSE with respect to m and b and set them both equal to zero:

$$
\begin{align*}
\frac{\partial SSE}{\partial m} = 0 &&
\frac{\partial SSE}{\partial b} = 0
\end{align*}
$$

We take derivatives,
and pretend we're solving for enlightenment.

#### Direct Equation

> Algebra, the Original Regression Tool™

Solving these equations simultaneously will,
give us the values of m and b that minimize SSE, 
hich are the least squares estimates of the slope and intercept.

After some algebraic manipulation,
dark magic and friendly spirit,
the formulas for m and b can be derived as:

$$
\begin{align*}
m &= \frac{n\sum{xy} - \sum{x}\sum{y}}{n\sum{x^2} - (\sum{x})^2} \\

b &= \frac{\sum{y} - m\sum{x}}{n}
\end{align*}
$$

Great for spreadsheets. Easy to compute.
Even easier to impress your manager with.

#### Equation with Mean

> For those who prefer elegance over raw sums.

This version centers around sample means,
and offers slightly more interpretable mat
(and maybe less typing):

$$
\begin{align*}
m &= \frac{\sum{(x_i - \bar{x})(y_i - \bar{y})}}{\sum{(x_i - \bar{x})^2}} \\

b &= \bar{y} - m\bar{x}
\end{align*}
$$

Perfect if you enjoy statistics and symmetry.

#### Matrix of System

> When your data wants to feel like linear algebra.

Same result, but now it looks smarter.
The least squares solution for linear regression can be derived using matrix notation.
In matrix notation, the equations are represented as:

$$
\begin{bmatrix}
n & \sum{x_i} \\
\sum{x_i} & \sum{x_i^2}
\end{bmatrix}
\begin{bmatrix}
b \\
m
\end{bmatrix}
=
\begin{bmatrix}
\sum{y_i} \\
\sum{x_i y_i}
\end{bmatrix}
$$

Solve `m` and `b` using matrix inversion:
The solution is given by:

$$
\begin{bmatrix}
b \\
m
\end{bmatrix}
=
\begin{bmatrix}
n & \sum{x_i} \\
\sum{x_i} & \sum{x_i^2}
\end{bmatrix}^{-1}
\begin{bmatrix}
\sum{y_i} \\
\sum{x_i y_i}
\end{bmatrix}
$$

Those three are the same least square equations.
Those would produce the same result.
There are other approach as well in the realm of least square,
but let's skip them this time.

#### Which Equation Should I Use?

As a summary

* Direct formula? Great for worksheets.
* Mean-based? More intuitive and elegant.
* Matrix form? Flexible, programmable, and scalable.

Use whichever fits your current mood, or spreadsheet layout.
Just remember: they all land on the same best-fit line.
And that's the least you can expect from least squares.

-- -- --

### 3: Direct Solution

Let's put all that beautiful theory to work,
and calculate a real least squares regression line using the direct formula.
Time to trade talking for tallying.

#### Known Values

Suppose you've collected this pristine (and suspiciously well-behaved) data set:

**(x, y)** = [(0, 5), (1, 12), (2, 25), (3, 44), (4, 69), (5, 100), (6, 137), (7, 180), (8, 229), (9, 284), (10, 345), (11, 412), (12, 485)]

If that looks like a quadratic curve wearing a linear disguise...
Well, you're not wrong.
But remember: we're only fitting a line,
no matter how the data screams otherwise.

First, let's get our stats straight:

$$
\begin{align*}
n = 13 &&
\sum x = 78 &&
\sum y = 2327 &&
\end{align*}
$$

For completeness (and spreadsheet nerds),
here's how those quantities are defined:

$$
\begin{align*}
\text{count} = \sum\limits_{i=1}^{n} 1 &&
\text{sum}_{x} = \sum\limits_{i=1}^{n} x_i &&
\text{sum}_{y} = \sum\limits_{i=1}^{n} y_i &&
\end{align*}
$$

In Excel (or LibreOffice Calc),
this translates to plain old `=COUNT(...)` and `=SUM(...)`.
You don't even need to remember the formulas,
just remember where your mouse is.



#### Tabular Calculation

Time to bring out the heavy artillery:
the direct equation for slope `(m`) and intercept (`b)`.

$$
\begin{align*}
m &= \frac{n\sum{xy} - \sum{x}\sum{y}}{n\sum{x^2} - (\sum{x})^2} \\
b &= \frac{\sum{y} - m\sum{x}}{n}
\end{align*}
$$

Now, let's add a few more ingredients to our sum soup.
We can calculate further:

$$
\begin{align*}
n &= 13 \\
\sum x &= 78 \\
\sum y &= 2327 \\
\sum (x)^2 &= 650 \\
\sum (x.y) &= 21242 \\
\end{align*}
$$

Let's plug it all into the blender (a.k.a. the formula) and see what comes out.

#### Calculating the Slope (m)

Now we can calculate, the m (slope):

$$
\begin{align*}
m &= \frac{(13 \times 21242) - (78 \times 2327)}{(13 \times 650 - (78)^2} \\
  &= \frac{276146 - 181506}{8450 - 6084} \\
  &= \frac{94640}{2366} \\
  &= 40.0
\end{align*}
$$

You read that right.
Exactly 40. The math gods are smiling.

#### Calculating the Intercept (b)

And also the b (intercept):

$$
\begin{align*}
b &= \frac{\sum{y} - m\sum{x}}{n} \\
  &= \frac{2327 - 40 \times 78}{13} \\
  &= \frac{-793}{13} \\
  &= -61
\end{align*}
$$

A negative intercept?
Yep. The line starts in debt. Relatable.

#### Final Regression Equation

Putting it all together,
our least-squares linear model is:

$$
y = -61 + 40x
$$

This line won't pass through every point (it's not supposed to!),
but it will minimize the total squared error across all of them.
That's what least squares is all about: fitting best, not perfectly.



With tabular calculation in a spreadsheet,
you can arrive at the exact same equation.
Now you can see how easy it is,
to write down the equation in tabular spreadsheet form.

-- -- --

### 4: Solution Using Mean

> Where averages do all the heavy lifting.

This is easy when you want to combine,
with tabular calculation of regression and correlation.

#### Tabular Calculation

The least squares regression line (y = mx + b),
can be found more gracefully using sample means.
This method skips some of the clunky summing of products and squares,
in favor of centering the data.

1.  Calculate the mean of x and y

$$
\bar{x} = \frac{1}{n} \sum\limits_{i=1}^{n} x_i
$$

$$
\bar{y} = \frac{1}{n} \sum\limits_{i=1}^{n} y_i
$$

2.  Calculate the slope (m)

$$
m = \frac{\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum\limits_{i=1}^{n} (x_i - \bar{x})^2}
$$

3.  Calculate the y-intercept (b)

$$
b = \bar{y} - m\bar{x}
$$

The final equation for the least squares regression line is:

$$
y = mx + b
$$

Now let's calculate the statistic properties for given data point above:

$$
\begin{align*}
n &= 13 \\
\sum x &= 78 \\
\sum y &= 2327 \\
\bar{x} &= 6 \\
\bar{y} &= 179 \\
\end{align*}
$$

And also:

$$
\begin{align*}
\sum{(x_i - \bar{x})^2} &= 182 \\
\sum{(x_i - \bar{x})(y_i - \bar{y})} &= 7280 \\
\end{align*}
$$

Now we can calculate, the m (slope):

$$
\begin{align*}
m &= \frac{7280}{182} \\
  &= 40.0
\end{align*}
$$

and the b (intercept):

$$
\begin{align*}
b &= \bar{y} - m\bar{x} \\
  &= 179 - 40 \times 6 \\
  &= -61
\end{align*}
$$

#### Spreadsheet View

Tabular calculation in Excel (or Calc)
makes this method super approachable,
and easier to audit when your regression line goes rogue:



When your data behaves reasonably
(and doesn't come with drama),
this method is clean, elegant, and friendly,
even to your future self looking back at the spreadsheet next week.

-- -- --

### 5: Solution Using Matrix

This is suitable as a basis,
when you need to extend to non linier curve fitting.

This method isn't just for the mathematically elite.
It's the foundation for curve fitting beyond straight lines.
Think of it as the gateway drug to polynomial regression,
splines, and your favorite buzzword: _machine learning_.

#### Tabular Calculation

Matrix form might look intimidating, but under the hood,
it's the same old least squares.
It also scales beautifully
when you move past linear trends into higher orders.

Let's revisit the matrix equation:

$$
\begin{bmatrix}
n & \sum{x_i} \\
\sum{x_i} & \sum{x_i^2}
\end{bmatrix}
\begin{bmatrix}
b \\
m
\end{bmatrix}
=
\begin{bmatrix}
\sum{y_i} \\
\sum{x_i y_i}
\end{bmatrix}
$$

Yes, this is still the good old `y = mx + b`,
just dressed up in its linear algebra tuxedo.

Now, applying actual numbers from our trusty dataset,
getting the m (slope) and b(intercept), using matrix inversion.

$$
\begin{array}{cc}
&
\begin{bmatrix}
13 & 78 \\
78 & 650
\end{bmatrix}
\begin{bmatrix}
b \\
m
\end{bmatrix}
=
\begin{bmatrix}
2327 \\
21242
\end{bmatrix} \\
\Rightarrow &
\begin{bmatrix}
b \\
m
\end{bmatrix}
=
\begin{bmatrix}
13 & 78 \\
78 & 650
\end{bmatrix}^{-1}
\begin{bmatrix}
2327 \\
21242
\end{bmatrix}
=
\begin{bmatrix}
-61 \\
40
\end{bmatrix}
\end{array}
$$

We arrive at the same solution as before:

* Slope (m) = 40, Intercept (b) = -61

Linear algebra: different route, same destination. Except this road is paved for scaling up.

#### Spreadsheet View

Even Excel's formula engine can handle this
with a few matrix tricks: `MMULT`, `MINVERSE`,
and the occasional coffee break while debugging array formulas.



#### Why It's a Big Deal

While you might not need the matrix form for a single line,
it's your golden ticket when the model evolves:

* Need to fit a parabola?
  Matrix.

* Multiple x variables?
  Matrix.

* Polynomial regression with terms up to x^10?
  You guessed it. Matrix.

Neo had to choose the red pill.
You? You just need `MINVERSE()`.

-- -- --

### 6: Built-in Formula

_When you love stats, but also love letting Excel do the heavy lifting._

Let's be honest: sometimes we don't want to manually crank,
through all the sums, products, and parentheses.
Sometimes, we want to tell our spreadsheet,
"_Figure it out_," and let the magic happen.

The good news is,
Excel (or Calc, if you're open source and proud) has use covered.

#### First Things First

>  The Basics

Before jumping to the fancy built-ins,
let's warm up with the classics.



Grab the totals and averages for `x` and `y`,
like you're stretching before a marathon of regression.

| Properties | x Formula        | y Formula         |
|------------|------------------|-------------------|
| Total      | =SUM(B7:B19)     | =SUM(C7:C19)      |
| Count      | =COUNT(B7:B19)   | =COUNT(C7:C19)    |
| Mean       | =AVERAGE(B7:B19) | =AVERAGE(C7:C19)  |

Even if we're using `AVERAGE`,
it's good practice to know the underlying logic.
Especially if we'll be coding this later,
in Python, R, or whispering to pandas.

In fact, here's how we can calculate the mean without `AVERAGE`
(yes, sometimes we like to flex on basic functions):

| Properties | Formula                    |
|------------|----------------------------|
| Mean x     | =SUM(B7:B19)/COUNT(B7:B19) |
| Mean y     | =SUM(C7:C19)/COUNT(C7:C19) |

### Built-in Regression

> No Pain, All Gain

Now we get to the really lazy part. 
I mean efficient, part.
Excel has built-in regression functions,
that give use slope and intercept in one clean shot.

Just remember: for array operation formulas, 
hit `Ctrl+Shift+Enter` or Excel will pretend you never asked.

| Properties    | Formula                     |
|---------------|-----------------------------|
| slope (m)     | {=SLOPE(C7:C19;B7:B19)}     |
| intercept (b) | {=INTERCEPT(C7:C19;B7:B19)} |

If we're testing many data sets or building a dashboard,
these functions are fast, reliable,
and save us from spreadsheet-induced carpal tunnel.

#### For the Brave

> Manual Calculation

Want to see how the built-ins work under the hood?
Try calculating it yourself using mean-centered values:

| Properties    | Formula                    |
|---------------|----------------------------|
| slope (m)     | =SUM((B7:B19 - G10)*(C7:C19 - H10))/SUM((B7:B19 - G10)^2) |
| intercept (b) | =H9-G14*G9 |

We're subtracting the mean, multiplying, summing,
conducting a tiny symphony of statistics.

#### Final Thoughts

That's it for now.
Whether we're letting Excel take the wheel,
or crunching numbers the old-fashioned way,
we've got solid tools for fitting a line.

Next up? We will turn the volume up,
and explore regression and correlation.
Dive into more complex formula,
where the real drama of data begins.

-- -- --

### 7: Python

So, what's happened when,
spreadsheets just aren't satisfying,
for our craving for automation and repeatability.

Python offers several ways to perform least squares regression,
ranging from the "_I trust NumPy with my life_" approach,
to "_let's see the residuals and p-values too, please._"

We'll look at:

* `numpy.polyfit` or `Polynomial.fit`:
   Quick and clean.

* `scipy.stats.linregress`
  Lightweight but statistically aware.

* `statsmodels.api.OLS`
  Heavy artillery for full statistical modeling.

You can follow along with the full script here:

* **41-least-square.py**

```python
import numpy as np
import statsmodels.api as sm

from scipy import stats

# Given data
x_values = np.array(
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y_values = np.array(
  [5, 12, 25, 44, 69, 100, 137,
    180, 229, 284, 345, 412, 485])

# Perform least squares regression
# for a linear model (polynomial degree 1)
order = 1
mC    = np.polyfit(x_values, y_values, deg=order)
m     = mC[0]
b     = mC[1]

print('Using polyfit')
print(f'Coefficients (b = {b:2,.2f}, m = {m:2,.2f})\n')

# SciPy: scientific computing built on top of NumPy.
m, b, _, _, _ = stats.linregress(x_values, y_values)

print('Using linregress')
print(f'Coefficients (b = {b:2,.2f}, m = {m:2,.2f})\n')

# Statsmodels: statistical modeling and hypothesis testing.
x = sm.add_constant(x_values)
model = sm.OLS(y_values, x).fit()
b = model.params[0]
m = model.params[1]

print('Using Statsmodels')
print(f'Coefficients (b = {b:2,.2f}, m = {m:2,.2f})\n')
```

Let's start with some data.
Think of this as our patient zero in a curve-fitting,
during current pandemic.

```python
# Given data
x_values = np.array(
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y_values = np.array(
  [5, 12, 25, 44, 69, 100, 137,
    180, 229, 284, 345, 412, 485])
```



#### Polyfit

> Fast, friendly, and polynomial-curious.

If you just want the best-fit line,
and don't need to explain it to your thesis advisor,
`numpy.polyfit` is your go-to.

```python
import numpy as np

# Perform least squares regression
# for a linear model (polynomial degree 1)
order = 1
mC    = np.polyfit(x_values, y_values, deg=order)
m     = mC[0]
b     = mC[1]

print('Using polyfit')
print(f'Coefficients (b = {b:2,.2f}, m = {m:2,.2f})\n')
```

Quick prototyping.
Great for trendlines.
And yes, it works for higher-degree polynomials too.
Just in case our data starts curving like a rollercoaster.



Note: Please be prepate for `polyfit` replacement called `Polynomial.fit`.

#### Linregress

> Like `polyfit`, but wears a lab coat.

`scipy.stats.linregress` gives us
slope, intercept, and bonus goodies like r-value and standard error.
Use it when we want our math to sound more "_peer-reviewable._"

```python
from scipy import stats

# SciPy: scientific computing built on top of NumPy.
m, b, _, _, _ = stats.linregress(x_values, y_values)

print('Using linregress')
print(f'Coefficients (b = {b:2,.2f}, m = {m:2,.2f})\n')
```



Ideal for statistical analysis with minimal fuss.
Also lets us pretend we're doing something much more complicated than we are.

#### OLS

Sometimes we want the full regression buffet,
not just the drive-thru.

For those of us who like residual plots, confidence intervals,
and enough statistical output to paper a conference,
statsmodels has us covered.

```python
import statsmodels.api as sm

# Statsmodels: statistical modeling and hypothesis testing.
x = sm.add_constant(x_values)
model = sm.OLS(y_values, x).fit()
b = model.params[0]
m = model.params[1]

print('Using Statsmodels')
print(f'Coefficients (b = {b:2,.2f}, m = {m:2,.2f})\n')
```

This is the professional toolkit.
We will want this when we start checking assumptions,
diagnosing models, or trying to impress our statistical consultant.



And voilà, no matter how we slice it.
NumPy, SciPy, or Statsmodels,
we end up with the same tidy equation:

```output
Using polyfit
Coefficients (b = -61.00, m = 40.00)

Using linregress
Coefficients (b = -61.00, m = 40.00)

Using Statsmodels
Coefficients (b = -61.00, m = 40.00)
```

Consistent results across different tools is a great sanity check,
especially if our sanity depends on reproducible results.



There is no need for fancy chart plot this time.

You can obtain the interactive `JupyterLab` in this following link:

* **41-least-square.py**

#### Manual Calculation

> For the Purists

When deep down, you don't trust functions,
unless you've re-derived them in a dimly lit lab.

Let's go back to first principles.
Here's how we'd do it ourself.
No black boxes, just beautiful algebra.

* **42-least-square.py**

```python
import numpy as np

# Given data
x_values = np.array(
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y_values = np.array(
  [5, 12, 25, 44, 69, 100, 137,
    180, 229, 284, 345, 412, 485])

# Number of data points
n = len(x_values)

# Calculate sums
sum_x = np.sum(x_values)
sum_y = np.sum(y_values)

# Calculate means
mean_x = np.mean(x_values)
mean_y = np.mean(y_values)

# Output of basic properties
print(f'f{"n":1s} = {n:5d}')
print(f'∑x (total) = {sum_x:7.2f}')
print(f'∑y (total) = {sum_y:7.2f}')
print(f'x̄ (mean)   = {mean_x:7.2f}')
print(f'ȳ (mean)   = {mean_y:7.2f}')
print()

# Calculate deviations
deviation_x = x_values - mean_x
deviation_y = y_values - mean_y

# Calculate squared deviations
sq_deviation_x = np.sum(deviation_x ** 2)

# Calculate cross-deviation
cross_deviation_xy = np.sum(deviation_x * deviation_y)

# Calculate slope (m) and intercept (b)
slope_m = cross_deviation_xy / sq_deviation_x
intercept_b = mean_y - slope_m * mean_x

print('Manual Calculation')
print(f'Coefficients (b = {intercept_b:2,.2f},'
    + f' m = {slope_m:2,.2f})\n')
```

First we calculate basic statistic properties.

```python
# Number of data points
n = len(x_values)

# Calculate sums
sum_x = np.sum(x_values)
sum_y = np.sum(y_values)

# Calculate means
mean_x = np.mean(x_values)
mean_y = np.mean(y_values)

# Output of basic properties
print(f'n = {n:5d}')
print(f'∑x (total) = {sum_x:7.2f}')
print(f'∑y (total) = {sum_y:7.2f}')
print(f'x̄ (mean)   = {mean_x:7.2f}')
print(f'ȳ (mean)   = {mean_y:7.2f}')
print()
```



Then go further, bring in the deviations:

```python
# Calculate deviations
deviation_x = x_values - mean_x
deviation_y = y_values - mean_y

# Calculate squared deviations
sq_deviation_x = np.sum(deviation_x ** 2)

# Calculate cross-deviation
cross_deviation_xy = np.sum(deviation_x * deviation_y)

# Calculate slope (m) and intercept (b)
slope_m = cross_deviation_xy / sq_deviation_x
intercept_b = mean_y - slope_m * mean_x

print('Manual Calculation')
print(f'Coefficients (b = {intercept_b:2,.2f},'
    + f' m = {slope_m:2,.2f})\n')
```

Manual calculation reinforces understanding
of the math behind the tools.
Also, great for debugging or impressing
our coworkers with a "_I did this without NumPy_" moment.



And here's the proof it worked:

```output
n =    13
∑x (total) =   78.00
∑y (total) = 2327.00
x̄ (mean)   =    6.00
ȳ (mean)   =  179.00

Manual Calculation
Coefficients (b = -61.00, m = 40.00)
```



Need to test or tinker interactively?
Fire up these `Jupyter Notebooks` and experiment like a modern-day Gauss:

* **42-least-square.py**

We take this straight line obsession further,
with regression, correlation, and maybe even 
the mysterious world of non-linear fitting.
Are you ready to curve things up?

-- -- --

### Where Do We Go From Here 🤔?

Now that we've bravely tamed the Least Squares beast,
let's talk about what lies ahead in our adventure.

We've taken a mathematical equation,
made it practical (because who doesn't love practical?),
turned it into a neat spreadsheet (tabular bliss, am I right?),
and even whipped up some Python code.
That's like the statistical equivalent of baking a cake from scratch,
but with fewer crumbs and more data insights.

And the best part? It's fun, right?
The kind of fun that only comes from numbers and formulas working together,
like a well-oiled machine. Ah, the joy of regression lines...

Now that we've conquered the basics,
we can explore even more statistical properties.
Regression and correlation are just the beginning.
We can dig deeper into the data,
and start exploring how variables relate to each other,
why they relate (or don't),
and how much faith we can place in our model's predictions.
Trust but verify, that's the statistician's mantra.

But don't worry,
the journey isn't over yet!
If we're still hungry for more statistical wizardry,
take a detour over to **Trend - Properties - Cheatsheet**.

It's like the ultimate guidebook for your next steps in the land of data trends.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Curve fitting examples for daily basis,
> using least squares method.

I'm not a statistician,
though I do occasionally dress like one (corduroy optional).
That's why when I do talk about statistics, I tread carefully.

We will start by laying out the math,
because math doesn't lie, only people misinterpret it.
Then move to spreadsheet implementation
using Calc (which plays nicely with Excel).
And finally round things off with a bit of Python scripting.
All practical, all grounded, and no asymptotic nonsense (yet).

From here, we will gracefully tiptoe,
into regression analysis and correlation

-- -- --

### 1: Statistic Notation

Before we hurl ourselves at least squares,
we need to brush up on the two pillars of statistical awkwardness:
populations (theoretical utopia) vs. samples (your messy spreadsheet data).

#### Population and Samples

> Statistical Properties

Statistic differ between population and samples.
For least squares, the calculation is the same,
even though the notation is different. 
For example the `Mean` notation.

Here's how statisticians distinguish between perfection and reality:

$$
\begin{align}
\begin{aligned}
&\text{Mean (Average):} \\
&\begin{array}{|c|c|}
\hline
\mathrm{\textbf{Population}} & \mathrm{\textbf{Sample}} \\
\hline
\mu = \frac{1}{N}\sum\limits_{i=1}^{N} x_i &
\bar{x} = \frac{1}{n}\sum\limits_{i=1}^{n} x_i \\
\hline
\end{array}
\end{aligned}
\end{align}
$$

Where

* μ (mu): The true average, as seen by an all, knowing statistical deity.
* x̄ (x-bar): Your best guess, based on whatever you scraped off a CSV file.

Notation impacts formulas,
especially when calculating things like variance, 
regression coefficients, and correlation.
Where degrees of freedom lurk,
like surprise plot twists in a statistics textbook.

For correlation and regression,
the equation has different degree of freedom.
This means, the equation is different.
We will talk about this later.

-- -- --

### 2: The Math Behind

> Which Least Square

Even least squares come in multiple flavors.
Like yogurt, but for math.

When it comes to solving least squares,
statisticians have options.
And by _options_, we mean slightly different ways,
to arrive at exactly the same answer.
Because math, like bureaucracy, loves redundancy.

Here are three friendly paths to the truth:

1. Direct Equation Derivation:
   algebra straight from calculus.

2. Equation Using Means:
   tidy, intuitive, and easier on the eyes.

3. Matrix Method:
   for when you're feeling fancy
   (or lazy, thanks to Excel and Python).



All three have the same result,
and with spreadsheet we can calculate with any method easily.
You can choose what equation suitable for your case.

Whichever method you pick,
they'll all walk you to the same solution.
That's the beauty of math.
Everyone disagrees on the path,
but we all end up at the same sad residuals.

#### Worksheet Source

> Playsheet Artefact

Yes, the spreadsheet exists.
And yes, it's editable.
Because what good is math if you can't poke at it?

* **github.com/.../math/trend/least-square.xlsx**

Go wild. Or at least, copy-paste responsibly.

#### Slope and Intercept

Let's say you've got a bunch of data points (x, y).
You want to find the best straight line that captures their general vibe.

$$
y = mx + b
$$

With the same x, from observed value (x,y), we can get the prediction value of y.
Now we have two kind of y, the observed value as the calculation source,
and the predicted value as the result of the curve fitting equation.

$$
\begin{array}{|c|c|}
\hline
x_i & \textbf{observed x} \\
\hline
y_i & \textbf{observed y} \\
\hline
\hat{y}_i & \textbf{predicted y}  \\
\hline
\end{array}
$$

Where:
* xᵢ: observed x-values (a.k.a. your independent variable)
* yᵢ: observed y-values (the thing you care about)
* ŷᵢ: predicted y-values from the fitted line

The fit equation for the predicted y value (ŷᵢ):

$$
\hat{y}_i = mx_i + b
$$

#### Residual

> Because data is never fully obedient.

Real-world data never falls perfectly on your line,
unless you're cheating.
The residual is the amount by which each point rebels:

The formula for the slope (m) and intercept (b) of the least squares regression line,
can be derived from the principle of minimizing the sum of squared errors (residuals) ,
etween the observed values of y and the values predicted by the regression line.

The residual for each observation is,
the difference between the observed value of y and the predicted value of y:

$$
e_i = y_i - \hat{y}_i
$$

The sum of squared residuals (SSE) is defined as:

$$
SSE = \sum\limits_{i=1}^{n} (e_i)^2 = \sum\limits_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

Our goal is to minimize SSE by choosing appropriate values of m and b
To find the values of m and b that minimize SSE,
we take the derivatives of SSE with respect to m and b and set them both equal to zero:

$$
\begin{align*}
\frac{\partial SSE}{\partial m} = 0 &&
\frac{\partial SSE}{\partial b} = 0
\end{align*}
$$

We take derivatives,
and pretend we're solving for enlightenment.

#### Direct Equation

> Algebra, the Original Regression Tool™

Solving these equations simultaneously will,
give us the values of m and b that minimize SSE, 
hich are the least squares estimates of the slope and intercept.

After some algebraic manipulation,
dark magic and friendly spirit,
the formulas for m and b can be derived as:

$$
\begin{align*}
m &= \frac{n\sum{xy} - \sum{x}\sum{y}}{n\sum{x^2} - (\sum{x})^2} \\

b &= \frac{\sum{y} - m\sum{x}}{n}
\end{align*}
$$

Great for spreadsheets. Easy to compute.
Even easier to impress your manager with.

#### Equation with Mean

> For those who prefer elegance over raw sums.

This version centers around sample means,
and offers slightly more interpretable mat
(and maybe less typing):

$$
\begin{align*}
m &= \frac{\sum{(x_i - \bar{x})(y_i - \bar{y})}}{\sum{(x_i - \bar{x})^2}} \\

b &= \bar{y} - m\bar{x}
\end{align*}
$$

Perfect if you enjoy statistics and symmetry.

#### Matrix of System

> When your data wants to feel like linear algebra.

Same result, but now it looks smarter.
The least squares solution for linear regression can be derived using matrix notation.
In matrix notation, the equations are represented as:

$$
\begin{bmatrix}
n & \sum{x_i} \\
\sum{x_i} & \sum{x_i^2}
\end{bmatrix}
\begin{bmatrix}
b \\
m
\end{bmatrix}
=
\begin{bmatrix}
\sum{y_i} \\
\sum{x_i y_i}
\end{bmatrix}
$$

Solve `m` and `b` using matrix inversion:
The solution is given by:

$$
\begin{bmatrix}
b \\
m
\end{bmatrix}
=
\begin{bmatrix}
n & \sum{x_i} \\
\sum{x_i} & \sum{x_i^2}
\end{bmatrix}^{-1}
\begin{bmatrix}
\sum{y_i} \\
\sum{x_i y_i}
\end{bmatrix}
$$

Those three are the same least square equations.
Those would produce the same result.
There are other approach as well in the realm of least square,
but let's skip them this time.

#### Which Equation Should I Use?

As a summary

* Direct formula? Great for worksheets.
* Mean-based? More intuitive and elegant.
* Matrix form? Flexible, programmable, and scalable.

Use whichever fits your current mood, or spreadsheet layout.
Just remember: they all land on the same best-fit line.
And that's the least you can expect from least squares.

-- -- --

### 3: Direct Solution

Let's put all that beautiful theory to work,
and calculate a real least squares regression line using the direct formula.
Time to trade talking for tallying.

#### Known Values

Suppose you've collected this pristine (and suspiciously well-behaved) data set:

**(x, y)** = [(0, 5), (1, 12), (2, 25), (3, 44), (4, 69), (5, 100), (6, 137), (7, 180), (8, 229), (9, 284), (10, 345), (11, 412), (12, 485)]

If that looks like a quadratic curve wearing a linear disguise...
Well, you're not wrong.
But remember: we're only fitting a line,
no matter how the data screams otherwise.

First, let's get our stats straight:

$$
\begin{align*}
n = 13 &&
\sum x = 78 &&
\sum y = 2327 &&
\end{align*}
$$

For completeness (and spreadsheet nerds),
here's how those quantities are defined:

$$
\begin{align*}
\text{count} = \sum\limits_{i=1}^{n} 1 &&
\text{sum}_{x} = \sum\limits_{i=1}^{n} x_i &&
\text{sum}_{y} = \sum\limits_{i=1}^{n} y_i &&
\end{align*}
$$

In Excel (or LibreOffice Calc),
this translates to plain old `=COUNT(...)` and `=SUM(...)`.
You don't even need to remember the formulas,
just remember where your mouse is.



#### Tabular Calculation

Time to bring out the heavy artillery:
the direct equation for slope `(m`) and intercept (`b)`.

$$
\begin{align*}
m &= \frac{n\sum{xy} - \sum{x}\sum{y}}{n\sum{x^2} - (\sum{x})^2} \\
b &= \frac{\sum{y} - m\sum{x}}{n}
\end{align*}
$$

Now, let's add a few more ingredients to our sum soup.
We can calculate further:

$$
\begin{align*}
n &= 13 \\
\sum x &= 78 \\
\sum y &= 2327 \\
\sum (x)^2 &= 650 \\
\sum (x.y) &= 21242 \\
\end{align*}
$$

Let's plug it all into the blender (a.k.a. the formula) and see what comes out.

#### Calculating the Slope (m)

Now we can calculate, the m (slope):

$$
\begin{align*}
m &= \frac{(13 \times 21242) - (78 \times 2327)}{(13 \times 650 - (78)^2} \\
  &= \frac{276146 - 181506}{8450 - 6084} \\
  &= \frac{94640}{2366} \\
  &= 40.0
\end{align*}
$$

You read that right.
Exactly 40. The math gods are smiling.

#### Calculating the Intercept (b)

And also the b (intercept):

$$
\begin{align*}
b &= \frac{\sum{y} - m\sum{x}}{n} \\
  &= \frac{2327 - 40 \times 78}{13} \\
  &= \frac{-793}{13} \\
  &= -61
\end{align*}
$$

A negative intercept?
Yep. The line starts in debt. Relatable.

#### Final Regression Equation

Putting it all together,
our least-squares linear model is:

$$
y = -61 + 40x
$$

This line won't pass through every point (it's not supposed to!),
but it will minimize the total squared error across all of them.
That's what least squares is all about: fitting best, not perfectly.



With tabular calculation in a spreadsheet,
you can arrive at the exact same equation.
Now you can see how easy it is,
to write down the equation in tabular spreadsheet form.

-- -- --

### 4: Solution Using Mean

> Where averages do all the heavy lifting.

This is easy when you want to combine,
with tabular calculation of regression and correlation.

#### Tabular Calculation

The least squares regression line (y = mx + b),
can be found more gracefully using sample means.
This method skips some of the clunky summing of products and squares,
in favor of centering the data.

1.  Calculate the mean of x and y

$$
\bar{x} = \frac{1}{n} \sum\limits_{i=1}^{n} x_i
$$

$$
\bar{y} = \frac{1}{n} \sum\limits_{i=1}^{n} y_i
$$

2.  Calculate the slope (m)

$$
m = \frac{\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum\limits_{i=1}^{n} (x_i - \bar{x})^2}
$$

3.  Calculate the y-intercept (b)

$$
b = \bar{y} - m\bar{x}
$$

The final equation for the least squares regression line is:

$$
y = mx + b
$$

Now let's calculate the statistic properties for given data point above:

$$
\begin{align*}
n &= 13 \\
\sum x &= 78 \\
\sum y &= 2327 \\
\bar{x} &= 6 \\
\bar{y} &= 179 \\
\end{align*}
$$

And also:

$$
\begin{align*}
\sum{(x_i - \bar{x})^2} &= 182 \\
\sum{(x_i - \bar{x})(y_i - \bar{y})} &= 7280 \\
\end{align*}
$$

Now we can calculate, the m (slope):

$$
\begin{align*}
m &= \frac{7280}{182} \\
  &= 40.0
\end{align*}
$$

and the b (intercept):

$$
\begin{align*}
b &= \bar{y} - m\bar{x} \\
  &= 179 - 40 \times 6 \\
  &= -61
\end{align*}
$$

#### Spreadsheet View

Tabular calculation in Excel (or Calc)
makes this method super approachable,
and easier to audit when your regression line goes rogue:



When your data behaves reasonably
(and doesn't come with drama),
this method is clean, elegant, and friendly,
even to your future self looking back at the spreadsheet next week.

-- -- --

### 5: Solution Using Matrix

This is suitable as a basis,
when you need to extend to non linier curve fitting.

This method isn't just for the mathematically elite.
It's the foundation for curve fitting beyond straight lines.
Think of it as the gateway drug to polynomial regression,
splines, and your favorite buzzword: _machine learning_.

#### Tabular Calculation

Matrix form might look intimidating, but under the hood,
it's the same old least squares.
It also scales beautifully
when you move past linear trends into higher orders.

Let's revisit the matrix equation:

$$
\begin{bmatrix}
n & \sum{x_i} \\
\sum{x_i} & \sum{x_i^2}
\end{bmatrix}
\begin{bmatrix}
b \\
m
\end{bmatrix}
=
\begin{bmatrix}
\sum{y_i} \\
\sum{x_i y_i}
\end{bmatrix}
$$

Yes, this is still the good old `y = mx + b`,
just dressed up in its linear algebra tuxedo.

Now, applying actual numbers from our trusty dataset,
getting the m (slope) and b(intercept), using matrix inversion.

$$
\begin{array}{cc}
&
\begin{bmatrix}
13 & 78 \\
78 & 650
\end{bmatrix}
\begin{bmatrix}
b \\
m
\end{bmatrix}
=
\begin{bmatrix}
2327 \\
21242
\end{bmatrix} \\
\Rightarrow &
\begin{bmatrix}
b \\
m
\end{bmatrix}
=
\begin{bmatrix}
13 & 78 \\
78 & 650
\end{bmatrix}^{-1}
\begin{bmatrix}
2327 \\
21242
\end{bmatrix}
=
\begin{bmatrix}
-61 \\
40
\end{bmatrix}
\end{array}
$$

We arrive at the same solution as before:

* Slope (m) = 40, Intercept (b) = -61

Linear algebra: different route, same destination. Except this road is paved for scaling up.

#### Spreadsheet View

Even Excel's formula engine can handle this
with a few matrix tricks: `MMULT`, `MINVERSE`,
and the occasional coffee break while debugging array formulas.



#### Why It's a Big Deal

While you might not need the matrix form for a single line,
it's your golden ticket when the model evolves:

* Need to fit a parabola?
  Matrix.

* Multiple x variables?
  Matrix.

* Polynomial regression with terms up to x^10?
  You guessed it. Matrix.

Neo had to choose the red pill.
You? You just need `MINVERSE()`.

-- -- --

### 6: Built-in Formula

_When you love stats, but also love letting Excel do the heavy lifting._

Let's be honest: sometimes we don't want to manually crank,
through all the sums, products, and parentheses.
Sometimes, we want to tell our spreadsheet,
"_Figure it out_," and let the magic happen.

The good news is,
Excel (or Calc, if you're open source and proud) has use covered.

#### First Things First

>  The Basics

Before jumping to the fancy built-ins,
let's warm up with the classics.



Grab the totals and averages for `x` and `y`,
like you're stretching before a marathon of regression.

| Properties | x Formula        | y Formula         |
|------------|------------------|-------------------|
| Total      | =SUM(B7:B19)     | =SUM(C7:C19)      |
| Count      | =COUNT(B7:B19)   | =COUNT(C7:C19)    |
| Mean       | =AVERAGE(B7:B19) | =AVERAGE(C7:C19)  |

Even if we're using `AVERAGE`,
it's good practice to know the underlying logic.
Especially if we'll be coding this later,
in Python, R, or whispering to pandas.

In fact, here's how we can calculate the mean without `AVERAGE`
(yes, sometimes we like to flex on basic functions):

| Properties | Formula                    |
|------------|----------------------------|
| Mean x     | =SUM(B7:B19)/COUNT(B7:B19) |
| Mean y     | =SUM(C7:C19)/COUNT(C7:C19) |

### Built-in Regression

> No Pain, All Gain

Now we get to the really lazy part. 
I mean efficient, part.
Excel has built-in regression functions,
that give use slope and intercept in one clean shot.

Just remember: for array operation formulas, 
hit `Ctrl+Shift+Enter` or Excel will pretend you never asked.

| Properties    | Formula                     |
|---------------|-----------------------------|
| slope (m)     | {=SLOPE(C7:C19;B7:B19)}     |
| intercept (b) | {=INTERCEPT(C7:C19;B7:B19)} |

If we're testing many data sets or building a dashboard,
these functions are fast, reliable,
and save us from spreadsheet-induced carpal tunnel.

#### For the Brave

> Manual Calculation

Want to see how the built-ins work under the hood?
Try calculating it yourself using mean-centered values:

| Properties    | Formula                    |
|---------------|----------------------------|
| slope (m)     | =SUM((B7:B19 - G10)*(C7:C19 - H10))/SUM((B7:B19 - G10)^2) |
| intercept (b) | =H9-G14*G9 |

We're subtracting the mean, multiplying, summing,
conducting a tiny symphony of statistics.

#### Final Thoughts

That's it for now.
Whether we're letting Excel take the wheel,
or crunching numbers the old-fashioned way,
we've got solid tools for fitting a line.

Next up? We will turn the volume up,
and explore regression and correlation.
Dive into more complex formula,
where the real drama of data begins.

-- -- --

### 7: Python

So, what's happened when,
spreadsheets just aren't satisfying,
for our craving for automation and repeatability.

Python offers several ways to perform least squares regression,
ranging from the "_I trust NumPy with my life_" approach,
to "_let's see the residuals and p-values too, please._"

We'll look at:

* `numpy.polyfit` or `Polynomial.fit`:
   Quick and clean.

* `scipy.stats.linregress`
  Lightweight but statistically aware.

* `statsmodels.api.OLS`
  Heavy artillery for full statistical modeling.

You can follow along with the full script here:

* **41-least-square.py**

```python
import numpy as np
import statsmodels.api as sm

from scipy import stats

# Given data
x_values = np.array(
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y_values = np.array(
  [5, 12, 25, 44, 69, 100, 137,
    180, 229, 284, 345, 412, 485])

# Perform least squares regression
# for a linear model (polynomial degree 1)
order = 1
mC    = np.polyfit(x_values, y_values, deg=order)
m     = mC[0]
b     = mC[1]

print('Using polyfit')
print(f'Coefficients (b = {b:2,.2f}, m = {m:2,.2f})\n')

# SciPy: scientific computing built on top of NumPy.
m, b, _, _, _ = stats.linregress(x_values, y_values)

print('Using linregress')
print(f'Coefficients (b = {b:2,.2f}, m = {m:2,.2f})\n')

# Statsmodels: statistical modeling and hypothesis testing.
x = sm.add_constant(x_values)
model = sm.OLS(y_values, x).fit()
b = model.params[0]
m = model.params[1]

print('Using Statsmodels')
print(f'Coefficients (b = {b:2,.2f}, m = {m:2,.2f})\n')
```

Let's start with some data.
Think of this as our patient zero in a curve-fitting,
during current pandemic.

```python
# Given data
x_values = np.array(
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y_values = np.array(
  [5, 12, 25, 44, 69, 100, 137,
    180, 229, 284, 345, 412, 485])
```



#### Polyfit

> Fast, friendly, and polynomial-curious.

If you just want the best-fit line,
and don't need to explain it to your thesis advisor,
`numpy.polyfit` is your go-to.

```python
import numpy as np

# Perform least squares regression
# for a linear model (polynomial degree 1)
order = 1
mC    = np.polyfit(x_values, y_values, deg=order)
m     = mC[0]
b     = mC[1]

print('Using polyfit')
print(f'Coefficients (b = {b:2,.2f}, m = {m:2,.2f})\n')
```

Quick prototyping.
Great for trendlines.
And yes, it works for higher-degree polynomials too.
Just in case our data starts curving like a rollercoaster.



Note: Please be prepate for `polyfit` replacement called `Polynomial.fit`.

#### Linregress

> Like `polyfit`, but wears a lab coat.

`scipy.stats.linregress` gives us
slope, intercept, and bonus goodies like r-value and standard error.
Use it when we want our math to sound more "_peer-reviewable._"

```python
from scipy import stats

# SciPy: scientific computing built on top of NumPy.
m, b, _, _, _ = stats.linregress(x_values, y_values)

print('Using linregress')
print(f'Coefficients (b = {b:2,.2f}, m = {m:2,.2f})\n')
```



Ideal for statistical analysis with minimal fuss.
Also lets us pretend we're doing something much more complicated than we are.

#### OLS

Sometimes we want the full regression buffet,
not just the drive-thru.

For those of us who like residual plots, confidence intervals,
and enough statistical output to paper a conference,
statsmodels has us covered.

```python
import statsmodels.api as sm

# Statsmodels: statistical modeling and hypothesis testing.
x = sm.add_constant(x_values)
model = sm.OLS(y_values, x).fit()
b = model.params[0]
m = model.params[1]

print('Using Statsmodels')
print(f'Coefficients (b = {b:2,.2f}, m = {m:2,.2f})\n')
```

This is the professional toolkit.
We will want this when we start checking assumptions,
diagnosing models, or trying to impress our statistical consultant.



And voilà, no matter how we slice it.
NumPy, SciPy, or Statsmodels,
we end up with the same tidy equation:

```output
Using polyfit
Coefficients (b = -61.00, m = 40.00)

Using linregress
Coefficients (b = -61.00, m = 40.00)

Using Statsmodels
Coefficients (b = -61.00, m = 40.00)
```

Consistent results across different tools is a great sanity check,
especially if our sanity depends on reproducible results.



There is no need for fancy chart plot this time.

You can obtain the interactive `JupyterLab` in this following link:

* **41-least-square.py**

#### Manual Calculation

> For the Purists

When deep down, you don't trust functions,
unless you've re-derived them in a dimly lit lab.

Let's go back to first principles.
Here's how we'd do it ourself.
No black boxes, just beautiful algebra.

* **42-least-square.py**

```python
import numpy as np

# Given data
x_values = np.array(
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y_values = np.array(
  [5, 12, 25, 44, 69, 100, 137,
    180, 229, 284, 345, 412, 485])

# Number of data points
n = len(x_values)

# Calculate sums
sum_x = np.sum(x_values)
sum_y = np.sum(y_values)

# Calculate means
mean_x = np.mean(x_values)
mean_y = np.mean(y_values)

# Output of basic properties
print(f'f{"n":1s} = {n:5d}')
print(f'∑x (total) = {sum_x:7.2f}')
print(f'∑y (total) = {sum_y:7.2f}')
print(f'x̄ (mean)   = {mean_x:7.2f}')
print(f'ȳ (mean)   = {mean_y:7.2f}')
print()

# Calculate deviations
deviation_x = x_values - mean_x
deviation_y = y_values - mean_y

# Calculate squared deviations
sq_deviation_x = np.sum(deviation_x ** 2)

# Calculate cross-deviation
cross_deviation_xy = np.sum(deviation_x * deviation_y)

# Calculate slope (m) and intercept (b)
slope_m = cross_deviation_xy / sq_deviation_x
intercept_b = mean_y - slope_m * mean_x

print('Manual Calculation')
print(f'Coefficients (b = {intercept_b:2,.2f},'
    + f' m = {slope_m:2,.2f})\n')
```

First we calculate basic statistic properties.

```python
# Number of data points
n = len(x_values)

# Calculate sums
sum_x = np.sum(x_values)
sum_y = np.sum(y_values)

# Calculate means
mean_x = np.mean(x_values)
mean_y = np.mean(y_values)

# Output of basic properties
print(f'n = {n:5d}')
print(f'∑x (total) = {sum_x:7.2f}')
print(f'∑y (total) = {sum_y:7.2f}')
print(f'x̄ (mean)   = {mean_x:7.2f}')
print(f'ȳ (mean)   = {mean_y:7.2f}')
print()
```



Then go further, bring in the deviations:

```python
# Calculate deviations
deviation_x = x_values - mean_x
deviation_y = y_values - mean_y

# Calculate squared deviations
sq_deviation_x = np.sum(deviation_x ** 2)

# Calculate cross-deviation
cross_deviation_xy = np.sum(deviation_x * deviation_y)

# Calculate slope (m) and intercept (b)
slope_m = cross_deviation_xy / sq_deviation_x
intercept_b = mean_y - slope_m * mean_x

print('Manual Calculation')
print(f'Coefficients (b = {intercept_b:2,.2f},'
    + f' m = {slope_m:2,.2f})\n')
```

Manual calculation reinforces understanding
of the math behind the tools.
Also, great for debugging or impressing
our coworkers with a "_I did this without NumPy_" moment.



And here's the proof it worked:

```output
n =    13
∑x (total) =   78.00
∑y (total) = 2327.00
x̄ (mean)   =    6.00
ȳ (mean)   =  179.00

Manual Calculation
Coefficients (b = -61.00, m = 40.00)
```



Need to test or tinker interactively?
Fire up these `Jupyter Notebooks` and experiment like a modern-day Gauss:

* **42-least-square.py**

We take this straight line obsession further,
with regression, correlation, and maybe even 
the mysterious world of non-linear fitting.
Are you ready to curve things up?

-- -- --

### Where Do We Go From Here 🤔?

Now that we've bravely tamed the Least Squares beast,
let's talk about what lies ahead in our adventure.

We've taken a mathematical equation,
made it practical (because who doesn't love practical?),
turned it into a neat spreadsheet (tabular bliss, am I right?),
and even whipped up some Python code.
That's like the statistical equivalent of baking a cake from scratch,
but with fewer crumbs and more data insights.

And the best part? It's fun, right?
The kind of fun that only comes from numbers and formulas working together,
like a well-oiled machine. Ah, the joy of regression lines...

Now that we've conquered the basics,
we can explore even more statistical properties.
Regression and correlation are just the beginning.
We can dig deeper into the data,
and start exploring how variables relate to each other,
why they relate (or don't),
and how much faith we can place in our model's predictions.
Trust but verify, that's the statistician's mantra.

But don't worry,
the journey isn't over yet!
If we're still hungry for more statistical wizardry,
take a detour over to **Trend - Properties - Cheatsheet**.

It's like the ultimate guidebook for your next steps in the land of data trends.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Getting to know statistical properties,
> equation by cheatsheet step by step.

Let's face it:
when things get messy (and they will),
we'll need more than just good vibes and Google.
Whether we're double-checking
a suspiciously magical result from a Python library,
or debugging a spreadsheet that's decided to betray us,
manual math is our lifeline.

Sure, there are calculators online.
There are tools that promise answers with zero thinking required.
But here's the catch: if we can't follow the math,
how do we know it's not lying to us?

#### The Inner Working

> "In regression we trust, but always verify." 😄

So before we get cozy with automated libraries
or built-in spreadsheet functions,
we'll walk through the equations.
Old school. Like our stats professor,
but with slightly better graphics.

Basic math is required
But we don't have to do math by hand forever,
that's what machines are for.
However, we do need to understand how it works, at least once.
So we can catch bugs, tweak models,
and sound convincing in a meeting.

Think of this cheat sheet as our statistical Rosetta Stone:
a reference to demystify the math behind linear regression.

Let's get it on!

#### Cheatsheet

For simplicity, we're working with sample statistics here.
Note that population and samples has different notation.
Population equations differ slightly
(and judge us silently when we confuse them).
We will deal with those later.

Here's a high-level view of what's involved,
in a basic least squares regression:



Yes, it looks like the math equivalent of a subway map,
but every symbol here has a job.
And no, none of them are optional.

We can download and remix the full diagram:

* 📎 **github.com/.../math/trend/equflow/equflow-02.svg**
* 📎 **github.com/.../math/trend/equflow/equflow.md**

This cheat sheet is a foundation we'll keep returning to,
especially when exploring correlation, residuals,
and how to impress your data team with Greek letters.

If you disagree with my math, feel free to correct it.
I welcome pull requests and polite statistical debates.

-- -- --

### 1: Equation for Linear Regression 

> Least Square Method

In a previous article,
we dipped our toes into the least squares method.
Think of it as statistics' way of drawing
the "_best guess_" line through a crowd of noisy data points.
But regression isn't just about drawing lines.
It's about understanding the math behind the curtain.

In this article, we'll cover more essential statistical properties,
like variance, covariance, correlation, and everyone's favorite:
R² (which sounds like a robot but is sadly less cute).



You can download the full cheatsheet diagram in raw LaTeX from here:

* **github.com/.../math/trend/50-cheatsheet.tex**

Regression analysis isn't just a plug-and-play task.
Whether we're working in Excel or Python, these formulas help us:

* Sanity-check built-in results
* Understand what the software is actually calculating
* Speak with authority in meetings
  ("_Clearly, the low R² suggests heteroscedasticity._" Boom. Respect.)

#### Data Series

> The Usual Suspects

With sample of data points

$$
\begin{array}{|c|c|}
\hline
x_i & \textbf{observed x} \\
\hline
y_i & \textbf{observed y} \\
\hline
\hat{y}_i & \textbf{predicted y}  \\
\hline
\end{array}
$$

These will appear in every equation.
Think of them as the cast of characters in our regression drama.

#### Total

The `count` and `sum` can be represented as:

$$
\begin{align*}
\text{count} = \sum\limits_{i=1}^{n} 1 &&
\text{sum}_{x} = \sum\limits_{i=1}^{n} x_i &&
\text{sum}_{y} = \sum\limits_{i=1}^{n} y_i &&
\end{align*}
$$

These are our building blocks.
Miss one, and our whole statistical Jenga tower wobbles.

#### Mean

>  The Center of the Universe

Actualy, just the average

$$
\begin{align}
\begin{aligned}
&\text{Mean (Average):} \\
&\begin{array}{|c|c|}
\hline
\mathrm{\textbf{Population}} & \mathrm{\textbf{Sample}} \\
\hline
\mu_X = \frac{1}{N}\sum\limits_{i=1}^{N} x_i &
\bar{x} = \frac{1}{n}\sum\limits_{i=1}^{n} x_i \\
\hline
\end{array}
\end{aligned}
\end{align}
$$

Our average defines the center of our data.
Also, it's where all the deviations start getting personal.

#### Variance

How far does the data stray from the mean?
This is the spreads of each data series.
This is the square of how unpredictable it is.

$$
\begin{align}
\begin{aligned}
&\text{Variance:} \\
&\begin{array}{|c|c|}
\hline
\mathrm{\textbf{Population}} & \mathrm{\textbf{Sample}} \\
\hline
\sigma_X^2 = \frac{1}{N}\sum\limits_{i=1}^{N} (x_i - \mu)^2 & 
s_x^2 = \frac{1}{n-1}\sum\limits_{i=1}^{n} (x_i - \bar{x})^2 \\
\hline
\end{array}
\end{aligned}
\end{align}
$$

Variance is like drama,
more variance, more surprises.

#### Covariance

It's like variance, but both axis.
Now the two variables are gossiping.

$$
\begin{align}
\begin{aligned}
&\text{Covariance:} \\
&\begin{array}{|c|}
\hline
\mathrm{\textbf{Population}} \\
\hline
\text{Cov}(X,Y) = \frac{1}{N}\sum\limits_{i=1}^{N} (x_i - \mu_X)(y_i - \mu_Y) \\
\hline
\mathrm{\textbf{Sample}} \\
\hline
\text{Cov}(x,y) = \frac{1}{n-1}\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) \\
\hline
\end{array}
\end{aligned}
\end{align}
$$

It tells us whether `x` and `y` tend to rise and fall together,
or ghost each other completely.

#### Standard Deviation

The standard deviation is the square root of variance

$$
\begin{align}
\begin{aligned}
&\text{Standard Deviation:} \\
&\begin{array}{|c|c|}
\hline
\mathrm{\textbf{Population}} & \mathrm{\textbf{Sample}} \\
\hline
\sigma_X = \sqrt{\sigma_X^2} & 
s_x = \sqrt{s_x^2} \\
\hline
\end{array}
\end{aligned}
\end{align}
$$

You can't really say our data is "_tight_",
or "_spread out_" until you look at this number.

#### Slope and Intercept

First, the slope `(m)`,
We can calculate using this equation:

$$
m = \frac{\text{Cov}(x,y)}{s_x^2}
$$

As an alternate form (for purists),
we can also represent as

$$
m = \frac{\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum\limits_{i=1}^{n} (x_i - \bar{x})^2}
$$

This way we can get the intercept (b) as follows:

$$
b = \bar{y} - m \bar{x}
$$

This is our regression line: `y = mx + b`.
Every decision, every forecast, every wild guess starts here.

#### Correlation Coefficient

> Pearson

How tightly are our `x` and `y` linked?
Similar to slope, but using both `sₓ` and `Sy`.

$$
\begin{align}
\begin{aligned}
&\text{Correlation Coefficient:} \\
&\begin{array}{|c|c|}
\hline
\mathrm{\textbf{Population}} & \mathrm{\textbf{Sample}} \\
\hline
\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y} &
r_{x,y} = \frac{\text{Cov}(x,y)}{s_x s_y} \\
\hline
\end{array}
\end{aligned}
\end{align}
$$

Or in expanded form,
the Pearson correlation coefficient can also be expressed as follows:

$$
r = \frac{\sum (x_i - \bar{x}) \cdot (y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \cdot \sum (y_i - \bar{y})^2}}
$$

This is the "_how strong is this relationship?_" number.

* 1 = soulmates,
* 0 = strangers,
* –1 = enemies.

#### Coefficient of Determination

> The R Square (R²)

Also known as "_how much of y can be explained by x?__"
In general, the R Square (R²) can be defined as follows.

$$
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

It is interesting that this is just comparing of
(dispersed yᵢ observed againts ŷᵢ predicted) and,
(dispersed yᵢ observed againts mean ȳ).

$$
R^2 = 1 - \frac{SSE}{TSS}
$$

The abbreviation are as below:

* SSE: **sum of squared errors**,
  represents the sum of squared differences
  between the observed values of the dependent variable (yᵢ​)
  and the predicted values (ŷᵢ) 
* TSS: **total sum of squares**,
  which measures the total variability
  of the dependent variable around its mean (ȳ​).

R² is our statistical bragging rights.
* 0.9? we're golden.
* 0.1? Maybe rethink that model.

#### R² for simple linear regression

The R Square (R²) for simple linear regression is the same as r².
This can be expressed as follows.

$$
\begin{align*}
r_{x,y} &= \frac{\text{Cov}(x,y)}{s_x . s_y} \\
R^2     &= r_{x,y}^2
\end{align*}
$$

The equation above is not true in general.
In cases where the relationship between the variables is non-linear,
the coefficient of determination (R²) may still be calculated using
the last one.

$$
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

Beware, this doesn't hold if we go fancy,
with multiple variables or nonlinear models.

#### Residual

Residual = observed minus predicted.
Also known as "_how wrong we were._"
SSE can be defined as:

$$
\begin{align*}
SSE &= \sum\limits_{i=1}^{n} (e_i)^2 \\
    &= \sum (y_i - \hat{y}_i)^2 \\
\end{align*}
$$

More error = more badness. SSE helps quantify that.

While the TSS measure against mean.
The SSE measure against error.
This similarity help me remember the concept.

#### MSE

MSE can be defined as,
divide SSE by the degrees of freedom (df):

$$
MSE = \frac{SSE}{df}
$$

It tells us how wrong, on average,
our model is per data point. Ouch.

While variance divided by total degrees of freedom (n-1).
The MSE divided by residual degrees of freedom (n-k-1).
This similarity help me remember the concept.

#### Standard Error of Slope

This is how much we trust our slope value.

This is also similar to Standard Deviation,
except that we need to divide (error in y axis)
by (variation in x) to get the slope.

$$
SE(\beta_1) = \sqrt{\frac{\sum (y_i - \hat{y}_i)^2}{(n - 2) \cdot \sum (x_i - \bar{x})^2}}
$$

This can be written as:

$$
SE(\beta_1) = \sqrt{\frac{MSE}{TSS_x}}
$$

This similarity help me remember the concept.

#### t-value

How many standard errors away from zero is our slope?

The equation for calculating the t-value,
in the context of linear regression analysis is as follows.
Where β̅₁ is the m slope.

$$
t = \frac{\hat{\beta}_1}{SE(\hat{\beta}_1)}
$$

This t-value helps us decide if our slope is just noise.

However, for non-linear regression models,
the concept of a t-value is not directly applicable
in the same way as it is in linear regression.
The interpretation and calculation of significance
for parameters in non-linear models can differ significantly
based on the estimation method used
and the specific context of the model.

#### p-value

> Just use Excel!

Technically, we can calculate this manually using gamma functions and tables,
but unless we're doing a stats PhD or enjoy pain... just don't.
I'd better not explaining here.
For beginner like us, it is practical to use excel built-in fomula instead.

`p-value` tells us how likely our slope is to exist by random chance.
Lower = better. Think "< 0.05" as our statistical safe zone.

-- -- --

### 2: Example

Statistically speaking, regression gives us a crystal ball.

#### Data Series

Let's walk through a worked example,
using this charming little `(x, y)` sample series.

```csv
x, y
0, 5
1, 12
2, 25
3, 44
4, 69
5, 100
6, 137
7, 180
8, 229
9, 284
10, 345
11, 412
12, 485
```

> Regression provides an equation to predict one variable from another.

Regression analysis involves predicting the value of one variable based on the value of another variable.
In this case, we are predicting the values of `y` based on the values of `x`.

#### Descriptive Stats

The first step in regression analysis is
to understand the dataset.
Here's the basic rundown:

```output
n = 13

∑x (total) = 78
∑y (total) = 2327

x̄ (mean) = 6
ȳ (mean) =  179

∑(xᵢ-x̄) = 0 ← always zero, if you did the mean right!
∑(yᵢ-ȳ) = 0 ← because the deviations always cancel out

∑(xᵢ-x̄)² = 182
∑(xᵢ-x̄)(yᵢ-ȳ) = 7280

m (slope) = 40
b (intercept) = -61
```

With this we get the formula equation as:

```output
y = -61 + 40*x
```

Now we can predict future `y` values.
For example, when `x` = 13, just plug and play.

#### Correlation

> Are x and y Friends 🤝?

Correlation measures the strength and direction
of the linear relationship between two variables.
It does not imply causation, only association.

Let's put it in metaphor,
Correlation tells us how tightly `x` and `y` are holding hands.
Are they soulmates or awkward acquaintances?

The correlation coefficient (r) ranges from -1 to 1.
A value closer to 1 indicates a strong positive correlation,
while a value closer to -1 indicates a strong negative correlation.
A value of 0 indicates no linear correlation.

```output
∑(yᵢ-ȳ)²      = 309218
∑(xᵢ-x̄)(yᵢ-ȳ) = 7280

sₓ² (variance) = 15,17
sy² (variance) = 25.768,17
covariance     = 606,67

sₓ (std dev)   = 3,89
sy (std dev)   = 160,52
r (pearson)    = 0,9704

R² = 0,9417
```

In this case, the correlation coefficient (r) is 0.97,
indicating a very strong positive correlation between x and y.

* r = 0.9704 → x and y are besties
  (very strong positive correlation).

* R² = 0.9417 → About 94% of the variation in y is explained by x.
  The rest? Chalk it up to chaos, noise, or maybe coffee spills in the lab.

#### Significance Check: SE, t, and p

We now test whether the slope of the line is statistically significant.
In simpler terms:
are we just seeing patterns in the tea leaves,
or is there real predictive power?

The standard error of the slope (SE(β₁)),
T-value, and p-value are related to the significance
of the slope coefficient in a regression model.
A low p-value indicates that the slope coefficient is significant.

```output
SSR = ∑ϵ² = 18.018
MSE = ∑ϵ²/(n-2) = 1.638
SE(β₁)  = √(MSE/sₓ) = 3,00
t-value = β̅₁/SE(β₁) = 13,33
p-value = 0,0000000391
```

What is the interpretation?

* SE(β₁) = 3.00 tells us how much uncertainty is in the slope estimate.
* t-value = 13.33 → Our slope is way more than just statistical noise.
* p-value ≈ 0.0000000391 → That's very significant. Like, "publishable in a journal" significant.
* TL;DR: Our regression model isn't just making noise. It's actually got something to say.

A t-value of 13.33 means the signal (slope) is 13 times bigger than the noise. That's huge.

#### Optional: DIY with Python or Excel

We can calculate above example using worksheet,
or scripting language such as python.

Although all of this can be calculated by hand if weu're feeling brave,
or if our professor hates calculators.
But more realistically: _Excel for speed, Python for style._

-- -- --

### 3: What's Wrong?

> Plot Twist: We Forgot the Intercept!

_I make my own notes, because I fail many times._

The step-by-step breakdown earlier was good. Almost great.
But like forgetting to include the salt in a bread recipe,
we missed one important ingredient: _the standard error for the intercept_.

Yes, the _t-value_ and _p-value_ we calculated earlier only apply to the slope.
But what about the poor intercept?
It also wants to feel statistically significant!

To find the standard error of the intercept, we use this slightly spicy formula:

$$
SE(\hat{\beta}_0) = \sqrt{MSE \cdot \left( \frac{1}{n} + \frac{\bar{x}^2}{\sum_{i=1}^{n} (x_i - \bar{x})^2} \right)}
$$

Ignoring the intercept's standard error is like,
assuming the origin of our line doesn't matter.
But in real-world forecasting
(like predicting costs, sales, or cat meme virality),
our intercept can carry meaning,
especially when `x` = 0 has a real-world interpretation.

I didn't calculate it earlier because, well...

_This equation looks like it was written during a caffeine-fueled existential crisis._

We will revisit this property properly,
in the upcoming polynomial regression article,
where this concept becomes essential,
and where things get delightfully curvy.

-- -- --

### What Lies Ahead 🤔?

It is fun. And empowering.
We just reverse-engineered the engine room of linear regression.
We can describe mathematical equation, in practical way.

_Do I Have to Memorize All This?_

Knowing how to manually calculate slope, intercept,
and all the extras gives us real understanding,
not just button-pushing skills.
But let's face it: in real life,
we don't want to spend all day computing SSE by candlelight.

Luckily, we can get the same results much faster with:

* Excel formulas (`=SLOPE()`, `=INTERCEPT()`, etc.)
* Python libraries like `scipy.stats`, `numpy,` and `sklearn.linear_model`

_Manual methods build understanding_. \
_Built-in methods build our weekend plans_.

If you enjoyed this, the next chapter **Trend – Properties – Formula**
will feel like switching from cooking rice in a pot to using a rice cooker.
Same result, way less hassle, and no burnt bottom layer.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Getting to know statistical properties,
> using worksheet formula step by step.

When we look at regression equations in textbooks,
it can feel like walking into a math dungeon without a torch.
But don't worry, we're bringing the flashlight and a map.
In this article, we'll take the scary symbols and turn them,
into something we can click and calculate in Excel.
Or maybe someday Google Sheets if I, the author, have time to learn.

We'll start with manual calculations,
because understanding why something works,
makes us smarter than just knowing that it works.
Then we'll show how to use built-in worksheet functions
which feel like finding out,
that we didn't need to count rice grains by hand after all.

Anyone can click buttons.
But knowing the guts of the formula helps us catch errors,
explain our results, and feel smarter at dinner parties
(or Zoom meetings).

#### Complete Worksheet

Yes, it looks long. Yes, it has lots of rows.
But once we walk through it section by section,
we will see that it is well organized.
And don't let the visual complexity fool you,
this monster includes regression and correlation analysis.
Two for the price of one!



This article starting with manual calculation using Excel cells.
After this section, we will reveal the built-in formulas that do all this faster.

#### Worksheet Source

> Playsheet Artefact

You don't have to build this from scratch
(unless you're into that).
Grab the actual Excel file and tweak,
break, and experiment to your heart's content.

* **github.com/.../math/trend/examples-properties.xlsx**

-- -- --

### Known Values from Samples

> Example Time! Let's make those numbers sweat.

Imagine we're handed a list of data points.
Just plain (x, y) pairs.
We don't know where they came from,
but they're ours now, and they need analysis.

Suppose our `x_observed`-series lives in `B7:B19`,
and our `y_observed`-series in `C7:C19`.
Here's what we're working with:

**(x, y)** = [(0, 5), (1, 12), (2, 25), (3, 44), (4, 69), (5, 100), (6, 137), (7, 180), (8, 229), (9, 284), (10, 345), (11, 412), (12, 485)]



We start with the basics: the mean.
It is crucial for measuring how much each value wanders off.

$$
\begin{align*}
\bar{x} = \frac{1}{n}\sum\limits_{i=1}^{n} x_i &&
\bar{y} = \frac{1}{n}\sum\limits_{i=1}^{n} y_i \\
\end{align*}
$$

You can calculate these with Excel's humble built-ins:
 `count`, `sum`, and `average`.

```excel
B22=SUM(B7:B19)
C22=SUM(C7:C19)

B26=COUNT(B7:B19)
C26=COUNT(C7:C19)

B30=AVERAGE(B7:B19)
C30=AVERAGE(C7:C19)
```

Or go DIY and divide the total using the `sum` and the `count`.

```excel
B30=B22/B26
C30=C22/C26
```

The result of the statistic properties, `total` and `mean` are:

$$
\begin{align*}
n = 13 &&
\sum x = 78 &&
\sum y = 2327 &&
\bar{x} = 6 &&
\bar{y} = 179 &&
\end{align*}
$$

These means will serve as the anchors for every calculation that follows.
Like a good coffee shop, everything starts here.

#### Plot Result


> 📈 Time to chart it!

Plotting these values helps us see the story our data wants to tell,
before we bury it in math.
Let's see how a visualization interpret the mean properties.



-- -- --

### Basic Statistic Properties

Now we can subtract, square, and stare at variances like true statisticians.

Let's calculate how far each `x_observed` and `y_observed`,
deviate from their respective means.
This gives us the foundational ingredients for:
variance, covariance, and other buzzwords in further calculation.



For the series range `E7:E19` and `F7:F19` the formula are:

```excel
E7=B7-$B$30
F7=C7-$C$30
...
E19=B19-$B$30
F19=C19-$C$30
```

Deviations measure "how far off",
each point is from average behavior.
We also need to know how many values we have,
and adjust for sample size (hello, degrees of freedom).

For samples, the unbiased estimate is (n-1).
I'm just following the convention to use (n-1).
The math behind is a hard topic, and beyond my knowledge,
so I refused to explain.

$$
n - 1 = 12
$$

We're not quite using df (degrees of freedom) yet,
but here's the teaser:

$$
df = n - k - 1 = 11
$$

Translated to Excel/Calc,
we can write this as:

```excel
E26=COUNT(B7:B19)-1
F26=COUNT(C7:C19)-1

E30=COUNT(B7:B19)-2
```

-- -- --

### Least Square Calculation

> Let's regress it

We now compute the least squares regression,
which is just a fancy way of drawing the best straight line,
through our cloud of data points.

We have discuss in depth about the math behind in previous article.
The slope `m` (from the “famous” line equation `y = mx + b`) is defined as:

$$
m = \frac{\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum\limits_{i=1}^{n} (x_i - \bar{x})^2}
$$

What we need is to find each total these properties:
* (xᵢ-x̄)²: how scattered x-values are
* (xᵢ-x̄)(yᵢ-ȳ): how x and y vary together



We need to find the nominator and the denominator.

$$
\begin{align*}
\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) &&
\sum\limits_{i=1}^{n} (x_i - \bar{x})^2 \\
\end{align*}
$$

For the series range `H7:H19` (xᵢ-x̄)² and `I7:I19` (xᵢ-x̄)(yᵢ-ȳ) the formula are:

```excel
H7=E7^2
I7=E7*F7
...
H19=E19^2
I19=E19*F19
```

The total ∑(xᵢ-x̄)² and ∑(xᵢ-x̄)(yᵢ-ȳ) can be defined as:

```excel
H22=SUM(H7:H19)
I22=SUM(I7:I19)
```

The result of the each total are:

$$
\begin{align*}
\sum\limits_{i=1}^{n} (x_i - \bar{x})^2 &= 182 \\
\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) &= 7280 \\
\end{align*}
$$

Now we got the `m` (slope) and` b` (intercept) as:

```excel
H26=I22/H22
I26=C30-H26*B30
```

Which gives us:

$$
\begin{align*}
m (slope) &= 40 \\
b (intercept) &= 61 \\
\end{align*}
$$

Finally we can get the full regression equation (y = b + mx) as:

```excel
H30=CONCATENATE("y = ";TEXT(I26;"#.##0,00");" + ";TEXT(H26;"#.##0,00");".x")
```

Let's write it in human form:

$$
y = -61 + 40x
$$

This formula gives us a predictive model.
Turn any `x` into an estimated `y`.
It's like statistical fortune telling,
except with math instead of incense.

Again, we can see how easy it is to write down
the equation in tabular spreadsheet form.

#### Plot Result

Time to visualize your best-fit line.
Now we will see how well our equation hugs the data.



-- -- --

### Variance and Covariance

Let's now wander into the realm of statistical relationships,
where variables whisper secrets to each other via variance and covariance.
These aren't just fancy words to impress our dinner guests,
they quantify how our data behaves around its mean,
and how two variables dance together.

The equations for sample variance and covariance,
for a sample of data series `(x, y)` is given as follows:

$$
\begin{align*}
s_x^2 &= \frac{1}{n-1}\sum\limits_{i=1}^{n} (x_i - \bar{x})^2 \\
s_y^2 &= \frac{1}{n-1}\sum\limits_{i=1}^{n} (y_i - \bar{y})^2 \\
\text{Cov}(x,y) &= \frac{1}{n-1}\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) \\
\end{align*}
$$

We're calculating these to understand:

* (xᵢ-x̄)² and (yᵢ-ȳ)²: How much variation each variable carries
* (xᵢ-x̄)(yᵢ-ȳ): Whether the variables move together or not

For the series range `K7:K19` (xᵢ-x̄)², `L7:L19` (yᵢ-ȳ)²
and `M7:M19` (xᵢ-x̄)(yᵢ-ȳ) the formula are:

```excel
K7=E7^2
L7=F7^2
M7=E7*F7
...
K19=E19^2
L19=F19^2
M19=E19*F19
```

This prepares our data for calculating how "spread out" the data is,
and whether `x` and `y` have any statistical chemistry.

Now for the totals:

$$
\begin{align*}
\sum\limits_{i=1}^{n} (x_i - \bar{x})^2 &&
\sum\limits_{i=1}^{n} (y_i - \bar{y})^2 &&
\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) \\
\end{align*}
$$

The total variation of the predictor,
∑(xᵢ-x̄)², (yᵢ-ȳ)² and ∑(xᵢ-x̄)(yᵢ-ȳ) can be defined as:

```excel
K22=SUM(K7:K19)
L22=SUM(L7:L19)
M22=SUM(M7:M19)
```

The result of the each total are:

$$
\begin{align*}
\sum\limits_{i=1}^{n} (x_i - \bar{x})^2 &= 182 \\
\sum\limits_{i=1}^{n} (y_i - \bar{y})^2 &= 309218 \\
\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) &= 7280 \\
\end{align*}
$$

To normalize these (and avoid bias )
we divide by degrees of freedom (n - 1).
Now we got the variance sₓ², sy² and also the covariance as:

```excel
K22=K22/E26
L22=L22/F26
M22=M22/E26
```

The result of the statistic properties are:

$$
\begin{align*}
s_X^2 &= 15.17 \\
s_Y^2 &= 25768.17 \\
\text{Cov}(X,Y) &= 606.67 \\
\end{align*}
$$

Variance tells us how unpredictable the data is,
and covariance gives us a sneak peek into,
whether the two variables move together (positive), apart (negative),
or ignore each other entirely (zero, the statistical equivalent of ghosting).

The tabular spreadsheet can be shown as follows:



Oh, and standard deviation is just the square root of variance.

#### Plot Result

We need a visualization so we can interpret
the standard deviation properties against original observed y.



-- -- --

### Correlation Calculation

Time to put the cool shades on our statistics.
Let's measure correlation,
the standardized version of covariance,
that fits nicely between -1 and 1.

From calculated properties above we can continue
to standard deviation sₓ, sy, along with the r (pearson) value:

```excel
K30=SQRT(K26)
L30=SQRT(L26)
M30=M26/(K30*L30)
```

This yields:

$$
\begin{align*}
s_x &= \sqrt{s_X^2} &= && 3.89 \\
s_y &= \sqrt{s_Y^2} &= && 160.52 \\
r_{x,y} &= \frac{\text{Cov}(x,y)}{s_x . s_y} &= && 0,97 \\
\end{align*}
$$

A correlation coefficient of 0.97?
That's about as close to a linear relationship as you can get,
without your data actually proposing marriage.

Note that the pearson coefficient can be denoted in different form.
Alternative formula for r (same dance, different choreography):

r = cov/sₓsy \
r = (∑(xᵢ-x̄).(yᵢ-ȳ))/√(∑(xᵢ-x̄)².∑(yᵢ-ȳ)²)

This way we can calculate the R square (R²)
and also the adjusted R square.
Note that R² for simple linear sample is the same as r².
In this case R² = 0,9417.
But the R² might be different for complex cases.

```excel
M33=M30^2
```

Also there is no need any adjusted R²,
for simple least square population.
But for sample we need to adjust with k=1,
for linear equation then adjusted R² = 0,9364.

```excel
M35=1-(1-M33)*(B26-1)/(B26-1-1)
```

We can have a look at the result,
focusing on this part of following spreadsheet:



R² = 0.94 → "_94% of the variance in `y` is explained by `x`_."
That's nearly everything, the other 6% probably noise,
or maybe just forgot to update their spreadsheets.

#### Plot Result

We need a visualization so we can interpret
the standard deviation properties against predicted y.



-- -- --

### Residual Calculation

Finally, we measure how far off our predictions are.
Every prediction has regrets,
and in statistics, they're called residuals.

We plug in our linear model
from the coefficient of the linear least square,

* m (slope)
* b (intercept)

We can built our curve fitting equation (y = b + mx),
and predict every yᵢ value.

$$
\begin{align*}
\hat{y}_i &= mx_i + b \\
e_i &= y_i - \hat{y}_i \\
\sum\limits_{i=1}^{n} (e_i)^2 &= \sum\limits_{i=1}^{n} (y_i - \hat{y}_i)^2 \\
\end{align*}
$$

Use the spreadsheet to compute.
For the series range `O7:O19` fit(xᵢ), `P7:P19` ϵᵢ (residual),
and `Q7:Q19` ϵᵢ² the formula are:

```excel
O7=$I$26+$H$26*B7
P7=C7-O7
M7=P7^2
...
O19=$I$26+$H$26*B19
P19=C19-O19
M19=P19^2
```

Note that we can use any curve fitting formula,
such as quadratic, cubic and so on,
but for this example we will use our linear one.

Now total residual error.
The total of ϵᵢ² can be defined as:

```excel
Q22=SUM(Q7:Q19)
```

The result of the each total are:

$$
\sum\limits_{i=1}^{n} (e_i)^2 = 18018
$$

The tabular spreadsheet can be shown as follows:



Residuals show us where our model is off.
If the residuals are too wild,
the model might just be blowing statistical smoke.

#### Plot Result

We need a plot to show,
how far off the actual `y_predicted` is,
from our model's predictions.



Plotting residuals is like proofreading our math.
Weou don't always like what we see,
but it makes everything better.

-- -- --

### Regressions Sum Square

Welcome to the world of SSR, Regression Sum of Squares,
or as we statisticians like to call it:
"_How much our predictions flex on the average._"
Here is the RSS:

$$
\sum\limits_{i=1}^{n} (\hat{y}_i - \bar{y})^2
$$

This represents the variation explained by our model.
The bigger it is (relative to total variance),
the more our model is saying,
"_Hey, I actually know what's going on!_"



Naturally, this brings us to SST.
Sum of Squares Total, a.k.a. the full buffet of variance:

The SST (Sum Square Total) is

$$
SST = SSR + RSS
$$

Mathematically, for each observed `yᵢ`, we can say:

$$
\sum\limits_{i=1}^{n} (y_i - \bar{y})^2
$$

Yes, it's a love triangle.
The total variation (SST) is shared between,
* what the model explains (RSS, Regressions Sum Square) and,
* what it misses (SSR, Sum of Squares of Residual).

#### Why does SST = SSR + RSS?

> It is easier to understand using the spreadsheet.

This equation is rooted in partitioning variance.
Essentially slicing up the total variation in our data into:

* **RSS** = Regression Sum of Squares (explained):
  The variation due to the model.
  It's how much our predicted values `ŷᵢ`​ deviate from the mean `ȳᵢ`​.
  If this is large, our model is picking up real structure in the data.

* **SSR** = Sum of Squares of Residual (unexplained):
  What's left over, the part of the variance our model fails to explain, 
  .e., the noisy, chaotic behavior of real-world data.
  It is how far off our predictions are from the actual `yᵢ` values.
  Ideally, this is small.

* **SST** = Total Sum of Squares:
  The total variation in the dependent variable `yᵢ`. essentially:
  “_How spread out is y overall, around its mean?_”

Our model projects the data onto a line,
and splits perfectly between "_explained_" and "_unexplained_."

#### Back to R²

This is the statistical backbone of R².
Want to know **how good** our regression line is?
Start here. It's the source of model validation.

R² (coefficient of determination) is defined as:

$$
R^2 = \frac{SSR}{SST} = 1 - \frac{RSS}{SST}
$$

It answers, "_How much of the variation in `y` is captured by `x`?_”

* If R² = 1, our model explains everything.
  Congratulations, we've either modeled reality perfectly,
  or we've committed statistical heresy (i.e., overfitting).

* If R² = 0,
  our model explains nothing,
  It's as useful as a horoscope.

-- -- --

### t-value and p-value

> Truth or Dare?

Now for the dramatic part, the hypothesis testing,
using `t-value` and `p-value`.
We want to know: "_Is our slope real or just a fluke?_"

First, calculate the degrees of freedom,
For linear equation `k=1`.

$$
df = n - k - 1 = 11
$$

In Excel/Calc we can write this as:

```excel
E30=COUNT(B7:B19)-2
```

Degrees of freedom are like free will in data.
The more we have, the more trust we can put in our analysis.

Next, enter the **Mean Squared Error**.
It tells us how wrong the model is,
on average, for each point:

$$
MSE = \frac{SSE}{df}
$$

In Excel/Calc we can write this as:

```excel
=Q22/$E$30
```

Then we compute the Standard Error of the Slope SE(β1) using MSE.

$$
SE(\beta_1) = \sqrt{\frac{MSE}{\sum_{i=1}^{n}(x_i - \bar{x})^2}}
$$

In Excel/Calc we can write this as:

```excel
=SQRT(Q25/K22)
```

Next, the `t-value`: This is where we look slope in the eye,
and say: “_Prove you matter._”

The `t-value` for the slope coefficient (`β₁`​) is computed,
as the ratio of the estimated slope (`βˉ₁`),
to the standard error of the slope (SE(`β₁`)).
This `t-value` will be used to test the null hypothesis,
that the true slope coefficient is equal to zero.

$$
t = \frac{\bar{\beta}_1}{SE(\beta_1)}
$$

In Excel/Calc we can write this as:

```excel
=H26/Q30
```

And finally, the `p-value`, the real drama queen.
It's the probability that our slope is due to random chance.
The smaller the `p-vlue`, the more confident we are,
that our model actually means something.

Here is the p-value for two tail test.

$$
p = 2 \times P(T > |t|)
$$

This is to complex for manual calculation.
so I use built-in formula instead.

In spreadsheet speak:

```excel
=T.DIST.2T(Q35;$E$30)
```

The `p-value` is our model's confession.
It either says: “"_Yep, I'm legit,_",
or "_Oops, maybe I was just noise._"

Here are the results of this statistical soap opera:

$$
\begin{align*}
df &= 11 \\
MSE &= 1638 \\
SE(\beta_1) &= 3.00 \\
t-value &= 13.33 \\
p-value &= 0,0000000391 \\
\end{align*}
$$

We have an incredibly significant result.
Oour slope isn't just a good guess,
it's a statistically valid superstar.

Check it out here:



We have a good confidence in our curve fitting function.

#### Alternative Worksheet

If you''e not into one worksheet layout, don't worry.
Spreadsheet is like statistics: it tolerates many truths.

Here's an alternative way of laying things out:



Just remember, the numbers must dance the same.
No matter how we rearrange the ballroom.

-- -- --

### Built In Formula

> The Lazy Genius of Regression

Who needs to crunch numbers by hand,
when spreadsheets and Python will gladly do our bidding?
Let's explore how built-in formulas make regression analysis,
feel less like statistical calculus,
and more like statistical calculus-on-autopilot.

#### Worksheet Source

> Your DIY Regression Playground

Welcome to spreadsheet heaven.
You'll find all the formulas preloaded in this `.ods` file.

* **github.com/.../math/trend/examples-properties.ods**

Even though everything here can work in Excel,
we're using LibreOffice.
Why? Because `.ods` lets us play with named ranges more flexibly,
and frankly, `.xlsx` sometimes throws a tantrum.

Still prefer Excel? We got you:

* **github.com/.../math/trend/examples-properties.xlsx**

#### Meet the Data

Let's revisit our familiar cast of statistical characters:



* xᵢ observed: `B7:B19`,
* yᵢ observed: `C7:C19`,
* ŷᵢ predicted: `D7:D19` calculated from m and b.

#### Named Range

_B7:B19 is Not a Personality_

To make the equation less cryptic,
we can define named range.
This can be done in both Excel and Calc:



Let's give our ranges real names.
"_x_observed_" just sounds more mature than "B7:B19".

* `B7:B19`: x_observed.
* `C7:C19`: y_observed.
* `D7:D19`: y_predicted.

Think of it as giving our variables,
name tags at a regression conference.

#### Using Array Operation

We can rebuild tabular woksheet from previous article,
into a simple one using Excel/Calc formula
with the help of `SUMSQ` formula.

With just using array formulas and built-in functions,
we can have direct result into a cell.
Because if Excel has a button for it,
why type three columns by hand?



Here the predicted value of `ŷᵢ` in `D7:D19`,
are calculated from `m ($G$17)` and `b ($G$18)`.

The complete formula can be shown here:

| properties              | formula                                             |
| ----------------------- | --------------------------------------------------- |
| ∑x	                    |  =SUM(x_observed)                                   |
| ∑y	                    |  =SUM(y_observed)                                   |
| n	                      |  =COUNT(x_observed)                                 |
| n-1	                    |  =G9-1                                              |
| df = n-k-1	            |  =G9-2                                              |
| x̄ (mean)	               |  =AVERAGE(x_observed)                               |
| ȳ (mean)	               |  =AVERAGE(y_observed)                               |
| ∑(xᵢ-x̄)²	               | {=SUMSQ(x_observed-$G$12)}                          |
| ∑(yᵢ-ȳ)²	               | {=SUMSQ(y_observed-$G$13)}                          |
| ∑(xᵢ-x̄)(yᵢ-ȳ)	          |  =SUMPRODUCT((x_observed-$G$12),(y_observed-$G$13)) |
| β̅₁ = m (slope)	         |  =G16/G14                                           |
| β̅₀ = b (intercept)	     |  =G13-G17*G12                                       |
| sₓ²=∑(xᵢ-x̄)²/(n-1)	     |  =G14/G10                                           |
| sy²=∑(yᵢ-ȳ)²/(n-1)	     |  =G15/G10                                           |
| cov=∑(xᵢ-x̄)(yᵢ-ȳ)/(n-1)	|  =G16/G10                                           |
| sₓ (std dev)	          |  =SQRT(G19)                                         |
| sy (std dev)	          |  =SQRT(G20)                                         |
| r (pearson)=cov/sₓsy	  |  =G21/(G22*G23)                                     |
| R² for linear is r²	    |  =G24^2                                             |
| adjusted R²	            |  =1-(1-G25)*G10/G11                                 |
| SSE = ∑ϵᵢ²	            | {=SUMSQ(y_observed-D7:D19)}                         |
| MSE = SSE/df	          |  =G27/G11                                           |
| SE(β₁) = std err slope	|  =SQRT(G28/G14)                                     |
| t-value = β̅₁/SE(β₁)	   |  =G17/G29                                           |
| p-value	                |  =T.DIST.2T(G30;G11)                                |


We're covering all our greatest statistical hits:
slope, variance, correlation, R², t-tests,
and the always-glamorous p-value.

This condenses a ton of regression math,
into digestible spreadsheet logic.
Less time formatting cells,
more time eating snacks and doing science.

#### Using Statistic Formula

> The Built-in Shortcut

Furthermore we can use statistic formula.

Want to double-check your math?
Or just feel like living dangerously by trusting Excel's statistical engine?
Let's name new ranges for a fresh worksheet:

* `B7:B19`: x_sample.
* `C7:C19`: y_sample.
* `D7:D19`: y_fit.

Then we let built-in stats formulas take over.



| properties              | formula                                         |
| ----------------------- | ----------------------------------------------- |
| ∑x	                    |  =SUM(x_sample)                                 |
| ∑y	                    |  =SUM(y_sample)                                 |
| n	                      |  =COUNT(x_sample)                               |
| n-1	                    |  =G9-1                                          |
| df = n-k-1	            |  =G9-2                                          |
| x̄ (mean)	               |  =AVERAGE(x_sample)                             |
| ȳ (mean)	               |  =AVERAGE(y_sample)                             |
| ∑(xᵢ-x̄)²	               | {=SUMSQ(x_sample-$G$12)}                        |
| ∑(yᵢ-ȳ)²	               | {=SUMSQ(y_sample-$G$13)}                        |
| ∑(xᵢ-x̄)(yᵢ-ȳ)	          |  =SUMPRODUCT((x_sample-$G$12),(y_sample-$G$13)) |
| β̅₁ = m (slope)	         |  =SLOPE(y_sample,x_sample)                      |
| β̅₀ = b (intercept)	     |  =INTERCEPT(y_sample,x_sample)                  |
| sₓ² (variance)	        |  =VAR.S(x_sample)                               |
| sy² (variance)	        |  =VAR.S(y_sample)                               |
| covariance	            |  =COVARIANCE.S(x_sample,y_sample)               |
| sₓ (std dev)	          |  =STDEV.S(x_sample)                             |
| sy (std dev)	          |  =STDEV.S(y_sample)                             |
| r (pearson)	            |  =PEARSON(x_sample,y_sample)                    |
| R² coeff	              |  =RSQ(y_sample,x_sample)                        |
| adjusted R²	            |  =1-(1-G25)*G10/G11                             |
| SSE = ∑ϵᵢ²	            | {=SUMSQ(y_sample-y_fit)}                        |
| MSE = SSE/df	          |  =G27/G11                                       |
| SE(β₁) = std err slope	|  =SQRT(G28/G14)                                 |
| t-value = β̅₁/SE(β₁)	   |  =G17/G29                                       |
| p-value	                |  =T.DIST.2T(G30;G11)                            |

The parameter required for each statistic formula is clear now.
These functions reduce error and save time.
Perfect when we've had our third coffee,
and still can't remember what ∑(xᵢ - x̄)² stands for.

#### Pearson Correlation Coeffecient

> Measuring Statistical Chemistry

Need to measure the linear love between `x` and `y`?
Use Pearson's `r` correlation coefficient:

```excel
=PEARSON(B7:B19;C7:C19) 
```

The formula for pearson is:

$$
r_{x,y} \frac{\text{Cov}(x,y)}{s_x . s_y} \\
$$

Which we can write manually in Excel/Calc as:

```excel
=COVARIANCE.P(B7:B19, C7:C19) / (STDEV.P(B7:B19) * STDEV.P(C7:C19))
```

And if you're feeling masochistic,
the Pearson correlation coefficient can also be expressed as follows:

$$
r = \frac{\sum (x_i - \bar{x}) \cdot (y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \cdot \sum (y_i - \bar{y})^2}}
$$

Sometimes you want to check if your equation right.
Again, the Excel/Calc formula can be rewritten as follows,
and having the same result.

```excel
= (SUM((B7:B19 - AVERAGE(B7:B19)) * (C7:C19 - AVERAGE(C7:C19)))) 
/ (SQRT(SUM((B7:B19 - AVERAGE(B7:B19))^2) * SUM((C7:C19 - AVERAGE(C7:C19))^2)))
```

Now you know, how helpful the built-in formula is,
compared to this complex formula above.

#### R Square

> The MVP of Model Metrics

Want to know how much of the variation in `y` is explained by our model?
Excel/Calc has a built-in formula for R Square (R²):

```excel
=RSQ(C7:C19;B7:B19)
```

The R Square (R²) for simple linear regression can be expressed as follows:

$$
\begin{align*}
r_{x,y} &= \frac{\text{Cov}(x,y)}{s_x . s_y} \\
R^2     &= r_{x,y}^2
\end{align*}
$$

Here's the long-form version.
The general R Square (R²) is defined as:

$$
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

Or furthermore, we can go low-level.

$$
R^2 = 1 - \frac{\sum (y_i - (\hat{\beta}_1 x_i + \hat{\beta}_0))^2}{\sum (y_i - \bar{y})^2}
$$

Down to the nuts and bolts,
the Excel/Calc formula can be rewritten as:

```excel
=1-SUM((C7:C19 - (B7:B19*G22+G24))^2)/SUM((C7:C19 - H9)^2)
```

The way you manage the calculation is depend on your situation.
Most of the time we can use simple `rsq` formula,
but sometimes we need to go low level,
for use with programming or just intellectual curiosity.

Let's see how RSQ behave in non-linear curve fitting discussed later on.

#### Compare and Contrast: Manual vs Built-in

Feel free to compare both methods, side-by-side.
Between manual formula and built-in formula as shown below:



Like a true stats nerd, always double-check our work.
But also, enjoy the shortcuts modern tools give us.
Regression shouldn't feel like a root canal.

Now we are ready to make statistical model,
in our worksheet to suit our specific needs.

_How you make the model is up to you._

-- -- --

### What Lies Ahead 🤔?

That method above? Elegant, yes.
But let's not kid ourselves.
Naturally, there's a simpler way.

If we want a spreadsheet model that doesn't require a PhD.
Or three cups of coffee and a blank stare,
we'll need a method more fit for everyday use.
Something robust, readable, and less likely to induce formula fatigue.

The easier it is to calculate,
the more likely we'll actually use it.
That's why in the next part of our adventure,
we shift gears from cells and formulas,
to the comforting embrace of Python.
There, we'll build tools that are both reusable,
and less fiddly than spreadsheet gymnastics.

Grab our virtual lab coat and join us in:
**Trend - Properties - Python Tools**.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Getting to know statistical properties,
> using worksheet formula step by step.

When we look at regression equations in textbooks,
it can feel like walking into a math dungeon without a torch.
But don't worry, we're bringing the flashlight and a map.
In this article, we'll take the scary symbols and turn them,
into something we can click and calculate in Excel.
Or maybe someday Google Sheets if I, the author, have time to learn.

We'll start with manual calculations,
because understanding why something works,
makes us smarter than just knowing that it works.
Then we'll show how to use built-in worksheet functions
which feel like finding out,
that we didn't need to count rice grains by hand after all.

Anyone can click buttons.
But knowing the guts of the formula helps us catch errors,
explain our results, and feel smarter at dinner parties
(or Zoom meetings).

#### Complete Worksheet

Yes, it looks long. Yes, it has lots of rows.
But once we walk through it section by section,
we will see that it is well organized.
And don't let the visual complexity fool you,
this monster includes regression and correlation analysis.
Two for the price of one!



This article starting with manual calculation using Excel cells.
After this section, we will reveal the built-in formulas that do all this faster.

#### Worksheet Source

> Playsheet Artefact

You don't have to build this from scratch
(unless you're into that).
Grab the actual Excel file and tweak,
break, and experiment to your heart's content.

* **github.com/.../math/trend/examples-properties.xlsx**

-- -- --

### Known Values from Samples

> Example Time! Let's make those numbers sweat.

Imagine we're handed a list of data points.
Just plain (x, y) pairs.
We don't know where they came from,
but they're ours now, and they need analysis.

Suppose our `x_observed`-series lives in `B7:B19`,
and our `y_observed`-series in `C7:C19`.
Here's what we're working with:

**(x, y)** = [(0, 5), (1, 12), (2, 25), (3, 44), (4, 69), (5, 100), (6, 137), (7, 180), (8, 229), (9, 284), (10, 345), (11, 412), (12, 485)]



We start with the basics: the mean.
It is crucial for measuring how much each value wanders off.

$$
\begin{align*}
\bar{x} = \frac{1}{n}\sum\limits_{i=1}^{n} x_i &&
\bar{y} = \frac{1}{n}\sum\limits_{i=1}^{n} y_i \\
\end{align*}
$$

You can calculate these with Excel's humble built-ins:
 `count`, `sum`, and `average`.

```excel
B22=SUM(B7:B19)
C22=SUM(C7:C19)

B26=COUNT(B7:B19)
C26=COUNT(C7:C19)

B30=AVERAGE(B7:B19)
C30=AVERAGE(C7:C19)
```

Or go DIY and divide the total using the `sum` and the `count`.

```excel
B30=B22/B26
C30=C22/C26
```

The result of the statistic properties, `total` and `mean` are:

$$
\begin{align*}
n = 13 &&
\sum x = 78 &&
\sum y = 2327 &&
\bar{x} = 6 &&
\bar{y} = 179 &&
\end{align*}
$$

These means will serve as the anchors for every calculation that follows.
Like a good coffee shop, everything starts here.

#### Plot Result


> 📈 Time to chart it!

Plotting these values helps us see the story our data wants to tell,
before we bury it in math.
Let's see how a visualization interpret the mean properties.



-- -- --

### Basic Statistic Properties

Now we can subtract, square, and stare at variances like true statisticians.

Let's calculate how far each `x_observed` and `y_observed`,
deviate from their respective means.
This gives us the foundational ingredients for:
variance, covariance, and other buzzwords in further calculation.



For the series range `E7:E19` and `F7:F19` the formula are:

```excel
E7=B7-$B$30
F7=C7-$C$30
...
E19=B19-$B$30
F19=C19-$C$30
```

Deviations measure "how far off",
each point is from average behavior.
We also need to know how many values we have,
and adjust for sample size (hello, degrees of freedom).

For samples, the unbiased estimate is (n-1).
I'm just following the convention to use (n-1).
The math behind is a hard topic, and beyond my knowledge,
so I refused to explain.

$$
n - 1 = 12
$$

We're not quite using df (degrees of freedom) yet,
but here's the teaser:

$$
df = n - k - 1 = 11
$$

Translated to Excel/Calc,
we can write this as:

```excel
E26=COUNT(B7:B19)-1
F26=COUNT(C7:C19)-1

E30=COUNT(B7:B19)-2
```

-- -- --

### Least Square Calculation

> Let's regress it

We now compute the least squares regression,
which is just a fancy way of drawing the best straight line,
through our cloud of data points.

We have discuss in depth about the math behind in previous article.
The slope `m` (from the “famous” line equation `y = mx + b`) is defined as:

$$
m = \frac{\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum\limits_{i=1}^{n} (x_i - \bar{x})^2}
$$

What we need is to find each total these properties:
* (xᵢ-x̄)²: how scattered x-values are
* (xᵢ-x̄)(yᵢ-ȳ): how x and y vary together



We need to find the nominator and the denominator.

$$
\begin{align*}
\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) &&
\sum\limits_{i=1}^{n} (x_i - \bar{x})^2 \\
\end{align*}
$$

For the series range `H7:H19` (xᵢ-x̄)² and `I7:I19` (xᵢ-x̄)(yᵢ-ȳ) the formula are:

```excel
H7=E7^2
I7=E7*F7
...
H19=E19^2
I19=E19*F19
```

The total ∑(xᵢ-x̄)² and ∑(xᵢ-x̄)(yᵢ-ȳ) can be defined as:

```excel
H22=SUM(H7:H19)
I22=SUM(I7:I19)
```

The result of the each total are:

$$
\begin{align*}
\sum\limits_{i=1}^{n} (x_i - \bar{x})^2 &= 182 \\
\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) &= 7280 \\
\end{align*}
$$

Now we got the `m` (slope) and` b` (intercept) as:

```excel
H26=I22/H22
I26=C30-H26*B30
```

Which gives us:

$$
\begin{align*}
m (slope) &= 40 \\
b (intercept) &= 61 \\
\end{align*}
$$

Finally we can get the full regression equation (y = b + mx) as:

```excel
H30=CONCATENATE("y = ";TEXT(I26;"#.##0,00");" + ";TEXT(H26;"#.##0,00");".x")
```

Let's write it in human form:

$$
y = -61 + 40x
$$

This formula gives us a predictive model.
Turn any `x` into an estimated `y`.
It's like statistical fortune telling,
except with math instead of incense.

Again, we can see how easy it is to write down
the equation in tabular spreadsheet form.

#### Plot Result

Time to visualize your best-fit line.
Now we will see how well our equation hugs the data.



-- -- --

### Variance and Covariance

Let's now wander into the realm of statistical relationships,
where variables whisper secrets to each other via variance and covariance.
These aren't just fancy words to impress our dinner guests,
they quantify how our data behaves around its mean,
and how two variables dance together.

The equations for sample variance and covariance,
for a sample of data series `(x, y)` is given as follows:

$$
\begin{align*}
s_x^2 &= \frac{1}{n-1}\sum\limits_{i=1}^{n} (x_i - \bar{x})^2 \\
s_y^2 &= \frac{1}{n-1}\sum\limits_{i=1}^{n} (y_i - \bar{y})^2 \\
\text{Cov}(x,y) &= \frac{1}{n-1}\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) \\
\end{align*}
$$

We're calculating these to understand:

* (xᵢ-x̄)² and (yᵢ-ȳ)²: How much variation each variable carries
* (xᵢ-x̄)(yᵢ-ȳ): Whether the variables move together or not

For the series range `K7:K19` (xᵢ-x̄)², `L7:L19` (yᵢ-ȳ)²
and `M7:M19` (xᵢ-x̄)(yᵢ-ȳ) the formula are:

```excel
K7=E7^2
L7=F7^2
M7=E7*F7
...
K19=E19^2
L19=F19^2
M19=E19*F19
```

This prepares our data for calculating how "spread out" the data is,
and whether `x` and `y` have any statistical chemistry.

Now for the totals:

$$
\begin{align*}
\sum\limits_{i=1}^{n} (x_i - \bar{x})^2 &&
\sum\limits_{i=1}^{n} (y_i - \bar{y})^2 &&
\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) \\
\end{align*}
$$

The total variation of the predictor,
∑(xᵢ-x̄)², (yᵢ-ȳ)² and ∑(xᵢ-x̄)(yᵢ-ȳ) can be defined as:

```excel
K22=SUM(K7:K19)
L22=SUM(L7:L19)
M22=SUM(M7:M19)
```

The result of the each total are:

$$
\begin{align*}
\sum\limits_{i=1}^{n} (x_i - \bar{x})^2 &= 182 \\
\sum\limits_{i=1}^{n} (y_i - \bar{y})^2 &= 309218 \\
\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) &= 7280 \\
\end{align*}
$$

To normalize these (and avoid bias )
we divide by degrees of freedom (n - 1).
Now we got the variance sₓ², sy² and also the covariance as:

```excel
K22=K22/E26
L22=L22/F26
M22=M22/E26
```

The result of the statistic properties are:

$$
\begin{align*}
s_X^2 &= 15.17 \\
s_Y^2 &= 25768.17 \\
\text{Cov}(X,Y) &= 606.67 \\
\end{align*}
$$

Variance tells us how unpredictable the data is,
and covariance gives us a sneak peek into,
whether the two variables move together (positive), apart (negative),
or ignore each other entirely (zero, the statistical equivalent of ghosting).

The tabular spreadsheet can be shown as follows:



Oh, and standard deviation is just the square root of variance.

#### Plot Result

We need a visualization so we can interpret
the standard deviation properties against original observed y.



-- -- --

### Correlation Calculation

Time to put the cool shades on our statistics.
Let's measure correlation,
the standardized version of covariance,
that fits nicely between -1 and 1.

From calculated properties above we can continue
to standard deviation sₓ, sy, along with the r (pearson) value:

```excel
K30=SQRT(K26)
L30=SQRT(L26)
M30=M26/(K30*L30)
```

This yields:

$$
\begin{align*}
s_x &= \sqrt{s_X^2} &= && 3.89 \\
s_y &= \sqrt{s_Y^2} &= && 160.52 \\
r_{x,y} &= \frac{\text{Cov}(x,y)}{s_x . s_y} &= && 0,97 \\
\end{align*}
$$

A correlation coefficient of 0.97?
That's about as close to a linear relationship as you can get,
without your data actually proposing marriage.

Note that the pearson coefficient can be denoted in different form.
Alternative formula for r (same dance, different choreography):

r = cov/sₓsy \
r = (∑(xᵢ-x̄).(yᵢ-ȳ))/√(∑(xᵢ-x̄)².∑(yᵢ-ȳ)²)

This way we can calculate the R square (R²)
and also the adjusted R square.
Note that R² for simple linear sample is the same as r².
In this case R² = 0,9417.
But the R² might be different for complex cases.

```excel
M33=M30^2
```

Also there is no need any adjusted R²,
for simple least square population.
But for sample we need to adjust with k=1,
for linear equation then adjusted R² = 0,9364.

```excel
M35=1-(1-M33)*(B26-1)/(B26-1-1)
```

We can have a look at the result,
focusing on this part of following spreadsheet:



R² = 0.94 → "_94% of the variance in `y` is explained by `x`_."
That's nearly everything, the other 6% probably noise,
or maybe just forgot to update their spreadsheets.

#### Plot Result

We need a visualization so we can interpret
the standard deviation properties against predicted y.



-- -- --

### Residual Calculation

Finally, we measure how far off our predictions are.
Every prediction has regrets,
and in statistics, they're called residuals.

We plug in our linear model
from the coefficient of the linear least square,

* m (slope)
* b (intercept)

We can built our curve fitting equation (y = b + mx),
and predict every yᵢ value.

$$
\begin{align*}
\hat{y}_i &= mx_i + b \\
e_i &= y_i - \hat{y}_i \\
\sum\limits_{i=1}^{n} (e_i)^2 &= \sum\limits_{i=1}^{n} (y_i - \hat{y}_i)^2 \\
\end{align*}
$$

Use the spreadsheet to compute.
For the series range `O7:O19` fit(xᵢ), `P7:P19` ϵᵢ (residual),
and `Q7:Q19` ϵᵢ² the formula are:

```excel
O7=$I$26+$H$26*B7
P7=C7-O7
M7=P7^2
...
O19=$I$26+$H$26*B19
P19=C19-O19
M19=P19^2
```

Note that we can use any curve fitting formula,
such as quadratic, cubic and so on,
but for this example we will use our linear one.

Now total residual error.
The total of ϵᵢ² can be defined as:

```excel
Q22=SUM(Q7:Q19)
```

The result of the each total are:

$$
\sum\limits_{i=1}^{n} (e_i)^2 = 18018
$$

The tabular spreadsheet can be shown as follows:



Residuals show us where our model is off.
If the residuals are too wild,
the model might just be blowing statistical smoke.

#### Plot Result

We need a plot to show,
how far off the actual `y_predicted` is,
from our model's predictions.



Plotting residuals is like proofreading our math.
Weou don't always like what we see,
but it makes everything better.

-- -- --

### Regressions Sum Square

Welcome to the world of SSR, Regression Sum of Squares,
or as we statisticians like to call it:
"_How much our predictions flex on the average._"
Here is the RSS:

$$
\sum\limits_{i=1}^{n} (\hat{y}_i - \bar{y})^2
$$

This represents the variation explained by our model.
The bigger it is (relative to total variance),
the more our model is saying,
"_Hey, I actually know what's going on!_"



Naturally, this brings us to SST.
Sum of Squares Total, a.k.a. the full buffet of variance:

The SST (Sum Square Total) is

$$
SST = SSR + RSS
$$

Mathematically, for each observed `yᵢ`, we can say:

$$
\sum\limits_{i=1}^{n} (y_i - \bar{y})^2
$$

Yes, it's a love triangle.
The total variation (SST) is shared between,
* what the model explains (RSS, Regressions Sum Square) and,
* what it misses (SSR, Sum of Squares of Residual).

#### Why does SST = SSR + RSS?

> It is easier to understand using the spreadsheet.

This equation is rooted in partitioning variance.
Essentially slicing up the total variation in our data into:

* **RSS** = Regression Sum of Squares (explained):
  The variation due to the model.
  It's how much our predicted values `ŷᵢ`​ deviate from the mean `ȳᵢ`​.
  If this is large, our model is picking up real structure in the data.

* **SSR** = Sum of Squares of Residual (unexplained):
  What's left over, the part of the variance our model fails to explain, 
  .e., the noisy, chaotic behavior of real-world data.
  It is how far off our predictions are from the actual `yᵢ` values.
  Ideally, this is small.

* **SST** = Total Sum of Squares:
  The total variation in the dependent variable `yᵢ`. essentially:
  “_How spread out is y overall, around its mean?_”

Our model projects the data onto a line,
and splits perfectly between "_explained_" and "_unexplained_."

#### Back to R²

This is the statistical backbone of R².
Want to know **how good** our regression line is?
Start here. It's the source of model validation.

R² (coefficient of determination) is defined as:

$$
R^2 = \frac{SSR}{SST} = 1 - \frac{RSS}{SST}
$$

It answers, "_How much of the variation in `y` is captured by `x`?_”

* If R² = 1, our model explains everything.
  Congratulations, we've either modeled reality perfectly,
  or we've committed statistical heresy (i.e., overfitting).

* If R² = 0,
  our model explains nothing,
  It's as useful as a horoscope.

-- -- --

### t-value and p-value

> Truth or Dare?

Now for the dramatic part, the hypothesis testing,
using `t-value` and `p-value`.
We want to know: "_Is our slope real or just a fluke?_"

First, calculate the degrees of freedom,
For linear equation `k=1`.

$$
df = n - k - 1 = 11
$$

In Excel/Calc we can write this as:

```excel
E30=COUNT(B7:B19)-2
```

Degrees of freedom are like free will in data.
The more we have, the more trust we can put in our analysis.

Next, enter the **Mean Squared Error**.
It tells us how wrong the model is,
on average, for each point:

$$
MSE = \frac{SSE}{df}
$$

In Excel/Calc we can write this as:

```excel
=Q22/$E$30
```

Then we compute the Standard Error of the Slope SE(β1) using MSE.

$$
SE(\beta_1) = \sqrt{\frac{MSE}{\sum_{i=1}^{n}(x_i - \bar{x})^2}}
$$

In Excel/Calc we can write this as:

```excel
=SQRT(Q25/K22)
```

Next, the `t-value`: This is where we look slope in the eye,
and say: “_Prove you matter._”

The `t-value` for the slope coefficient (`β₁`​) is computed,
as the ratio of the estimated slope (`βˉ₁`),
to the standard error of the slope (SE(`β₁`)).
This `t-value` will be used to test the null hypothesis,
that the true slope coefficient is equal to zero.

$$
t = \frac{\bar{\beta}_1}{SE(\beta_1)}
$$

In Excel/Calc we can write this as:

```excel
=H26/Q30
```

And finally, the `p-value`, the real drama queen.
It's the probability that our slope is due to random chance.
The smaller the `p-vlue`, the more confident we are,
that our model actually means something.

Here is the p-value for two tail test.

$$
p = 2 \times P(T > |t|)
$$

This is to complex for manual calculation.
so I use built-in formula instead.

In spreadsheet speak:

```excel
=T.DIST.2T(Q35;$E$30)
```

The `p-value` is our model's confession.
It either says: “"_Yep, I'm legit,_",
or "_Oops, maybe I was just noise._"

Here are the results of this statistical soap opera:

$$
\begin{align*}
df &= 11 \\
MSE &= 1638 \\
SE(\beta_1) &= 3.00 \\
t-value &= 13.33 \\
p-value &= 0,0000000391 \\
\end{align*}
$$

We have an incredibly significant result.
Oour slope isn't just a good guess,
it's a statistically valid superstar.

Check it out here:



We have a good confidence in our curve fitting function.

#### Alternative Worksheet

If you''e not into one worksheet layout, don't worry.
Spreadsheet is like statistics: it tolerates many truths.

Here's an alternative way of laying things out:



Just remember, the numbers must dance the same.
No matter how we rearrange the ballroom.

-- -- --

### Built In Formula

> The Lazy Genius of Regression

Who needs to crunch numbers by hand,
when spreadsheets and Python will gladly do our bidding?
Let's explore how built-in formulas make regression analysis,
feel less like statistical calculus,
and more like statistical calculus-on-autopilot.

#### Worksheet Source

> Your DIY Regression Playground

Welcome to spreadsheet heaven.
You'll find all the formulas preloaded in this `.ods` file.

* **github.com/.../math/trend/examples-properties.ods**

Even though everything here can work in Excel,
we're using LibreOffice.
Why? Because `.ods` lets us play with named ranges more flexibly,
and frankly, `.xlsx` sometimes throws a tantrum.

Still prefer Excel? We got you:

* **github.com/.../math/trend/examples-properties.xlsx**

#### Meet the Data

Let's revisit our familiar cast of statistical characters:



* xᵢ observed: `B7:B19`,
* yᵢ observed: `C7:C19`,
* ŷᵢ predicted: `D7:D19` calculated from m and b.

#### Named Range

_B7:B19 is Not a Personality_

To make the equation less cryptic,
we can define named range.
This can be done in both Excel and Calc:



Let's give our ranges real names.
"_x_observed_" just sounds more mature than "B7:B19".

* `B7:B19`: x_observed.
* `C7:C19`: y_observed.
* `D7:D19`: y_predicted.

Think of it as giving our variables,
name tags at a regression conference.

#### Using Array Operation

We can rebuild tabular woksheet from previous article,
into a simple one using Excel/Calc formula
with the help of `SUMSQ` formula.

With just using array formulas and built-in functions,
we can have direct result into a cell.
Because if Excel has a button for it,
why type three columns by hand?



Here the predicted value of `ŷᵢ` in `D7:D19`,
are calculated from `m ($G$17)` and `b ($G$18)`.

The complete formula can be shown here:

| properties              | formula                                             |
| ----------------------- | --------------------------------------------------- |
| ∑x	                    |  =SUM(x_observed)                                   |
| ∑y	                    |  =SUM(y_observed)                                   |
| n	                      |  =COUNT(x_observed)                                 |
| n-1	                    |  =G9-1                                              |
| df = n-k-1	            |  =G9-2                                              |
| x̄ (mean)	               |  =AVERAGE(x_observed)                               |
| ȳ (mean)	               |  =AVERAGE(y_observed)                               |
| ∑(xᵢ-x̄)²	               | {=SUMSQ(x_observed-$G$12)}                          |
| ∑(yᵢ-ȳ)²	               | {=SUMSQ(y_observed-$G$13)}                          |
| ∑(xᵢ-x̄)(yᵢ-ȳ)	          |  =SUMPRODUCT((x_observed-$G$12),(y_observed-$G$13)) |
| β̅₁ = m (slope)	         |  =G16/G14                                           |
| β̅₀ = b (intercept)	     |  =G13-G17*G12                                       |
| sₓ²=∑(xᵢ-x̄)²/(n-1)	     |  =G14/G10                                           |
| sy²=∑(yᵢ-ȳ)²/(n-1)	     |  =G15/G10                                           |
| cov=∑(xᵢ-x̄)(yᵢ-ȳ)/(n-1)	|  =G16/G10                                           |
| sₓ (std dev)	          |  =SQRT(G19)                                         |
| sy (std dev)	          |  =SQRT(G20)                                         |
| r (pearson)=cov/sₓsy	  |  =G21/(G22*G23)                                     |
| R² for linear is r²	    |  =G24^2                                             |
| adjusted R²	            |  =1-(1-G25)*G10/G11                                 |
| SSE = ∑ϵᵢ²	            | {=SUMSQ(y_observed-D7:D19)}                         |
| MSE = SSE/df	          |  =G27/G11                                           |
| SE(β₁) = std err slope	|  =SQRT(G28/G14)                                     |
| t-value = β̅₁/SE(β₁)	   |  =G17/G29                                           |
| p-value	                |  =T.DIST.2T(G30;G11)                                |


We're covering all our greatest statistical hits:
slope, variance, correlation, R², t-tests,
and the always-glamorous p-value.

This condenses a ton of regression math,
into digestible spreadsheet logic.
Less time formatting cells,
more time eating snacks and doing science.

#### Using Statistic Formula

> The Built-in Shortcut

Furthermore we can use statistic formula.

Want to double-check your math?
Or just feel like living dangerously by trusting Excel's statistical engine?
Let's name new ranges for a fresh worksheet:

* `B7:B19`: x_sample.
* `C7:C19`: y_sample.
* `D7:D19`: y_fit.

Then we let built-in stats formulas take over.



| properties              | formula                                         |
| ----------------------- | ----------------------------------------------- |
| ∑x	                    |  =SUM(x_sample)                                 |
| ∑y	                    |  =SUM(y_sample)                                 |
| n	                      |  =COUNT(x_sample)                               |
| n-1	                    |  =G9-1                                          |
| df = n-k-1	            |  =G9-2                                          |
| x̄ (mean)	               |  =AVERAGE(x_sample)                             |
| ȳ (mean)	               |  =AVERAGE(y_sample)                             |
| ∑(xᵢ-x̄)²	               | {=SUMSQ(x_sample-$G$12)}                        |
| ∑(yᵢ-ȳ)²	               | {=SUMSQ(y_sample-$G$13)}                        |
| ∑(xᵢ-x̄)(yᵢ-ȳ)	          |  =SUMPRODUCT((x_sample-$G$12),(y_sample-$G$13)) |
| β̅₁ = m (slope)	         |  =SLOPE(y_sample,x_sample)                      |
| β̅₀ = b (intercept)	     |  =INTERCEPT(y_sample,x_sample)                  |
| sₓ² (variance)	        |  =VAR.S(x_sample)                               |
| sy² (variance)	        |  =VAR.S(y_sample)                               |
| covariance	            |  =COVARIANCE.S(x_sample,y_sample)               |
| sₓ (std dev)	          |  =STDEV.S(x_sample)                             |
| sy (std dev)	          |  =STDEV.S(y_sample)                             |
| r (pearson)	            |  =PEARSON(x_sample,y_sample)                    |
| R² coeff	              |  =RSQ(y_sample,x_sample)                        |
| adjusted R²	            |  =1-(1-G25)*G10/G11                             |
| SSE = ∑ϵᵢ²	            | {=SUMSQ(y_sample-y_fit)}                        |
| MSE = SSE/df	          |  =G27/G11                                       |
| SE(β₁) = std err slope	|  =SQRT(G28/G14)                                 |
| t-value = β̅₁/SE(β₁)	   |  =G17/G29                                       |
| p-value	                |  =T.DIST.2T(G30;G11)                            |

The parameter required for each statistic formula is clear now.
These functions reduce error and save time.
Perfect when we've had our third coffee,
and still can't remember what ∑(xᵢ - x̄)² stands for.

#### Pearson Correlation Coeffecient

> Measuring Statistical Chemistry

Need to measure the linear love between `x` and `y`?
Use Pearson's `r` correlation coefficient:

```excel
=PEARSON(B7:B19;C7:C19) 
```

The formula for pearson is:

$$
r_{x,y} \frac{\text{Cov}(x,y)}{s_x . s_y} \\
$$

Which we can write manually in Excel/Calc as:

```excel
=COVARIANCE.P(B7:B19, C7:C19) / (STDEV.P(B7:B19) * STDEV.P(C7:C19))
```

And if you're feeling masochistic,
the Pearson correlation coefficient can also be expressed as follows:

$$
r = \frac{\sum (x_i - \bar{x}) \cdot (y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \cdot \sum (y_i - \bar{y})^2}}
$$

Sometimes you want to check if your equation right.
Again, the Excel/Calc formula can be rewritten as follows,
and having the same result.

```excel
= (SUM((B7:B19 - AVERAGE(B7:B19)) * (C7:C19 - AVERAGE(C7:C19)))) 
/ (SQRT(SUM((B7:B19 - AVERAGE(B7:B19))^2) * SUM((C7:C19 - AVERAGE(C7:C19))^2)))
```

Now you know, how helpful the built-in formula is,
compared to this complex formula above.

#### R Square

> The MVP of Model Metrics

Want to know how much of the variation in `y` is explained by our model?
Excel/Calc has a built-in formula for R Square (R²):

```excel
=RSQ(C7:C19;B7:B19)
```

The R Square (R²) for simple linear regression can be expressed as follows:

$$
\begin{align*}
r_{x,y} &= \frac{\text{Cov}(x,y)}{s_x . s_y} \\
R^2     &= r_{x,y}^2
\end{align*}
$$

Here's the long-form version.
The general R Square (R²) is defined as:

$$
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

Or furthermore, we can go low-level.

$$
R^2 = 1 - \frac{\sum (y_i - (\hat{\beta}_1 x_i + \hat{\beta}_0))^2}{\sum (y_i - \bar{y})^2}
$$

Down to the nuts and bolts,
the Excel/Calc formula can be rewritten as:

```excel
=1-SUM((C7:C19 - (B7:B19*G22+G24))^2)/SUM((C7:C19 - H9)^2)
```

The way you manage the calculation is depend on your situation.
Most of the time we can use simple `rsq` formula,
but sometimes we need to go low level,
for use with programming or just intellectual curiosity.

Let's see how RSQ behave in non-linear curve fitting discussed later on.

#### Compare and Contrast: Manual vs Built-in

Feel free to compare both methods, side-by-side.
Between manual formula and built-in formula as shown below:



Like a true stats nerd, always double-check our work.
But also, enjoy the shortcuts modern tools give us.
Regression shouldn't feel like a root canal.

Now we are ready to make statistical model,
in our worksheet to suit our specific needs.

_How you make the model is up to you._

-- -- --

### What Lies Ahead 🤔?

That method above? Elegant, yes.
But let's not kid ourselves.
Naturally, there's a simpler way.

If we want a spreadsheet model that doesn't require a PhD.
Or three cups of coffee and a blank stare,
we'll need a method more fit for everyday use.
Something robust, readable, and less likely to induce formula fatigue.

The easier it is to calculate,
the more likely we'll actually use it.
That's why in the next part of our adventure,
we shift gears from cells and formulas,
to the comforting embrace of Python.
There, we'll build tools that are both reusable,
and less fiddly than spreadsheet gymnastics.

Grab our virtual lab coat and join us in:
**Trend - Properties - Python Tools**.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Getting to know statistical properties,
> using python library step by step.

_Why are we even doing this?_

We should know the statistical concept,
before wrestling with a statistical model using worksheet formula.
Understanding what the mean, variance, skewness,
and their rowdy cousins really do helps us,
in debugging more effectively,
when something goes wrong in our calculation.

Here’s the usual path:

* Understand the equation.
* Implement it in a spreadsheet.
* Rebuild it in Python like a proper data monk.
* Use it for slick plots, automation,
  or feeding it into AI models.

We're not just learning stats.
We’re learning how to weaponize stats with tools like,
pandas, numpy, and scipy.
One property at a time.

From equation, and statistic model in worksheet.
we can step further to implement the model in scripting.
This way we can go further with automation,
nice visualization, and combine with other technologies.

-- -- --

### Manual Calculation

> Doing it the hard way, so Python doesn’t have to.

Before we let libraries like scipy do all the heavy lifting,
it's important to know what they're actually doing under the hood.
Think of this as the "manual transmission" part of statistical driving.
We’ll understand the gears better before hitting the cruise control.

We can summarize all manual calculation of,
statistic properties from previous worksheet with python:

#### Python Source

All the Python sorcery we're about to walk through lives here:

* **51-least-square.py**

```python
import numpy as np

# Getting Matrix Values
pairCSV = np.genfromtxt("50-samples.csv",
  skip_header=1, delimiter=",", dtype=float)

# Extract x and y values from CSV data
x_observed = pairCSV[:, 0]
y_observed = pairCSV[:, 1]

# Number of data points
n = len(x_observed)

# Calculate sums
x_sum = np.sum(x_observed)
y_sum = np.sum(y_observed)

# Calculate means
x_mean = np.mean(x_observed)
y_mean = np.mean(y_observed)

# Output of basic properties
print(f'{f"n":10s} = {n:4d}')
print(f'∑x (total) = {x_sum:7.2f}')
print(f'∑y (total) = {y_sum:7.2f}')
print(f'x̄ (mean)   = {x_mean:7.2f}')
print(f'ȳ (mean)   = {y_mean:7.2f}')
print()

# Calculate deviations
x_deviation = x_observed - x_mean
y_deviation = y_observed - y_mean

# Calculate squared deviations
x_sq_deviation = np.sum(x_deviation ** 2)
y_sq_deviation = np.sum(y_deviation ** 2)

# Calculate cross-deviation
xy_cross_deviation = np.sum(x_deviation * y_deviation)
# Calculate slope (m) and intercept (b)
m_slope = xy_cross_deviation / x_sq_deviation
b_intercept = y_mean - m_slope * x_mean

# Output of least square calculation
print(f'∑(xᵢ-x̄)    = {np.sum(x_deviation):9.2f}')
print(f'∑(yᵢ-ȳ)    = {np.sum(y_deviation):9.2f}')
print(f'∑(xᵢ-x̄)²   = {x_sq_deviation:9.2f}')
print(f'∑(yᵢ-ȳ)²   = {y_sq_deviation:9.2f}')
print(f'∑(xᵢ-x̄)(yᵢ-ȳ)  = {xy_cross_deviation:9.2f}')
print(f'm (slope)      = {m_slope:9.2f}')
print(f'b (intercept)  = {b_intercept:9.2f}')
print()

print(f'Equation     y = ' \
  + f'{b_intercept:5.2f} + {m_slope:5.2f}.x')
print()

# Calculate variance
x_variance = x_sq_deviation / (n-1)
y_variance = y_sq_deviation / (n-1)

# Calculate covariance
xy_covariance = xy_cross_deviation / (n-1)

# Calculate standard deviations
x_std_dev = np.sqrt(x_variance)
y_std_dev = np.sqrt(y_variance)

# Calculate Pearson correlation coefficient (r)
r = xy_covariance / (x_std_dev * y_std_dev)

# Calculate R-squared (R²)
r_squared = r ** 2

# Output of correlation calculation
print(f'sₓ² (variance) = {x_variance:9.2f}')
print(f'sy² (variance) = {y_variance:9.2f}')
print(f'covariance     = {xy_covariance:9.2f}')
print(f'sₓ (std dev)   = {x_std_dev:9.2f}')
print(f'sy (std dev)   = {y_std_dev:9.2f}')
print(f'r (pearson)    = {r:9.2f}')
print(f'R²             = {r_squared:9.2f}')
print()

# Create regression line
y_fit = m_slope * x_observed + b_intercept
y_err = y_observed - y_fit

# Calculate sum of squared residuals
ss_residuals = np.sum(y_err ** 2)

# Calculate degrees of freedom
df = n - 2

# Calculate variance of residuals (MSE)
var_residuals = ss_residuals / df

# Calculate standard error of the slope
std_err_slope = np.sqrt(var_residuals / x_sq_deviation)

# Calculate t-value
t_value = m_slope / std_err_slope

# Output the results
print(f'SSR = ∑ϵ²           = {ss_residuals:9.2f}')
print(f'MSE = ∑ϵ²/(n-2)     = {var_residuals:9.2f}')
print(f'SE(β₁)  = √(MSE/sₓ) = {std_err_slope:9.2f}')
print(f't-value = β̅₁/SE(β₁) = {t_value:9.2f}')
print()

```

#### Data Source

We’ve moved past hardcoded numbers.
Let’s be civilized and use a CSV:

* **50-samples.csv**:

What's inside?
A sweet little dataset with `x_observed` and `y_observed` pairs.

```output
x,y
0,5
1,12
2,25
3,44
4,69
5,100
6,137
7,180
8,229
9,284
10,345
11,412
12,485
```



#### Loading Data Series

First, we politely invite the data into memory:

```python
import numpy as np

# Getting Matrix Values
pairCSV = np.genfromtxt("50-samples.csv",
  skip_header=1, delimiter=",", dtype=float)

# Extract x and y values from CSV data
x_values = pairCSV[:, 0]
y_values = pairCSV[:, 1]
```



Garbage in, garbage out. Always know how our data is being loaded.

#### Basic Properties

Time to warm up with some classic stats:

```python
# Number of data points
n = len(x_observed)

# Calculate sums
x_sum = np.sum(x_observed)
y_sum = np.sum(y_observed)

# Calculate means
x_mean = np.mean(x_observed)
y_mean = np.mean(y_observed)

# Output of basic properties
print(f'{f"n":10s} = {n:4d}')
print(f'∑x (total) = {x_sum:7.2f}')
print(f'∑y (total) = {y_sum:7.2f}')
print(f'x̄ (mean)   = {x_mean:7.2f}')
print(f'ȳ (mean)   = {y_mean:7.2f}')
print()
```



These are the building blocks.
Like knowing the flour, sugar, and eggs before we bake a regression cake.

#### Deviations

Now we look at how each point misbehaves compared to the average.
Deviations are the rebels of our dataset, with the least square coefficient:

```python
# Calculate deviations
x_deviation = x_observed - x_mean
y_deviation = y_observed - y_mean

# Calculate squared deviations
x_sq_deviation = np.sum(x_deviation ** 2)
y_sq_deviation = np.sum(x_deviation ** 2)

# Calculate cross-deviation
xy_cross_deviation = np.sum(x_deviation * y_deviation)
# Calculate slope (m) and intercept (b)
m_slope = xy_cross_deviation / x_sq_deviation
b_intercept = y_mean - m_slope * x_mean
```



Now let's print our slope-intercept poetry, in terminal.

```python
# Output of least square calculation
print(f'∑(xᵢ-x̄)    = {np.sum(x_deviation):9.2f}')
print(f'∑(yᵢ-ȳ)    = {np.sum(y_deviation):9.2f}')
print(f'∑(xᵢ-x̄)²   = {x_sq_deviation:9.2f}')
print(f'∑(yᵢ-ȳ)²   = {y_sq_deviation:9.2f}')
print(f'∑(xᵢ-x̄)(yᵢ-ȳ)  = {xy_cross_deviation:9.2f}')
print(f'm (slope)      = {m_slope:9.2f}')
print(f'b (intercept)  = {b_intercept:9.2f}')
print()

print(f'Equation     y = ' \
  + f'{b_intercept:5.2f} + {m_slope:5.2f}.x')
print()
```



This is our regression line.
If stats were a rom-com,
this would be the love interest.
Everything leads to this.

#### Variance and Covariance

Let's dive into the spread of our data,
and their relationship status by getting the R square:

```python
# Calculate variance
x_variance = x_sq_deviation / n
y_variance = y_sq_deviation / n

# Calculate covariance
xy_covariance = xy_cross_deviation / n

# Calculate standard deviations
x_std_dev = np.sqrt(x_variance)
y_std_dev = np.sqrt(y_variance)

# Calculate Pearson correlation coefficient (r)
r = xy_covariance / (x_std_dev * y_std_dev)

# Calculate R-squared (R²)
r_squared = r ** 2
```



Print it loud and proud:

```python
# Output of correlation calculation
print(f'sₓ² (variance) = {x_variance:9.2f}')
print(f'sy² (variance) = {y_variance:9.2f}')
print(f'covariance     = {xy_covariance:9.2f}')
print(f'sₓ (std dev)   = {x_std_dev:9.2f}')
print(f'sy (std dev)   = {y_std_dev:9.2f}')
print(f'r (pearson)    = {r:9.2f}')
print(f'R²             = {r_squared:9.2f}')
print()
```



R² tells you how well our model is doing.
If it's close to 1, our model’s a genius.
If not... maybe go meditate on your data.

#### Residuals

This is where we check how wrong we are, elegantly.
Let's get the correlation, until we get the t-value.

```python
# Create regression line
y_fit = m_slope * x_observed + b_intercept
y_err = y_observed - y_fit

# Calculate sum of squared residuals
ss_residuals = np.sum(y_err ** 2)

# Calculate degrees of freedom
df = n - 2

# Calculate variance of residuals (MSE)
var_residuals = ss_residuals / df

# Calculate standard error of the slope
std_err_slope = np.sqrt(var_residuals / x_sq_deviation)

# Calculate t-value
t_value = m_slope / std_err_slope
```



Wrap it up with a bow:

```python
# Output the results
print(f'SSR = ∑ϵ²           = {ss_residuals:9.2f}')
print(f'MSE = ∑ϵ²/(n-2)     = {var_residuals:9.2f}')
print(f'SE(β₁)  = √(MSE/sₓ) = {std_err_slope:9.2f}')
print(f't-value = β̅₁/SE(β₁) = {t_value:9.2f}')
print()
```



The `t-value` gives use an idea of how significant your slope is.
If it's large, congratulations,
Our regression is statistically more than just a coincidence.

#### Output Result

Here’s the satisfying full output, no magic, no black boxes.
Just raw, honest math:

```output
n          =   13
∑x (total) =   78.00
∑y (total) = 2327.00
x̄ (mean)   =    6.00
ȳ (mean)   =  179.00

∑(xᵢ-x̄)    =      0.00
∑(yᵢ-ȳ)    =      0.00
∑(xᵢ-x̄)²   =    182.00
∑(yᵢ-ȳ)²   = 309218.00
∑(xᵢ-x̄)(yᵢ-ȳ)  =   7280.00
m (slope)      =     40.00
b (intercept)  =    -61.00

Equation     y = -61.00 + 40.00.x

sₓ² (variance) =     14.00
sy² (variance) =  23786.00
covariance     =    560.00
sₓ (std dev)   =      3.74
sy (std dev)   =    154.23
r (pearson)    =      0.97
R²             =      0.94

SSR = ∑ϵ²           =  18018.00
MSE = ∑ϵ²/(n-2)     =   1638.00
SE(β₁)  = √(MSE/sₓ) =      3.00
t-value = β̅₁/SE(β₁) =     13.33
```



This is the full audit trail.
If a fellow nerd asks, "_Did you check the residuals?_",
we can say "_Absolutely_."

#### Interactive JupyterLab

Want to play with it live?
Fire up the interactive version here:

You can obtain the interactive `Jupyter Notebook` in this following link:

* **51-least-square.py**

-- -- --

### Properties Helper

As you can see the the script above is too long,
for just obtaining least square coefficient.
We can simply use with python library,
to get only what we need, then shorten the script.

We also need to refactor the code for reuse,
So before that we need to solve this refactoring issue.

#### Handling Multiple Variables

Script above using a lot of statistics properties,
these local variables are scattered,
and the worst part is we don't know what we need,
while doing statistic exploration.
This makes coding harder to modularized.

With python we can use python `locals()` built-in method.

* **Properties.py**

With this `locals()`, we can bundle all variables as dictionary.

```python
def get_properties(file_path) -> Dict:
  ...

  return locals()
```

The in other python files,
we can load properties from `Properties.py`` helper
and unpack them into local variables.

```python
properties = get_properties("50-samples.csv")
locals().update(properties)
```

Now, in our other Python scripts,
we can just call this like ordering takeout:

```python
def display(properties: Dict) -> None:
  p = Dict2Obj(properties)

  ...
```

Or go full OOP and pass them around in a function:

```python
class Dict2Obj:
  def __init__(self, properties_dict):
    self.__dict__.update(properties_dict)
```



#### The Properties Helper

Let's build a **reusable** Python helper for basic statistical properties.
Think of this as our multipurpose wrench for trend analysis.

The helper has two main parts:
* `get_properties()` for computation
* `display()` for output

The first half is similar to our earlier longhand script.
But now it's organized and tucked inside a function:

```python
def get_properties(file_path) -> Dict:
  # Getting Matrix Values
  pairCSV = np.genfromtxt(file_path,
    skip_header=1, delimiter=",", dtype=float)
  
  # Extract x and y values from CSV data
  x_observed = pairCSV[:, 0]
  y_observed = pairCSV[:, 1]

  # Number of data points
  n = len(x_observed)

  # Calculate sums
  x_sum = np.sum(x_observed)
  y_sum = np.sum(y_observed)

  # Calculate means
  x_mean = np.mean(x_observed)
  y_mean = np.mean(y_observed)
```



Now, let’s crank the gears using `numpy`:

```python
  # Calculate variance
  x_variance = np.var(x_observed)
  y_variance = np.var(y_observed)

  # Calculate covariance
  xy_covariance = np.cov(x_observed, y_observed)[0, 1]

  # Calculate standard deviations
  x_std_dev = np.std(x_observed)
  y_std_dev = np.std(y_observed)
```



And then we can get the regression using `linregress()`:

```python
  # Calculate slope (m), intercept (b),
  # and other regression parameters
  m_slope, b_intercept, r_value, p_value, \
  std_err_slope = linregress(x_observed, y_observed)

  # Create regression line
  y_fit = m_slope * x_observed + b_intercept
  y_err = y_observed - y_fit

  return locals()
```



Then we can display the properties in different function.
Separating the model and the view.

```python
def display(properties: Dict) -> None:
  p = Dict2Obj(properties)

  # Output basic properties
  print(f'{f"n":10s} = {p.n:4d}')
  print(f'∑x (total) = {p.x_sum:7.2f}')
  print(f'∑y (total) = {p.y_sum:7.2f}')
  print(f'x̄ (mean)   = {p.x_mean:7.2f}')
  print(f'ȳ (mean)   = {p.y_mean:7.2f}')
  print()

  # Output statistics properties
  print(f'sₓ² (variance) = {p.x_variance:9.2f}')
  print(f'sy² (variance) = {p.y_variance:9.2f}')
  print(f'covariance     = {p.xy_covariance:9.2f}')
  print(f'sₓ (std dev)   = {p.x_std_dev:9.2f}')
  print(f'sy (std dev)   = {p.y_std_dev:9.2f}')
  print(f'm (slope)      = {p.m_slope:9.2f}')
  print(f'b (intercept)  = {p.b_intercept:9.2f}')
  print()

  print(f'Equation     y = ' \
    + f'{p.b_intercept:5.2f} + {p.m_slope:5.2f}.x')
  print()
```



Separation of concerns isn't just good design.
It’s emotional hygiene.
Keep our calculations away from our presentation layer.

-- -- --

### Using The Helper

In the previous section,
we built a reusable statistical Swiss Army knife.
Now it’s time to use it,
To crunch numbers with elegance
and avoid turning our script into spaghetti stats

We've tamed the math, now let's teach it to dance.
Let's go further with other statistical properties.

#### Python Source

You can find the full script here:

* **52-least-square.py**

```python
import numpy as np

# Local Library
from Properties import get_properties, display

# Load properties from Properties.py helper
# and unpack them into local variables
properties = get_properties("50-samples.csv")
display(properties)
locals().update(properties)

# Calculate R-squared (R²)
r_squared = r_value ** 2

# Output of correlation calculation

print(f'sₓ (std dev)   = {x_std_dev:9.2f}')
print(f'sy (std dev)   = {y_std_dev:9.2f}')
print(f'r (pearson)    = {r_value:9.2f}')
print(f'R²             = {r_squared:9.2f}')
print()

# Create regression line
y_fit = m_slope * x_observed + b_intercept
y_err = y_observed - y_fit

# Calculate variance of residuals (MSE)
var_residuals = np.sum(y_err ** 2) / (n - 2)

# Calculate t-value
t_value = m_slope / std_err_slope

# Output the results
print(f'MSE = ∑ϵ²/(n-2)     = {var_residuals:9.2f}')
print(f'SE(β₁)  = √(MSE/sₓ) = {std_err_slope:9.2f}')
print(f't-value = β̅₁/SE(β₁) = {t_value:9.2f}')
print()
```


This is where the simple computation meets simple reusability.

#### Loading The Helper

The `get_properties()` function bundles everything we need,
from means to regression slopes,
and hands them over in a tidy dictionary.
Then, like a magician pulling rabbits from a hat
(except the rabbits are statistical metrics),
we unpack them into our local workspace.

```python
import numpy as np

# Local Library
from Properties import get_properties, display

# Load properties from Properties.py helper
# and unpack them into local variables
properties = get_properties("50-samples.csv")
display(properties)
locals().update(properties)
```

Maintaining dozens of variables manually is like,
keeping track of pigeons in a park.
Let Python herd them for us.



#### Calculate R-squared (R²)

> Proceed Further

Now we calculate can proceed other calculation,
such as the coefficient of determination.

```python
# Calculate R-squared (R²)
r_squared = r_value ** 2

# Output of correlation calculation

print(f'sₓ (std dev)   = {x_std_dev:9.2f}')
print(f'sy (std dev)   = {y_std_dev:9.2f}')
print(f'r (pearson)    = {r_value:9.2f}')
print(f'R²             = {r_squared:9.2f}')
print()
```

R² tells us how much of the variation in `y`,
that we've successfully explained with `x`.
It's the academic equivalent of a victory lap.



#### Calculating t-value

> Academic Showdown

Once we have residuals,
we can compute the `t-value` to test the slope's statistical significance.
It's like asking, "Hey, β₁, are you real or just random noise?".

```python
# Create regression line
y_fit = m_slope * x_observed + b_intercept
y_err = y_observed - y_fit

# Calculate variance of residuals (MSE)
var_residuals = np.sum(y_err ** 2) / (n - 2)

# Calculate t-value
t_value = m_slope / std_err_slope

# Output the results
print(f'MSE = ∑ϵ²/(n-2)     = {var_residuals:9.2f}')
print(f'SE(β₁)  = √(MSE/sₓ) = {std_err_slope:9.2f}')
print(f't-value = β̅₁/SE(β₁) = {t_value:9.2f}')
print()
```



Regression without checking `t-values` is like,
baking a cake and skipping the taste test.
It might look good, but is it actually meaningful?

#### Output Result

The final output gives us all the important values at a glance.
No need to dive into formulas every time.
Our helper did the heavy lifting.
How about us? We just sip coffee and interpret.

```output
n          =   13
∑x (total) =   78.00
∑y (total) = 2327.00
x̄ (mean)   =    6.00
ȳ (mean)   =  179.00

sₓ² (variance) =     14.00
sy² (variance) =  23786.00
covariance     =    606.67
sₓ (std dev)   =      3.74
sy (std dev)   =    154.23
m (slope)      =     40.00
b (intercept)  =    -61.00

Equation     y = -61.00 + 40.00.x

sₓ (std dev)   =      3.74
sy (std dev)   =    154.23
r (pearson)    =      0.97
R²             =      0.94

MSE = ∑ϵ²/(n-2)     =   1638.00
SE(β₁)  = √(MSE/sₓ) =      3.00
t-value = β̅₁/SE(β₁) =     13.33
```



#### Interactive JupyterLab

Want to poke around and tweak things?
Grab the interactive `Jupyter notebook`:

* **52-least-square.py**

A playground where the regression lines are friendly,
and the errors politely raise their hands.

-- -- --

### Further Library

If you've ever wondered how to raise eyebrows,
at a party full of statisticians, just whisper:

“_I calculated the p-value myself..._”

Let's peek under the hood and manually compute that mysterious number.
Yes, Python makes the calculation of `p-value` using `t_distribution` easy,
but understanding the math earns you honorary membership in the 

#### Python Source

Full script available here:

* **52-p-value.py**

```python
import numpy as np
from scipy.stats import linregress
from scipy.stats import t as t_distribution

# Getting Matrix Values
pairCSV = np.genfromtxt("50-samples.csv",
  skip_header=1, delimiter=",", dtype=float)

# Extract x and y values from CSV data
x_observed = pairCSV[:, 0]
y_observed = pairCSV[:, 1]

# Number of data points
n = len(x_observed)

# Calculate slope (m), intercept (b),
# and other regression parameters
m_slope, b_intercept, r_value, p_value, \
std_err_slope = linregress(x_observed, y_observed)

# Create regression line
y_fit = m_slope * x_observed + b_intercept
y_err = y_observed - y_fit

# Calculate degrees of freedom
df = n - 2

# Calculate variance of residuals (MSE)
var_residuals = np.sum(y_err ** 2) / (n - 2)

# Calculate t-value
t_value = m_slope / std_err_slope

# Calculate two-tailed p-value
p_value = 2 * (1 - t_distribution.cdf(abs(t_value), df))

# Output the results
print(f'Slope (m): {m_slope:.2f}')
print(f'Standard error of the slope: {std_err_slope:.2f}')
print(f't-value: {t_value:.2f}')
print(f'Two-tailed p-value: {p_value:.10f}')
print()

# Define the significance level (alpha)
alpha = 0.05  # for a two-tailed test

# Calculate critical t-value
critical_t = t_distribution.ppf(1 - alpha / 2, df)

# Calculate the p-value manually
td = t_distribution.cdf(abs(t_value), df)
if abs(t_value) > critical_t:
  p_value_manual = 2 * (1 - td)
else:
  p_value_manual = 2 * td

print(f'Critical t-value: {critical_t:.10f}')
print(f'Manually calculated p-value: {p_value_manual:.10f}')
```

#### T Distribution

> Just forget the helper

First we need to import the `t-distribution`,
Mote that we do not need `Properties` helper,
to show how easy it is to obtain the value with python.

```python
import numpy as np
from scipy.stats import linregress
from scipy.stats import t as t_distribution
```

Now, let's grab the data:

```python
# Getting Matrix Values
pairCSV = np.genfromtxt("50-samples.csv",
  skip_header=1, delimiter=",", dtype=float)

# Extract x and y values from CSV data
x_observed = pairCSV[:, 0]
y_observed = pairCSV[:, 1]

# Number of data points
n = len(x_observed)
```



Sometimes it's refreshing to calculate things manually.
Like grinding our own coffee instead of using instant.

#### Linear Regression

Let's run a quick regression with `linregress`,
which kindly gives us the slope, intercept, and standard error,
no questions asked.

```python
# Calculate slope (m), intercept (b),
# and other regression parameters
m_slope, b_intercept, r_value, p_value, \
std_err_slope = linregress(x_observed, y_observed)

# Create regression line
y_fit = m_slope * x_observed + b_intercept
y_err = y_observed - y_fit
```

This is our first checkpoint.
`linregress` gives us the `t-value` and `p-value`,
but we’ll double-check it ourselves,
just like a paranoid statistician should.



#### P Value and T Value

Then manually calculate `p value` using `cdf()`.

```python
# Calculate degrees of freedom
df = n - 2

# Calculate variance of residuals (MSE)
var_residuals = np.sum(y_err ** 2) / (n - 2)

# Calculate t-value
t_value = m_slope / std_err_slope

# Calculate two-tailed p-value
p_value = 2 * (1 - t_distribution.cdf(abs(t_value), df))

# Output the results
print(f'Slope (m): {m_slope:.2f}')
print(f'Standard error of the slope: {std_err_slope:.2f}')
print(f't-value: {t_value:.2f}')
print(f'Two-tailed p-value: {p_value:.10f}')
print()
```



The `cdf()` function helps us estimate the probability of getting a `t-value`.

#### P Value and T Value

> The Long Way: trust, but verify.
> Manual Verification with Critical `t`

Let's pretend we're suspicious of scipy,
and want to verify everything with our own critical `t-table` logic.

And also calculate `p-value` manually using critical `t-value`,
using `ppf` and also `cdf`.

```python
# Define the significance level (alpha)
alpha = 0.05  # for a two-tailed test

# Calculate critical t-value
critical_t = t_distribution.ppf(1 - alpha / 2, df)

# Calculate the p-value manually
td = t_distribution.cdf(abs(t_value), df)
if abs(t_value) > critical_t:
  p_value_manual = 2 * (1 - td)
else:
  p_value_manual = 2 * td

print(f'Critical t-value: {critical_t:.10f}')
print(f'Manually calculated p-value: {p_value_manual:.10f}')
```



#### Output Result

And voilà, both automatic and manual methods agree.
Our slope is statistically significant,
and now we know exactly why.

```output
Slope (m): 40.00
Standard error of the slope: 3.00
t-value: 13.33
Two-tailed p-value: 0.0000000391

Critical t-value: 2.2009851601
Manually calculated p-value: 0.0000000391
```



#### Ask Your Statistician

That's it for this hands-on walkthrough!
And remember: when in doubt, consult your friendly neighborhood statistician
We're the only people who get excited over tiny `p-values`.

#### Interactive JupyterLab

You can obtain the interactive `JupyterLab` in this following link:

* **52-p-value.py**

-- -- --

### What's the Next Exciting Step 🤔?

Now that we've crunched the numbers,
danced with `t-values`, and wrestled with `p-values`,
it's time to stop staring at digits,
and see what the data is really trying to say.

Visualization turns abstract math into intuitive insight.
It's the difference between saying, "_This line fits pretty well,_"
and showing a graph that makes your colleagues say, "_Ah, now I get it._"

Ready to turn numbers into pictures? Dive into the next chapter:
**Trend - Properties - Visualization**.
Where math meets art, and our regression line finally,
gets the spotlight it deserves.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Visualizing interpretation of statistic properties,
> using python matplotlib.

Congratulations,
we've survived standard deviations,
`t-values`, and `p-values`.
Welcome to the fun part: making the numbers dance.

In this part, we'll use our trusty Python helper,
to interpret statistical properties through visualizations.
Think of this as the moment where our regression equation,
stops being abstract and starts looking like something our eyes can high-five.

No matter how elegant our model is,
if you can't visualize it,
our audience will nod politely,
and then go back to watching cat videos.

By learning how to draw these statistics,
we also learn to read them better.
A good chart tells a story,
and if you've been following along,
this one is about trends, relationships,
and how suspiciously straight that regression line looks.

Got ideas to improve these visualizations?
Spotted something off? Great!
Stats is a team sport, just with less running and more coffee.
Drop your thoughts, feedback, or rants,
I welcome all contributions that make these interpretations more useful or correct.

-- -- --

### Visualizing Interpretation

This is visualization,
where statistics gets tired of being misunderstood,
and starts drawing diagrams.

We will use matplotlib to turn our statistical properties into visual interpretations.
But not every statistic needs a spotlight on stage,
some are shy little numbers that prefer to stay in a summary table.
Of course not everything can be visualized,
some properties are just a number,
without any need to be visualized at all.
That's fine. We’ll focus on the extroverts.

Interpretation isn't just about numbers.
It's about seeing the story they tell.
A good visualization helps communicate correlation,
trends, and residuals to humans who don't dream in formulas.
You might recognize some of these plots from earlier articles.
Now it's time to go behind the scenes.

If you spot anything fishy in my visuals,
calculations, or interpretations,
be a kind statistician and let me know.
I promise not to take it personally.
(Unless you use Comic Sans.)

#### Skeleton

We'll lean on our trusty `Properties.py` helper again:

* **Properties.py**

And the CSV file with our data samples,
instead of hardcoded data.

* **50-samples.csv**:

```csv
x,y
0,5
1,12
2,25
3,44
4,69
5,100
6,137
7,180
8,229
9,284
10,345
11,412
12,485
```

Here's the basic skeleton for any visualization using our helper:

```python
import matplotlib.pyplot as plt

# Local Library
from Properties import get_properties, display

properties = get_properties("50-samples.csv")
display(properties)
locals().update(properties)

def plot() -> int:
  ...

  return 0

if __name__ == "__main__":
  raise SystemExit(plot())
```

This pattern gives us a reusable starting point.
If the script ends gracefully with exit code 0,
your plot hasn’t caught fire.
That’s a win in data visualization.



We will use this pattern again and again,
like a template for artistic (and statistically valid) expression.

-- -- --

### Basic Data Series

Let's ease into visualization with the basics,
no fancy toppings yet.

* **53-plot.py**

```python
import matplotlib.pyplot as plt

# Local Library
from Properties import get_properties, display

# Load properties from Properties.py helper
# and unpack them into local variables
properties = get_properties("50-samples.csv")
display(properties)
locals().update(properties)

def plot() -> int:
  plt.figure(figsize=(10, 6))

  # Plot the data series
  plt.scatter(x_observed, y_observed,
    color='blue', s=100, label='Data Points')

  # Plot deviation from mean
  plt.axhline(y=y_mean, color='orange',
    linestyle='--',  label='Mean of y')
  plt.vlines(x_observed, y_observed, y_mean,
    linestyle='--', color='teal',
    label='Deviation from Mean (y)')

  # Chart Decoration
  plt.title('Mean and Deviation')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.legend()
  plt.grid(True)

  plt.show()

  return 0

if __name__ == "__main__":
  raise SystemExit(plot())
```

We start with a `scatter` plot,
the default love language of data points:

```python
def plot() -> int:
  plt.figure(figsize=(10, 6))

  # Plot the data series
  plt.scatter(x_observed, y_observed, color='blue',
    s=100, label='Data Points')
```



Now, let’s add a touch of drama:
the horizontal line showing the mean (ȳ),
and the dashed lines showing how far each point deviates from it.
This visualizes (yᵢ − ȳ), one of the unsung heroes of variance,
for each independent oberserved x.

```python
  # Plot deviation from mean
  plt.axhline(y=y_mean, color='orange',
    linestyle='--',  label='Mean of y')
  plt.vlines(x_observed, y_observed, y_mean,
    linestyle='--', color='teal',
    label='Deviation from Mean (y)')
```

Saying "standard deviation" doesn't make people see it.
But this shows it, each vertical line whispering,
"_I'm how far this point strayed from the group."



Now it's time to make it pretty
(or at least readable)
with axes labels, a grid, and a legend.
Even data deserves good UX.

```python
def plot() -> int:
  ...

  # Chart Decoration
  plt.title('Mean and Deviation')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.legend()
  plt.grid(True)

  plt.show()

  return 0
```



Let's plot this data points and mean (average),
along with it's (yᵢ-ȳ) interpretation.
And voilà, we've visualized our first interpretation:
raw data and deviation from the mean.
You now have a graph that says, "_I know my stats and my matplotlib._"



Plotting is pretty simple, right?
Plotting doesn’t have to be scary,
it's just math in makeup.

#### Interactive JupyterLab

Prefer to tweak, explore, and tinker live?
You can interact with the `Jupyter Notebook` version:

* **53-plot.py**

-- -- --

### Standard Deviation

> The Shaky Truth Beneath the Mean

Let's take our visualization game one step further,
into the realm of standard deviation.
No regression line yet, just pure deviation joy.

This tells the story of how data points wobble around the mean,
without anyone trying to predict anything.

* **54-plot.py**

```python
import matplotlib.pyplot as plt

# Local Library
from Properties import get_properties, display

# Load properties from Properties.py helper
# and unpack them into local variables
properties = get_properties("50-samples.csv")
display(properties)
locals().update(properties)

blueScale = {
  0: '#E3F2FD', 1: '#BBDEFB', 2: '#90CAF9',
  3: '#64B5F6', 4: '#42A5F5', 5: '#2196F3',
  6: '#1E88E5', 7: '#1976D2', 8: '#1565C0',
  9: '#0D47A1'
}

def plot() -> int:
  plt.figure(figsize=(10, 6))

  # Plot the data series
  plt.scatter(x_observed, y_observed,
    color=blueScale[9], s=100, zorder=5,
    label='Data Points')

  # Plot deviation from mean
  plt.axhline(y=y_mean, color=blueScale[7],
    linestyle='--',  label='Mean of y')
  plt.vlines(x_observed, y_observed, y_mean,
    linestyle='--', color=blueScale[5],
    label='Deviation from Mean (y)')

  # Plot shaded region for standard deviation
  plt.fill_between(x_observed,
    y_mean - y_std_dev, y_mean + y_std_dev,
    color=blueScale[1], alpha=0.3, zorder=1,
    label='Standard Deviation')

  # Plot covariance
  plt.text(x_mean, max(y_observed),
    f'Covariance: {xy_covariance:.2f}',
    fontsize=12, color=blueScale[9])

  # Chart Decoration
  plt.title('Mean and Deviation')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.legend()
  plt.grid(True)

  plt.show()

  return 0

if __name__ == "__main__":
  raise SystemExit(plot())
```

#### Aesthetic 

I’ve added a custom color palette based on Google’s Material Design.
Not only is it pretty, but it helps keep visual cues consistent.
(And yes, statisticians care about design too. We're not animals.)

```python
blueScale = {
  0: '#E3F2FD', 1: '#BBDEFB', 2: '#90CAF9',
  3: '#64B5F6', 4: '#42A5F5', 5: '#2196F3',
  6: '#1E88E5', 7: '#1976D2', 8: '#1565C0',
  9: '#0D47A1'
}
```



Let's paint the previous plot with this new palette,
a nicer color output:

```python
  # Plot the data series
  plt.scatter(x_observed, y_observed,
    color=blueScale[9], s=100, zorder=5,
    label='Data Points')

  # Plot deviation from mean
  plt.axhline(y=y_mean, color=blueScale[7],
    linestyle='--',  label='Mean of y')
  plt.vlines(x_observed, y_observed, y_mean,
    linestyle='--', color=blueScale[5],
    label='Deviation from Mean (y)')
```



Next, we'll add a shaded region that shows the standard deviation zone.

```python
  # Plot shaded region for standard deviation
  plt.fill_between(x_observed,
    y_mean - y_std_dev, y_mean + y_std_dev,
    color=blueScale[1], alpha=0.3, zorder=1,
    label='Standard Deviation')

  # Plot covariance
  plt.text(x_mean, max(y_observed),
    f'Covariance: {xy_covariance:.2f}',
    fontsize=12, color=blueScale[9])
```



Now we can plot the interpretation of
standard deviation relative to mean.



Not bad, huh? A little color, a little shade,
and suddenly our chart goes from "_meh_" to "_statistically insightful_."

#### Interactive JupyterLab

You can experiment interactively using the `JupyterLab Notebook` here:

* **54-plot.py**

-- -- --

### Mean and Standard Deviation

So you want a simpler way to visualize the mean and standard deviation?
One that looks like a student project but gets the job done?
I got you.

* **55-plot.py**

```python
import matplotlib.pyplot as plt

# Local Library
from Properties import get_properties, display

# Load properties from Properties.py helper
# and unpack them into local variables
properties = get_properties("50-samples.csv")
display(properties)
locals().update(properties)


def plot() -> int:
  plt.figure(figsize=(10, 6))

  # Plot the data and the mean as axis
  plt.scatter(x_observed, y_observed,
    color='blue', label='Data Points')

  plt.axvline(x=x_mean, color='green',
    linestyle='--', label='Mean of x')
  plt.axhline(y=y_mean, color='orange',
    linestyle='--', label='Mean of y')

  # Plot standard deviation as error bars
  plt.errorbar(x_mean, y_mean,
    xerr=x_std_dev, yerr=y_std_dev,
    fmt='o', color='purple',
    label='Standard Deviation')

  # Chart Decoration
  plt.title('Linear Regression')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.legend()
  plt.grid(True)

  plt.show()

  return 0

if __name__ == "__main__":
  raise SystemExit(plot())
```

We start with a scatterplot (again, our favorite),
and then plot the mean on both axes.
Like a big statistical "X marks the spot."

```python
  plt.scatter(x_observed, y_observed,
    color='blue', label='Data Points')

  plt.axvline(x=x_mean, color='green',
    linestyle='--', label='Mean of x')
  plt.axhline(y=y_mean, color='orange',
    linestyle='--', label='Mean of y')
```



And now for the star of the show:
the standard deviation error bars.
These are like tiny, symmetric whiskers on the mean,
useful for showing spread, but not trying too hard.

```python
  plt.errorbar(x_mean, y_mean,
    xerr=x_std_dev, yerr=y_std_dev,
    fmt='o', color='purple',
    label='Standard Deviation')
```



While this chart may not win design awards,
it gives us a clean, orthogonal view of how spread-out our data is from the center.
Both horizontally and vertically.
It's humble, but honest.

And here's what that naïve-yet-informative plot looks like:



It's not winning beauty contests,
but it’s doing its job.
Like a dedicated old spreadsheet with no conditional formatting.

#### Interactive JupyterLab

Feel free to poke around in the notebook here:

* **55-plot.py**

-- -- --

### Linear Regression

> A Line, a Fit, and a Whole Lot of Assumptions

Let's roll out the big guns: linear regression.
The statistical equivalent of drawing a best-guess straight line,
through a cloud of uncertainty.

We're going to plot our linear regression,
based on the least squares method.
It's the classic: minimize the sum of squared regrets, I mean, residuals..

* **56-plot.py**

```
import matplotlib.pyplot as plt

# Local Library
from Properties import get_properties, display

# Load properties from Properties.py helper
# and unpack them into local variables
properties = get_properties("50-samples.csv")
display(properties)
locals().update(properties)

tealScale = {
  0: '#E0F2F1', 1: '#B2DFDB', 2: '#80CBC4',
  3: '#4DB6AC', 4: '#26A69A', 5: '#009688',
  6: '#00897B', 7: '#00796B', 8: '#00695C',
  9: '#004D40'
}

def plot() -> int:
  plt.figure(figsize=(10, 6))

  # Plot the data and regression line
  plt.scatter(x_observed, y_observed,
    color=tealScale[9], label='Data Points')
  plt.plot(x_observed, y_fit,
    color=tealScale[5], label='Regression Line')

  # Chart Decoration
  plt.title('Linear Regression')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.legend()
  plt.grid(True)

  plt.show()

  return 0

if __name__ == "__main__":
  raise SystemExit(plot())
```

The plot is

```python
  # Plot the data and regression line
  plt.scatter(x_observed, y_observed,
    color=tealScale[9], label='Data Points')
  plt.plot(x_observed, y_fit,
    color=tealScale[5], label='Regression Line')
```

We're using Google's teal color scale.
Even math deserves good design choices:

```python
tealScale = {
  0: '#E0F2F1', 1: '#B2DFDB', 2: '#80CBC4',
  3: '#4DB6AC', 4: '#26A69A', 5: '#009688',
  6: '#00897B', 7: '#00796B', 8: '#00695C',
  9: '#004D40'
}
```

Here’s the output:

* Observed y, and
* Predicted ŷ = fit(x) as line.

No interpretation this time. The plot speaks for itself.



Very simple. No Comment.

#### Interactive JupyterLab

Check it out here:

* **56-plot.py**

This is the foundation of predictive analytics.
The line isn't just a line. 
It’s a model, a summary, and a hopeful whisper that patterns exist.

-- -- --

### Residual

> The Distance Between Ambition and Reality

Let's now face the cold, hard truth: residuals.
The vertical gap between what our model predicted,
and what the data actually did.

How about error (ϵ)? Of course we can draw using `vlines`.

* **57-plot.py**

```python
import matplotlib.pyplot as plt

# Local Library
from Properties import get_properties, display

# Load properties from Properties.py helper
# and unpack them into local variables
properties = get_properties("50-samples.csv")
display(properties)
locals().update(properties)

blueScale = {
  0: '#E3F2FD', 1: '#BBDEFB', 2: '#90CAF9',
  3: '#64B5F6', 4: '#42A5F5', 5: '#2196F3',
  6: '#1E88E5', 7: '#1976D2', 8: '#1565C0',
  9: '#0D47A1'
}

def plot() -> int:
  plt.figure(figsize=(10, 6))

  # Plot the data and regression line
  plt.scatter(x_observed, y_observed,
    color=blueScale[9], label='Data Points')
  plt.plot(x_observed, y_fit,
    color=blueScale[5], label='Regression Line')

  # Plot residual errors
  plt.vlines(x_observed, y_observed, y_fit,
  linestyle='--', color=blueScale[3],
  label='Residual')

  # Chart Decoration
  plt.title('Linear Regression')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.legend()
  plt.grid(True)

  plt.show()

  return 0

if __name__ == "__main__":
  raise SystemExit(plot())
```

The plot

```python
  # Plot the data and regression line
  plt.scatter(x_observed, y_observed,
    color=blueScale[9], label='Data Points')
  plt.plot(x_observed, y_fit,
    color=blueScale[5], label='Regression Line')

  # Plot residual errors
  plt.vlines(x_observed, y_observed, y_fit,
  linestyle='--', color=blueScale[3],
  label='Residual')
```

Each dashed line = one regret.
Or in more technical terms: ϵᵢ = yᵢ − ŷᵢ.



The interpretation of residual or error  (ϵ),
is simple as shown in below plot:



Simple, but enough to to interpret the (yᵢ-ŷ) difference.

#### Interactive JupyterLab

Get interactive with our residuals:

* **57-plot.py**

Residuals reveal the quality of our model.
They tell you if our line is just pretty,
or actually useful.

-- -- --

### Standard Deviation

How about interpretation of
standard deviation relative to predicted values,
of regression line?

* **58-plot.py**

```python
import matplotlib.pyplot as plt

# Local Library
from Properties import get_properties, display

# Load properties from Properties.py helper
# and unpack them into local variables
properties = get_properties("50-samples.csv")
display(properties)
locals().update(properties)

tealScale = {
  0: '#E0F2F1', 1: '#B2DFDB', 2: '#80CBC4',
  3: '#4DB6AC', 4: '#26A69A', 5: '#009688',
  6: '#00897B', 7: '#00796B', 8: '#00695C',
  9: '#004D40'
}

def plot() -> int:
  plt.figure(figsize=(10, 6))

  # Plot the data and regression line
  plt.scatter(x_observed, y_observed,
    color=tealScale[9], label='Data Points')
  plt.plot(x_observed, y_fit,
    color=tealScale[5], label='Regression Line')

  plt.plot(x_observed, y_fit + y_std_dev,
    c=tealScale[1], linestyle='--')
  plt.plot(x_observed, y_fit - y_std_dev,
    c=tealScale[1], linestyle='--',
    label='Regression ± Standard Deviation')

  # Fill between upper and lower bounds
  plt.fill_between(x_observed,
  y_fit - y_std_dev, y_fit + y_std_dev,
  color=tealScale[1], alpha=0.3,
  label='Standard Deviation')

  # Chart Decoration
  plt.title('Standard Deviation')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.legend()
  plt.grid(True)

  plt.show()

  return 0

if __name__ == "__main__":
  raise SystemExit(plot())
```

First, we need to draw our data series,
and the regression line.

```python
  # Plot the data and regression line
  plt.scatter(x_observed, y_observed,
    color=tealScale[9], label='Data Points')
  plt.plot(x_observed, y_fit,
    color=tealScale[5], label='Regression Line')
```

Then plot standard deviation,
on both above and below the curve fitting trend.

```python
  plt.plot(x_observed, y_fit + y_std_dev,
    c=tealScale[1], linestyle='--')
  plt.plot(x_observed, y_fit - y_std_dev,
    c=tealScale[1], linestyle='--',
    label='Regression ± Standard Deviation')
```



Then we fill a shaded region,
between upper and lower bounds:

```python
  plt.fill_between(x_observed,
  y_fit - y_std_dev, y_fit + y_std_dev,
  color=tealScale[1], alpha=0.3,
  label='Standard Deviation')
```



With settings above, we can plot the interpretation of
standard deviation relative to curve fitting trend.

This shaded area tells us how much variation exists around our trend.
More wiggle = more chaos. Less wiggle = more confidence.
No wiggle? We're either dealing with perfect data,
or we've broken causality.



This should be pretty cool.

#### Interactive JupyterLab

Dig in interactively:

* **58-plot.py**

Standard deviation helps us understand the spread of your predictions.
It answers: "_How typical is a typical point?_",
or in plain English, "_Is this line even believable?_"

-- -- --

### Standard Error with Level of Confidence

> Turning Probabilities into Boundaries

Standard deviation was fun,
but now it's time to bring in confidence.
(Statistically speaking — not emotionally.)

Instead of measuring spread like standard deviation, 
we now estimate the standard error and use it to draw a confidence interval.

* **59-plot.py**

```python
import numpy as np
import matplotlib.pyplot as plt

# Local Library
from Properties import get_properties, display

# Load properties from Properties.py helper
# and unpack them into local variables
properties = get_properties("50-samples.csv")
display(properties)
locals().update(properties)

tealScale = {
  0: '#E0F2F1', 1: '#B2DFDB', 2: '#80CBC4',
  3: '#4DB6AC', 4: '#26A69A', 5: '#009688',
  6: '#00897B', 7: '#00796B', 8: '#00695C',
  9: '#004D40'
}

def get_CI() -> float:
  # Create regression line
  y_fit = m_slope * x_observed + b_intercept
  y_err = y_observed - y_fit

  # Calculate variance of residuals (MSE)
  var_residuals = np.sum(y_err ** 2) / (n - 2)

  SE = np.sqrt(var_residuals)

  # Calculate the confidence interval
  # for the predictions using 95% confidence
  return 1.96 * SE

def plot() -> int:
  plt.figure(figsize=(10, 6))

  # Plot the data and regression line
  plt.scatter(x_observed, y_observed,
    color=tealScale[9], label='Data Points')
  plt.plot(x_observed, y_fit,
    color=tealScale[5], label='Regression Line')

  plt.plot(x_observed, y_fit + y_std_dev,
    c=tealScale[1], linestyle='--')
  plt.plot(x_observed, y_fit - y_std_dev,
    c=tealScale[1], linestyle='--',
    label='Regression ± Standard Deviation')

  # Fill between upper and lower bounds
  CI = get_CI()
  plt.fill_between(x_observed,
  y_fit - CI, y_fit + CI,
  color=tealScale[1], alpha=0.3,
  label='Standard Error')

  # Chart Decoration
  plt.title('Standard Deviation and Standard Error')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.legend()
  plt.grid(True)

  plt.show()

  return 0

if __name__ == "__main__":
  raise SystemExit(plot())
```


This confidence of interval can be predicted using OLS.
For example, let's use 95% confidence level, with the result of approximately 1.96.

```python
def get_CI() -> float:
  # Create regression line
  y_fit = m_slope * x_observed + b_intercept
  y_err = y_observed - y_fit

  # Calculate variance of residuals (MSE)
  var_residuals = np.sum(y_err ** 2) / (n - 2)

  SE = np.sqrt(var_residuals)

  # Calculate the confidence interval
  # for the predictions using 95% confidence
  return 1.96 * SE
```



Now shade in your statistical surety zone.
Use this calculation to fill the standard region.

```python
  # Fill between upper and lower bounds
  CI = get_CI()
  plt.fill_between(x_observed,
  y_fit - CI, y_fit + CI,
  color=tealScale[1], alpha=0.3,
  label='Standard Error')
```



And voilà, a band of confidence wrapped around our prediction line.
It's like saying, "_I may be wrong, but here's how wrong I might be, with math._”



Ultimately, the choice of our plot depends on
the specific interpretation and 
communication goals of our analysis. 
You should contact your nearest statistician
to get most valid visual interpretation.

#### Interactive JupyterLab

Tinker with confidence:

* **59-plot.py**

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Getting Matrix Values
pairCSV = np.genfromtxt("50-samples.csv",
  skip_header=1, delimiter=",", dtype=float)

# Extract x and y values from CSV data
x_observed = pairCSV[:, 0]
y_observed = pairCSV[:, 1]

# Scatter plot with regression line
plt.figure(figsize=(8, 6))
sns.regplot(x=x_observed, y=y_observed)
plt.title('Scatter Plot with Regression Line')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
```

Confidence intervals quantify uncertainty.
While standard deviation describes the scatter of our data,
standard error tells us how confident we are in our model's predictions.

Think of it this way:
* Standard deviation is what our data does.
* Standard error is what our model thinks it's doing.

_When in doubt, shade it out._

-- -- --

### Other Tools: Seaborn

> When You Want Stats and Style in One Line

Sure, matplotlib is powerful,
like using a wrench to tighten bolts by hand.
But what if you want your plots,
to look sleek, smart, and socially acceptable,
without a hundred lines of config?

Enter `seaborn`: Matplotlib’s artsy cousin,
who took a data science minor and discovered color theory.

Just add `sns` to our imports,
and we're ready to plot like a pro with commitment issues.

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Getting Matrix Values
pairCSV = np.genfromtxt("50-samples.csv",
  skip_header=1, delimiter=",", dtype=float)

# Extract x and y values from CSV data
x_observed = pairCSV[:, 0]
y_observed = pairCSV[:, 1]
```

Ready for magic?
Here's the one-liner of the century:

```python
# Scatter plot with regression line
plt.figure(figsize=(8, 6))
sns.regplot(x=x_observed, y=y_observed)
plt.title('Scatter Plot with Regression Line')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
```



_Boom._

You get a fully styled regression plot,
with confidence bands and proper labels,
all before your coffee even cools.



Now, let's be honest:
At the time of writing,
I have no idea how Seaborn calculates its regression curve.
Probably via `statsmodels` under the hood.
Possibly powered by `pandas`, caffeine, and statistical sorcery.
I refuse to dig further.

All I know is this plot is cool.
And have pretty color pallete too.

* It works,
* It looks good, and
* It doesn't complain.

#### Interactive JupyterLab

Play with this stylish shortcut here:

* **59-sns.py**

Tools like Seaborn remove friction from visualization.
When we just want to show a trend,
and move on with our analysis (or life),
this kind of one-liner plotting is pure gold.

Don’t worry, we're still statisticians.
It’s only cheating if you don’t know how Seaborn did the math,
and still publish it in a journal.

#### At Last

This wraps up our visualization journey,
for regression and trend analysis.
Of course, the statistical landscape is wide,
there are plenty of parameters and visualizations,
I may not have covered
(or even known about at the time of writing).

If you have other preferred tools,
interpretations, or aesthetic preferences
(e.g. "can we use hot pink?"), 
Or just a strong opinion on shaded confidence intervals,
feel free to share. I’d love to hear it.

Feedback is welcome.
Especially if it comes with coffee.

-- -- --

### What's the Next Exciting Step 🤔?

We've charted the straight and narrow path of linear regression.
Clean, elegant, and satisfying,
like a line of best fit through a row of perfectly behaved ducks.

But life (and data) isn't always that obedient.
Sometimes, the trend curves.
That's where polynomial regression steps in.
It lets us bend our model—gracefully—to,
better capture complex relationships.

As usual, we will start from first principles,
move into spreadsheet formulas
(yes, Excel/Calc still deserves a seat at the statistics table),
then dive into Python implementations and juicy visualizations.

Ready to curve things up? Head over to
**Trend - Polynomial Regression - Theory**.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Goes further from linear regression to polynomial regression.
> The theoretical foundations, explains why the math works.

If linear regression is the "statistically safe" choice,
like vanilla ice cream or using `mean()`,
then polynomial regression is where things start getting fun.
And slightly more dangerous. 

_The math gets spicy._

Polynomial regression isn't just linear regression with more terms.
Under the hood, it pulls in linear algebra concepts,
like the Gram matrix, matrix transposes, and inverses.
If these words sound intimidating, don’t worry.
We will decode them one at a time.

⚠️ **Warning**: This article contains traces of matrix math.
Those with linear algebra allergies should proceed with caution,
or at least have a coffee in hand.

#### Cheatsheet

> The Equation Flow

To help us navigate the swirling formulas,
here's a visual cheatsheet that ties everything together:

* The core regression model
* Error and residual breakdown
* Hypothesis testing logic
* And that sweet, sweet R² (plus the grown-up version: adjusted R²)

In one diagram, we will see how polynomial regression,
gently parts ways from its linear sibling.



We can also grab the SVG version here
(for printing, remixing, custom, black long sleeve t-shirt, or tattoo ideas):

📎 **github.com/.../math/trend/equflow/equflow-04.svg**

⚠️ A note for the statistically curious:
This article only deals with samples, not populations.
The math differs slightly, and yes, we'll get to that later,
still in this article.

#### Beyond This Basic

> A must-have knowledge

With a solid grasp of **polynomial regression**,
stepping into multivariate regression becomes much easier.
Like swapping our socket wrench for a full torque-calibrated toolkit
From here, we can smoothly move on to ANOVA, ANAREG, MANOVA, and beyond.

The underlying math principles stay familiar,.
The workflows in spreadsheets is similar,
We can build our own tabular data, just more columns to tune.
Python stays approachable, still the same workbench.
And PSPP? Built for everyday end-users like us,
great for routine jobs.

In modern data science (DS), big data (BD), machine learning (ML), and AI,
the real horsepower often comes from **Bayesian Regression**.
Think of it as a royal marriage between two statistical dynasties:
**Regression** and **Probability**.

To become a true AI engineer, we need to understand how both families work.
Otherwise, we risk ending up as just a PyTorch/Keras/TensorFlow technician.
Able to operate the tools, but not design the engine.

We will continue that journey,
after we finish the Probability article series.

#### Basic Instinct

Years as engineering student,
two decades, ago taught me the instinct to:

* Understand systems,
* Break down complexity,
* Explain it like it's no big deal (in this blog or telegram),
* And when the system fails, not panic, but fix the blueprint.

So let's start with blueprint.

-- -- --

### 1: Theoretical Backbone

> Fitting Curves Without Losing Our Minds

Instead of focusing on Covariance, the equation is started with gram matrix.

This is the Equation for Polynomial Regression,
but not the least square method.
This is where we take raw data,
and try to make it sing with the help of polynomials.
Like karaoke, but with more math and less embarrassment.

#### Big Picture

Most of the equation in the left side part has been covered in polynomial calculation article.

* **Trend - Polynomial Algebra**

If you've already peeked at above algebra article,
you have met most of these formulas before. No need for déjà vu.
I don't think that I need to refresh the equation over and over again.
But let's describe the equation notation in other forms.

#### Observed Data

We start with a humble set of observed data pairs:

$$
\begin{align*}
&& {x_i}_\text{ (observed)} &= [\ldots] \quad , \\
&& {y_i}_\text{ (observed)} &= [\ldots] \\
\end{align*}
$$


Our mission (and we’ve chosen to accept it):
find predicted values (by curve fittings).

$$
\begin{align*}
&& {\hat{y}_i}_\text{ (prediction)} &= [\ldots] \\
\end{align*}
$$

In essence, we want a curve that says:
"_I see your scatter, and I raise you a smooth function._"

Let's find the solution for this using polynomial coefficients.

#### Fit Model

> Polynomial Prediction Model

We have the generic theoritical model with this explicit form below.
As cozy as a power series in a warm blanket.

$$
y = \beta_0 + \beta_1 x + \beta_2 x^2 + \cdots + \beta_k x^k
$$

But let's keep things simple.
Most of the time, we don’t go beyond cubic because:

* Linear (1st order): \
  "_Let’s just draw a line and see what happens._"

* Quadratic (2nd order): \
  "_Curvy, but still sober._"

* Cubic (3rd order): \
  "_Elegant, dramatic, but still behaves at dinner._"

$$
\begin{array}{|l|l|l|}
  \hline
    \scriptstyle \text{1st order} &
    \scriptstyle \text{linear} &
    \hat{y}_i = \beta_0 + \beta_1{x_i} \rule{0pt}{2ex} \\
  \hline
    \scriptstyle \text{2nd order} &
    \scriptstyle \text{quadratic} &
    \hat{y}_i = \beta_0 + \beta_1{x_i} + \beta_2{x_i}^2 \rule{0pt}{2ex} \\
  \hline
    \scriptstyle \text{3rd order} &
    \scriptstyle \text{cubic} &
    \hat{y}_i = \beta_0 + \beta_1{x_i} + \beta_2{x_i}^2 + \beta_3{x_i}^3 \rule{0pt}{2ex} \\
  \hline
\end{array}
$$

Where order is the degree of the polynomial.
And β (beta) denotes the coefficients for specific polynomial degrees.

Higher-degree polynomials can capture more nuances (wiggles!),
but beware the Curse of Overfitting™.
Higher-order terms help model curvature, but also risk overfitting.
This can be problematic in real world situations.
Just because a model can hit every point doesn’t mean it should.

#### Matrix Form

> Where Algebra Puts On Its Lab Coat

Enter the Vandermonde matrix,
our handy companion for building polynomial models.
In general this Vandermonde is looks like this.

$$
    \begin{bmatrix}
        1 & x_1 & x_1^2 & \cdots & x_1^k \\
        1 & x_2 & x_2^2 & \cdots & x_2^k \\
        \vdots & \vdots & \vdots & \ddots & \vdots \\
        1 & x_n & x_n^2 & \cdots & x_n^k \\
    \end{bmatrix}
    \begin{bmatrix}
        \beta_0 \\
        \beta_1 \\
        \beta_2 \\
        \vdots \\
        \beta_k \\
    \end{bmatrix} 
    =
    \begin{bmatrix}
        y_1 \\
        y_2 \\
        \vdots \\
        y_n \\
    \end{bmatrix} \\
$$

Where 

* n: Number of observations (rows in X)

The Vandermonde matrix builds our X-values into powers,
setting the stage for regression magic.
The higher the column, the more wiggles our curve gets.

For the all three curve fittings,
the actual matrix can be described as following:

$$
\begin{array}{|l|l|l|}
  \hline
    \scriptstyle \text{linear} &

    \mathbf{X}
    =
    \begin{bmatrix}
        1 & x_1 \\
        1 & x_2 \\
        \vdots & \vdots \\
        1 & x_n \\
    \end{bmatrix} &

    \mathbf{y}
    =
    \begin{bmatrix}
        y_1 \\
        y_2 \\
        \vdots \\
        y_n \\
    \end{bmatrix} \\

  \hline
    \scriptstyle \text{quadratic} &

    \mathbf{X}
    =
    \begin{bmatrix}
        1 & x_1 & x_1^2 \\
        1 & x_2 & x_2^2 \\
        \vdots & \vdots & \vdots \\
        1 & x_n & x_n^2 \\
    \end{bmatrix} &

    \mathbf{y}
    =
    \begin{bmatrix}
        y_1 \\
        y_2 \\
        \vdots \\
        y_n \\
    \end{bmatrix} \\

  \hline
    \scriptstyle \text{cubic} &

    \mathbf{X}
    =
    \begin{bmatrix}
        1 & x_1 & x_1^2 & x_1^3 \\
        1 & x_2 & x_2^2 & x_2^3 \\
        \vdots & \vdots & \vdots & \vdots \\
        1 & x_n & x_n^2 & x_n^3 \\
    \end{bmatrix} &

    \mathbf{y}
    =
    \begin{bmatrix}
        y_1 \\
        y_2 \\
        \vdots \\
        y_n \\
    \end{bmatrix} \\

  \hline
\end{array}
$$

#### Solution

> The Gram Matrix Moves In

It's time for the main event: solving for the betas.
The regression solution dances in with the Gram Matrix.

This is the solution,
where `X` is the predictor variables,
and `y` is dependent variables.

$$
\begin{aligned}
              &&    X \mathbf{\beta} &= \mathbf{y} \\
  \Rightarrow &&    X^\top X \mathbf{\beta} &= X^\top \mathbf{y} \\
  \Rightarrow &&    \mathbf{\beta} &= (X^\top X)^{-1} X^\top \mathbf{y}
\end{aligned}
$$

This equation finds the best-fit coefficients,
by minimizing the squared errors.
Think of it as the least regret path,
a statistically polite guess.

For each curve fittings,
the coefficients solutions can be described as following:

$$
\begin{array}{|l|l|}
  \hline
    \scriptstyle \text{linear} &

    \left(\mathbf{X}^T \mathbf{X}\right)
    \begin{bmatrix}
        \beta_0 \\ \beta_1 \\
    \end{bmatrix} 
    = \mathbf{X}^T \mathbf{y} \\

  \hline
    \scriptstyle \text{quadratic} &

    \left(\mathbf{X}^T \mathbf{X}\right)
    \begin{bmatrix}
        \beta_0 \\ \beta_1 \\ \beta_2 \\
    \end{bmatrix} 
    = \mathbf{X}^T \mathbf{y}  \\

  \hline
    \scriptstyle \text{cubic} &

    \left(\mathbf{X}^T \mathbf{X}\right)
    \begin{bmatrix}
        \beta_0 \\ \beta_1 \\ \beta_2 \\ \beta_3 \\
    \end{bmatrix} 
    = \mathbf{X}^T \mathbf{y} \\

  \hline
\end{array}
$$

#### Explicit Gram Matrix

> Polynomial Symmetry Society

Now we also the generalized form the gram matrix (Xᵗ.X).

$$
X^\top X = 
\begin{bmatrix}
n                        & \sum x_m       & \sum x_m^2     & \cdots & \sum x_m^k \\
\sum x_m                 & \sum x_m^2     & \sum x_m^3     & \cdots & \sum x_m^{k+1} \\
\sum x_m^2               & \sum x_m^3     & \sum x_m^4     & \cdots & \sum x_m^{k+2} \\
\vdots                   & \vdots         & \vdots         & \ddots & \vdots \\
\sum x_m^k               & \sum x_m^{k+1} & \sum x_m^{k+2} & \cdots & \sum x_m^{2k}
\end{bmatrix}
$$

Where 

* m: Index used in sums for (Xᵗ.X) entries

The Gram matrix is always symmetric, always serious.

We are going use computation.
But for clarity, we can show
the actual gram matrix for each curve fittings
can be described as following:

$$
\begin{array}{|l|l|}
  \hline
    \scriptstyle \text{linear} &

    \begin{bmatrix}
        n & \sum x_i \\
        \sum x_i & \sum x_i^2 \\
    \end{bmatrix}
    \begin{bmatrix}
        a \\ b \\
    \end{bmatrix}
    =
    \begin{bmatrix}
        \sum y_i \\
        \sum x_i y_i \\
    \end{bmatrix} \\

  \hline
    \scriptstyle \text{quadratic} &

    \begin{bmatrix}
        n & \sum x_i & \sum x_i^2 \\
        \sum x_i & \sum x_i^2 & \sum x_i^3 \\
        \sum x_i^2 & \sum x_i^3 & \sum x_i^4 \\
    \end{bmatrix}
    \begin{bmatrix}
        a \\ b \\ c \\
    \end{bmatrix}
    =
    \begin{bmatrix}
        \sum y_i \\
        \sum x_i y_i \\
        \sum x_i^2 y_i \\
    \end{bmatrix} \\

  \hline
    \scriptstyle \text{cubic} &

    \begin{bmatrix}
        n & \sum x_i & \sum x_i^2 & \sum x_i^3 \\
        \sum x_i & \sum x_i^2 & \sum x_i^3 & \sum x_i^4 \\
        \sum x_i^2 & \sum x_i^3 & \sum x_i^4 & \sum x_i^5 \\
        \sum x_i^3 & \sum x_i^4 & \sum x_i^5 & \sum x_i^6 \\
    \end{bmatrix}
    \begin{bmatrix}
        a \\ b \\ c \\ d \\
    \end{bmatrix}
    =
    \begin{bmatrix}
        \sum y_i \\
        \sum x_i y_i \\
        \sum x_i^2 y_i \\
        \sum x_i^3 y_i \\
    \end{bmatrix} \\

  \hline
\end{array}
$$

This matrix captures the relationship between predictor powers.
Its symmetry is a mathematical peace treaty.

#### Inverse Gram Matrix

> Matrix Gymnastics (Use Excel, Not Chalk)

To calculate each Coefficients,
we need the inverse Gram Matrix (Xᵗ.X)ˉ¹ from the x observed values.
There is no simple closed-form expression for inverse gram matrix (Xᵗ.X)ˉ¹.
No need to brute-force the inverse by hand,
just let Excel (or `numpy`) do the matrix gymnastics.

#### Fit Prediction

> Prediction Time: Coefficients Meet X

Now that we have our shiny new **estimated coefficients β**
(calculated from data),
we plug them into our model and let the predictions flow.

$$
  \hat{\beta} = (X^\top X)^{-1} X^\top \mathbf{y}
$$

Each `xᵢ`​ becomes the input to our polynomial machine.

#### Predicted Values

> How Each Fit Performs, By Model Type

Using the estimated coefficients β,
we substitute into the explicit polynomial forms.
For each observed value xᵢ,
we compute predictions yᵢ for each model:

$$
\begin{array}{|l|l|}
  \hline
    \scriptstyle \textbf{Model Type} &
    \textbf{Prediction Equation} \\ 

  \hline
    \scriptstyle \text{Observed predictors} &
    \mathbf{x} = [x_1, x_2, \ldots, x_n]^\top \\ 

  \hline
    \scriptstyle \text{Linear fit} &
    \hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i \\ 

  \hline
    \scriptstyle \text{Quadratic fit} &
    \hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i
              + \hat{\beta}_2 x_i^2 \\ 

  \hline
    \scriptstyle \text{Cubic fit} &
    \hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i
              + \hat{\beta}_2 x_i^2 + \hat{\beta}_3 x_i^3 \\ 

\hline
\end{array}
$$

Testing predictions against the observed values shows us,
if the model is hugging the data... or ghosting it

#### Direct Comparison

> Predicted vs Observed Values

The actual calculations use the same observed xᵢ values,
enabling direct comparison with observed yᵢ.
Compare these values side-by-side,
and see how well our model hugs the data points:

$$
\begin{array}{|l|l|}
  \hline
    \scriptstyle \text{samples} &
    {x_i}_\text{ (observed)} = [\ldots] \\

  \hline
    \scriptstyle \text{samples} &
    {y_i}_\text{ (observed)} = [\ldots] \\

  \hline
    \scriptstyle \text{linear} &
    {\hat{y}_i}_\text{ (prediction)} = [\ldots] \\

  \hline
    \scriptstyle \text{quadratic} &
    {\hat{y}_i}_\text{ (prediction)} = [\ldots]  \\

  \hline
    \scriptstyle \text{cubic} &
    {\hat{y}_i}_\text{ (prediction)} = [\ldots] \\

  \hline
\end{array}
$$

The model comparison reveals how polynomial complexity affects fit quality.

$$
\begin{array}{|l|l|l|}
  \hline
    \text{Sample} &
    x_i \text{ (observed)} &
    y_i \text{ (observed)} \\ 

  \hline
    1 & x_1 & y_1 \\ 
    2 & x_2 & y_2 \\ 
    \vdots & \vdots & \vdots \\ 
    n & x_n & y_n \\ 

  \hline
\end{array}
$$

$$
\begin{array}{|l|l|l|l|}
  \hline
    \text{Prediction} &
    \text{Linear} &
    \text{Quadratic} &
    \text{Cubic} \\ 

  \hline
    \hat{y}_1 & \hat{\beta}_0 + \hat{\beta}_1 x_1 & \hat{\beta}_0 + 
    \hat{\beta}_1 x_1 + \hat{\beta}_2 x_1^2 & \hat{\beta}_0 + \cdots + \hat{\beta}_3 x_1^3 \\ 

    \hat{y}_2 & \hat{\beta}_0 + \hat{\beta}_1 x_2 & \hat{\beta}_0 + 
    \hat{\beta}_1 x_2 + \hat{\beta}_2 x_2^2 & \hat{\beta}_0 + \cdots + \hat{\beta}_3 x_2^3 \\ 

    \vdots & \vdots & \vdots & \vdots \\ 

    \hat{y}_n & \hat{\beta}_0 + \hat{\beta}_1 x_n & \hat{\beta}_0 + 
    \hat{\beta}_1 x_n + \hat{\beta}_2 x_n^2 & \hat{\beta}_0 + \cdots + \hat{\beta}_3 x_n^3 \\ 

  \hline
\end{array}
$$

Seeing how predictions match the actual data helps us choose the right model.
It's like a job interview for polynomials.

_Only the best fit gets hired._

The interesting parts comes in the next section below.

-- -- --

### 2: Equation for Regression

> When linear thinking just doesn't cut it.

Polynomial regression doesn't just bend the line.
It bends our brain a little too.
The equations look familiar… until they don’t.

Cheat mode reminder: Many formulas here were foreshadowed in

* **Trend - Properties - Cheatsheet**

This section walks through the theory with a gentle curve (pun intended),
showing what's really happening under the Excel hood or Python matrix.

#### No Variance?

> Where’s the Usual Gang?

_Where’s Standard Deviation? Where's Waldo? Where’s my sanity?_

In linear regression,
we hang out with slope, intercept, Pearson’s r,
and the rest of the cool kids.
But in polynomial regression? Some of those buddies don’t get invited.

* Standard deviation? Only for total variance, not slope.
* Covariance? Still around, but much sneakier.
* Intercept and slope? Replaced with a full orchestra of betas.

So where is the famous Standard Deviation? Pearson, and covariance?
Actually these properties are only relevant for linear regression.

Still, we calculate total variance (SST) the same way,
with mean inside the equation.

$$
\sum (y_i - \bar{y})^2
$$

This total variance is our baseline.
The "_total noise_" we're trying to explain with our curve.
Even if the curve squiggles, the goal remains: reduce this total chaos.

We still have covariance,
but not in the simple form as used in previous linear regression.

#### Degrees of Freedom

> More predictors = more complexity = fewer degrees of freedom.

It's like giving a child too many crayons.
Things get wilder, but less meaningful.

In polynomial regression,
the degrees of freedom (df) for the error term (residuals) is calculated as:

$$
\begin{align*}
& df = n - p - 1 \\
& \scriptstyle \text{(degree of freedom)}
\end{align*}
$$

Where the equation itself can be interpreted as:

* n = Total number of observations (data points).
* p = Number of predictors (independent variables) in the model.
* -1 = Accounts for the intercept term (β₀​).

The use of the _**predictors**_ is pretty clear for each case.
Now we can rewrite for each model as:

$$
\begin{array}{|l|l|l|}
  \hline
    \scriptstyle \text{linear} &
    p = 1: \text{only } x &
    df = n - 2 \\
  \hline
    \scriptstyle \text{quadratic} &
    p = 2: x \text{ and } x^2 &
    df = n - 3 \\
  \hline
    \scriptstyle \text{cubic} &
    p = 3: x, x^2, x^3 &
    df = n - 4 \\
  \hline
\end{array}
$$

`df` controls how "_penalized_" our model is for being fancy.
Without it, we'd just keep adding powers of x until the model folds in on itself.

#### Residual

> Where the Errors Hide

The SSE (Sum of Squared Errors) is still the champion of model diagnostics.
SSE is calculated the same way for all models,
but the residuals differ based on the model's complexity:

$$
\begin{align*}
SSE &= \sum\limits_{i=1}^{n} (\epsilon_i)^2 \\
    &= \sum (y_i - \hat{y}_i)^2 \\
\end{align*}
$$

Where the predicted values of ŷᵢ vary by model.
Each ŷᵢ​ is shaped by our model’s ego:

$$
\begin{array}{|l|l|}
  \hline
    \scriptstyle \text{linear} &
    \sum (y_i - \left(\beta_0 + \beta_1{x_i})\right)^2 \\
  \hline
    \scriptstyle \text{quadratic} &
    \sum (y_i - \left(\beta_0 + \beta_1{x_i} + \beta_2{x_i}^2)\right)^2 \\
  \hline
    \scriptstyle \text{cubic} &
    \sum (y_i - \left(\beta_0 + \beta_1{x_i} + \beta_2{x_i}^2 + \beta_3{x_i}^3)\right)^2 \\
  \hline
\end{array}
$$

Don't worry, we are not going to derive these equation.
We'll compute these directly in Excel using tabular calculations.

Residuals are the leftover errors our model couldn't explain.
Polynomial regression lets our line dance more freely to reduce them.
But it also risks overfitting the floor.

#### Coefficient of Determination

> The R Square (R²), the ego meter of our model.

In general, the R Square (R²) is still defined as follows.

$$
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

Using tabular in Excel (or python),
we can just put the residual calculation above into above equation.
Still works the same. Just plug in new predictions.

And here comes the wise sibling.
We can calculate the adjusted R Square with following equation:

$$
R^2 _\text{(adjusted)} = 1 - \frac{{(1 - R^2)(n - 1)}}{{n - p - 1}}
$$

Adjusted R² keeps us honest.
It says: “_Sure, our curve fits well, but did it really earn it?_”

#### MSE

> The average shame of our models predictions.

MSE stand for Mean Standard Errors.
The mean word refers to the average of squared errors,
adjusted for degrees of freedom.

$$
MSE = \frac{SSE}{df} = \frac{\sum (y_i - \hat{y}_i)^2 }{n - p - 1}
$$

Then take the square root for Root Mean Squared Error (RMSE),
as a helper for further calculation.

$$
RMSE = \sqrt{MSE}
$$

MSE is the backbone of every test and confidence interval that follows
 Think of it as our model's humility score.

#### Gram Matrix

To calculate Standard Error of each Coefficients,
we need Gram Matrix (Xᵗ.X) from the x observed values.

From the matrix form:

$$
X
=
\begin{bmatrix}
        1 & x_1 & x_1^2 & \cdots & x_1^k \\
        1 & x_2 & x_2^2 & \cdots & x_2^k \\
        \vdots & \vdots & \vdots & \ddots & \vdots \\
        1 & x_n & x_n^2 & \cdots & x_n^k \\
\end{bmatrix}
$$

This matrix is like our model's blueprint.
Without it, you can’t build standard errors, variances, or credibility.

#### Covariance Matrix of β

> β = coefficient estimates

The theoretical covariance matrix is:

$$
\text{Cov}(\hat{\mathbf{\beta}}) = \sigma^2 (X^\top X)^{-1}
$$

where:

* σ² is the true error variance (unknown in practice)
* (Xᵗ.X)ˉ¹ is the inverse Gram matrix

In practice, we estimate σ² using the Mean Squared Error (MSE):

$$
\text{Cov}(\hat{\mathbf{\beta}}) \approx \text{MSE} \cdot (X^\top X)^{-1}
$$

To find inverse gram matrix (Xᵗ.X)ˉ¹,
we have to rely on computation instead of
finding generalization equation.

#### Variance of β

> β = coefficient estimates

The **true variance** of the coefficient estimates is

$$
\text{Var}(\hat{\beta}_j) = \sigma^2 \cdot \left(X^\top X\right)^{-1}_{jj}
$$

Where

* σ² is the unknown error variance 

In practice, we estimate σ² using the **Mean Squared Error (MSE)**:

$$
\text{Var}(\hat{\beta}_j) \approx \text{MSE} \cdot \left(X^\top X\right)^{-1}_{jj}
$$

Want to know how “_wobbly_" each coefficient is?
This tells us. 

_High variance = less trust_.

#### Diagonal Matrix

The diagonal of the inverse Gram matrix,
the diags|(Xᵗ.X)ˉ¹|,
represents the scaled variance of β
(variance per unit of σ²):

$$
\left(X^\top X\right)^{-1}_{jj} \approx \text{Var}_{scaled}(\hat{\beta}_j)\cdot 
$$

Or in other notation can be written as

$$
\text{diag}|(X^\top X)^{-1}|_j
$$

The same applied for diags|(Xᵗ.X)ˉ¹|ⱼ.
There is no generalization either,
so we have to rely on computation instead.

_No closed formula. Just crunch it._

#### Standard Error of Coefficient

> Like standard deviation, but for the guesswork inyour βs.

Standard deviation is the square root of the variance right?
Then the standard error (SE) is indeed,
the square root of the variance of the coefficient estimates.

For any coefficient βⱼ​ in polynomial regression:

$$
\begin{align*}
SE(\hat{\beta}_j) &= \sqrt{\text{Var}(\hat{\beta}_j) } \\
                  &= \sqrt{MSE \cdot (X^\top X)^{-1}_{jj}}
\end{align*}
$$

We can break down for each case.
The standard Errors by Polynomial Degree are:

$$
\begin{array}{|l|l|}
  \hline
    \scriptstyle \text{linear} &
    SE(\hat{\beta}_0) , SE(\hat{\beta}_1) \\
  \hline
    \scriptstyle \text{quadratic} &
    SE(\hat{\beta}_0) , SE(\hat{\beta}_1) , SE(\hat{\beta}_2) \\
  \hline
    \scriptstyle \text{cubic} &
    SE(\hat{\beta}_0) , SE(\hat{\beta}_1) , SE(\hat{\beta}_2) , SE(\hat{\beta}_3) \\
  \hline
\end{array}
$$

These errors define our confidence intervals, t-tests,
and how much trust we place in each term.

A high SE(βⱼ)? Suspicious term (predictor like x² or x³) 
may not actually be contributing useful information to the model.
It's possibly just capturing random variation in the data (i.e., noise).
In polynomial regression, as we add higher-degree terms,
some of them might look like they fit better.
But if their standard errors are large
 it's a red flag.

#### t-value

> In Polynomial Regression

Want to know if a coefficient is doing real work,
or just lounging around?

The t-value for each coefficient β​ tests the null hypothesis H₀: βj=0.
It is calculated as:

$$
t_{\text{value}, j} = \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)}
$$

Where:

* Numerator β​ = Estimated coefficient
* Denumerator SE(β) = Standard error of β​ (from previous section)

H₀: βⱼ=0 asserts that the predictor xⱼ (e.g., x, x², etc.),
has no effect on the response variable y.
If H₀​ is true, the term xⱼ should be dropped from the model.

This is our litmus test.
If βⱼ​ is tiny, maybe your precious x² or x³ isn’t adding value.

#### p-value

> Just trust Excel or Python!

No need any gamma function complexity for practical calculation by hand.
For beginner like us, it is better to use excel built-in fomula instead.

`p-values` tell us whether to keep or dump predictors.
It's like speed dating for variables.

#### Confidence Intervals

We can continue to other statistical properties beyond just coefficients.
There's more we could calculate:
confidence bounds, prediction intervals, F-tests.
But let's save that for next time.
I guess I need to stop before this article become to complex.
Let's keep this article to be statistics for beginner.

NNow's the time to tabulate all of this in Excel,
or code it in Python for style points.
Just remember: under all these equations,
we're still doing one thing.
Trying to explain variance without overfitting our sanity.

-- -- --

### What Lies Ahead 🤔?

> Math is fun, right?

_No, really! Don’t run away just yet!_

From theoretical foundations we are going shift
to practical implementation in daily basis,
using spreadsheet formula, python tools, and visualizations.
Now that we've untangled the algebra spaghetti of polynomial regression,
it's time to roll up our sleeves and get our hands dirty,
with Excel, Python, and a healthy skepticism of curve fitting gone wild.

While the theory explains why the math works,
the practice shows how to execute it with real tools.
With the flow, from theory to tabular spreadsheets,
then from we are going to build visualization using python.

The theory gives us the why.
Why these equations matter,
why the degrees of freedom shrink,
faster than our confidence in a stats exam,
and why that suspicious x³ term might just be freeloading.
But knowing isn't enough. The real-world payoff comes in the how:

* How to implement all this using spreadsheet formulas (yes, even Excel deserves love)
* How to double-check our coefficients without crying into our coffee
* How to visualize trends like a pro using Python

We're shifting gears: from theory to table,
from formula to function, from blackboard to browser.
Whether we're working on trend analysis for stock prices,
or just trying to figure out if our cat's weight gain is linear or exponential
(spoiler: it’s usually cubic around holidays), this next step matters.

Time to move from "_hmm, interesting_" to "_aha!_"
Curious to see it all come together? March forward to
👉 **Trend – Polynomial Regression – Formula**.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Goes further from linear regression to polynomial regression.
> The practical implementation, shows how to execute the theory with spreadsheet.

Now that we've survived the theoretical terrain of polynomial regression
(and our coffee mugs are still half full),
it's time to put numbers into cells and formulas into action.

Theory is where we understand,
why fitting a 3rd-degree curve doesn’t mean we’re overfitting, necessarily.
But practice is where we catch that overfit before it eats our model alive.

We're going to:

* Use both the `LINEST` function and manual calculations.

* Start with raw cell references,
  to show what's going on under the hood.

* Later, evolve to named ranges,
  because `{=MMULT(E48:G50,E54:E56)}` isn't exactly readable poetry.

We want clarity, precision, and just a little flair.
Think of it as data fashion:
we're not just dressing up the numbers.
We’re making them walk the runway.

-- -- --

From theoretical foundations we are going shift
to practical implementation in daily basis,
using spreadsheet formula, python tools, and visualizations.

While the theory explains why the math works,
the practice shows how to execute it with real tools.
With the flow, from theory to tabular spreadsheets,
then from we are going to build visualization using python.

We are going to use both `linest` formula and manual calculation.
We are going to start with simple cell address in formula,
avoiding complex spreadsheet feature.
Then we are going to continue by using named range,
simplifying the formula understanding,
by using name instead of plain cell address.

-- -- --

### 1: What the Sheet Does

> And Why It Matters

The simplest way to get standard error from a polynomial regression in Excel?
Just summon the mighty `=LINEST(y-range, x-range^{1,2,...,n}, TRUE, TRUE)` formula.
Boom. Coefficients. Stats. Done.

But if you are the sort who reads footnotes and double-checks calculators,
you might want to peek behind the curtain and replicate it manually.

Here’s the catch: unlike linear regression,
Excel doesn’t hand you variance, covariance,
and residuals on a silver platter for higher-order polynomials.
We’re on our own.

Fear not! We’re already armed.
The previous articles gave us the mathematical gear,
we just need to wield it.

#### Worksheet Source

> The Artefact of Polynomial Power

You can download and dissect the Excel file used in this article.
It's ready for experimentation, and yes,
feel free to break it.
That's how breakthroughs happen.

* **github.com/.../math/trend/poly-regs.xlsx**

#### Basic Stuff

> Nomore spoon-feeding.

If you've followed along this far,
chances are your spreadsheet reflexes are already warmed up.

This sheet builds directly on the formulas introduced in:

* **Trend - Properties - Formula**

So no hand-holding here.
Instead of step-by-step spoon-feeding,
we'll do brief overviews for each section,
like a cooking show for regression.

#### Complete Worksheet

Although this looks complex.
It is easy when you have a working example.
Here's what the whole thing looks like,
when it's dressed up and ready for analysis:



Yes, it’s long.
Yes, it includes regression metrics, correlation, and some bonus bits.
But it's also user-friendly.
We just input our observed values, and voilà—results.

The hardest part?
Making complex things beginner-friendly without dumbing them down.
That's the magic trick here.
We don’t need to understand all the backend sorcery,
but it's there when we're curious.

We'll walk through the core components in this article,
using manual calculations.
So you can trust, verify, or even recreate the magic from scratch.

-- -- --

### 2: Prediction using Linest

> How to Cheat Elegantly with Built-In Magic.

In statistics, as in life,
if there's a shortcut that works.
Take it, and pretend it was your plan all along!

The easiest way to perform polynomial regression in a spreadsheet? Just use `LINEST`.
Why reinvent the wheel when Excel already gave us a Formula-Ferrari?



#### Getting Coefficients

Let's say our data lives in cells `B13:C25`,
where each (xᵢ, yᵢ) pair hangs out politely.
Here's how to extract the polynomial coefficients using `LINEST`:

```excel
Linear: Range E8:E9
(=TRANSPOSE(LINEST(C13:C25,B13:B25)))

Quadratic: Range F7:F9
{=TRANSPOSE(LINEST(C13:C25,B13:B25^{1,2}))}

Cubic: Range: G6:G9
{=TRANSPOSE(LINEST(C13:C25,B13:B25^{1,2,3}))}
```

Where 

1. Linear Fit = first order
2. Quadratic Fit = second order
3. Cubic Fit = third order

This is our go-to method for quick regression.
Ideal for most real-world use,
especially when we're prototyping,
or need instant insights without full matrix rituals.

#### Getting Predictions

Now that you have our coefficients,
let’s put them to use and generate predicted values of `Ŷᵢ = fit1(xᵢ)` as:

$$
\begin{array}{|l|l|l|}
  \hline
    \scriptstyle \text{1st order} &
    \scriptstyle \text{linear} &
    \hat{y}_i = \beta_0 + \beta_1{x_i} \rule{0pt}{2ex} \\
  \hline
    \scriptstyle \text{2nd order} &
    \scriptstyle \text{quadratic} &
    \hat{y}_i = \beta_0 + \beta_1{x_i} + \beta_2{x_i}^2 \rule{0pt}{2ex} \\
  \hline
    \scriptstyle \text{3rd order} &
    \scriptstyle \text{cubic} &
    \hat{y}_i = \beta_0 + \beta_1{x_i} + \beta_2{x_i}^2 + \beta_3{x_i}^3 \rule{0pt}{2ex} \\
  \hline
\end{array}
$$

And here's how they look in Excel:

```excel
Linear: E13:E25
=$E$9+$E$8*B13

Quadratic: F13:F25
=$F$9+$F$8*B13+$F$7*B13^2

Cubic: G13:G25
=$G$9+$G$8*B13+$G$7*B13^2+$G$6*B13^3
```

These predictions let us model trends beyond straight lines.
Ideal when our data clearly has curvature
(and our boss clearly has expectations).

Done, without any complexity.

-- -- --

### 3: Prediction using Gram Matrix

> How to Understand It Like a Real Nerd

What good is it learning without knowing how it works?
Let's go dive into the matrix.

_Why use one function when you can suffer with 12?_

The `LINEST` function is lovely,
until we want to understand what it's actually doing.
Reverse engineer the calculation using manual calculation,
to understand how the math works internally.

Welcome to the Matrix 🧠.
Here’s the classic normal equation in action:

$$
\begin{aligned}
              &&    A \mathbf{\beta} &= \mathbf{B} \\
  \Rightarrow &&    A^\top A \mathbf{\beta} &= A^\top \mathbf{B} \\
  \Rightarrow &&    \mathbf{\beta} &= (A^\top A)^{-1} A^\top \mathbf{B}
\end{aligned}
$$

We can compare the result to linest result directly.



#### Gram Matrix (Aᵗ.A)

Now let's break it into pieces using Excel formulas.

```excel
Linear: B42:C43
{=MMULT(
    TRANSPOSE(CHOOSE({1,2}, 1, B13:B25)),
    CHOOSE({1,2}, 1, B13:B25))}}

Quadratic: E42:G44
(=MMULT(
    TRANSPOSE(CHOOSE({1,2,3}, 1, B13:B25, B13:B25^2)),
    CHOOSE({1,2,3}, 1, B13:B25, B13:B25^2))))

Cubic: I42:L45
=MMULT(
    TRANSPOSE(CHOOSE({1,2,3,4}, 1, B13:B25, B13:B25^2, B13:B25^3)),
    CHOOSE({1,2,3,4}, 1, B13:B25, B13:B25^2, B13:B25^3))
```

This forms the core structure of our regression system.
Like the chassis of a car, it doesn't move on its own,
but without it, we’re sitting on the road.

> Inverse Gram Matrix (Aᵗ.A)ˉ¹

```excel
Linear: B48:C49
{=MINVERSE(B42:C43)}

Quadratic: E48:G50
{=MINVERSE(E42:G44)}

Cubic: I48:L51
{=MINVERSE(I42:L45)}
```

This lets us solve the system **algebraically**.
Yes, crafting in Excel is slow, 
but we can now claim we "_computed the inverse manually_" at parties.

> Right Hand Side (Aᵗ.B)

```excel
Linear: B54:B55
{=MMULT(
    TRANSPOSE(CHOOSE({1,2}, 1, B13:B25)),
    C13:C25)}}

Quadratic: E54:E56
{=MMULT(
    TRANSPOSE(CHOOSE({1,2,3}, 1, B13:B25, B13:B25^2)),
    C13:C25)}}

Cubic: I54:I57
{=MMULT(
    TRANSPOSE(CHOOSE({1,2,3,4}, 1, B13:B25, B13:B25^2, B13:B25^3)),
    C13:C25)}
```

This combines our design matrix with actual observed values
 i.e., this is where the "_real world_" enters our beautiful math.

#### Estimated Coefficients (β = [a, ...])

```excel
Linear: B60:B61
{=MMULT(B48:C49,B54:B55)}

Quadratic: E60:E62
{=MMULT(E48:G50,E54:E56)}

Cubic: I60:I63
{=MMULT(I48:L51,I54:I57)}
```

We've reverse-engineered `LINEST` ,
nd proven to ourself that regression isn’t black magic.
Just highly organized matrix multiplication.

Yes, it's a lot of formulas.
But once we've wrangled Excel into solving matrix equations,
we’ve basically earned your honorary statistician cape.

#### Using Raw Range Address

I keep the address cell, to keep basic spreadsheet,
without named range feature that lead
to incompatibility between different software.

If you think reading cell address is painful.
I completely agree with you.
Welcome to the club!
In the next section,
we'll use named ranges to make things friendlier, more readable, 
and less like a crossword puzzle written by a matrix.

-- -- --

### 4: Degrees of Freedom

> Freedom is not given, it is calculated. 

Degrees of freedom (df) might sound like something philosophers argue over,
but in regression, it's just a headcount.
How many data points we have minus
how many coefficients we're estimating (including the intercept).
It tells us how much "_wiggle room_",
our model has before it starts overfitting like an overzealous intern.

The calculation of degree of freedom is obvious.
I don't think that It require detail descriptions.

$$
\begin{align*}
& df = n - p - 1 \\
& \scriptstyle \text{(degree of freedom)}
\end{align*}
$$



In our spreadsheet, that translates to:

```excel
Linear: E33
=COUNT($B$13:$B$25)-2

Quadratic: F33
=COUNT($B$13:$B$25)-3

Cubic: G33
=COUNT($B$13:$B$25)-4
```

Degrees of freedom influence standard errors, confidence intervals,
and ultimately how much we can trust your model.
No freedom = no fun = no inference.

-- -- --

### 5: Linear Properties

> Correlation Calculation

"_All models are wrong, but some have correlation._” – G.E.P. Box (probably)

We do not need all the basic correlaton properties here.
We're not chasing every detail of correlation properties here,
just the essentials.
Think of it like carrying only whatwe need for a hike:
water, snacks, and maybe a chi-square joke.



The variance, covariance and standard deviation here only applied to linear regression.
But however we still need this one thing: `SST = ∑(yᵢ-ȳ)²`.
Here, we zoom in on the Total Sum of Squares (SST),
the granddaddy of variance in our model:

```excel
∑(yᵢ-ȳ)²: M28
=SUM(M13:M25)
```

This SST value tells us how much total variation is in our data.
Later, we'll see how much of that variation our model actually explains. 
The birth of R².

We don't need anything else.
Feel free to delete those unused variance/covariance cells,
and then see what's happened.
Enjoy the slight thrill of living on the edge.

-- -- --

### 6: Standard Error using Linest

> `LINEST` not only draws the line, it confesses its uncertainty.

The `LINEST` function isn’t just a pretty face that spits out coefficients.
If we add the right optional arguments, it also gives us the standard errors,
which are basically the confidence level of each estimated β.
Think of them as the margin of error in our model's smooth-talking predictions.



#### Getting Coefficients

Given our observed data pair (xᵢ, yᵢ) in `B13:C25`,
here's how we summon both the coefficients,
and their standard errors, all in one go:

```excel
Linear: Range Q8:R9
=TRANSPOSE(LINEST(C13:C25,B13:B25,1,1))

Quadratic: Range T7:U9
=TRANSPOSE(LINEST(C13:C25,B13:B25^{1,2},1,1))

Cubic: Range: W6:X9
=TRANSPOSE(LINEST(C13:C25,B13:B25^{1,2,3},1,1))
```

With transpose, the standard error of the coefficients,
is available in the second column.
Now inn these ranges:

* First column: the coefficients (βs)
* Second column: the standard errors (how nervous each β is about its own value)

Standard error helps us judge which coefficients are pulling their weight,
and which ones are just adding drama.
A large standard error? That β might be bluffing.

-- -- --

### 7: Residual Properties

> If it fits too well, it might be suspicious.

While `LINEST` generously hands us standard errors on a silver platter,
sometimes it's good for the soul (and the brain) to cook the meal ourself.
By calculating residuals manually, we get to peek under the hood,
and understand how the standard error stew is really made.

$$
\begin{align*}
SSE &= \sum\limits_{i=1}^{n} (\epsilon_i)^2 \\
    &= \sum (y_i - \hat{y}_i)^2 \\
\end{align*}
$$

#### Tabular Residual and SSR

Let's roll up our sleeves and tabulate the residuals (ϵᵢ),
their squares (ϵᵢ²), and also (∑ϵᵢ²) aka the sum of them all (SSE).
This is the part where we count how much our model missed.



Remember the fit range?
This is the address of predicted values for each model.

```excel
Y Observed: C13:C25
Linear: E13:E25
Quadratic: F13:F25
Cubic: G13:G25
```

Then we can compute residuals,
like a true spreadsheet warrior,
using the following formulas:

```excel
Linear: 
* ϵᵢ   =$C13-E13
* ϵᵢ²  =Q13^2
* ∑ϵᵢ² =SUM(R13:R25) at R28

Quadratic: 
* ϵᵢ   =$C13-F13
* ϵᵢ²  =T13^2
* ∑ϵᵢ² =SUM(U13:U25) at U28

Cubic: 
* ϵᵢ   =$C13-G13
* ϵᵢ²  =W13^2
* ∑ϵᵢ² =SUM(X13:X25) at X28
```

The residuals are the noise our model failed to capture.
Their sum of squares (SSE) tells us how far off our predictions are from the real world.
The smaller, the better, unless we're fitting noise instead of data.

#### Coefficient of Determination

Once we have SSE, we can compute the famous R².
It’s the applause meter for our model,
how much of the variance in our data is actually being explained.
Now we can continue with R² and R²adjusted:

$$
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$



```excel
∑(yᵢ-ȳ)² at M28
df linear at E32
df quadratic at F32
df cubic at G32
```

Now plug 'n play.
We can substitute the formula.

```excel
Linear: 
* R² =1-($R$28/$M$28) at Q32
* R²adjusted =1-((1-Q32)*($B$32-1)/$E32)

Quadratic: 
* R² =1-($U$28/$M$28) at T32
* R²adjusted =1-((1-T32)*($B$32-1)/$E32)

Cubic: 
* R² =1-($X$28/$M$28) at W32
* R²adjusted =1-((1-W32)*($B$32-1)/$E32)
```

R² tells us what portion of the chaos (variance) our model can explain.
Adjusted R² keeps us honest, penalizing us for adding variables,
that don't pull their weight.

#### Standard Error of the Estimate

We now calculate the MSE (Mean Squared Error),
and take its square root to get the SEE (Standard Error of the Estimate).
Think of SEE as how far, on average, our predictions land from the truth.
Kind of like our personal modeling credibility index.

With the same reference we can substitute MSE and SSE:

$$
MSE = \frac{SSE}{df} = \frac{\sum (y_i - \hat{y}_i)^2 }{n - p - 1}
$$

```excel
Linear: 
* MSE =R28/$E$32 at Q36
* SEE =SQRT(Q36)

Quadratic: 
* MSE =U28/$F$32 at T36
* SEE =SQRT(T36)

Cubic: 
* MSE =X28/$G$32 at W36
* SEE =SQRT(W36)
```

SEE is your model's average prediction error.
If it's too high, our model may need a tuning,
or therapy.

#### Statiscian Joke

We have `SEE`, why can't we have `HEAR`, or even `SPEAK`?

* We have `SEE` (Standard Error of the Estimate),
* but no `HEAR`, because residuals never listen.
* And certainly no `SPEAK`, because p-values only whisper.

We are done.

-- -- --

### 8: Standard Error using Diagonal Matrix

Let's revisit our beloved matrix form.
This time, pay attention to the diagonals.
They hold secrets.
Specifically, the diagonals of the inverse Gram matrix are,
proportional to the variances of the estimated coefficients.



The diagonal of inverse of gram matrix is actualy,
the variance of the estimated coefficients,
but required to be scaled.

$$
\left(X^\top X\right)^{-1}_{jj} = \text{Var}_{scaled}(\hat{\beta}_j)\cdot 
$$

The easiest thing to do is by pointing the cell,
for example Var(β₀) for linear fit is `=B47`.
But if we want to be looks like a real intellectual doing practical solution,
we can make ourself suffer using `INDEX` formula.



For example this tabulation of variance before scaled shown below.
This is using alphabet notation (instead of beta):

```excel
Linear: 
* a =INDEX(B47:C48,1,1)
* b =INDEX(B47:C48,2,2)

Quadratic: 
* a =INDEX(E47:G49,1,1)
* b =INDEX(E47:G49,2,2)
* c =INDEX(E47:G49,3,3)

Cubic: 
* a =INDEX(L47:O50,1,1)
* b =INDEX(L47:O50,2,2)
* c =INDEX(L47:O50,3,3)
* d =INDEX(L47:O50,4,4)
```

Now we can calculate the standard error by square root all of them.

$$
\begin{align*}
SE(\hat{\beta}_j) &= \sqrt{\text{Var}(\hat{\beta}_j) } \\
                  &= \sqrt{MSE \cdot (X^\top X)^{-1}_{jj}}
\end{align*}
$$

```excel
Linear: 
* SE(a) =SQRT($Q$36*R47)
* SE(b) =SQRT($Q$36*R48)

Quadratic: 
* SE(a) =SQRT($T$36*U47)
* SE(b) =SQRT($T$36*U48)
* SE(c) =SQRT($T$36*U49)`

Cubic: 
* SE(a) =SQRT($W$36*X47)
* SE(b) =SQRT($W$36*X48)
* SE(c) =SQRT($W$36*X49)
* SE(d) =SQRT($W$36*X50)
```

These standard errors tell us how stable our coefficients are.
Large SE means that β might be throwing darts.
Small SE? Now we're talking precision.

That's it. We're al most finished.

-- -- --

### 9: t-value and p-value

We've estimated the coefficients.
We've calculated their standard errors.
Now it’s time to interrogate them,
are they just innocent bystanders,
or guilty of being statistically significant?

Enter the t-value, our test statistic,
the lie detector of linear modeling:
by substituting the result of each SE(β).

$$
t_{\text{value}, j} = \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)}
$$

The `t-value` tells us whether each coefficient is distinct from zero,
or just pretending to do something useful.



For example `t-value` in these cells below.
Let’s plug in the formulas and see who's guilty.

```excel
Linear: 
* t-value(a) =B59/R53
* t-value(b) =B60/R54

Quadratic: 
* t-value(a) =B60/R54
* t-value(b) =E60/U54
* t-value(c) =E61/U55

Cubic: 
* t-value(a) =L59/X53
* t-value(b) =L60/X54
* t-value(c) =L61/X55
* t-value(d) =L62/X56
```

Now, to determine just how guilty, we convert the `t-value`s into `p-value`s.
Think of this as how much evidence we have to doubt the null hypothesis.

Use `T.DIST.2T` (two-tailed test, because we’re equal opportunity skeptics):
Since we are using two tail, we are need `ABS` formula to avoid negative value.

```excel
Linear: 
* p-value(a) =T.DIST.2T(ABS(R59),$E$32)
* p-value(b) =T.DIST.2T(ABS(R60),$E$32)

Quadratic: 
* p-value(a) =T.DIST.2T(ABS(U59),$F$32)
* p-value(b) =T.DIST.2T(ABS(U60),$F$32)`
* p-value(c) =T.DIST.2T(ABS(U61),$F$32)

Cubic: 
* p-value(a) =T.DIST.2T(ABS(X59),$G$32)`
* p-value(b) =T.DIST.2T(ABS(X60),$G$32)
* p-value(c) =T.DIST.2T(ABS(X61),$G$32)
* p-value(d) =T.DIST.2T(ABS(X62),$G$32)
```

Why the `ABS()`?
Because for two tailed, we don't care which side the coefficient lies on.
If it's far from zero, it better have a reason.

#### Tools Differences

Heads-up for tool differences.
Libreoffice Calc and Excel might calculate inifinte number differently.

* Excel may yell `DIV/0!` if a coefficient is completely flatlined.
* LibreOffice is a bit more philosophical. it simply whispers 0 as if to say, “I saw nothing.”

Statistical detectives, we've done well.
But alas, this sheet is way too long for daily patrol duty.
Let's prepare something shorter, sleeker,
and more street-ready for practical regression analysis.
Ready for that?

-- -- --

### 10: Practical Sheet

In real world daily basis,
we should avoid the complexity.

Let's face it, statistical elegance is nice,
but when the boss says, "_I want that trend report by lunch,_",
we don’t have time to wrestle matrix algebra.
We need a practical sheet.
Something less like a math journal and more like a spreadsheet that doesn't bite.

#### Data Entry Consideration

A key design principle of this worksheet:
_make data entry so easy our cat could do it_.
Real-world data isn't always polite.
It grows unpredictably.
We might have 12 rows today and 120 tomorrow.

So, we let the data flow from the bottom up,
like hot coffee in a cold mug.
Statistical summaries stay at the top
(where they don't scroll away),
while the raw data expands downward,
like a rebellious teenager's laundry pile.



#### Worksheet Source

> Open-Source Fun, No Fine Print

This isn't a proprietary black box.
This is an artefact, baby.
With named ranges and clean formulas,
you can fork it, tweak it, break it,
fix it, trash it, change it… (🎵 Daft Punk intensifies).

🧪 Get the sheet:
   **github.com/.../math/trend/poly-regs.ods**

You can open this document in LibreOffice.

LibreOffice recommended.
Because `.ods` is the new `.xlsx`.
The world is shifting.
Modern world needs modern tools.
`ods` is my choice.

#### Named Range

Named ranges are the breadcrumb trails for grown-up statisticians.
Rather than hunt for `$O$6:$O$9`, we call it `coeff_3`.
It's like giving our matrix a proper name.

This is how the named range looks like in LibreOffice Calc.
You can do the same thing with Microsoft Excel.
But there are incompatibilies.
Since I use LibreOffice for daily basis,
This is what I've got.



The steps are:

1. First I defined the observed range.
   From here I get the coefficient value (and standard error).

2. With coefficient value, I can calculate predicted values.

3. With predicted range I can calculate statistial properties.

Let say our sheet name is `regression',
Here's how they’re laid out.
The name address range can described as below:

| Named Range    | Range Address             |
|----------------|---------------------------|
| x_observed     | $regression.$B$42:$B$54   |
| y_observed     | $regression.$C$42:$C$54   |
| coeff_1        | $regression.$I$8:$I$9     |
| coeff_2        | $regression.$L$7:$L$9     |
| coeff_3        | $regression.$O$6:$O$9     |
| y1_predicted   | $regression.$E$42:$E$54   |
| y2_predicted   | $regression.$F$42:$F$54   |
| y3_predicted   | $regression.$G$42:$G$54   |

#### Observed Value

Let's start with observed value.
The raw materials of our regression forge.
The value might vary from samples to other samples,
but let's just use this example below:



Let's set the named range with these cell address.

```excel
x_observed at B42:B54
y_observed at C42:C54
```

"_Garbage in, garbage out_",
but here, we start with clean input.

#### Basic Properties

From this observed value we can calculate basic statistical properties.
Before we fit fancy curves,
let's start with the humble mean.



```excel
n =COUNT(x_observed) at B30
x̄ (mean) =AVERAGE(x_observed) at B34 
ȳ (mean) =AVERAGE(y_observed) at C34
```

We use ȳ to calculate ∑(yᵢ-ȳ)².
And we can completely dispose x̄ from the sheet.
ȳ helps us measure how well our regression line explains the variance,
and x̄… well, we don't really use x̄ here.

#### Linest Result

> Coefficient and Standard Error

_The lazy genius method for coefficients and SE_

Since we have already know how it works,
let Excel do the heavy lifting with `LINEST`.
Because life's too short to invert a matrix manually.

| Name           | Range                     |
|----------------|---------------------------|
| coeff_1        | $regression.$I$8:$I$9     |
| coeff_2        | $regression.$L$7:$L$9     |
| coeff_3        | $regression.$O$6:$O$9     |



Let's choose that range, calculate,
then set the named range with these cell address.

```excel
coeff_1 at I8:I9
=TRANSPOSE(LINEST(y_observed,x_observed,1,1))

coeff_2 at L7:L9
=TRANSPOSE(LINEST(y_observed,x_observed^{1,2},1,1))

coeff_3 at O8:O9
=TRANSPOSE(LINEST(y_observed,x_observed^{1,2,3},1,1))
```

It is more clear this way than using cell address right?
Saves time. Saves headaches.
In some countries, `LINEST` is prescribed as a stress reliever

#### Predicted Values

We plug our coefficients into the regression equation.
Wwe can calculate the predicted values.
But this time I'm going to use different formula,
other than previously mentioned.
This is our model speaking.
I've seen the data, and here's what I think.



```excel
y1_predicted at E42:E54
=SUMPRODUCT(TRANSPOSE(coeff_1),B43^{1,0})

y2_predicted at F42:F54
=SUMPRODUCT(TRANSPOSE(coeff_2),B43^{2,1,0})

y3_predicted at G42:G54
=SUMPRODUCT(TRANSPOSE(coeff_3),B43^{3,2,1,0})
```

Looks weird?
It is even weirder when we understand that
each coeff named range has two columns.
Well.. Let's get used to it.

#### t-value

We compute `t-values` to see if our coefficients,
are just making noise, or actually playing jazz.

$$
t_{\text{value}, j} = \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)}
$$



```excel
t-value β₀ at K14
=J8/K8
```

We can just copy this cell to the rest of the t-value for each β.

It's our detector.

* A big `t-value` says,
  “_Hey, this coefficient might actually mean something._”

* A small one says,
  “_Meh, maybe flip a coin._”

##### Degrees of Freedom

_Freedom is beautiful_. \
_Unless we subtract too many predictors_.

In order to get the p-value, we need to calculate the degree of freedom.

$$
\begin{align*}
& df = n - p - 1 \\
& \scriptstyle \text{(degree of freedom)}
\end{align*}
$$



_Each polynomial degree costs us a degree of freedom._ \
_Choose wisely, Padawan._

```excel
df1 at J25
=COUNT(x_observed)-2

df2 at M25
=COUNT(x_observed)-3

df3 at P25
=COUNT(x_observed)-4
```

Let's compared with previous form.

```excel
Linear df: E33
=COUNT($B$13:$B$25)-2

Quadratic df: F33
=COUNT($B$13:$B$25)-3

Cubic df: G33
=COUNT($B$13:$B$25)-4
```

Now the formula would make sense right?

#### p-value

The `p-value` tells us how shocked you should be by the `t-value`.
Lower is better (unless you're in an ethics committee).

```excel
t-value β₀ at K14
=J8/K8

p-value β₀
=T.DIST.2T(ABS(K14),$J$25)
```

We can just copy this cell to the rest of the p-value for each β.

It's our detector.

* A small p-value? We're probably on to something.
* A big one? Maybe it's just statistical small talk.


#### Statistic Properties

We have different statistic properties,
Let's cover-up the formula one by one.
This is the metrics that make or break our model's ego.



> SSR = ∑ϵᵢ²

```excel
Linear ∑ϵᵢ²: at K25
=SUMSQ(y_observed-y1_predicted)

Quadratic ∑ϵᵢ²: at M25
=SUMSQ(y_observed-y2_predicted)

Cubic ∑ϵᵢ²: at M25
=SUMSQ(y_observed-y3_predicted)
```

> SST = ∑(yᵢ-ȳ)²

```excel
General:
ȳ (mean) at C34
=AVERAGE(y_observed)

SST = ∑(yᵢ-ȳ)² at H30
=SUMSQ(y_observed-$C$34)
```

> R²

$$
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

No improvement here.
We go back to use address directly.

```excel
Linear R²: at J30
=1-($K$25/$H$30)

Quadratic R²: at M30
=1-($N$25/$H$30)

Cubic R²: at Q30
=1-($Q$25/$H$30)
```

> MSE and RMSE

$$
MSE = \frac{SSE}{df} = \frac{\sum (y_i - \hat{y}_i)^2 }{n - p - 1}
$$

```excel
Linear:
MSE  =K25/$J$25 at J34
RMSE =SQRT(J34)

Quadratic:
MSE  =N25/$M$25 at M34
RMSE =SQRT(M34)

Cubic:
MSE  =Q25/$P$25 at Q34
RMSE =SQRT(P34)
```

And just like that,
we've turned math into a working spreadsheet.
Congratulations, we now speak fluent regressionese.

Next up? Let's make this thing dance with charts.

-- -- --

### What Lies Ahead 🤔?

So far, we've bravely navigated the polynomial seas ,
from linear models that behave to cubic ones that flirt with chaos.
We've tamed the math, wrangled the formulas,
and even convinced a spreadsheet to do our bidding
(mostly without screaming). But what’s next?

We're now shifting gears from "_Why the math works_",
to “How to actually use this without sacrificing our weekend.”
Then let’s be honest: oour spreadsheet might be smart, 
ut it’s not going to code itself.

#### From Spreadsheet Zen to Python Wizardry 🐍✨

While a well-prepared spreadsheet can,
make any office admin look like a statistical genius
("_Oh this? It’s just my multi-degree polynomial model._"),
sometimes we need more power, flexibility, and sure fewer mouse clicks.

Spreadsheets are great for quick insights and small datasets,
but when our data grows, or we want automation, reproducibility,
or just prefer typing to dragging formulas with our mouse,
**Python** becomes the natural habitat for our analytical side.
Also, Python doesn't forget our named ranges. Ever.

So what lies ahead?

* Practical code we can tweak, extend, or meme-ify.
* Visualizations to make sense of all these numbers.
* Tools to help us tell better data stories, or at least look cool while trying.

Let’s take the next step and walk into,
the land of `pandas`, `numpy`, and `matplotlib` with style.
You deserve it.

👉 Start here:
**Trend - Polynomial Regression - Python**.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Goes further from linear regression to polynomial regression.
> The practical implementation, shows how to implement the theory in python code.

We've already built the theoretical scaffolding,
and wrestled Excel into obedience.
But real-world data is messy, expectations are high,
and Ctrl+C only goes so far as the rows grow.
It's time to move from spreadsheets to scripts,
from clicking to coding.

Now don’t get me wrong, spreadsheets are fantastic.
They make us look brilliant in meetings,
and our office admin can spot a trend,
faster than our manager can say "_Q4 report._"
But let's face it: they're not built for scale, automation, or creative chaos.

That’s where Python enters, stage left. 🐍
With Python, we will:

* Reproduce our polynomial models programmatically

* Automate the boring stuff
  (goodbye, repetitive formula updates!)

* Customize for edge cases
  (reality rarely follows your tidy cell ranges)

When your data hits 10,000 rows,
we'll want something more robust than Excel and a prayer.

So sharpen our Jupyter notebooks, warm up our terminal,
and prepare for lift-off into,
the statistically thrilling world of Polynomial Regression in Python.

Let’s bring theory to life, with code.

-- -- --

### 1: Statisctic Properties

Welcome to the part where we roll up our sleeves,
and inspect the machinery inside polynomial regression.
Not just admiring the curve,
but poking at the math that put it there.

We'll begin with minimalist tools (hello, `numpy`)
before bringing in reinforcements from `scipy` and `sklearn`.
This is the programmer's equivalent of,
starting with a torque wrench before switching to a power drill.

We are going to start from minimalist to solve this situation,
using numpy manual calculation only, then utilize other library as well.
Since most topic is already covered in previous section,
we are going to skip the explanation, and goes to ready to use class,
for practical application.

#### 1: From Skeletons to Stats:

> Building Blocks

This time we’re engineering a master-detail class setup,
with `CurveFitting` orchestrating the show,
and `PolynomialOrderAnalyzer` doing the dirty work,
for linear, quadratic, and cubic fits.
One main class, manage three kind of polynomial order.

```python
import ...

class PolynomialOrderAnalyzer:
    ...

class CurveFitting:
    ...

def main() -> int:
    ...

if __name__ == "__main__":
    raise SystemExit(main())
```

A reusable, extensible codebase saves future-us,
from copy-paste regret.
And lets us test multiple fits with a single call.



Yes, it's verbose.
But so is our favorite statistics professor,
who often explain things in great depth.

#### 2: CurveFitting

> The Conductor

The first is the main `CurveFitting` class.
This is the main controller.
It stores data, prints general stats, 
and loops through each polynomial order.

```python
class CurveFitting:
    def __init__(self, xs, ys : List[int]) -> None:
        ...

    def print_props_general(self) -> None:
        ...

    def process(self) -> None:
        ...
```

Polynomial fitting is only useful,
if we understand how the curve behaves across different complexities.
This lets us test and compare all three in one go.

#### 3: PolynomialOrderAnalyzer

> The Intern Who Does the Actual Work

Then comes the `PolynomialOrderAnalyzer` class to analyse each order.

```python
class PolynomialOrderAnalyzer:
    COEFF_TEXTS = {1: '(a, b)', 2: '(a, b, c)', 3: '(a, b, c, d)'}
    ORDER_TEXTS = {1: 'Linear', 2: 'Quadratic', 3: 'Cubic'}

    def __init__(self, xs, ys: np.ndarray, order: int) -> None:
        ...
       
    def calc_props_matrix(self) -> None:
        ...

    def calc_props_mse(self) -> None:
        ...

    def calc_props_t_p_value(self) -> None:
        ...
```

This is where we compute the good stuff.
The matrix math, error stats, and the ever-humble `p-values`.


#### 4 : Required Imports

> The Arsenal

We need to include a few import statements.



```python
import numpy as np
from numpy.polynomial import Polynomial
from scipy.stats import t
from sklearn.metrics import r2_score
from typing import List
```

You can see that we are going to use a few different library.
Yes, `scipy.stats.t` is our friendly `t-distribution`.
Like any good academic, it's judgy and loves small `p-values`.

#### 5: Data Series

From humble rows, mighty fits are born.
For example using these series,
you may choose `ys₁`, `ys₂`, or `ys₃`:

* **series.csv**

```csv
xs, ys1, ys2, ys3
0,  5,   5,   5
1,  9,   12,  14
2,  13,  25,  41
3,  17,  44,  98
4,  21,  69,  197
5,  25,  100, 350
6,  29,  137, 569
7,  33,  180, 866
8,  37,  229, 1253
9,  41,  284, 1742
10, 45,  345, 2345
11, 49,  412, 3074
12, 53,  485, 3941
```



Real-world data often bends and curves.
Linear fits get nervous.
Higher-order polynomials step in.

#### 6: Entry Point

> Where the Show Begins

The entry point is simply as below:

```python
if __name__ == "__main__":
    raise SystemExit(main())
```

While the main function itself is just CSV loader,
featuring column chooser.



```python
def main() -> int:
    # Getting Matrix Values
    mCSV = np.genfromtxt("series.csv",
      skip_header=1, delimiter=",", dtype=float)
    mCSVt   = np.transpose(mCSV)

    example = CurveFitting(mCSVt[0], mCSVt[3])
    example.process()

    return 0
```

Yes, we pick a column and unleash math on it.

#### 7: CurveFitting: Initialization

We just need to convert he list to `np.array`, for further use.



```python
class CurveFitting:
    def __init__(self, xs, ys : List[int]) -> None:
        # Given data
        self.xs = np.array(xs)
        self.ys = np.array(ys)
```

#### 8: CurveFitting: General Properties

> ȳ and ∑(yᵢ - ȳ)²

Then print general properties.



```python
    def print_props_general(self) -> None:
        y_mean = np.mean(self.ys)
        self.y_sq_deviation = np.sum((self.ys-y_mean) ** 2)
        print('General')
        print(f'\tȳ (mean)   : {y_mean:15,.2f}')
        print(f'\t∑(yᵢ-ȳ)²   : {self.y_sq_deviation:15,.2f}')
        print()
```



Before fitting a curve,
we need to know how wild the data is.
This is our baseline.
The "no model" chaos.

#### 9: CurveFitting: Process

>  Loop Through Orders

Here we print all the properties.



```python
    def process(self) -> None:
        # Print Statistical Properties
        self.print_props_general()
        
        for order in [1, 2, 3]:
            case = PolynomialOrderAnalyzer(self.xs, self.ys, order)
            case.calc_props_matrix()
            case.calc_props_mse()
            case.calc_props_t_p_value()
            print()
```

Not all curves are created equal.
Some just overfit and lie.
This loop checks who's telling the truth.

#### 10: Polynomial Order Analyzer: Initialization

Here we take care of each polynomial order.



```python
class PolynomialOrderAnalyzer:
    COEFF_TEXTS = {1: '(a, b)', 2: '(a, b, c)', 3: '(a, b, c, d)'}
    ORDER_TEXTS = {1: 'Linear', 2: 'Quadratic', 3: 'Cubic'}

    def __init__(self, xs, ys: np.ndarray, order: int) -> None:
        self.xs = xs
        self.ys = ys
        self.order = order
        self.df = len(self.xs) - order -1

        self.mA   = None
        self.mC   = None
        self.yp   = None
        self.diag = None
        self.MSE  = None

        # Display
        self.coeff_text = self.COEFF_TEXTS[order]
        self.order_text = self.ORDER_TEXTS[order]
```

#### 11: Properties Calculation: Matrix

> Design and Coefficients

The actual matrix calculation is short.



```python
    def calc_props_matrix(self) -> None:
        # Perform regression using polynomial.
        poly = Polynomial.fit(self.xs, self.ys, deg=self.order)
        self.mC = poly.convert().coef
        self.yp = poly(self.xs)

        # Matrix Operation
        self.mA = np.flip(np.vander(self.xs, self.order+1), axis=1)
        mAt   = self.mA.T
        mAt_A = mAt @ self.mA # gram matrix
        mI   = np.linalg.inv(mAt_A)
        self.diag = np.diag(mI)

        print(f'Using polyfit : {self.order_text}')
        print(f'Coefficients  : {self.coeff_text}: '
            + f'{self.mC}')
```



But for broader overview,
we have different kind of calculations.
I commented the alterantive calculation.

> Design Matrix A

```python
        # Design Matrix A
        # mA_1 = np.column_stack([np.ones_like(self.xs), self.xs, self.xs**2])
        # mA_2 = np.column_stack([self.xs**j for j in range(self.order+1)])  # Design matrix
        self.mA = np.flip(np.vander(self.xs, self.order+1), axis=1)
```

> Matrix Operation

```python
        mB = self.ys
        mAt   = self.mA.T
        mAt_A = mAt @ self.mA # gram matrix
        mAt_B = mAt @ mB 
        # mC_1 = np.linalg.solve(mAt_A, mAt_B)
        # mC_2 = np.polyfit(self.xs, self.ys, deg=order)
        # mC_3 = np.linalg.inv(self.mA.T @ self.mA) @ (self.mA.T @ mB)
        # mC_4 = np.linalg.lstsq(self.mA, mB, rcond=None)[0]
        # print(mC_4)
        mI   = np.linalg.inv(mAt_A)
        self.diag = np.diag(mI)
```

> Getting Prediction Series

```python
        poly = Polynomial.fit(self.xs, self.ys, deg=self.order)
        self.mC = poly.convert().coef
        # yp_1    = np.polyval(mC, self.xs)
        self.yp = poly(self.xs)
        # y_pred_2 = self.mA @ mC
        # print(y_pred_2)
```

> Print The Statistic Properties Header

```python
        print(f'Using polyfit : {self.order_text}')
        print(f'Coefficients  : {self.coeff_text}: '
            + f'{self.mC}')
```

we don’t get meaningful `t-tests`,
unless we’ve built the model matrix right.
This is our math foundation.

#### 12: Properties Calculation: MSE and R²

> Mean Square Error

_Are We Even Close?_

This is how we calculate MSE manually.



```python
    def calc_props_mse(self) -> None:
        # Calculate SST and SSE
        y_mean = np.mean(self.ys)
        SST = y_sq_deviation = np.sum((self.ys-y_mean) ** 2)
        SSR = np.sum((self.ys - self.yp) ** 2) # ∑ϵᵢ²
        R_squared = 1 - (SSR / SST)
        # r2 = r2_score(self.ys, yp)
        self.MSE = SSR/self.df

        print(f'\t∑(yᵢ - ŷᵢ)² : {SSR:15,.2f}')
        print(f'\tR²          : {R_squared:15,.4f}')
        print(f'\tMSE         : {self.MSE:15,.2f}')
```



R² is our curve's bragging score.
MSE is its humility check.
Together, they balance hubris and usefulness.

> `r2_score()`?

Note that we can calculate R² using `r2_score()` function from `sklearn.metrics`.
But why can't we calculate MSE using `mean_squared_error()` function from `sklearn.metrics`.

This is because of difference of degree freedom.
This is due of the focus of the `sklearn.metrics` is not for the statistical properties,
but designed for general use (e.g., evaluating predictions without knowing model internals).
The DoF in `sklearn.metrics` use `n` as divisor, while we are using `(n - k -1)`.

Degrees of freedom matter, and `sklearn` doesn’t care about our academic rigor.

#### 13: Properties Calculation: t-value, p-value

> The Statistical Lie Detector

The calculation using `t distribution` is simple.



```python
    def calc_props_t_p_value(self) -> None:
        # t-value, p-value
        SE   = np.sqrt(self.MSE * self.diag)
        t_value = self.mC/SE
        p_value = 2 * (1 - t.cdf(abs(t_value), self.df))
```

But we need to convert the array inpit,
so that this would have nice looks in output.

```python
        diag_formatted = [f"{x:15,.4f}" for x in self.diag]
        SE_formatted   = [f"{x:15,.4f}" for x in SE]
        t_v_formatted  = [f"{x:15,.2e}" for x in t_value]
        p_v_formatted  = [f"{x:15,.10f}" for x in p_value]
```

Now we can finally print the result.

```python
        print(f"diag    : [" + " ".join(diag_formatted) + "]")
        print(f"SE(β)   : [" + " ".join(SE_formatted) + "]")
        print(f"t_value : [" + " ".join(t_v_formatted) + "]")
        print(f"p_value : [" + " ".join(p_v_formatted) + "]")
```



This is where we ask,
"_Are these coefficients statistically significant,_
_or just enthusiastic guesswork?_"

-- -- --

### 2: Simple Plot

After printing the stats
(yes, all those glorious coefficients and R2R2 values),
it's time to do what every stats professor secretly lives for: draw a nice plot.
But this time, we will give our chart a little more personality,
and a lot more polynomial.

_This time with emphasis of selected properties._

#### Skeleton

> Anatomy of a Trend-Plotter

This plotting class is lean, and clean.
We have only three new functions here:



```python
class CurveFitting:
    def __init__(self, xs, ys : List[int]) -> None:
        ...

    def print_props_general(self) -> None:
        ...

    def calc_plot_all(self) -> None:
        ...

    def add_plot_text(self, plt) -> None:
        ...

    def plot_trend(self, plt) -> None:
        ...

    def draw_plot(self) -> None:
        ...

    def process(self) -> None:
        ...
```

Separating concerns in code is like labeling our axes.
It saves our sanity later.
Each method here has a clear purpose,
just like each coefficient in a quadratic equation
(even the one that always seems to vanish).

#### Prediction Calculation

> A Gentle Squeeze from Chaos into Curve

From given points, it got us three beautiful, smooth curves:
linear, quadratic, and cubic. No drama.
The calculation is as simple as this one below:



```python
    def calc_plot_all(self) -> None:
        self.x_plot = xp = np.linspace(
            min(self.xs), max(self.xs), 100)

        # Calculate coefficients directly
        self.y1_plot = Polynomial.fit(self.xs, self.ys, deg=1)(xp)
        self.y2_plot = Polynomial.fit(self.xs, self.ys, deg=2)(xp)
        self.y3_plot = Polynomial.fit(self.xs, self.ys, deg=3)(xp)
```

A plot without prediction is like regression without a cause.
These lines help us see how the model fits.
Not just mathematically, but viscerally (cue dramatic music).

#### Plot Trend

> The Curve Awakens

Time to let `matplotlib` strut its stuff.
`Scatter` + `curves` = the stats professor's version of abstract art.
The plot is also the same as in previous section,
but I put it in separate function.



```python
    def plot_trend(self, plt) -> None:
        # Scatter plot with Seaborn color
        sns.scatterplot(
            x=self.xs, y=self.ys, color=self.colors[0], 
            s=100, label='Data points', edgecolor='w', linewidth=0.5)

        # Polynomial curves with Seaborn colors
        plt.plot(self.x_plot, self.y1_plot, color=self.colors[1], 
                linewidth=2.5, label='Linear fit')
        plt.plot(self.x_plot, self.y2_plot, color=self.colors[2], 
                linewidth=2.5, label='Quadratic fit')
        plt.plot(self.x_plot, self.y3_plot, color=self.colors[3], 
                linewidth=2.5, label='Cubic fit')

        plt.legend(fontsize=10, framealpha=0.9)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        plt.title('Polynomial Regression with Statistics')
        plt.grid(True, linestyle='--', alpha=0.3)

        plt.tight_layout()
```

Visualizing each polynomial degree side by side,
lets us compare their fit personalities.
Linear is minimal, quadratic is flexible,
and cubic is a drama queen. Pick our champion.

#### Main Plot Function

> Bringing It All Together (With Style)

Now we can merge that trend plot into the main plot function.
this way we can add additional plot later easily.
This is where it all merges:
`scatterplot`, `curves`, and stats-packed `annotation box`.



```python
    def draw_plot(self) -> None:
        plt.figure()
        self.plot_trend(plt)
        self.add_plot_text(plt)

        plt.tight_layout()
        plt.show()
```

Notes that I add this weird line here.
Yes, this line below may seem mysterious, but it’s the secret sauce:

```python
        self.add_plot_text(plt)
```

Numbers are powerful,
but annotations turn our chart into a conversation.
Especially when our audience is tired and caffeinated.

#### Selected Properties

> Stats in a Box

Sometimes, we want the plot to speak,
specifically, to whisper something like:

    _Hey, quadratic fit here._
    _I’ve got an R²=0.928,_
    _and a mean squared error of only 2.1._
    _Just saying._

This line add a box for any text.
For example, if we want to emphasis,
the result of the second order polynomial,
We can display the statistical properties easily.



```python
    def add_plot_text(self, plt) -> None:
        # Add statistics for quadratic fit (example)
        poly = Polynomial.fit(self.xs, self.ys, deg=2)
        mC = poly.convert().coef
        yp = poly(self.xs)
        SST = self.y_sq_deviation
        SSR = np.sum((self.ys - yp) ** 2)
        R_squared = 1 - (SSR / SST)
        MSE = SSR / (len(self.xs) - 3)  # deg=2 → 3 params (a, b, c)

        # Format equation and stats
        eqn = f"$y = {mC[0]:.2f} + {mC[1]:.2f}x + {mC[2]:.2f}x^2$"
        stats_text = (
            f"$R^2 = {R_squared:.3f}$\n"
            f"$MSE = {MSE:.2f}$\n"
        )

        # Place text on plot
        plt.text(
            0.05, 0.95, 
            f"{eqn}\n{stats_text}",
            transform=plt.gca().transAxes,
            ha='left', va='top',
            bbox=dict(facecolor='white', alpha=0.8)
        )
```

This turns our graph into a mini-report.
When people ask, “So, how good is your model?”,
we can just point at the chart smugly.

#### Execute The Process

> The Grand Finale

Put it all together.
This is the conductor cueing the orchestra.
Then add the plot to the main process.

```python
    def process(self) -> None:
        # Print Statistical Properties
        self.print_props_general()
        
        for order in [1, 2, 3]:
            case = PolynomialOrderAnalyzer(self.xs, self.ys, order)
            case.calc_props_matrix()
            case.calc_props_mse()
            case.calc_props_t_p_value()
            print()

        self.calc_plot_all()
        self.draw_plot()
```

If this method were a person,
it would be your overachieving classmate,
who not only finishes the assignment,
but also builds a working demo with animated transitions.

#### The Result

> Not Just a Chart, But a Conversation

Yes, it’s still a humble old scatter plot chart.
But now it speaks. It tells us how well the curve fits,
which model performs better,
and whether our hypothesis has any statistical backbone.



#### Feedback

Got a different way to interpret the fit?
Found a flaw in the logic?
Or just want to argue that cubic fits are overkill 90% of the time?
Let's chat—data nerd to data nerd.

I welcome any other useful interpretation, or any feedback.
If you think my visualization, or interpretation is wrong, please let me know.

-- -- --

### 3: Visualizing the Invisible

> Coefficients

When our regression results are feeling a little too abstract,
like a shy statistician at a party,
it’s time to give them a visual voice.
Let's plot the statistical properties of our polynomial coefficients,
because staring at numbers in a table is so last century.

I actually do not have any idea for the visualization of the statistical properties.
But I think we can recap the coefficient result in a simple chart.
so people can just read our result easily.

We're talking standard errors, t-values, and p-values.
Yes, those awkward guests at every stats gathering,
let's shine a spotlight on them.

#### Saving the Statistical Goods

Before we can show off our coefficients' credentials,
we need to save them.
Think of this step as grabbing their résumé before printing it on a billboard.



```python
class PolynomialOrderAnalyzer:
    ...

    def calc_props_t_p_value(self) -> None:
        ...

        return {
            'SE'      :  SE,
            't-value' :  t_value,
            'p-value' :  p_value
        }
```

These values tell us how trustworthy each coefficient is.
They're like GPA scores for your polynomial terms.

* Big t-values? Great!
* Tiny p-values? Even better!

And no, no need to add abs(t_value).
Negative coefficients deserve love too.
The direction in positive and negative is matter.

#### Statistic Plot

> Bar Charts to the Rescue

Numbers can mumble, but plots shout.
Let's pick one polynomial order (say, degree 2),
and visualize how each coefficient performs.



```python
    def plot_stats(self, plt) -> None:
        # Statistics bar plots
        order = 2
        stats = self.stats[order]
        labels = [f"β{i}" for i in range(order+1)]

        def stat_bar(ax, values, title, color):
            ax.bar(labels, values, color=color)
            ax.set_title(title)
            ax.grid(True, axis='y', linestyle='--', alpha=0.3)

        ax1 = plt.subplot(1, 3, 1)
        stat_bar(ax1, stats['SE'], "Standard Error (SE)", 'orange')

        ax2 = plt.subplot(1, 3, 2)
        stat_bar(ax2, stats['t-value'], "t-values", 'skyblue')

        ax3 = plt.subplot(1, 3, 3)
        stat_bar(ax3, stats['p-value'], "p-values", 'salmon')

        # log scale to better show small p-values
        ax3.set_yscale('log')
```

These plots reveal which coefficients are reliable,
and which are just freeloaders pretending to help the model.
The p-values in particular help us judge,
whether a coefficient is significantly different from zero,
or just statistically loitering.

#### Main Plot Function

> Drawing the Big Picture

Let's blend everything together in the `draw_plot()` method,
both the trend and the stats.
Context is everything:
without the trend line, those stats are just numbers in a vacuum.



```python
    def draw_plot(self) -> None:
        # Plot 1: Trend + Equation
        plt.figure()
        self.plot_trend(plt)
        self.add_plot_text(plt)

        # Plot 2: Bar Plots
        plt.figure()
        self.plot_stats(plt)
        plt.show()
```

By combining the regression plot and its statistical underpinnings,
we create a full narrative: "_Here’s the curve, and here's why we should believe it_."



No, the chart doesn't talk (yet),
but it does whisper important truths:
"_This coefficient is legit,_" or "_This term might be nonsense._"
And if our β₂ has a `p-value` that could legally be rounded to zero,
that's our cue to shout "_Statistically significant!_",
like a proud parent at graduation.

I'm still curious how to visualize further, for better visual metaphors in future posts.
But this time I still have no idea.
For now, these bar plots help turn statistical smoke into readable signal.

-- -- --

### What's the Next Exciting Step 🤔?

Now that we've tamed the coefficients,
what's next on this statistical safari?

Well, we've plotted the trend.
We've grilled the coefficients for their `p-values`.
We've even thrown their `t-values` onto a public chart for all to see.
Now it's time to turn our eyes toward another shady character in statistics:

> 📈 The Distribution Curve.

If our statistical properties are the "what,"
the distribution plot is the "why."
It helps us see the shape of the data that justifies those values.
It's like finally meeting the parents after dating the regression line for a while.

Understanding the distribution helps us validate assumptions.
Are the residuals normal?
Are we modeling randomness or just noise with a fancy hat?

But before we go full Gauss,
we'll need to brush up on the basics of drawing distribution plots.
So we can later connect them with the statistical interpretations we’ve just made.

Curious how this unfolds? Continue your exploration in
👉 **Trend - Visualizing Distribution**.
Because even regression models deserve to know where they come from.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Getting to know the basic of visualizing distribution curve.

Since we also need to visualize
the interpretation of statistics properties against the distribution plot curve,
we need to get the basic of making distribution plot curve.

Before we get too excited about `t-values` and `p-values`,
let's remember where they live: in the comforting arms of the distribution curve.
If statistics had a family tree, the normal distribution would be the well-dressed grandparent,
who everyone references but nobody fully understands.

To better interpret our regression output,
it's wise to revisit how distributions work.
Starting from scratch, let's draw them, shade them, and twist them into funny shapes.
Behind every `t-test` is a bell curve just waiting to shine.

-- -- --

### Distribution

Ah, plotting! The visual symphony of statistics.
Let’s roll up our sleeves and start composing.
Crafting a plot is interesting.

#### Probability Density Function (PDF)

Our first guest: the standard normal distribution.
Elegant. Symmetrical. Like a bell that never rings.

Its probability density function (PDF) is:

$$
f(x) = \frac{1}{\sqrt{2\pi}} \cdot e^{-\frac{x^2}{2}}
$$

This is the benchmark of "normality" in statistics.
Most tests, including our regression's `p-values`,
assume something roughly bell-shaped underneath.
Knowing how it looks helps us spot when things go awry.

#### Normal

Start by generating a set of values along the x-axis:

* **63-dist.py**

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate data points for x-axis
x = np.linspace(-5, 5, 1000)

# Calculate the corresponding y-values
# for a standard normal distribution
y = 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * x**2)

# Plot the normal distribution
plt.plot(x, y, color='blue')

# Add labels and title
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Standard Normal Distribution')

# Show grid
plt.grid(True)

# Show plot
plt.show()
```

Explanation

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
```

We can implement the equation for the probability density function (PDF) of a standard normal distribution as follows:

```python
y = 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * x**2)
plt.plot(x, y, color='blue')
```

> 🎨 Voilà: the classic bell curve.



The result of the plot can be visualized as below:



Not in the mood for calculus? Let scipy do the heavy lifting:

Instead of manually calculating,
Let `scipy.stats` do the heavy lifting:

```python
from scipy.stats import norm
y = norm.pdf(x)
```

We can play around with it in this `Jupyter notebook`:

* **63-dist.py**

#### Quantiles

With normal distribution,
we can go further with visualizing quantiles.
Let's add some color by slicing the bell into pieces.

* **63q-dist.py**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate data points for x-axis
x = np.linspace(-5, 5, 1000)

# Calculate the corresponding y-values
# for a standard normal distribution
y = norm.pdf(x)

# Calculate the percentiles
percentiles = [25, 50, 75, 100]
quantiles = np.percentile(x, percentiles)

# Plot the normal distribution
plt.plot(x, y, color='black')

# Shade regions corresponding to percentiles
for i, q in enumerate(quantiles):
  plt.fill_between(
    x[x <= q], y[x <= q],
    color=f'C{i}', alpha=0.3)

# Add labels and title
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Standard Normal Distribution '
  + 'with Quantiles')

# Show grid
plt.grid(True)

# Show plot
plt.show()
```

Explanation

```python
y = norm.pdf(x)

percentiles = [25, 50, 75, 100]
quantiles = np.percentile(x, percentiles)

plt.plot(x, y, color='black')
```

Now we can shade regions corresponding to percentiles as follows:

```python
for i, q in enumerate(quantiles):
  plt.fill_between(
    x[x <= q], y[x <= q],
    color=f'C{i}', alpha=0.3)
```

The terms **quartiles** and **quantiles**,
are related but not exactly the same.
Quartiles divide a dataset into four equal parts.
Quantiles, on the other hand,
divide a dataset into any number of equal parts.



The result of the plot can be visualized as below:



Notebook for tinkering:

* **63q-dist.py**

Quantiles tell yus where your data falls.
Great for understanding outliers,
or explaining why our boss's sales numbers are in the _95th percentile_.

#### Kurtosis

Let's meet our first rebel: `kurtosis`.
It measures whether the tails of a distribution are chunky or skinny.

* Think of it as _how dramatic your data likes to be._

We'll use `skewnorm.pdf` with different scale values to simulate kurtosis.

* **64-kurtosis.py**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm, norm, kurtosis

# Generate data points for x-axis
x = np.linspace(-5, 5, 1000)

# Calculate the corresponding y-values
# for the standard normal distribution
y_standard = norm.pdf(x)

# Examples of distributions
# with different levels of kurtosis

# Standard normal distribution (Kurtosis = 0)
y_kurtosis_1 = skewnorm.pdf(x, a=0, loc=1, scale=1)

# Lower kurtosis
y_kurtosis_2 = skewnorm.pdf(x, a=0, loc=1, scale=0.5)

# Higher kurtosis
y_kurtosis_3 = skewnorm.pdf(x, a=0, loc=1, scale=2)

# Plot the normal distribution
plt.plot(x, y_standard, label='Standard Normal')

# Plot distributions with
# different levels of kurtosis
plt.plot(x, y_kurtosis_1, ls='-.',
  label='Standard Kurtosis = 0')
plt.plot(x, y_kurtosis_2, ls='-.',
  label='Lower Kurtosis')
plt.plot(x, y_kurtosis_3, ls='-.',
  label='Higher Kurtosis')

# Add labels and title
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Normal Distribution with Different Kurtosis')

# Add legend
plt.legend(loc='upper left')

# Show grid
plt.grid(True)

# Show plot
plt.show()
```

Explanation

Let’s compare them visually.
Below arrangement are visualization examples of distributions
with different levels of kurtosis.
To differ with the normal distribution,
I move the curve to the right.

```python
from scipy.stats import skewnorm, norm, kurtosis

x = np.linspace(-5, 5, 1000)
y_standard = norm.pdf(x)

y_kurtosis_1 = skewnorm.pdf(x, a=0, loc=1, scale=1)
y_kurtosis_2 = skewnorm.pdf(x, a=0, loc=1, scale=0.5)
y_kurtosis_3 = skewnorm.pdf(x, a=0, loc=1, scale=2)
```



Now we can plot distributions with
different levels of kurtosis,
on the same plot with the normal distribution.

```python
plt.plot(x, y_standard, label='Standard Normal')

plt.plot(x, y_kurtosis_1, ls='-.',
  label='Standard Kurtosis = 0')
plt.plot(x, y_kurtosis_2, ls='-.',
  label='Lower Kurtosis')
plt.plot(x, y_kurtosis_3, ls='-.',
  label='Higher Kurtosis')
```



The result of the plot can be visualized as below:



Notebook for hands-on play:

* **64-kurtosis.py**

High kurtosis means more extreme values.
Great for finance. Terrible for blood pressure.

#### Skewness

Next up: skewness, the art of asymmetry.
If our distribution leans to one side like a suspicious alibi, it’s skewed.
We can utilize `skewnorm.pdf` again to visualize skewness.

* **65-skewness.py**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm, norm, kurtosis

# Generate data points for x-axis
x = np.linspace(-5, 5, 1000)

# Calculate the corresponding y-values
# for the standard normal distribution
y_standard = norm.pdf(x)

# Calculate the corresponding y-values 
# or distributions with different skewness parameters
# Examples of skewed distributions
# with different skewness parameters

# Negative skewness
y_skewed_1 = skewnorm.pdf(x, a=-4)

# Moderate positive skewness
y_skewed_2 = skewnorm.pdf(x, a=2)

# High positive skewness
y_skewed_3 = skewnorm.pdf(x, a=6)

# Plot the normal distribution
plt.plot(x, y_standard, label='Standard Normal')

# Plot skewed distributions
# with different skewness parameters
plt.plot(x, y_skewed_1, ls='--',
         label='Negative Skewness = -4')
plt.plot(x, y_skewed_2, ls='--',
         label='Moderate Positive Skewness = 2')
plt.plot(x, y_skewed_3, ls='--',
         label='High Positive Skewness = 6')

# Add labels and title
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Normal Distribution '
 + 'with Different Skewness')

# Add legend on the top left
plt.legend(loc='upper left')

# Show grid
plt.grid(True)

# Show plot
plt.show()
```

Explanation

The same method of kurtosis above applied for skewness.
Below arrangement are visualization examples of distributions
with different skewness parameters.

```python
y_skewed_1 = skewnorm.pdf(x, a=-4)
y_skewed_2 = skewnorm.pdf(x, a=2)
y_skewed_3 = skewnorm.pdf(x, a=6)
```

Let's draw their curious curves.



```python
plt.plot(x, y_standard, label='Standard Normal')

plt.plot(x, y_skewed_1, ls='--',
         label='Negative Skewness = -4')
plt.plot(x, y_skewed_2, ls='--',
         label='Moderate Positive Skewness = 2')
plt.plot(x, y_skewed_3, ls='--',
         label='High Positive Skewness = 6')
```



The result of the plot can be visualized as below:



Notebook for exploration:

* **65-skewness.py**

Skewness tells us where most data is hiding.
Useful when averages lie,
like when a few rich folks mess up the "_average income_".

#### Scaled Skewness

Statistically speaking,
it's not fair to compare plots,
when one is shouting and the other's whispering.
The actual of skewness has different height.
For simplicity we can scale so that,
the height looks visually the same.
Let’s level the playing field.

* **65-skewness-same-height.py**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm, norm, kurtosis

# Generate data points for x-axis
x = np.linspace(-5, 5, 1000)

# Calculate the corresponding y-values
# for the standard normal distribution
y_standard = norm.pdf(x)

# Calculate the maximum height
# of the standard normal distribution
max_height_standard = np.max(y_standard)

# Calculate the corresponding y-values 
# or distributions with different skewness parameters
# Examples of skewed distributions
# with different skewness parameters

# Negative skewness
y_skewed_1 = skewnorm.pdf(x, a=-4)

# Moderate positive skewness
y_skewed_2 = skewnorm.pdf(x, a=2)

# High positive skewness
y_skewed_3 = skewnorm.pdf(x, a=6)

# Scale the skewed distributions
# to have the same maximum height
# as the standard normal distribution
y_skewed_1_scaled = y_skewed_1 \
  / np.max(y_skewed_1) * max_height_standard
y_skewed_2_scaled = y_skewed_2 \
  / np.max(y_skewed_2) * max_height_standard
y_skewed_3_scaled = y_skewed_3 \
  / np.max(y_skewed_3) * max_height_standard

# Plot the normal distribution
plt.plot(x, y_standard, label='Standard Normal')

# Plot skewed distributions
# with different skewness parameters
plt.plot(x, y_skewed_1_scaled, ls='--',
         label='Negative Skewness = -4')
plt.plot(x, y_skewed_2_scaled, ls='--',
         label='Moderate Positive Skewness = 2')
plt.plot(x, y_skewed_3_scaled, ls='--',
         label='High Positive Skewness = 6')

# Add labels and title
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Normal Distribution '
 + 'with Different Skewness')

# Add legend on the top left
plt.legend(loc='upper left')

# Show grid
plt.grid(True)

# Show plot
plt.show()
```

Explanation

We'll scale the skewed curves to match the standard normal’s peak height:
Set the skewed distributions
to have the same maximum height
as the standard normal distribution.
This way we can compare better.

```python
max_height_standard = np.max(y_standard)

y_skewed_1_scaled = y_skewed_1 \
  / np.max(y_skewed_1) * max_height_standard
y_skewed_2_scaled = y_skewed_2 \
  / np.max(y_skewed_2) * max_height_standard
y_skewed_3_scaled = y_skewed_3 \
  / np.max(y_skewed_3) * max_height_standard
```



The result of the plot can be visualized as below:



Notebook available here:

* **65-skewness-height.py**

When comparing shapes,
height shouldn't distract from symmetry (or the lack thereof).
Scaling gives a fair visual comparison.

-- -- --

### What's the Next Chapter 🤔?

There are also common properties for statistics not related with trend.
In trend context let's call them additional properties.
This properties is important for other statistics analysis.

Distribution is just the appetizer.
Now that we know how the data looks,
we're ready to inspect some behind-the-scenes properties,
that aren't directly about trendlines, but still impact analysis.

Up next: **Trend - Properties - Additional**
Because even statistics have bonus features.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Exploring additional statistic properties
> not related to trend.

While trends often hog the spotlight in data analysis
(they're the drama queens of statistics),
some lesser, known side characters, like variance, standard deviation, and friends,
play quietly in the background and actually hold the story together.

In the context of trends,
we'll call these additional properties.
They may not tell you where the data is going,
but they do whisper whether it's marching in a straight line,
or chaotically dancing like it's data prom night.

And here's why it matters:
Before we strap our statistical properties onto a machine-learning rocket,
and launch it into our app,
we should first test them with a solid mathematical model.
Because if our code outputs nonsense,
the issue might not be your coding,
it could be that our math is drunk.

we can model these properties in a spreadsheet.
Yes, Excel isn't just for budget planning or tracking,
who borrowed your flash drive in 2012.
But before that, let's make sure we understand the math that powers the formulas.
Trust me: understanding the math is like reading the manual,
before assembling IKEA furniture.
Sure, it's optional. But do you really want three leftover screws?

Stay tuned, this isn't just academic.
These properties will sneak their way,
into nearly every corner of statistical analysis,
from A/B testing to anomaly detection.
Ignore them at our peril (or worse, our boss’s angry emails).

-- -- --

### Equation

The trend might be the star of the show,
but these supporting characters often steal the scene.
Now that we've left the trend spotlight,
it's time to meet the less glamorous,
but just as critical, statistical properties.
Think of them as the data janitors,
quiet, consistent, and the reason the whole system doesn't fall apart.

Let's start laying down the symbolic groundwork.
Yes, it's math time. But the kind of math that makes you look really smart in meetings.
We begin with equation symbol, as our base of calculation.

#### Min, Max, Range

> The Bounds of Data Dignity

Obvious, yes. But still foundational. Like socks.
They don’t get attention unless missing.

$$
\begin{align*}
&& \text{min} &= \min(x_1, x_2, \ldots, x_n) \\
&& \text{max} &= \max(x_1, x_2, \ldots, x_n) \\
&& \text{range} &= \text{max} - \text{min} \\
\end{align*}
$$

Set-theoretically speaking,
the `max` function can be express in set notation:

$$
\text{max}(x_i) = \{ x \in x_i \mid x \text{ is the largest element in } x_i \}
$$

Pretty explanatory

Range gives us the first glance at data spread.
A huge range might signal outliers,
or just a sensor gone rogue.

#### Median

> The Middle Manager of Our Data

No favoritism here,
median doesn't care about how wild the numbers are,
just who's in the middle.
The median can be described as below:

$$
Md_x = 
\begin{cases}
x_{\frac{n+1}{2}} & \text{if } n \text{ is odd} \\
\frac{x_{\frac{n}{2}} + x_{\frac{n}{2}+1}}{2} & \text{if } n \text{ is even}
\end{cases}
$$

Median resists drama.
It stays cool even if our data includes a billionaire or a zero-dollar bank account.

#### Mode

> Popularity Contest Winner

The most frequently appearing value.
The celebrity of the dataset.

We need two steps to find the modus.
First we have to find frequencies,
then find the maximum frequencies,
and finally get the value of that frequencies.

To find the frequencies of each unique value in a dataset,
where I() is the indicator function,
which equals 1 if the condition is true and 0 otherwise.

> Step 1: Count how many times each value shows up.

$$
f_i = \sum_{j=1}^{n} I(x_j = x_i)
$$

> Step 2: Find the biggest fanbase

Then we find the maximum frequency.

$$
f_{max} = \max\{f_1, f_2, \ldots, f_k\}
$$​

Or in the set notation as:

$$
f_{max}​={f_i​∈{f_1​,f_2​,…,f_k​}∣f_i​ \text{ is the largest element in } {f_1​,f_2​,…,f_k​}}
$$​

> Final step: identify the actual winner(s).

Mathematically, we would find the mode value​ using this equation:

$$
Mo_x = \{ x_i \mid f_i = f_{max} \}
$$​

Or if you're a fan of compact "_math-as-a-one-liner_" expressions:

$$
x_{mode} = \{ x_i \mid f_i = \max\{ \sum_{j=1}^{n} [x_j = x_i] \} \}
$$​

If our dataset were a party,
the mode is the person everyone's talking to.
Important for understanding dominant categories.

#### SEM (Standard Error of the Mean)

> The Nervousness of the Mean

Think of the Standard Error of the Mean (SEM) as our data's social anxiety.
It tells us how much the mean might fluctuate with different samples.

The equation for SEM is:

$$
SEM = \frac{s}{\sqrt{n}}
$$​

Smaller SEM means more confidence in our average.
Larger SEM? Time to re-evaluate our sampling or our life choices.

#### Kurtosis and Skewness

> The Drama Analysts

These two detect asymmetry and "_peakedness_."
Skewness checks if our data is leaning left or right.
Kurtosis checks if it's just chill or obsessively spiky.

The Standard Error equation for both Kurtosis and Skewness can be tricky,
and can be differ from one reference to another.

$$
\begin{align*}
&& \text{Kurtosis} &= \frac{\sum_{i=1}^{n}(x_i - \bar{x})^4}{n \cdot s^4} - 3 \\
&& \text{Skewness} &= \frac{\sum_{i=1}^{n}(x_i - \bar{x})^3}{n \cdot s^3} \\
\end{align*}
$$

These moments (third and fourth) help assess normality.
If skewness or kurtosis are off the charts,
so is our assumption of normal distribution.

#### Standard Error of Kurtosis and Skewness

> Measuring Your Measurement's Wobble

Here's where things get spicy.
There's more than one way to calculate these.

> Simplified approximations:

The simplified approximation of Standard Error can be expressed as below:

$$
\begin{align*}
&& SE_k &= \sqrt{\frac{24}{(n-1)}} \\
&& SE_s &= \sqrt{\frac{6}{(n-1)}} \\
\end{align*}
$$

> Fancy-pants formulas:

While the complex Standard Error equation can be described as follows:

$$
\begin{align*}
&& SE_k &= \sqrt{\frac{24n(n-2)(n-3)}{(n+1)(n+3)(n-1)^2}} \\
&& SE_s &= \sqrt{\frac{6n(n-1)}{(n-2)(n+1)(n+3)}} \\
\end{align*}
$$

> From StackOverflow ???

From stackoverflow I found out that,
on different software the equation of Standard Error of gaussian kurtosis,
can be expressed as follows.

$$
SE_k = \sqrt{\frac{4(n^2-1) \times SE_s^2}{(n-3)(n+5)}}
$$

Thanks to Howard Seltman,
whose R script taught my spreadsheet to do calculus after midnight:
I'm simply copying and pasting the code from here:

* [spssSkewKurtosis.R](http://www.stat.cmu.edu/~hseltman/files/spssSkewKurtosis.R)

Note that above equation only applied for data that follow gaussian distribution.

Standard errors help us understand,
whether our skewness or kurtosis values are meaningful,
or just statistical noise dressed in fancy math.

-- -- --

### Spreadsheet Sorcery

> Statistics at Your Fingertips

_A brief tale of numbers, built-in functions, and spreadsheet wizardry_.

I have already prepare the built in formula for these statistics properties.

#### Worksheet Source

> The Magical Artefact

🧙 "_Behold, the Spreadsheet of Secrets!_"

The Excel file has been forged and uploaded.
Tinker, test, or tear it apart.
We're holding a fully functional statistical toolbox:
 
* 📎 **github.com/.../math/trend/examples-properties.ods**

#### Min, Max, Range

> The Big Three

We begin with the three musketeers of statistical bounds: minimum, maximum, and range.
They help define the battlefield.
Telling us how far our data stretches.
Range might not be sophisticated, but it's honest and loud.

The formula is also obvious.



These simple formulas can be summarized as follows:

| properties              | formula                          |
| ----------------------- | -------------------------------- |
| x min                   |  =MIN(x_sample)                  |
| y min                   |  =MIN(y_sample)                  |
| x max                   |  =MAX(x_sample)                  |
| y max                   |  =MAX(y_sample)                  |
| x range                 |  =MAX(x_sample)-MIN(x_sample)    |
| y range                 |  =MAX(y_sample)-MIN(y_sample)    |

If our range is zero, either oour data is broken,
or we’ve got a perfect flatline.
Call a doctor or a mathematician

#### Median and Mode

> The Democratic Center and the Popular Vote

_When mean feels too mainstream._

Median resists outliers like a grumpy old professor ignoring student trends.
Mode, on the other hand, is all about popularity, if it exists.

But here’s the catch:
For datasets with all unique values,
mode politely declines to show up,
giving us a `#VALUE!` instead.
Think of it as statistics saying "_I don’t do groupies._"

We can use built-in `median()` formula.
But we should be careful while i uderstanding the `mode()` formula.
For example for a completely unique data series,
the result should be no mode, because all data frequency is 1.
Then our beloved spreadsheet is right to give error as `#VALUE1`.

To fix this, use a helper column (e.g., x_freq),
then channel our inner Excel sage.
The solution is make a new helper column to calculate frequency.
Let's name the range as `x_freq` and `y_freq`,
and we can use our excel/calc expertise to craft this formula:

```excel
=INDEX(y_sample, MATCH(MAX(y_freq), y_freq, 0))
```

Voilà!.
Manual mode detection, spreadsheet-style.

The summary can be described as follows:



| properties              | formula                                            |
| ----------------------- | -------------------------------------------------- |
| x median                |  =MEDIAN(x_sample)                                 |
| y median                |  =MEDIAN(y_sample)                                 |
| x mode                  |  =MODE(x_sample)                                   |
| y mode                  |  =MODE(y_sample)                                   |
| x mode (alternative)    |  =INDEX(x_sample, MATCH(MAX(x_freq), x_freq, 0))   |
| y mode (alternative)    |  =INDEX(y_sample, MATCH(MAX(y_freq), y_freq, 0))   |
| x SE Mean               |  =STDEV.S(x_sample) / SQRT(COUNT(x_sample))        |
| y SE Mean               |  =STDEV.S(y_sample) / SQRT(COUNT(y_sample))        |

#### Kurtosis and Skewness

> The Drama Queens of Distribution

_When our data has a mood._

Skewness shows asymmetry, how lopsided your data is.
Kurtosis checks whether our data is heavy-tailed (peaky) or chill (flat).
It's like asking: is our dataset more like,
a volcano, a pancake, or somewhere in between?

Excel gives us `KURT()` and `SKEW()` to play with.
But for the error bars (standard error),
we will have to roll up our sleeves.
Unfortunately no built-in formula for standard error.
With equation above, we can craft our SE formula as follows:



| properties              | formula                                            |
| ----------------------- | -------------------------------------------------- |
| x kurtosis              |  =KURT(x_sample)                                   |
| y kurtosis              |  =KURT(y_sample)                                   |
| x skewness              |  =SKEW(x_sample)                                   |
| y skewness              |  =SKEW(y_sample)                                   |
| n                       |  =COUNT(x_sample)                                  |
| SE kurtosis             |  =SQRT((24*(n*(n-2)*(n-3)))/((n+1)*(n+3)*(n-1)^2)) | 
| SE skewness             |  =SQRT((6*n*(n-1))/((n-2)*(n+1)*(n+3)))            |
| SE kurtosis (gaussian)  |  =SQRT(4*(n^2-1)*SE_s^2/((n-3)*(n+5))              |

When Excel doesn't have the function we need,
we become the function.
It's like statistical DIY,
but with more square roots and fewer splinters.

It is fun to play with these two properties,
if you understand the concept.
We will also give you the visualization in this article.

#### A Word About Outliers

> We love them, we fear them.

Outliers are the eccentrics of the dataset,
possibly geniuses, possibly errors.
We will give them their own stage in another article,
because like all rebels, they deserve their spotlight.

-- -- --

### Python Tools

> Oonce we've got the average, the real fun begins.

Welcome to the second half of our statistical makeover session,
this time with Python as our glamorous assistant.
We're diving into those less-talked-about but absolutely vital properties:
median, mode, range, skewness, and kurtosis.
Think of them as the supporting actors who steal the show,
if the mean ever calls in sick.

#### Python Source

You don't have to reinvent the bell curve,
just clone the script:

* **61-additional.py**

```python
import numpy as np
import statistics

from scipy.stats import kurtosis, skew

# Getting Matrix Values
pairCSV = np.genfromtxt("50-samples.csv",
  skip_header=1, delimiter=",", dtype=int)

# Extract x and y values from CSV data
x_observed = pairCSV[:, 0]
y_observed = pairCSV[:, 1]

# Number of data points
n = len(x_observed)

# Calculate maximum, minimum, and range
x_max = np.max(x_observed)
x_min = np.min(x_observed)
x_range = x_max - x_min

y_max = np.max(y_observed)
y_min = np.min(y_observed)
y_range = y_max - y_min

# Output of maximum, minimum, and range
print('x (max, min, range) = '
 + f'({x_min:7.2f}, {x_max:7.2f}, {x_range:7.2f} )')
print('y (max, min, range) = '
 + f'({y_min:7.2f}, {y_max:7.2f}, {y_range:7.2f} )')
print()

def calc_median(data: np.array) -> float:
  # Sort the data
  sorted_data = np.sort(data)

  # Calculate the median
  n = len(sorted_data)
  if n % 2 == 1:
    # If odd number of data points
    median = sorted_data[n // 2]
  else:
    # If even number of data points
    median = (sorted_data[n // 2 - 1] \
           +  sorted_data[n // 2]) / 2
  
  return median

# Calculate additional propeties
x_median = calc_median(x_observed)
y_median = calc_median(y_observed)

x_mode = statistics.mode(x_observed)
y_mode = statistics.mode(y_observed)

# Output of additional propeties
print(f'x median       = {x_median:9.2f}')
print(f'y median       = {y_median:9.2f}')
print(f'x mode         = {x_mode:9.2f}')
print(f'y mode         = {y_mode:9.2f}')
print()

def calc_se_kurtosis(n):
  return np.sqrt( \
    (24 * n * (n - 2) * (n - 3)) \
    / ((n + 1) * (n + 3) * (n - 1) ** 2))

def calc_se_skewness(n):
  return np.sqrt( \
    (6 * n * (n - 1)) \
    / ((n - 2) * (n + 1) * (n + 3)))

def calc_se_kurtosis_gaussian(n):
  return np.sqrt( \
    (4 * n**2 * calc_se_skewness(n)**2) \
    / ((n - 3) * (n + 5)))

# Calculate kurtosis and skewness
x_kurtosis = kurtosis(x_observed, bias=False)
y_kurtosis = kurtosis(y_observed, bias=False)

x_skewness = skew(x_observed, bias=False)
y_skewness = skew(y_observed, bias=False)

print(f'x kurtosis     = {x_kurtosis:9.2f}')
print(f'y kurtosis     = {y_kurtosis:9.2f}')
print(f'x skewness     = {x_skewness:9.2f}')
print(f'y skewness     = {y_skewness:9.2f}')
print()

# number of data points
x_n = len(x_observed)
y_n = len(y_observed)

# Calculate SE kurtosis and SE skewness
x_se_kurtosis = calc_se_kurtosis_gaussian(x_n)
y_se_kurtosis = calc_se_kurtosis_gaussian(y_n)
x_se_skewness = calc_se_skewness(x_n)
y_se_skewness = calc_se_skewness(y_n)

print(f'x SE kurtosis  = {x_se_kurtosis:9.2f}')
print(f'y SE kurtosis  = {y_se_kurtosis:9.2f}')
print(f'x SE skewness  = {x_se_skewness:9.2f}')
print(f'y SE skewness  = {y_se_skewness:9.2f}')
print()
```

#### Data Source

No hardcoding here. We like our data fresh and CSV-flavored:

* **50-samples.csv**:

```csv
x,y
0,5
1,12
2,25
3,44
4,69
5,100
6,137
7,180
8,229
9,284
10,345
11,412
12,485
```

#### Min, Max, Range

Like in any good soap opera,
it's all about the highs and lows,
and the emotional distance in between.

```python
import numpy as np

# Getting Matrix Values
pairCSV = np.genfromtxt("50-samples.csv",
  skip_header=1, delimiter=",", dtype=int)

# Extract x and y values from CSV data
x_observed = pairCSV[:, 0]
y_observed = pairCSV[:, 1]

# Number of data points
n = len(x_observed)
```



We can calculate

```python
# Calculate maximum, minimum, and range
x_max = np.max(x_observed)
x_min = np.min(x_observed)
x_range = x_max - x_min

y_max = np.max(y_observed)
y_min = np.min(y_observed)
y_range = y_max - y_min

# Output of maximum, minimum, and range
print('x (max, min, range) = '
 + f'({x_min:7.2f}, {x_max:7.2f}, {x_range:7.2f} )')
print('y (max, min, range) = '
 + f'({y_min:7.2f}, {y_max:7.2f}, {y_range:7.2f} )')
print()
```



Min, max, and range help us understand the battlefield.
How wide is the spread\
Are we talking table tennis or intergalactic warfare?

#### Median and Mode

If the mean is a people-pleaser,
the median is the unbothered introvert,
and the mode is... 
the popular kid who may or may not exist.

We can find mode using `statistics` library.

```python
import statistics

x_mode = statistics.mode(x_observed)
y_mode = statistics.mode(y_observed)
```

But Python isn't always diplomatic.
If there’s no repeating value, `statistics.mode()` might throw a tantrum (i.e., raise an error).
So here’s a DIY method to calculate median:

We can implement above equation to find median:

```python
def calc_median(data: np.array) -> float:
  # Sort the data
  sorted_data = np.sort(data)

  # Calculate the median
  n = len(sorted_data)
  if n % 2 == 1:
    # If odd number of data points
    median = sorted_data[n // 2]
  else:
    # If even number of data points
    median = (sorted_data[n // 2 - 1] \
           +  sorted_data[n // 2]) / 2
  
  return median
```



And display.

```python
# Calculate additional propeties
x_median = calc_median(x_observed)
y_median = calc_median(y_observed)

x_mode = statistics.mode(x_observed)
y_mode = statistics.mode(y_observed)

# Output of additional propeties
print(f'x median       = {x_median:9.2f}')
print(f'y median       = {y_median:9.2f}')
print(f'x mode         = {x_mode:9.2f}')
print(f'y mode         = {y_mode:9.2f}')
print()
```



Pro tip for rebels: we can also utilize.

```python
y_mode = np.argmax(np.bincount(y_observed))
```

This bypasses `statistics.mode()`’s sensitivities.
You're welcome.

Median is robust against outliers.
Mode? Great for categorical or oddly-behaved data.
Know our tools before we wield them.

#### Kurtosis and Skewness

Because data can be weird, lopsided, and prone to drama.
Enter `scipy.stat` to calculate `kurtosis` and `skewness`.

```python
from scipy.stats import kurtosis, skew

# Calculate kurtosis and skewness
x_kurtosis = kurtosis(x_observed, bias=False)
y_kurtosis = kurtosis(y_observed, bias=False)

x_skewness = skew(x_observed, bias=False)
y_skewness = skew(y_observed, bias=False)

print(f'x kurtosis     = {x_kurtosis:9.2f}')
print(f'y kurtosis     = {y_kurtosis:9.2f}')
print(f'x skewness     = {x_skewness:9.2f}')
print(f'y skewness     = {y_skewness:9.2f}')
print()
```



Skewness tells us if our data leans left, right, or politically neutral.
Kurtosis tells us whether the tails are drama queens or chill.

#### Standard Error of Kurtosis and Skewness

We should craft our own method to get the standard errors.

```python
def calc_se_kurtosis(n):
  return np.sqrt( \
    (24 * n * (n - 2) * (n - 3)) \
    / ((n + 1) * (n + 3) * (n - 1) ** 2))

def calc_se_skewness(n):
  return np.sqrt( \
    (6 * n * (n - 1)) \
    / ((n - 2) * (n + 1) * (n + 3)))

def calc_se_kurtosis_gaussian(n):
  return np.sqrt( \
    (4 * n**2 * calc_se_skewness(n)**2) \
    / ((n - 3) * (n + 5)))
```



Now deploy those formulas like a well-trained stats ninja:

```python
# number of data points
x_n = len(x_observed)
y_n = len(y_observed)

# Calculate SE kurtosis and SE skewness
x_se_kurtosis = calc_se_kurtosis_gaussian(x_n)
y_se_kurtosis = calc_se_kurtosis_gaussian(y_n)
x_se_skewness = calc_se_skewness(x_n)
y_se_skewness = calc_se_skewness(y_n)

print(f'x SE kurtosis  = {x_se_kurtosis:9.2f}')
print(f'y SE kurtosis  = {y_se_kurtosis:9.2f}')
print(f'x SE skewness  = {x_se_skewness:9.2f}')
print(f'y SE skewness  = {y_se_skewness:9.2f}')
print()
```



Without standard errors,
we’re just guessing in a lab coat.
These formulas help us tell signal from noise,
and wisdom from nonsense.

#### Output Result

Just like we practiced,
here's what it looks like when the numbers come home from school:

```output
x (max, min, range) = (   0.00,   12.00,   12.00 )
y (max, min, range) = (   5.00,  485.00,  480.00 )

x median       =      6.00
y median       =    137.00
x mode         =      0.00
y mode         =      5.00

x kurtosis     =     -1.20
y kurtosis     =     -0.73
x skewness     =      0.00
y skewness     =      0.70

x SE kurtosis  =      1.19
y SE kurtosis  =      1.19
x SE skewness  =      0.62
y SE skewness  =      0.62
```



📈 Translation:

* Our x data is symmetrical and well-behaved—basically a textbook student.
* y is a little skewed and platykurtic (a fancy way of saying it’s allergic to drama).
* But nothing’s too wild. Standard errors confirm: we’re in safe territory.

#### Interactive JupyterLab

Want to poke and prod these stats like a true data scientist?
Try it live:

* **61-additional.py**

-- -- --

### Properties Visualization

> Visualizing Descriptive Stats Like a Statistician With a Paintbrush

Welcome to the part where statistics come alive.
Not just as numbers in a table, but as glorious visualizations.
Think of this as the "Instagram filter" phase of our dataset.
We’re going to draw lines, plot curves,
and throw some color around like a statistician in art school.

Let's turn those abstract stat properties into actual plots.
Python and matplotlib are our brushes.
Our dataset is the canvas. Picasso would approve.

#### Min, Max, Range, Median and Mode

We'll begin by scattering the important descriptive stats.
But horizontally, like a minimalist's bookshelf.

* **62-plot.py**

```python
import numpy as np
import matplotlib.pyplot as plt

# Getting Matrix Values
pairCSV = np.genfromtxt("50-samples.csv",
  skip_header=1, delimiter=",", dtype=int)

# Extract x and y values from CSV data
x_observed = pairCSV[:, 0]
y_observed = pairCSV[:, 1]

# Calculate properties
y_median = np.median(y_observed)
y_mean   = np.mean(y_observed)
y_min    = np.min(y_observed)
y_max    = np.max(y_observed)

# Calculate mode using numpy
y_mode   = np.argmax(np.bincount(y_observed))

# Plot x,y scatter plot
plt.scatter(x_observed, y_observed,
  color='blue', label='Data')

# Add horizontal lines for properties
plt.axhline(y_median, c='r', ls='--',
  label=f'Median: {y_median}')
plt.axhline(y_mean,   c='g', ls='--',
  label=f'Mean: {y_mean:.2f}')
plt.axhline(y_mode,   c='m', ls='--',
  label=f'Mode: {y_mode}')
plt.axhline(y_min,    c='c', ls='--',
  label=f'Min: {y_min}')
plt.axhline(y_max,    c='y', ls='--',
  label=f'Max: {y_max}')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot with Y-axis Properties')
plt.legend()

# Show plot
plt.grid(True)
plt.show()
```

Explanation

```python
# Add horizontal lines for properties
plt.axhline(y_median, c='r', ls='--',
  label=f'Median: {y_median}')
plt.axhline(y_mean,   c='g', ls='--',
  label=f'Mean: {y_mean:.2f}')
plt.axhline(y_mode,   c='m', ls='--',
  label=f'Mode: {y_mode}')
plt.axhline(y_min,    c='c', ls='--',
  label=f'Min: {y_min}')
plt.axhline(y_max,    c='y', ls='--',
  label=f'Max: {y_max}')
```



The result of the plot can be visualized as below:



Try it yourself:

* **62-plot.py**

These lines help us see where our data hangs out.
Is the mean close to the median?
Is the mode just photobombing?
Horizontal stats lines = instant data vibes.

#### Histogram and Distribution Curve

Time to check how our data is distributed.
A histogram shows the crowd,
while the curve shows how it's supposed to behave,
in an ideal world. Spoiler: it rarely does.

You can create a histogram,
and overlay a normal distribution curve on top of it.

* **66-plot-normal.py**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Getting Matrix Values
pairCSV = np.genfromtxt("50-samples.csv",
  skip_header=1, delimiter=",", dtype=int)

# Extract x and y values from CSV data
x_observed = pairCSV[:, 0]
y_observed = pairCSV[:, 1]

# Calculate mean and standard deviation of y
y_mean = np.mean(y_observed)
y_std  = np.std(y_observed)

# Calculate skewness and kurtosis of y
y_skewness = np.mean(
  ((y_observed - y_mean) / y_std) ** 3)
y_kurtosis = np.mean(
  ((y_observed - y_mean) / y_std) ** 4)

# Create histogram
plt.hist(y_observed, bins=10,
  density=True, alpha=0.6, color='cyan')

# Create range for x values
x_range = np.linspace(
  min(y_observed), max(y_observed), 100)

y_dist = norm.pdf(x_range, y_mean, y_std)

# Plot normal distribution curve
plt.plot(x_range, y_dist, color='blue',
  label='Normal Distribution')

plt.xlabel('y')
plt.ylabel('Density')
plt.title('Normal Distribution Plot of '
  + 'Observed y with Skewness and Kurtosis')
plt.legend()
plt.grid(True)
plt.show()
```

Explanation

```python
# Calculate skewness and kurtosis of y
y_skewness = np.mean(
  ((y_observed - y_mean) / y_std) ** 3)
y_kurtosis = np.mean(
  ((y_observed - y_mean) / y_std) ** 4)

# Create histogram
plt.hist(y_observed, bins=10,
  density=True, alpha=0.6, color='cyan')

# Create range for x values
x_range = np.linspace(
  min(y_observed), max(y_observed), 100)

y_dist = norm.pdf(x_range, y_mean, y_std)

# Plot normal distribution curve
plt.plot(x_range, y_dist, color='blue',
  label='Normal Distribution')
```



The result of the plot can be visualized as below:



You can obtain the interactive `JupyterLab` in this following link:

* **66-plot-normal.py**

Histograms show real data.
The curve? That's the stat professor's dream.
The comparison tells us how rebellious our data is.

#### Revisited: Min, Max, Range, Median and Mode

Same plot party,
but now we flip everything 90 degrees.
Using scatter plot we can put the statistic properties,
but this time in vertical line.

* **68-plot-props.py**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, skewnorm

pairCSV = np.genfromtxt("50-samples.csv",
  skip_header=1, delimiter=",", dtype=int)

# Extract x and y values from CSV data
x_observed = pairCSV[:, 0]
y_observed = pairCSV[:, 1]

# Calculate mean and standard deviation of y
y_mean = np.mean(y_observed)
y_std  = np.std(y_observed)

# Calculate skewness and kurtosis of y
y_skewness = 0.61
y_kurtosis = -0.91

# Create histogram
plt.hist(y_observed, bins=10,
  density=True, alpha=0.6, color='cyan')

# Plot normal distribution curve
x_range = np.linspace(
  min(y_observed), max(y_observed), 1000)
y_standard = norm.pdf(x_range, y_mean, y_std)
plt.plot(x_range, y_standard,
  label='Standard Normal')

# Plot vertical lines
# or add annotations for properties
y_median = np.median(y_observed)
y_mean   = np.mean(y_observed)
y_min    = min(y_observed)
y_max    = max(y_observed)

# Calculate mode using numpy
y_mode = np.argmax(np.bincount(y_observed))

# Add vertical lines for properties
plt.axvline(y_median, c='r', ls='--',
  label=f'Median: {y_median}')
plt.axvline(y_mean,   c='g', ls='--',
  label=f'Mean: {y_mean:.2f}')
plt.axvline(y_mode,   c='m', ls='--',
  label=f'Mode: {y_mode}')
plt.axvline(y_min,    c='c', ls='--',
  label=f'Min: {y_min}')
plt.axvline(y_max,    c='y', ls='--',
  label=f'Max: {y_max}')

# Add labels and title
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Normal Distribution '
  + 'with Y-axis Properties')
plt.legend()

# Show grid
plt.grid(True)

# Show plot
plt.show()
```

Explanation

```python
# Add vertical lines for properties
plt.axvline(y_median, c='r', ls='--',
  label=f'Median: {y_median}')
plt.axvline(y_mean,   c='g', ls='--',
  label=f'Mean: {y_mean:.2f}')
plt.axvline(y_mode,   c='m', ls='--',
  label=f'Mode: {y_mode}')
plt.axvline(y_min,    c='c', ls='--',
  label=f'Min: {y_min}')
plt.axvline(y_max,    c='y', ls='--',
  label=f'Max: {y_max}')
```



The result of the plot can be visualized as below:



You can obtain the interactive `JupyterLab` in this following link:

* **68-plot-props.py**

#### Kurtosis and Skewness

Want to really see what tailedness and tiltedness look like?
This is the grand performance.
Yes, it's experimental.
Yes, it's beautiful.
No, I still don't fully understand the shape parameter.

With histogram, we can also overlay a distribution curve,
with applied kurtosis and skewness.

* **67-plot-ks.py**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, skewnorm

pairCSV = np.genfromtxt("50-samples.csv",
  skip_header=1, delimiter=",", dtype=int)

# Extract x and y values from CSV data
x_observed = pairCSV[:, 0]
y_observed = pairCSV[:, 1]

# Calculate mean and standard deviation of y
y_mean = np.mean(y_observed)
y_std  = np.std(y_observed)

# Create histogram
plt.hist(y_observed, bins=10,
  density=True, alpha=0.6, color='cyan')

# Define skewness and kurtosis values
y_skewness = 0.61
y_kurtosis = -0.91

# Create range for x values
x_range = np.linspace(
  min(y_observed), max(y_observed), 100)

# Calculate the corresponding y-values
# for the standard normal distribution
y_standard = norm.pdf(x_range, y_mean, y_std)

# Adjust the shape parameter manually
# to achieve the desired kurtosis
# You may need to experiment with different values
# to get closer to the desired kurtosis
shape_param = 4

# Calculate the corresponding y-values
# for skewnorm distribution with given skewness
# and adjusted shape parameter
y_ks = skewnorm.pdf(x_range, a=y_skewness,
  loc=y_mean, scale=y_std / shape_param)

# Plot normal distribution curve
plt.plot(x_range, y_standard,
  label='Standard Normal')

# Plot skewnorm distribution
# with given skewness and kurtosis
plt.plot(x_range, y_ks, ls='-.',
  label='With Kurtosis and Skewness')

# Add labels and title
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Normal Distribution '
  + 'with Kurtosis and Skewness')

# Add legend
plt.legend()

# Show grid
plt.grid(True)

# Show plot
plt.show()
```

Explanation

First we need to calculate the corresponding y-values
for the standard normal distribution.
Then we need to adjust the shape parameter manually
to achieve the desired kurtosis
We may need to experiment with different values
to get closer to the desired kurtosis.
Then calculate the corresponding y-values
for skewnorm distribution with given skewness
and adjusted shape parameter.
Finally plot both normal distribution curve,
and skewnorm distribution.

```python
y_standard = norm.pdf(x_range, y_mean, y_std)

shape_param = 2

y_ks = skewnorm.pdf(x_range, a=y_skewness,
  loc=y_mean, scale=y_std / shape_param)

plt.plot(x_range, y_standard,
  label='Standard Normal')

plt.plot(x_range, y_ks, ls='-.',
  label='With Kurtosis and Skewness')
```



The result of the plot can be visualized as below:



You can obtain the interactive `JupyterLab` in this following link:

* **67-plot-ks.py**

Actually, I'm not sure if I get the visual right.
I still don't know how this shape parameter works.
I may have plotted something artistic instead of accurate.
If your plot starts to resemble abstract art,
please consult your local statistician.
Especially one who's into distribution curves.

#### Density with Seaborne

> Pretty Matters

Let's end with dessert.
Seaborn gives us plots so pretty they could be wall art.
It combines histogram, KDE, and rug plot into a beautiful statistical parfait.
Seaborne can make a really pretty chart.

* **69-sns.py**

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

pairCSV = np.genfromtxt("50-samples.csv",
  skip_header=1, delimiter=",", dtype=int)

# Extract x and y values from CSV data
x_observed = pairCSV[:, 0]
y_observed = pairCSV[:, 1]

# Calculate skewness and kurtosis of y
y_skew     = skew(y_observed)
y_kurtosis = kurtosis(y_observed)

# Plot distribution of y with annotations
sns.set(style="whitegrid")
sns.displot(y_observed,
  bins=10, kde=True, rug=True)

# Annotate skewness and kurtosis on the plot
plt.text(0.9, 0.9,
  f'Skewness = {y_skew:.2f}',
  ha='center', va='center',
  transform=plt.gca().transAxes)
plt.text(0.9, 0.8,
  f'Kurtosis = {y_kurtosis:.2f}',
  ha='center', va='center',
  transform=plt.gca().transAxes)

plt.xlabel('y')
plt.ylabel('Density')
plt.title('Distribution of Observed y '
  + 'with Skewness and Kurtosis')
plt.show()
```

Explanation

```python
# Plot distribution of y with annotations
sns.set(style="whitegrid")
sns.displot(y_observed,
  bins=10, kde=True, rug=True)
```



The result of the plot can be visualized as below:



You can obtain the interactive `JupyterLab` in this following link:

* **69-sns.py**

Clean, informative, beautiful. All in one plot.
Like the pie chart's cooler cousin who went to design school.

-- -- --

### What's the Next Chapter 🤔?

> A brief intermission before the next scatterplot.

So far, matplotlib has been like that trusty old wrench.
Reliable, precise, and a bit clunky when it comes to aesthetics.
It gets the job done, but sometimes, you want more... pizzazz.

Enter Seaborn, the statistics nerd's favorite artist.
Think of it as matplotlib after a makeover,
easier to use, and with a deep love for statistical plots.

We're about to crank up the visuals again,
this time with Seaborn's pre-built plots designed for statistics.
It's like switching from hand-tooling our car to,
using a diagnostic scanner with a touchscreen.
Same insights, way more fun.

Great visualization tools reduce friction.
Less time tweaking, more time interpreting.
Or sipping our coffee while the plot impresses the team.

So buckle up, because the next chapter will unlock even prettier,
more intuitive ways to visualize our dataset's story.
And don't forget, seaborn library is specifically made for statistics.

When we're feeling ready to evolve,
from matplotlib sketches to Seaborn artistry, head on over to:
🔗 **Trend - Visualization - Seaborn**.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Pretty statistics visualization with Seaborn,
> equipped with example script for each plots.

Let's face it: plotting raw numbers in `matplotlib` is,
like eating plain oatmeal. Nutritious but a little… bland.
Enter Seaborn, the library that dresses our data in a tuxedo,
adds a spotlight, and whispers the punchline for you.

In this article, we will find ready-to-run example scripts for each plot.
No tedious step-by-step handholding
(the internet’s already brimming with tutorials).
Our mission is to showcase what Seaborn can do for our statistical properties,
so we can spend less time wrestling with code,
and more time interpreting elegant visuals.

Remember: real-world data rarely stays neat and tidy.
These are simple demos, consider them our rehearsal dinner before the big data wedding.
Now, grab our favorite beverage and let's our Seaborn’s stat-smarts in action.


-- -- --

### Visualizing Linear Regression

Yes, we are still talking about trend,
now with Seaborn.

#### Data Series

Instead of just one series,
we'll play with these three: `ys₁`, `ys₂`, or `ys₃`.
That way we can compare how different curves behave side by side.

```csv
xs, ys1, ys2, ys3
0,  5,   5,   5
1,  9,   12,  14
2,  13,  25,  41
3,  17,  44,  98
4,  21,  69,  197
5,  25,  100, 350
6,  29,  137, 569
7,  33,  180, 866
8,  37,  229, 1253
9,  41,  284, 1742
10, 45,  345, 2345
11, 49,  412, 3074
12, 53,  485, 3941
```

* **series.csv**



Comparing multiple series in one plot helps us,
see at a glance which trendlines are stubbornly linear,
and which ones go off to dramatic nonlinear land.

#### Regression Plot

A simple way to overlay regression lines,
on scatter points for each series.
Plotting linear regression plot is straightforward.
We can plot all these three series at once in one plot figure.

* **71a-regplot.py**

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Getting Matrix Values
pairCSV = np.genfromtxt("series.csv",
  skip_header=1, delimiter=",", dtype=float)

# Extract x and y values from CSV data
xs, ys1, ys2, ys3 = pairCSV.T

# Scatter plot with regression line
plt.figure(figsize=(8, 6))
sns.regplot(x=xs, y=ys1)
sns.regplot(x=xs, y=ys2)
sns.regplot(x=xs, y=ys3)

# Plot formatting
plt.title('Scatter Plot with Regression Line')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
```

Explanation

```python
# Getting Matrix Values
pairCSV = np.genfromtxt("series.csv",
  skip_header=1, delimiter=",", dtype=float)

# Extract x and y values from CSV data
xs, ys1, ys2, ys3 = pairCSV.T

# Scatter plot with regression line
plt.figure(figsize=(8, 6))
sns.regplot(x=xs, y=ys1)
sns.regplot(x=xs, y=ys2)
sns.regplot(x=xs, y=ys3)
```

With one command per series we get data points,
regression line, and confidence band.
It's like magic, but with math under the hood.



The result of the plot can be visualized as below:



You can obtain the interactive `JupyterLab` in this following link:

* **71a-regplot.py**

Or if you wish you can have three subplots in one figure
with the help of tight layout,

* **71b-regplot-3x.py**

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Getting Matrix Values
pairCSV = np.genfromtxt("series.csv",
  skip_header=1, delimiter=",", dtype=float)

# Extract x and y values from CSV data
xs, ys1, ys2, ys3 = pairCSV.T

# Creating subplots
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

# Defining a Seaborn color palette
# You can specify the number of colors here
palette = sns.color_palette("husl", 3)

# Plotting each scatter plot with regression line
pairs = zip([ys1, ys2, ys3], ['ys1', 'ys2', 'ys3'])

for i, (ys, title) in enumerate(pairs):
  sns.regplot(x=xs, y=ys,
    ax=axs[i], color=palette[i])

  axs[i].set_title(title)
  axs[i].set_xlabel('x')
  axs[i].set_ylabel('y')

# Plot formatting
plt.tight_layout()
plt.show()
```

Explanation

> Three-in-One Subplots

When overlaying clutters the view,
we can split into three panels, all neatly aligned.

Prepare our data first.
Getting Matrix Values, and
extract x and y values from CSV data.

```python
pairCSV = np.genfromtxt("series.csv",
  skip_header=1, delimiter=",", dtype=float)

xs, ys1, ys2, ys3 = pairCSV.T
```

Create the subplots.
And also defining seaborn color palette.
You can specify the number of colors here.

```python
# Creating subplots
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

palette = sns.color_palette("husl", 3)
```

Then plotting each scatter plot with regression line.

```python
pairs = zip([ys1, ys2, ys3], ['ys1', 'ys2', 'ys3'])

for i, (ys, title) in enumerate(pairs):
  sns.regplot(x=xs, y=ys,
    ax=axs[i], color=palette[i])

  axs[i].set_title(title)
  axs[i].set_xlabel('x')
  axs[i].set_ylabel('y')

plt.tight_layout()
plt.show()
```



The result of the plot can be visualized as follows.
All with pretty color.
You can see the color is better than matplotlib.



You can obtain the interactive `JupyterLab` in this following link:

* **71b-regplot-3x.py**

Side-by-side panels make it easy,
to compare slopes and scatter spread across series.
Plus the colors from `husl` give our eyes a treat.

#### Linear Model Plot

> LM: Linear Model

Leverage `lmplot` for a concise call,
that handles DataFrame melting and faceting under the hood.
We can make the code above simpler with `lmplot`.

* **72a-lmplot.py**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from CSV file directly
# into a pandas DataFrame,
# strip leading spaces from column names
df = pd.read_csv("series.csv") \
  .rename(columns=lambda x: x.strip())

# Melt the DataFrame to long format
# for linear model plot
df_melted = pd.melt(df,
  id_vars='xs', var_name='y', value_name='value')

# Scatter plot with regression line
plt.figure(figsize=(8, 6))
sns.lmplot(x='xs', y='value',
  data=df_melted, hue='y')

# Adjust the position of the title
plt.subplots_adjust(top=0.9)

# Plot formatting
plt.title('Scatter Plot with Regression Line')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
```

Explanation

With panda dataframe,
we can read data from CSV directly.
But beware of the strip leading spaces from column names.

Before using the dataframe,
we need to transform the DataFrame to long format for linear model plot.
We can do this using `melt` method from `panda`.

```python
df = pd.read_csv("series.csv") \
  .rename(columns=lambda x: x.strip())

df_melted = pd.melt(df,
  id_vars='xs', var_name='y', value_name='value')
```

Then we can draw scatter plot with regression line.
For convenience, I adjust the title position a bit,
so the title fit in small sized figure.

```python
plt.figure(figsize=(8, 6))
sns.lmplot(x='xs', y='value',
  data=df_melted, hue='y')

plt.subplots_adjust(top=0.9)
```



The result of the plot can be visualized as below:



You can obtain the interactive `JupyterLab` in this following link:

* **72a-lmplot.py**

`lmplot` combines regression, hue-based grouping, 
and faceting in one shot.
It's the Swiss Army knife of trend visualization.

#### Facet Grid

> Grid of Plot

For ultimate control we can use `FacetGrid`,
for multiple subplots sharing axes or not.
Instead of using subplots,
we can arrange our plot in a grid.
I give you two different examples.
One with shared y-axis,
and the other having different y-axis for each.

* **73a-facetgrid.py**

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Getting Matrix Values
pairCSV = np.genfromtxt("series.csv",
  skip_header=1, delimiter=",", dtype=float)

cols_all = ['xs', 'ys1', 'ys2', 'ys3']
cols_sel = ['ys1', 'ys2', 'ys3']

# Convert to pandas DataFrame
df = pd.DataFrame(pairCSV, columns=cols_all)

# Melt the DataFrame to long format for FacetGrid
df_melted = pd.melt(df,
  id_vars='xs', var_name='y', value_name='value')

# Create a FacetGrid with one row and three columns
g = sns.FacetGrid(df_melted,
  col='y', col_wrap=3, height=4, sharey=False)

# Map regplot to each facet
g.map_dataframe(sns.regplot,
  x='xs', y='value', color='b')

# Add different colors for each ys category
for ax, ys_name in zip(g.axes.flat, cols_sel):
  df_subset = df_melted[
    df_melted['y'] == ys_name]
  
  # with different color for each ys
  color = sns.color_palette("husl", 3)[
    cols_sel.index(ys_name)]

  sns.regplot(x='xs', y='value',
    data=df_subset, ax=ax,
    color=color)

# Set titles for each facet
g.set_titles('{col_name}')

# Set common labels for x-axis and y-axis
g.set_axis_labels('x', 'y')

# Show plot
plt.show()
```

Explanation

First we need to get the matrix values.
Then convert the values to pandas dataframe.
For use with this `facetgrid`,
we need to melt the dataframe to long format.

```python
pairCSV = np.genfromtxt("series.csv",
  skip_header=1, delimiter=",", dtype=float)

cols_all = ['xs', 'ys1', 'ys2', 'ys3']
cols_sel = ['ys1', 'ys2', 'ys3']

df = pd.DataFrame(pairCSV, columns=cols_all)

df_melted = pd.melt(df,
  id_vars='xs', var_name='y', value_name='value')
```

Or share the y-axis and vary x-axis limits.
We need to create a `facetgrid` with one row and three columns,
with different y-axis for each.
Then we can map regplot to each facet.

```python
g = sns.FacetGrid(df_melted,
  col='y', col_wrap=3, height=4, sharey=False)

g.map_dataframe(sns.regplot,
  x='xs', y='value', color='b')
```

We can iterate over selected columns and
map regplot to each column in the `facetgrid`.

In the iteration,
we should filter dataframe subset for each `ys` category.
Also for each `ys` category we can use different color,
based on `sns.color_palette`.

```python
for ax, ys_name in zip(g.axes.flat, cols_sel):
  df_subset = df_melted[
    df_melted['y'] == ys_name]

  color = sns.color_palette("husl", 3)[
    cols_sel.index(ys_name)]

  sns.regplot(x='xs', y='value',
    data=df_subset, ax=ax,
    color=color)
```



The result of the plot can be visualized as below.
They all shared the same y-axis.



You can obtain the interactive `JupyterLab` in this following link:

* **73a-facetgrid.py**

Explanation

If you want you can have different y-axis for each grid.

* **73b-facetgrid.py**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data from CSV file directly
# into a pandas DataFrame,
# strip leading spaces from column names
df = pd.read_csv("series.csv") \
  .rename(columns=lambda x: x.strip())
  
# Define selected columns
cols_sel = ['ys1', 'ys2', 'ys3']

# Melt the DataFrame to long format for FacetGrid
df_melted = df.melt(
  id_vars='xs', value_vars=cols_sel)

# Create a FacetGrid with seaborn
g = sns.FacetGrid(df_melted,
  col='variable', col_wrap=3,
  sharex=False, sharey=True)

# Iterate over selected columns and
# map regplot to each column in the FacetGrid
for ax, col in zip(g.axes.flatten(), cols_sel):
  df_subset = df.melt(
    id_vars='xs', value_vars=col)

  color = sns.color_palette("husl", 3)[
    cols_sel.index(col)]

  sns.regplot(x='xs', y='value',
    data=df_subset, ax=ax, color=color)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
```

With panda dataframe,
we can read data from CSV directly.
Do not firget to strip leading spaces from column names.
Now we define selected columns for `ys` series.

```python

df = pd.read_csv("series.csv") \
  .rename(columns=lambda x: x.strip())
  
cols_sel = ['ys1', 'ys2', 'ys3']
```

As usual we should melt the DataFrame to long format for `facetgrid`.
So we can create a `facetgrid` with seaborn

```python
df_melted = df.melt(
  id_vars='xs', value_vars=cols_sel)

g = sns.FacetGrid(df_melted,
  col='variable', col_wrap=3,
  sharex=False, sharey=True)
```

Like previous example, we can iterate over selected columns and
map regplot to each column in the `facetgrid`.

```python
for ax, col in zip(g.axes.flatten(), cols_sel):
  df_subset = df.melt(
    id_vars='xs', value_vars=col)

  color = sns.color_palette("husl", 3)[
    cols_sel.index(col)]

  sns.regplot(x='xs', y='value',
    data=df_subset, ax=ax, color=color)
```



The result of the plot can be visualized as below:



You can obtain the interactive `JupyterLab` in this following link:

* **73b-facetgrid.py**

FacetGrid is our multi-paneled stage.
We decide whether our subplots share scales or stand alone,
giving us granular control over comparisons.

-- -- --

### Visualizing Statistics Properties

We have four plots that share almost identical setup.
Each one gives us a different lens on the same data
Let's prepare our data once and then explore:

1. Boxplot
2. Violinplot
3. Swarmplot
4. Striplot

#### Preparing Dataframe

These plot required the the same data preparation.
As usual, you might either read the dataframe from panda directly,
or using numpy's `np.genfromtxt`.

First we need to get the matrix values.
Then convert the values to pandas dataframe.
For use with this these four kinds of plot,
we need to melt the dataframe to long format.

```python
pairCSV = np.genfromtxt("series.csv",
  skip_header=1, delimiter=",", dtype=float)

cols_all = ['xs', 'ys1', 'ys2', 'ys3']
df = pd.DataFrame(pairCSV, columns=cols_all)

df_melted = pd.melt(df,
  id_vars='xs', var_name='y', value_name='value')
```

We load the CSV, convert to a DataFrame,
and melt it into long form. This step powers every plot below.



One tidy DataFrame fuels many plots.
We avoid copy paste and ensure consistency across visuals.

#### Box Plot

The box plot is the classic.
It shows median quartiles and outliers at a glance.

* **81a-boxplot.py**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Getting Matrix Values
pairCSV = np.genfromtxt("series.csv",
  skip_header=1, delimiter=",", dtype=float)

# Convert the data to a pandas DataFrame
cols_all = ['xs', 'ys1', 'ys2', 'ys3']
df = pd.DataFrame(pairCSV, columns=cols_all)

# Melt the DataFrame to long format for boxplot
df_melted = pd.melt(df,
  id_vars='xs', var_name='y', value_name='value')

# Create boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='y', y='value', data=df_melted)

# Visualize the distribution of values
# across different categories.
plt.title('Box Plot for ys1, ys2, and ys3')
plt.xlabel('Variable')
plt.ylabel('Value')
plt.show()
```

Creating `boxplot` is as simple as below:

```python
plt.figure(figsize=(8, 6))
sns.boxplot(x='y', y='value', data=df_melted)
```



The result of the plot can be visualized as below:



You can obtain the interactive `JupyterLab` in this following link:

* **81a-boxplot.py**

Box plots highlight center spread and extreme points.
If a whisker goes rogue we notice immediately.

#### Violin Plot

Violin plots layer a kernel density estimate,
around the box plot structure for extra flair.
This is basically the sum of normal distribution.

* **81b-violin.py**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Getting Matrix Values
pairCSV = np.genfromtxt("series.csv",
  skip_header=1, delimiter=",", dtype=float)

# Convert the data to a pandas DataFrame
cols_all = ['xs', 'ys1', 'ys2', 'ys3']
df = pd.DataFrame(pairCSV, columns=cols_all)

# Melt the DataFrame to long format for boxplot
df_melted = pd.melt(df,
  id_vars='xs', var_name='y', value_name='value')

# Create violinplot
plt.figure(figsize=(8, 6))
sns.violinplot(x='y', y='value', data=df_melted)

# Visualize the distribution of values
# across different categories.
plt.title('Violin Plot for ys1, ys2, and ys3')
plt.xlabel('Variable')
plt.ylabel('Value')
plt.show()
```

Creating `violinplot` is also simple.

```python
plt.figure(figsize=(8, 6))
sns.violinplot(x='y', y='value', data=df_melted)
```



The result of the plot can be visualized as below:



You can obtain the interactive `JupyterLab` in this following link:

* **81b-violin.py**

Violin plots reveal the full distribution shape.
We see multimodal bumps or smooth bell curves at a glance.

#### Swarm Plot

Swarm plots show individual observations while avoiding overlap.
It's like inviting each data point to stand in its own space.

* **81c-swarm.py**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Getting Matrix Values
pairCSV = np.genfromtxt("series.csv",
  skip_header=1, delimiter=",", dtype=float)

# Convert the data to a pandas DataFrame
cols_all = ['xs', 'ys1', 'ys2', 'ys3']
df = pd.DataFrame(pairCSV, columns=cols_all)

# Melt the DataFrame to long format for boxplot
df_melted = pd.melt(df,
  id_vars='xs', var_name='y', value_name='value')

# Define colors for swarmplot
# Adjust the number of colors as needed
colors = sns.color_palette("husl", 3)

# Create swarmplot with different colors
plt.figure(figsize=(8, 6))
sns.swarmplot(x='y', y='value',
  hue='y', data=df_melted, palette=colors)

# Visualize the distribution of values
# across different categories.
plt.title('Swarm Plot for ys1, ys2, and ys3')
plt.xlabel('Variable')
plt.ylabel('Value')
plt.show()
```

We can define colors for `swarmplot`,
by adjust the number of colors as needed,
so we can create `swarmplot` with different colors

```python
colors = sns.color_palette("husl", 3)

plt.figure(figsize=(8, 6))
sns.swarmplot(x='y', y='value',
  hue='y', data=df_melted, palette=colors)
```



The result of the plot can be visualized as below:



You can obtain the interactive `JupyterLab` in this following link:

* **81c-swarm.py**

Swarm plots let us see the actual data points.
We spot clusters, gaps, and any singletons that box or violin plots might hide.

#### Strip Plot

Strip plots are like swarms but allow us,
to dodge points side by side.
They give a sense of overlap density.

* **81d-strip.py**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Getting Matrix Values
pairCSV = np.genfromtxt("series.csv",
  skip_header=1, delimiter=",", dtype=float)

# Convert the data to a pandas DataFrame
cols_all = ['xs', 'ys1', 'ys2', 'ys3']
df = pd.DataFrame(pairCSV, columns=cols_all)

# Melt the DataFrame to long format for boxplot
df_melted = pd.melt(df,
  id_vars='xs', var_name='y', value_name='value')

# Define colors for swarmplot
# Adjust the number of colors as needed
colors = sns.color_palette("husl", 3)

# Create stripplot with different colors
plt.figure(figsize=(8, 6))
sns.stripplot(x='y', y='value', data=df_melted,
  hue='y', palette=colors, dodge=True)

# Visualize the distribution of values
# across different categories.
plt.title('Strip Plot for ys1, ys2, and ys3')
plt.xlabel('Variable')
plt.ylabel('Value')
plt.legend(title='Category', loc='upper left')
plt.show()
```

Just like `swarmplot`,
We can define colors by adjust the number of colors as needed,
so we can create the `striplot` with different colors

```python
colors = sns.color_palette("husl", 3)

plt.figure(figsize=(8, 6))
sns.stripplot(x='y', y='value', data=df_melted,
  hue='y', palette=colors, dodge=True)
```



The result of the plot can be visualized as below:



You can obtain the interactive `JupyterLab` in this following link:

* **81d-strip.py**

Strip plots combine the clarity of swarm plots with grouping dodge.
We see individual values and group separation at once.

-- -- --

### Visualizing Distribution

When it comes to distribution plots,
Seaborn makes our lives a breeze.
We get beautiful charts with minimal code,
and maximum statistical insight.

#### KDE Plot

> Kernel Density Estimation

Kernel Density Estimation turns each data point,
into a little bell curve and sums them all together.
The result is a smooth silhouette of our data’s true shape.

This is the sum of normal distribution for each points for a data series.

* **82a-kdeplot.py**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data from CSV file directly
# into a pandas DataFrame,
# strip leading spaces from column names
df = pd.read_csv("series.csv") \
  .rename(columns=lambda x: x.strip())

# Set the style of seaborn
sns.set_style("whitegrid")

# Define a color palette for the KDE plot
# Adjust the number of colors as needed
palette = sns.color_palette("husl", 3)

# Create a KDE plot for each ys category
plt.figure(figsize=(8, 6))
for i, col in enumerate(['ys1', 'ys2', 'ys3']):
  sns.kdeplot(data=df[col],
    color=palette[i], label=col)

# Add title and labels
plt.title('KDE Plot for ys1, ys2, and ys3')
plt.xlabel('Value')
plt.ylabel('Density')

# Add legend
plt.legend()

# Show plot
plt.show()
```

As usual we can prepare the data.
Then seaborn decoration such as the style.
And also define a color palette for the KDE plot,
with adjustable number of colors as you needed.

```python
df = pd.read_csv("series.csv") \
  .rename(columns=lambda x: x.strip())

sns.set_style("whitegrid")
palette = sns.color_palette("husl", 3)

plt.figure(figsize=(8, 6))
```

And create a KDE plot for each ys category.

```python
for i, col in enumerate(['ys1', 'ys2', 'ys3']):
  sns.kdeplot(data=df[col],
    color=palette[i], label=col)
```



The result of the plot can be visualized as below:



You can obtain the interactive `JupyterLab` in this following link:

* **82a-kdeplot.py**

If you wish, you can customize the style,
with other parameters.

* **82b-kdeplot.py**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data from CSV file directly
# into a pandas DataFrame
df = pd.read_csv("series.csv")

# Melt the DataFrame to long format for kdeplot
df_melted = pd.melt(df, id_vars='xs',
  var_name='Category', value_name='Value')

# Set the style of seaborn
sns.set_style("darkgrid")

# Create KDE plot for all categories
plt.figure(figsize=(8, 6))

sns.kdeplot(data=df_melted,
  x='Value', hue='Category', palette='deep',
  alpha=0.7, multiple='stack', linewidth=2)

# Add title and labels
plt.title('KDE Plot for ys1, ys2, and ys3')
plt.xlabel('Value')
plt.ylabel('Density')

# Add legend
plt.legend(title='Category', loc='upper left')

# Show plot
plt.show()
```

Explanation

```python
df = pd.read_csv("series.csv")
df_melted = pd.melt(df, id_vars='xs',
  var_name='Category', value_name='Value')

sns.set_style("darkgrid")

plt.figure(figsize=(8, 6))
```

Then we can create KDE plot
for all categories with oneliner settings.

```python
sns.kdeplot(data=df_melted,
  x='Value', hue='Category', palette='deep',
  alpha=0.7, multiple='stack', linewidth=2)
```



The result of the plot can be visualized as below:



Customize further:

* **82b-kdeplot.py**

KDE plots reveal subtle bumps and tails that histograms can miss.
They help us spot multimodal distributions or heavy tails in a flash.

#### Rug Plot

Sometimes the simplest visualization is the most telling.
A rug plot adds one tick for each observation.
It's like sprinkling sugar on a cake. Small but impactful.

* **83a-rugplot.py**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the style of seaborn
sns.set_style("ticks")

# Read data from CSV file directly
# into a pandas DataFrame
df = pd.read_csv("series.csv")

# Melt the DataFrame to long format for rugplot
df_melted = pd.melt(df, id_vars='xs',
  var_name='Category', value_name='Value')

# Define a color palette for the rug plots
# Use one less color for 'xs'
palette = sns.color_palette(
  "husl", len(df.columns) - 1)  

# Create rug plot for each category
plt.figure(figsize=(8, 6))

# Exclude 'xs' column
for i, col in enumerate(df.columns[1:]):
  df_subset = df_melted[df_melted['Category'] == col]
  sns.rugplot(data=df_subset, x='Value',
    color=palette[i], label=col, alpha=0.7)

# Add title and labels
plt.title('Rug Plot for ys1, ys2, and ys3')
plt.xlabel('Value')
plt.ylabel('Density')

# Add legend
plt.legend(title='Category', loc='upper left')

# Show plot
plt.show()
```

As usual we need to `melt` the dataframe to long format for rugplot.

```python
df = pd.read_csv("series.csv")

df_melted = pd.melt(df, id_vars='xs',
  var_name='Category', value_name='Value')
```

For decoration purpose we need to 
define a color palette for the rug plots.
With using one less color for 'xs'

```python
palette = sns.color_palette(
  "husl", len(df.columns) - 1)  

plt.figure(figsize=(8, 6))
```

Then we can create rug plot for each category,
with 'xs' column excluded.

```python
for i, col in enumerate(df.columns[1:]):
  df_subset = df_melted[df_melted['Category'] == col]
  sns.rugplot(data=df_subset, x='Value',
    color=palette[i], label=col, alpha=0.7)
```



The result of the plot can be visualized as below.
This looks like an empty chart as first.
But you can see the ticks at the below of the figure.



You can obtain the interactive `JupyterLab` in this following link:

* **83a-rugplot.py**

Rug plots show raw data density without binning.
They let us see exact observation locations and gaps in the data.

#### Histogram Plot

We all know histograms.
So what is so special with this histogram?
Seaborn's histplot can add a KDE curve on top to combine the best of both worlds.

* **83b-histplot.py**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the style of seaborn
sns.set_style("whitegrid")

# Read data from CSV file directly
# into a pandas DataFrame,
# strip leading spaces from column names
df = pd.read_csv("series.csv") \
  .rename(columns=lambda x: x.strip())

# Select columns ys1, ys2, and ys3
cols_selected = ['ys1', 'ys2', 'ys3']

# Create a figure and axis objects
plt.figure(figsize=(8, 6))

# Plot displot for selected columns
sns.histplot(data=df[cols_selected],
  kde=True, element='step',
  multiple='layer', palette='husl')

# Add title and labels
plt.title('Distribution Plot for ys1, ys2, and ys3')
plt.xlabel('Value')
plt.ylabel('Density')

# Show plot
plt.show()
```

As usual we need to prepare data.
Then select columns such as `ys₁`, `ys₂`, and `ys₃`.
Then create a figure and axis objects.

```python
df = pd.read_csv("series.csv") \
  .rename(columns=lambda x: x.strip())

cols_selected = ['ys1', 'ys2', 'ys3']

plt.figure(figsize=(8, 6))
```

This way we can plot displot for selected columns.

```python
sns.histplot(data=df[cols_selected],
  kde=True, element='step',
  multiple='layer', palette='husl')
```



The result of the plot can be visualized as below:



Explore more: 

* **83b-histplot.py**

Layering KDE on a histogram helps us,
see both individual bin counts and the underlying density estimate.
It's clarity and style rolled into one.

#### Distribution Plot

Seaborn's displot ties it all together: histogram, KDE, and rug,
into a single convenient function.

* **83c-displot.py**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data from CSV file directly
# into a pandas DataFrame,
# strip leading spaces from column names
df = pd.read_csv("series.csv") \
  .rename(columns=lambda x: x.strip())

# Select only columns ys1, ys2, and ys3
cols_selected = ['ys1', 'ys2', 'ys3']
df_selected = df[cols_selected]

# Define a color palette for the displot
palette = sns.color_palette(
  "husl", len(cols_selected))

# Create displot for selected columns
plt.figure(figsize=(8, 6))
sns.displot(data=df_selected,
  kind='hist', rug=True, kde=True,
  palette=palette, alpha=0.7, multiple='layer')

# Add title and labels
plt.title('Distribution Plot for ys1, ys2, and ys3')
plt.xlabel('Value')
plt.ylabel('Density')

# Show plot
plt.show()
```

As above, we need to select columns,
such as `ys₁`, `ys₂`, and `ys₃`.

```python
df = pd.read_csv("series.csv") \
  .rename(columns=lambda x: x.strip())

cols_selected = ['ys1', 'ys2', 'ys3']
df_selected = df[cols_selected]
```

Let's decorate the figure as usual.
Defining a color palette for the `displot`.

```python
palette = sns.color_palette(
  "husl", len(cols_selected))

plt.figure(figsize=(8, 6))
```

Now we can create displot for selected columns.

```python
sns.displot(data=df_selected,
  kind='hist', rug=True, kde=True,
  palette=palette, alpha=0.7, multiple='layer')
```



The result of the plot can be visualized as below:



You can obtain the interactive `JupyterLab` in this following link:

* **83c-displot.py**

`displot` is our all-in-one distribution toolkit.
It saves us boilerplate code and gives a comprehensive view of:
frequency, density, and individual data points.

-- -- --

### Further Visualization

We can combine multiple layers of information into a single figure.
For example these two plots add marginal distributions on the top and right sides,
giving us both joint and individual views in one glance.

#### Joint Plot

Seaborn's jointplot makes it trivial to pair a scatterplot
with marginal density or histogram plots.
Here we'll illustrate a regression between xs and ys₃
with KDE filling on the margins.

* **84a-jointplot.py**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data from CSV file directly
# into a pandas DataFrame,
# strip leading spaces from column names
df = pd.read_csv("series.csv") \
  .rename(columns=lambda x: x.strip())

# Use seaborn's jointplot to create
# a scatter plot with KDE at the marginal
sns.jointplot(data=df, x='xs', y='ys3',
  kind='reg', marginal_kws={'fill': True})

# Show the plot
plt.show()
```

For eaxmple, we can use seaborn's `jointplot`
to create a scatter plot,
with KDE at the marginal.

```python
df = pd.read_csv("series.csv") \
  .rename(columns=lambda x: x.strip())

sns.jointplot(data=df, x='xs', y='ys3',
  kind='reg', marginal_kws={'fill': True})
```



The result of the plot can be visualized as below:



You can obtain the interactive `JupyterLab` in this following link:

* **84a-jointplot.py**

This plot shows both the relationship,
between two variables and their individual distributions.
We get regression insight and marginal shape in one compact view.

#### Joint Grid

For full customization we can build the same view by hand using JointGrid.
This lets us choose any plot type for the center and the margins.

* **84b-jointgrid.py**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data from CSV file directly
# into a pandas DataFrame,
# strip leading spaces from column names
df = pd.read_csv("series.csv") \
  .rename(columns=lambda x: x.strip())

# Create a JointGrid object
g = sns.JointGrid(data=df, x='xs', y='ys3')

# Plot the scatter plot in the center
g.plot_joint(sns.regplot)

# Plot the histograms on the marginal axes
g.plot_marginals(sns.boxplot)

# Show the plot
plt.show()
```

First we need to create a JointGrid object.
Then plot the scatter plot in the center,
and also set the histograms plot on the marginal axes.

```python
df = pd.read_csv("series.csv") \
  .rename(columns=lambda x: x.strip())

g = sns.JointGrid(data=df, x='xs', y='ys3')
g.plot_joint(sns.regplot)
g.plot_marginals(sns.boxplot)
```



The result of the plot can be visualized as below:



You can obtain the interactive `JupyterLab` in this following link:

* **84b-jointgrid.py**

With JointGrid we control every layer.
We can swap in histograms, violinplots,
or any custom chart on the margins to suit our analysis needs.

-- -- --

### What Comes Next 🤔?

We have dazzled our plots and explored distributions in all their glory.
Now it is time to broaden our toolkit beyond Python and Seaborn.

I am eager to dive into PSPPire, the open source cousin of SPSS.
It lets us run familiar statistical tests in a free,
community-driven environment.
Think of it as a statistical theme park,
where all the rides are free and the cotton candy never runs out.

Learning PSPPire gives us another arrow in our quiver.
When we need quick hypothesis tests or standardized reporting,
PSPPire can deliver without licensing headaches.

Let us continue our adventure here:
🔗 **Trend - Properties - PSPPire**.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: A quick glance to the open source PSPPire.

We've built spreadsheets and Python scripts to conquer statistics.
Now let's double-check our results with a bona fide statistical application.
PSPPire gives us a full GUI on top of PSPP's trusty terminal interface.
Think of it as putting a tuxedo on a spreadsheet,
same reliable engine, plus a sleek dashboard.

Verifying results across tools helps catch slip-ups.
If Excel, Python, and PSPPire all agree,
our confidence in those numbers just took a joyride.

-- -- --

### 1: Using PSPPire

Getting started feels surprisingly familiar once we spot the menus.

#### User Interface

By default PSPP lives in the terminal.
It's lean and mean but can feel like driving a rally car with no windshield.



We need PSPPire to run the GUI (graphical user interface)
Enter PSPPire for point-and-click joy.
All the features of PSPP dressed up in windows and buttons.



A GUI reduces the learning curve.
We spend fewer brain cycles on syntax and more on interpreting p-values.

-- -- --

### 2: Import Data

Let's bring in our trusty CSV of (x, y) pairs.
We use the `Import Data` menu and follow PSPPire's prompts.
For example this CSV file

```csv
x, y
0, 5
1, 12
2, 25
3, 44
4, 69
5, 100
6, 137
7, 180
8, 229
9, 284
10, 345
11, 412
12, 485
```

#### File → Import Data → CSV

We point PSPPire at 50-samples.csv.



We need to follow required procedure,
such as selecting rows.



#### Select Data Start

We skip the header row and pick line 2 as first case.



#### Choose Delimiter

> Separator.

A comma tells PSPPire where one number ends and the next begins.



#### Define Variables

> Variable format.

We assign x F2.0 and y F3.0 formats,
enough precision for point plots.



#### Data View

Once complete, the Data View shows our numbers in a grid.



PSPPire also spits out the equivalent PSPP command syntax in the Output Viewer:

```output
GET DATA
  /TYPE=TXT
  /FILE="/home/epsi/50-samples.csv"
  /ARRANGEMENT=DELIMITED
  /DELCASE=LINE
  /FIRSTCASE=2
  /DELIMITERS=","
  /VARIABLES=
    x F2.0
    y F3.0.
```



_The output above is the command line._

Having the generated command gives us reproducibility,
and a behind-the-scenes peek at PSPP's underbelly.
If we ever need to automate or script a batch of files,
we already have the template.

-- -- --

### 3: Frequency Analysis

With our data safely in PSPPire,
we can summon a full suite of descriptive statistics in just a few clicks.
Now you can do analysis easily.

#### Running Frequencies

> Analysis → Frequencies

We select variables x and y to analyze,
using analysis menu.



> Dialog Settings

We check options for tables and all statistics.
Then click OK.



> Output Viewer

In an instant PSPPire serves up our results in the Output Viewer.



#### Behind the Scenes: PSPP Syntax

PSPPire graciously shows us the equivalent command syntax,
so we know exactly what happened under the hood:

```output
FREQUENCIES
	/VARIABLES= x y
	/FORMAT=AVALUE TABLE
	/STATISTICS=ALL.
```

Seeing the command ensures our analysis is reproducible.
We can save or tweak it later for batch processing,
no mystery clicks required.

#### The Table of Truth

PSPPire lays out all the key properties we calculated earlier.
Here's a condensed view:

```output
        Statistics
╭─────────┬─────┬────────╮
│         │  x  │    y   │
├─────────┼─────┼────────┤
│N Valid  │   13│      13│
│  Missing│    0│       0│
├─────────┼─────┼────────┤
│Mean     │ 6.00│  179.00│
├─────────┼─────┼────────┤
│S.E. Mean│ 1.08│   44.52│
├─────────┼─────┼────────┤
│Median   │ 6.00│  137.00│
├─────────┼─────┼────────┤
│Mode     │    0│       5│
├─────────┼─────┼────────┤
│Std Dev  │ 3.89│  160.52│
├─────────┼─────┼────────┤
│Variance │15.17│25768.17│
├─────────┼─────┼────────┤
│Kurtosis │-1.20│    -.73│
├─────────┼─────┼────────┤
│S.E. Kurt│ 1.19│    1.19│
├─────────┼─────┼────────┤
│Skewness │  .00│     .70│
├─────────┼─────┼────────┤
│S.E. Skew│  .62│     .62│
├─────────┼─────┼────────┤
│Range    │12.00│  480.00│
├─────────┼─────┼────────┤
│Minimum  │    0│       5│
├─────────┼─────┼────────┤
│Maximum  │   12│     485│
├─────────┼─────┼────────┤
│Sum      │78.00│ 2327.00│
╰─────────┴─────┴────────╯
```

In one neat table we confirm sample size,
missing data, central tendency dispersion shape and range.
It's our statistical Swiss army knife.

#### Verify Excel

> Cross-Tool Verification

You may compare the result,
with our previous calculation with Excel.



Our built-in formulas produced identical means medians variances and so on.

#### Verify Python

> Cross-Tool Verification

You may compare the result,
with our previous calculation with Python.

Our `numpy` `scipy` script echoed the same results:

```output
x (max, min, range) = (   0.00,   12.00,   12.00 )
y (max, min, range) = (   5.00,  485.00,  480.00 )

x median       =      6.00
y median       =    137.00
x mode         =      0.00
y mode         =      5.00

x kurtosis     =     -1.20
y kurtosis     =     -0.73
x skewness     =      0.00
y skewness     =      0.70

x SE kurtosis  =      1.19
y SE kurtosis  =      1.19
x SE skewness  =      0.62
y SE skewness  =      0.62
```



When three independent tools agree we can trust our numbers.
Discrepancies would signal a bug or a typo.

-- -- --

### 4: Linear Regression Analysis

We can harness PSPPire to run a full linear regression in a few clicks.
Let us see how our GUI stacks up against spreadsheets and scripts.

#### Running the Regression

> Analysis → Regression → Linear

Again, fill the necessary dialog.
We assign `x` as predictor and `y` as dependent. Then click OK.



> Output Viewer

PSPPire serves up tables for model summary,
ANOVA, and coefficients. No calculator required.



A built-in regression procedure frees us from manual formula work,
and ensures consistency with standard statistical methods.

#### PSPP Command Syntax

PSPPire logs the equivalent command so we can script this later:

```output
REGRESSION
	/VARIABLES= x
	/DEPENDENT= y
	/METHOD=ENTER
	/STATISTICS=COEFF R ANOVA.
```

Seeing the command offers reproducibility.
We can batch process multiple datasets by tweaking one script.

#### Model Summary

PSPPire's Model Summary matches our earlier calculations,
for R, R², adjusted R², and standard error of estimate:

```output
                     Model Summary (y)
╭───┬────────┬─────────────────┬──────────────────────────╮
│ R │R Square│Adjusted R Square│Std. Error of the Estimate│
├───┼────────┼─────────────────┼──────────────────────────┤
│.97│     .94│              .94│                     40.47│
╰───┴────────┴─────────────────┴──────────────────────────╯
```

This table tells us how well x explains y.
An R² of 0.94 means 94% of variance in y is captured by our linear model.

#### ANOVA Table

Next PSPPire gives us ANOVA details:
sums of squares, degrees of freedom, mean squares, F statistic, and significance:

```output
                       ANOVA (y)
╭──────────┬──────────────┬──┬───────────┬──────┬────╮
│          │Sum of Squares│df│Mean Square│   F  │Sig.│
├──────────┼──────────────┼──┼───────────┼──────┼────┤
│Regression│      291200.0│ 1│   291200.0│177.78│.000│
│Residual  │      18018.00│11│    1638.00│      │    │
│Total     │      309218.0│12│           │      │    │
╰──────────┴──────────────┴──┴───────────┴──────┴────╯
```

The huge F value and p-value < 0.001 confirm that,
our regression model is statistically significant.

#### Coefficients

Finally we see the unstandardized and standardized coefficients,
their standard errors, t-values, and significance:

```output
                               Coefficients (y)
╭──────────┬────────────────────────────┬─────────────────────────┬─────┬────╮
│          │ Unstandardized Coefficients│Standardized Coefficients│     │    │
│          ├────────────┬───────────────┼─────────────────────────┤     │    │
│          │      B     │   Std. Error  │           Beta          │  t  │Sig.│
├──────────┼────────────┼───────────────┼─────────────────────────┼─────┼────┤
│(Constant)│      -61.00│          21.21│                      .00│-2.88│.014│
│x         │       40.00│           3.00│                      .97│13.33│.000│
╰──────────┴────────────┴───────────────┴─────────────────────────┴─────┴────╯
```

Coefficient B = 40 tells us that,
for each one-unit increase in x, y,
increases by 40 on average.

The intercept −61 and its p-value let us judge,
whether the line truly crosses zero meaningfully.

#### Verify Excel

> Cross-Tool Verification

You may compare the result,
with our previous calculation with excel and python.
Our tabular worksheet yielded identical slope,
intercept, t-value, and standard errors.



And also the right part of the worksheet.



#### Verify Python

> Cross-Tool Verification

You may compare the result,
with our previous calculation with Python.
Our `numpy`/`scipy` calculations match PSPPire's output:

```output
n          =   13
∑x (total) =   78.00
∑y (total) = 2327.00
x̄ (mean)   =    6.00
ȳ (mean)   =  179.00

∑(xᵢ-x̄)    =      0.00
∑(yᵢ-ȳ)    =      0.00
∑(xᵢ-x̄)²   =    182.00
∑(yᵢ-ȳ)²   = 309218.00
∑(xᵢ-x̄)(yᵢ-ȳ)  =   7280.00
m (slope)      =     40.00
b (intercept)  =    -61.00

Equation     y = -61.00 + 40.00.x

sₓ² (variance) =     14.00
sy² (variance) =  23786.00
covariance     =    560.00
sₓ (std dev)   =      3.74
sy (std dev)   =    154.23
r (pearson)    =      0.97
R²             =      0.94

SSR = ∑ϵ²           =  18018.00
MSE = ∑ϵ²/(n-2)     =   1638.00
SE(β₁)  = √(MSE/sₓ) =      3.00
t-value = β̅₁/SE(β₁) =     13.33
```



Agreement across Excel, Python, and PSPPire confirms,
that no computations are off.
We can trust these regression estimates.

-- -- --

### 5: Polynomial Regression Analysis

> Using Shell

After getting comfortable with PSPPire,
let's go full command line,
trade the GUI for a keyboard only experience.
The PSPP terminal gives us more flexibility,
than the point-and-click world.
And yes, we can run polynomial regression right here in the shell.



#### Data Source

Let's try a new dataset.

```csv
xs, ys1, ys2, ys3
0,  5,   5,   5
1,  9,   12,  14
2,  13,  25,  41
3,  17,  44,  98
4,  21,  69,  197
5,  25,  100, 350
6,  29,  137, 569
7,  33,  180, 866
8,  37,  229, 1253
9,  41,  284, 1742
10, 45,  345, 2345
11, 49,  412, 3074
12, 53,  485, 3941
```



We'll focus on `xs` and `ys3`,
but feel free to explore the other columns too.
They're not just filler, they’re backup dancers.

#### Import Data

Here's how we get our data into PSPP shell.
 The command is simple, nothing fancy.
 This time we have four columns.

```output
GET DATA
  /TYPE=TXT
  /FILE="/home/epsi/series.csv"
  /ARRANGEMENT=DELIMITED
  /DELCASE=LINE
  /FIRSTCASE=2
  /DELIMITERS=","
  /VARIABLES=
    xs F2.0
    ys1 F2.0
    ys2 F3.0
    ys3 F4.0.
```



#### Statistic Properties

> Check the Metrics

Before we dive into curves, let's get a sense of scale.
This time only what we need.: Mean, standard deviation, min, max.

```output
FREQUENCIES
  /VARIABLES=xs ys3
  /FORMAT=NOTABLE
  /STATISTICS=MEAN STDDEV MIN MAX.
```

With the result as below:

```output
       Statistics
╭─────────┬────┬───────╮
│         │ xs │  ys3  │
├─────────┼────┼───────┤
│N Valid  │  13│     13│
│  Missing│   0│      0│
├─────────┼────┼───────┤
│Mean     │6.00│1115.00│
├─────────┼────┼───────┤
│Std Dev  │3.89│1296.44│
├─────────┼────┼───────┤
│Minimum  │   0│      5│
├─────────┼────┼───────┤
│Maximum  │  12│   3941│
╰─────────┴────┴───────╯
```



#### Polynomial Regression Coefficient

> Quadratic

To compute polynomial regression,
we need to define `xs²` helper variable first.
This turns our linear regression into something a bit curvier.

```output
COMPUTE xs_squared = xs * xs.

REGRESSION
  /VARIABLES=xs xs_squared
  /DEPENDENT=ys3
  /METHOD=ENTER
  /STATISTICS=COEFF.
```

And we get:

```output
                              Coefficients (ys3)
╭──────────┬────────────────────────────┬─────────────────────────┬─────┬────╮
│          │ Unstandardized Coefficients│Standardized Coefficients│     │    │
│          ├────────────┬───────────────┼─────────────────────────┤     │    │
│          │      B     │   Std. Error  │           Beta          │  t  │Sig.│
├──────────┼────────────┼───────────────┼─────────────────────────┼─────┼────┤
│(Constant)│      137.00│          65.22│                      .00│ 2.10│.060│
│xs        │     -162.00│          25.25│                     -.49│-6.42│.000│
│xs_squared│       39.00│           2.03│                     1.46│19.23│.000│
╰──────────┴────────────┴───────────────┴─────────────────────────┴─────┴────╯
```

It matches our results in Excel/Calc and Python.
Harmony across platforms, every data analyst's dream.



> Cubic

Let's go one degree hotter, cubic regression with `xs²` and `xs³`.
Add a third power term and suddenly we're modeling rollercoasters.

```output
COMPUTE xs_squared = xs * xs.
COMPUTE xs_cubed = xs * xs * xs.

REGRESSION
  /VARIABLES=xs xs_squared xs_cubed
  /DEPENDENT=ys3
  /METHOD=ENTER
  /STATISTICS=COEFF.
```

And here's the result:

```output
                                Coefficients (ys3)
╭──────────┬────────────────────────────┬─────────────────────────┬────────┬────╮
│          │ Unstandardized Coefficients│Standardized Coefficients│        │    │
│          ├───────────┬────────────────┼─────────────────────────┤        │    │
│          │     B     │   Std. Error   │           Beta          │    t   │Sig.│
├──────────┼───────────┼────────────────┼─────────────────────────┼────────┼────┤
│(Constant)│       5.00│             .00│                      .00│+Infinit│.000│
│xs        │       4.00│             .00│                      .01│+Infinit│.000│
│xs_squared│       3.00│             .00│                      .11│+Infinit│.000│
│xs_cubed  │       2.00│             .00│                      .88│+Infinit│.000│
╰──────────┴───────────┴────────────────┴─────────────────────────┴────────┴────╯
```



Still consistent with our Excel/Calc and Python results.

_Do you think that the variable format is very similar to `LINEST` formula?_ \
_Do you think that this similarity has to do with design matrix?_

That's the power of methodical math.
We can call this replication,
but it feels more like statistical déjà vu.

#### Beyond Regression

> Easy peasy? Don't be so sure.

If all we needed were the coefficients,
we could stop here and call it a day.
But PSPP (and its big sibling SPSS) are statistical beasts,
with much more beneath the surface.
We've only tiptoed into the shallow end.

There's a world of diagnostics, assumptions, plots, and tests ahead.
Think of this as checking your tire pressure before a race.
Important, but far from the whole event.

Now that we’ve done our part:

```output
exit.
```

Stay humble, statisticians.

* The more we explore, the clearer it becomes,
  we've only just touched the surface.

* In the sea of statistics,
  every method we master reveals deeper waters ahead.

* Moving from spreadsheets to statistical tools,
  we realize how vast the field truly is.

* No matter how far we've come,
  there's always more to learn.

_Stay humble!_

-- -- --

### What’s Next for Our Curious Clipboard? 📋

We've poked around PSPPire, ran some regressions,
and even peeked under the hood at those ANOVA pistons firing.
But where do we steer our statistical engine next?
Let's break it down—three lanes ahead.

#### Further Analysis

> PSPPire Knows More Than It Shows

If we regularly wrestle with data, PSPP is not just a friend.
It's the nerdy lab partner who finishes our sentences with a p-value.
PSPPire offers way more than we've explored here,
from nonparametric tests to factor analysis,
but diving into every nook would require another trilogy.

Let's be honest.
This article was never meant to be a full tour of PSPPire.
Think of it as a strong cup of coffee,
and a friendly push into the statistics playground.
The rest? Explore when the data screams louder,
or when our spreadsheet starts judging us.

Mastering the basics lets us decide,
when to trust software and when to double-check.
Knowing the tools means we're never stuck,
staring at an error bar like it's an existential crisis.

#### The Curiosities We Skipped (But Might Revisit)

> What's left behind 🤔?

Yes, we did regression.
We danced with the line of best fit.
We even toyed with quadratic and cubic forms,
like high schoolers rewriting song lyrics into parabolas.

But we skipped a few gems:

* What if we measured correlation,
  between two datasets on the same x-axis?

* Or looked at how the fluctuation of one variable,
  predicts the fluctuation of another?
  Think of it as emotional intelligence for spreadsheets.

And we haven't touched splines.
Because honestly, splines are the deep-fried snacks of stats.
Delicious but hard to digest without proper guidance.

Regression is just the beginning.
Real-world data is rarely linear and never polite.
These advanced approaches let us understand,
when data moves together, when it rebels,
and when it just wants to be left alone.

#### Other Languages, Same Obsession

Sure, we've dabbled in Python.
But the statistical family dinner is much bigger:

* R: The grandmaster of stats.
  It comes with more packages than a post office in December.

* Julia: Lightning-fast and math-savvy.
  For those who want to feel both trendy and efficient.

* Go: For when we need stats to run inside a production-grade backend,
  and still sleep well at night.

Choosing a language is like picking a wrench.
The goal isn't to be fancy.
It's to make the data talk, and sometimes scream.

Feeling adventurous? Join us in the next article:
👉 **Trend - Language - R - Part One**

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Explore R Programming language visualization with ggplot2.
> Providing the data using linear model.

_R You Ready?_

Welcome to the `R`-side of our trend trilogy.
If this were a movie, this would be where
we zoom in on a shy but powerful character.
The kind who looks awkward in crowds
but aces calculus in their sleep.

Let’s be honest. 
or many of us who came from a coding,
first background, `R` feels... different.
Less like a programming language,
more like a statistics whisperer,
with strong opinions on plotting aesthetics.
At first, I tiptoed around it. Then I made a few plots.
And suddenly, I was in love.

`R` may be quirky,
but like that brilliant friend who labels their spice jars alphabetically,
it rewards patience. And let’s talk power:

* ike python’s seaborn, R has ggplot2,
  a charting ninja with a PhD in grammar.

* Like python’s polyfit, R has lm(),
  a humble function that delivers linear models with confidence intervals and style.

* Like python, R is beginner-friendly.
  Until it isn't. Then it’s mysterious.
  But then you learn one more trick, and it all clicks again.

Instead of asking every question in the `R` forums
(and being hit with “Have you read the docs?”),
I took the engineer's path: build a bunch of working examples first.
Now, I can answer questions and feel smug while doing it.

-- -- --

### Preparation

> Gearing Up

Before we dive in,
let's do the statistical equivalent of,
sharpening our chisels and lining up our rulers.

Of course you need `R` installed in your system.
No need for `RStudio`, but there is a few things to consider.

#### 📦 Library Check

We’ll start simple. No tidyverse buffet yet.
We’re going à la carte for understanding’s sake.
Install only what we need.

The script provided here start from the very basic,
and you need to get additional library from time to time.
You can install the package from `R` terminal.

```r
install.packages("readr")
install.packages("ggplot2")
install.packages("ggthemes")
```

Yes, `tidyverse` is like installing a whole kitchen set.
But for now, we're just learning how to fry an egg,
not host a cooking show.
I'd simply choose one library at a time,
to get more understanding.

#### Jupyter Lab

> Jupyter + R = ❤️

Prefer to work in a `Jupyter Lab` environment like a civilized data nerd?
Great! we'll want to activate the `R` kernel:

```r
IRkernel::installspec()
```

Totally optional, but nice when we like mixing Markdown with `R` code,
and pretending we're writing a thesis.

#### Data Series Samples

> One Table to Rule Them All

Why do we care about having a tiny dataset with only a few values?
Because small data = fewer distractions.
We want to focus on the plotting and analysis,
not debugging typos in row 2748.

We will use two example datasets:

> 1. 📈 Series Data for Plotting Practice

This one's got multiple series—great for trying out melt,
layering lines, and watching trends grow exponentially,
like our panic before a stats exam.

* **series.csv**

```csv
xs, ys1, ys2, ys3
0,  5,   5,   5
1,  9,   12,  14
2,  13,  25,  41
3,  17,  44,  98
4,  21,  69,  197
5,  25,  100, 350
6,  29,  137, 569
7,  33,  180, 866
8,  37,  229, 1253
9,  41,  284, 1742
10, 45,  345, 2345
11, 49,  412, 3074
12, 53,  485, 3941
```

**R: ggplot2: Statistical Properties: CSV Source**

Useful when we want to get fancy and explore the art of beautiful chaos.

2. 📏 Sample Data for Regression

This one is plain and perfect for linear regression,
least squares, and other noble pursuits.

* **50-samples.csv**

```csv
x,y
0,5
1,12
2,25
3,44
4,69
5,100
6,137
7,180
8,229
9,284
10,345
11,412
12,485
```

Yes, we call it samples instead of population,
because we're honest statisticians,
and don't want to go to academic jail.

-- -- --

### Trend: LM Model

> Linear Model

Let us summon the power of `lm()` and enter the arcane art of modeling.
Today, we predict the future using the most noble of tools:
the line (and its polynomial siblings).

#### Vector

In the mystical land of `R`, arrays are known as vectors.
Think of them as the "data sushi rolls" that hold everything together.

* **01-lm-vector.r**

```r
# Given data
x_values <- c(
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
y_values <- c(
  5, 14, 41, 98, 197, 350, 569, 866, 
  1253, 1742, 2345, 3074, 3941)

# Curve Fitting Order
order <- 3

# Perform cubic regression using lm()
lm_model <- lm(y_values ~
  poly(x_values, order, raw = TRUE))

# Coefficients
coefficients <- coef(lm_model)

# Reverse order to match output
coefficients <- coefficients[
  length(coefficients):1]

# Print coefficients
cat("Coefficients (a, b, c, d):\n\t",
  coefficients, "\n")
```

Explanation

```r
# Given data
x_values <- c(
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
y_values <- c(
  5, 14, 41, 98, 197, 350, 569, 866, 
  1253, 1742, 2345, 3074, 3941)
```



This is the classic “_x and y walked into a scatterplot_” setup.

We aim to fit our values using a linear regression model.
Mathematically, it looks like tthis.

$$
y = a + b{x}
$$

But why stop at a line when we can escalate this to curves with extra flair?
Let us unleash the `lm()` function with a polynomial twist.

First we need to define the order of the curve fitting.
Then perform cubic regression using `lm()`.
With the `lm_model` object we can get the coefficient.
But for printing, we need to reverse order to match output.
At last, we can print the coefficients with `cat`.

```r
order <- 3

lm_model <- lm(y_values ~
  poly(x_values, order, raw = TRUE))

coefficients <- coef(lm_model)
coefficients <- coefficients[
  length(coefficients):1]

cat("Coefficients (a, b, c, d):\n\t",
  coefficients, "\n")
```



This should output something along the lines of:

```output
❯ Rscript 01-lm-vector.r
Coefficients (a, b, c, d):
         2 3 4 5 
```

It is so predictable, right?
with the confidence of a stats professor grading on a curve.

Need something more interactive? Check the JupyterLab version:

* **01-lm-vector.r**

Starting with hardcoded vectors helps us test the waters.
We build intuition without file I/O headaches.

#### Reading from CSV

Let’s switch gears from hardcoding vector to file reading.
Because eventually, all our precious data ends up in CSVs,
the duct tape of data science.
We can utilize built-in `read.csv` method
to read data from CSV file.

* **02-lm-csv.r**

```r
# Read data from CSV file
data <- read.csv("series.csv")

# Extract x_values and y_values
x_values <- data$xs
y_values <- data$ys3

# Curve Fitting Order
order <- 3

# Perform cubic regression using lm()
lm_model <- lm(y_values ~
  poly(x_values, order, raw = TRUE))

# Coefficients
coefficients <- coef(lm_model)

# Reverse order to match output
coefficients <- coefficients[
  length(coefficients):1]

# Print coefficients
cat("Coefficients (a, b, c, d):\n\t",
  coefficients, "\n")
```

We need to extract x values and y values from the data frame.

```r
data <- read.csv("series.csv")

x_values <- data$xs
y_values <- data$ys3
```



Same data, different delivery method.
It's like ordering the same meal,
dine-in versus takeaway.

Interactive version here:

* **02-lm-csv.r**

Real-world datasets rarely arrive as perfectly typed vectors.
CSVs are the bridge between the wild data world and our cozy `R` environment.

#### Using Readr

Now for the fancier way, with `readr` library.
We upgrade from public transport to a private data limousine.
It's faster, more flexible, and supports better metadata handling.

First we need to load the required `readr` library.
Then read data from CSV file and put into a dataframe.
Then create a variable shortcut,
by extracting x values and y values.

* **03-lm-readr.r**

```r
# # Load required library
library(readr)

# Read data from CSV file
data <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Retrieve column specifications
column_spec <- spec(data)

# Extract x_values and y_values
x_values <- data$xs
y_values <- data$ys3

# Curve Fitting Order
order <- 3

# Perform cubic regression using lm()
lm_model <- lm(y_values ~
  poly(x_values, order, raw = TRUE))

# Coefficients
coefficients <- coef(lm_model)

# Reverse order to match output
coefficients <- coefficients[
  length(coefficients):1]

# Print coefficients
cat("Coefficients (a, b, c, d):\n\t",
  coefficients, "\n")
```

Explanation

```r
library(readr)

data <- read_csv(
  "series.csv",
  show_col_types = FALSE)

column_spec <- spec(data)

x_values <- data$xs
y_values <- data$ys3
```



We can retrieve the column specifications,
and print if we need to inspect.
The `spec()` function helps us peek,
into how `R` interprets each column,
no surprises allowed.

`JupyterLab` version available here:

* **03-lm-readr.r**

 In large or complex projects,
 `readr` improves data loading reliability and error messages.
 More stats, less drama.

#### Different Order of LM

Why settle for one flavor of linear modeling,
when we can sample the whole polynomial buffet?
We can repeat above code for different order,
or make it simpler.

$$
\begin{array}{|c|c|}
\hline
order = 1 & y = a + b{x}  \\
\hline
order = 2 & y = a + b{x} + c{x}^2 \\
\hline
order = 3 & y = a + b{x} + c{x}^2 + d{x}^3  \\
\hline
\end{array}
$$

Let's write a reusable function so we don’t feel like a broken record.

* **04-lm-merge.r**

```r
calc_coeff <- function(x_values, y_values, order) {
  # Perform linear regression using lm()
  lm_model <- lm(y_values ~ 
    poly(x_values, order, raw = TRUE))

  # Define a named vector
  # to map order numbers to curve types
  coeff_text <- c(
    "(a, b)" = 1, "(a, b, c)" = 2, "(a, b, c, d)" = 3)
  order_text <- c(
    "Linear" = 1, "Quadratic" = 2, "Cubic" = 3)

  # Print the curve type
  cat(paste("Using lm_model :",
    names(order_text)[order], "\n"))

  # Coefficients
  coefficients <- coef(lm_model)

  # Reverse order to match output
  coefficients <- coefficients[
    length(coefficients):1]

  # Print coefficients
  cat("Coefficients ",
    names(coeff_text)[order], ":\n\t",
    coefficients, "\n")
}

# Load required library
library(readr)

# Read data from CSV file
data <- read_csv(
  "series.csv",
  show_col_types = FALSE)

calc_coeff(data$xs, data$ys1, 1)
calc_coeff(data$xs, data$ys2, 2)
calc_coeff(data$xs, data$ys3, 3)
```

This function,
perform linear regression using `lm()`.
Also define a named vector to map order numbers to curve types.
Get the coefficients and also reverse order to match equation above.
And we can finally print the coefficients result.

```r
calc_coeff <- function(x_values, y_values, order) {
  lm_model <- lm(y_values ~ 
    poly(x_values, order, raw = TRUE))

  coeff_text <- c(
    "(a, b)" = 1, "(a, b, c)" = 2, "(a, b, c, d)" = 3)
  order_text <- c(
    "Linear" = 1, "Quadratic" = 2, "Cubic" = 3)

  cat(paste("Using lm_model :",
    names(order_text)[order], "\n"))

  coefficients <- coef(lm_model)
  coefficients <- coefficients[
    length(coefficients):1]

  cat("Coefficients ",
    names(coeff_text)[order], ":\n\t",
    coefficients, "\n")
```



This way we can calculate coefficient,
for different order and for different series.
Now let's throw in some real data and try multiple models.

```r
library(readr)
data <- read_csv(
  "series.csv",
  show_col_types = FALSE)

calc_coeff(data$xs, data$ys1, 1)
calc_coeff(data$xs, data$ys2, 2)
calc_coeff(data$xs, data$ys3, 3)
```



Expected output:

```output
❯ Rscript 04-lm-merge.r
Using lm_model : Linear 
Coefficients  (a, b) :
         4 5 
Using lm_model : Quadratic 
Coefficients  (a, b, c) :
         3 4 5 
Using lm_model : Cubic 
Coefficients  (a, b, c, d) :
         2 3 4 5 
```



`JupyterLab` edition available here:

* **04-lm-merge.r**

We can test different models and complexity levels with ease.
This is critical when the true relationship is,
hiding behind layers of curve-fitting suspense.

That wraps up the core machinery of linear modeling in `R`.
We started with simple vectors, took a CSV detour,
leveled up with `readr`, and built a flexible regression toolkit.

And remember, in statistics, it's all about fitting in.
Even if that means adding a few extra powers of x just to impress the plot.

-- -- --

### Trend: Built-in Plot

> When in doubt, plot it out.

Sometimes we do not need shiny visuals or fancy libraries.
Base `R`'s plotting functions may look like they were designed in the late '90s,
because they were.
But they get the job done with minimal fuss.
It is like the trusty wrench in a toolbox: not flashy, but reliable.

_It is rather limited, but enough to get started with plotting._

#### Default Output

By default, `R` quietly saves the result to a file called `Rplot.pdf`.
It is polite like that,
but we might prefer PNG for easier embedding or sharing.
Let us switch gears:

```r
# Open PNG graphics device
png("11-lm-line.png", width = 800, height = 400)
```

Choosing our output format early saves the embarrassment of,
emailing a 4MB PDF when all we needed was a lightweight image for our blog post.

#### Linear Equation

Let us start with the basics: plotting the data points.
No drama. No packages. Just pixels and points.

* **11-lm-line.r**

```r
# Given data
x_values <- c(
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
y_values <- c(
  5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53)

# Curve Fitting Order
order <- 1

# Perform linear regression using lm()
lm_model <- lm(y_values ~ 
  poly(x_values, order, raw = TRUE))

# Coefficients
coefficients <- coef(lm_model)

# Reverse order to match output
coefficients <- coefficients[
  length(coefficients):1]

# Print coefficients
cat("Coefficients (a, b):\n\t",
  coefficients, "\n")

# Open PNG graphics device
png("11-lm-line.png", width = 800, height = 400)

# Plot data points
plot(
  x_values, y_values,
  pch = 16, col = "blue",
  xlab = "x", ylab = "y",
  main = "Straight line fitting")

# Generate values for the regression line
x_plot <- seq(
  min(x_values), max(x_values),
  length.out = 100)
y_plot <- predict(
  lm_model,
  newdata = data.frame(x_values = x_plot))

# Add regression line
lines(x_plot, y_plot, col = "red")

# Add legend
legend("topright",
  legend = c("Data points", "Linear Equation"),
  col = c("blue", "red"),
  pch = c(16, NA), lty = c(NA, 1))
```

Explanation

```r
plot(
  x_values, y_values,
  pch = 16, col = "blue",
  xlab = "x", ylab = "y",
  main = "Straight line fitting")
```



And continue with lines,
from precalculated plot values.
The `y` values comes from the regression line,
previously performed by `lm()` into `lm_model`.

```r
x_plot <- seq(
  min(x_values), max(x_values),
  length.out = 100)
y_plot <- predict(
  lm_model,
  newdata = data.frame(x_values = x_plot))

lines(x_plot, y_plot, col = "red")
```



Then, communicate the visual result.
For those of us who like clarity,
or want to impress our thesis advisor,
we add a legend:

```r
legend("topright",
  legend = c("Data points", "Linear Equation"),
  col = c("blue", "red"),
  pch = c(16, NA), lty = c(NA, 1))
```

The plot result can be shown as follows:



You can explore the interactive `JupyterLab` version here:

* **11-lm-line.r**

A regression without a plot is like a punchline without a joke.
Visuals make trends obvious, and suspicious outliers even more so.

#### Straight Line

For those who believe in minimalism and shortcuts
(i.e., statisticians during finals week),
we can use `abline()` to draw the regression line,
directly from the model to the plot.
so we don't have to generate the `y_plot` values manually.

* **11-lm-line-ab.r**

```r
# Given data
x_values <- c(
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
y_values <- c(
  5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53)

# Curve Fitting Order
order <- 1

# Perform linear regression using lm()
lm_model <- lm(y_values ~ 
  poly(x_values, order, raw = TRUE))

# Coefficients
coefficients <- coef(lm_model)

# Reverse order to match output
coefficients <- coefficients[
  length(coefficients):1]

# Print coefficients
cat("Coefficients (a, b):\n\t",
  coefficients, "\n")

# Open PNG graphics device
png("11-lm-line-ab.png", width = 800, height = 400)

# Draw Plot
plot(
  x_values, y_values, 
   xlab = "x", ylab = "y", 
   main = "Straight line fitting", 
   pch = 16, col = "blue", 
   ylim = c(min(y_values), max(y_values)))

# Add linear regression line
abline(lm_model, col = "red")

# Add legend
legend("topleft",
  legend = c("Data points", "Linear Equation"), 
  col = c("blue", "red"),
  pch = c(16, NA), lty = c(NA, 1))
```

Explanation


```r
abline(lm_model, col = "red")
```

The plot result can be shown as follows:



Interactive `Jupyter Notebook`:

* **11-lm-line-ab.r**

`abline()` is like `Ctrl+C` for plotting regression lines.
Quick. Dirty. Efficient.
Use when elegance is less important than speed.

#### Quadratic Curve

What if the data curves a little?
Like life, sometimes it is not linear.
All we need to do is increase the polynomial order,
and adjust the decorations accordingly.

* **12-lm-quadratic.r**

```r
# Given data
x_values <- c(
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
y_values <- c(
  5, 12, 25, 44, 69, 100, 137,
  180, 229, 284, 345, 412, 485)

# Curve Fitting Order
order <- 2

# Perform quadratic regression using lm()
lm_model <- lm(y_values ~
  poly(x_values, order, raw = TRUE))

# Coefficients
coefficients <- coef(lm_model)

# Reverse order to match output
coefficients <- coefficients[
  length(coefficients):1]

# Print coefficients
cat("Coefficients (a, b, c):\n\t",
  coefficients, "\n")

# Open PNG graphics device
png("12-lm-quadratic.png", width = 800, height = 400)

# Draw Plot
plot(
  x_values, y_values, 
  xlab = "x", ylab = "y", 
  main = "Quadratic curve fitting", 
  pch = 16, col = "blue", 
  ylim = c(min(y_values), max(y_values)))

# Generate values for the quadratic curve
x_plot <- seq(
  min(x_values), max(x_values),
  length.out = 100)
y_plot <- predict(
  lm_model,
  newdata = data.frame(x_values = x_plot))

# Add quadratic curve
lines(x_plot, y_plot, col = "red")

# Add legend
legend("topleft",
  legend = c("Data points", "Quadratic Curve"), 
  col = c("blue", "red"),
  pch = c(16, NA), lty = c(NA, 1))
```

Explanation


```r
order <- 2
```

The plot result can be shown as follows:



Interactive `Jupyter Notebook`:

* **12-lm-quadratic.r**

Quadratic regression captures parabolic trends,
essential when things speed up or slow down in a curve,
like population growth or our anxiety curve before a deadline.

#### Cubic Curve

When linear and quadratic just do not cut it, cubic fits come to the rescue.
More flexible. More wiggly. More impressive looking in presentations.

* **13-lm-cubic.r**

```r
# Given data
x_values <- c(
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
y_values <- c(
  5, 14, 41, 98, 197, 350, 569, 866, 
  1253, 1742, 2345, 3074, 3941)

# Curve Fitting Order
order <- 3

# Perform cubic regression using lm()
lm_model <- lm(y_values ~
  poly(x_values, order, raw = TRUE))

# Coefficients
coefficients <- coef(lm_model)

# Reverse order to match output
coefficients <- coefficients[
  length(coefficients):1]

# Print coefficients
cat("Coefficients (a, b, c, d):\n\t",
  coefficients, "\n")

# Open PNG graphics device
png("13-lm-cubic.png", width = 800, height = 400)

# Draw Plot
plot(
  x_values, y_values, 
  xlab = "x", ylab = "y", 
  main = "Cubic curve fitting", 
  pch = 16, col = "blue", 
  ylim = c(min(y_values), max(y_values)))

# Generate values for the cubic curve
x_plot <- seq(
  min(x_values), max(x_values),
  length.out = 100)
y_plot <- predict(
  lm_model,
  newdata = data.frame(x_values = x_plot))

# Add cubic curve
lines(x_plot, y_plot, col = "red")

# Add legend
legend("topleft",
  legend = c("Data points", "Cubic Curve"), 
  col = c("blue", "red"),
  pch = c(16, NA), lty = c(NA, 1))
```

Explanation


```r
order <- 3
```

The plot result can be shown as follows:



You can obtain the interactive `JupyterLab` in this following link:

* **13-lm-cubic.r**

Cubic fits can capture subtle turning points in data,
though if the model starts oscillating wildly,
it may be a cry for help.
Statistically speaking, that's called overfitting. 
ocially speaking, it's called trying too hard.

-- -- --

### Trend: ggplot2

_Plotting with the elegance of a violin plot at a tuxedo gala._

When our data gets more expressive,
and our plots need to level up from "_quick sketch_" to "_conference-ready_",
we turn to the ever-fancy `ggplot2`.
But be warned: `ggplot2` is not just a library, it is a grammar.
A syntax ballet of layers and aesthetics.

_This plotting has its own grammar._

#### Linear Equation

Let us begin our first dance with a simple straight line.

* **14-lm-gg-line.r**

```r
# Load required libraries
library(readr)
library(ggplot2)

# Read data from CSV file
data <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Extract x_values and y_values
x_values <- data$xs
y_values <- data$ys1

# Curve Fitting Order
order <- 1

# Perform linear regression using lm()
lm_model <- lm(y_values ~ 
  poly(x_values, order, raw = TRUE))

# Coefficients
coefficients <- coef(lm_model)

# Reverse order to match output
coefficients <- coefficients[
  length(coefficients):1]

# Print coefficients
cat("Coefficients (a, b):\n\t",
  coefficients, "\n")

# Generate values for the regression line
x_plot <- seq(
  min(x_values), max(x_values),
  length.out = 100)
y_plot <- predict(
  lm_model,
  newdata = data.frame(x_values = x_plot))

# Create data frame for ggplot2
data <- data.frame(x = x_values, y = y_values)

# Plot using ggplot2
plot <- ggplot(data, aes(x = x, y = y)) +
  geom_point(aes(color="Data Points"), size = 0.5) +
  geom_line(
    data = data.frame(x = x_plot, y = y_plot),
    aes(x, y, color="Linear Equation"),
    linewidth = 0.2) +
  labs(
    x = "x", y = "y",
    title = "Straight line fitting") +
  theme_minimal() +
  theme(legend.position = "right",
        legend.text = element_text(size = 2),
        plot.background = element_rect(fill = "white"),
        text = element_text(size = 4)) +
  scale_color_manual(
    name = "Plot",
    breaks = c(
      "Data Points",
      "Linear Equation"),
    values = c(
      "Data Points"="red",
      "Linear Equation"="black")) +
  guides(
    color = guide_legend(
      override.aes = list(
        shape = c(16, NA), linetype = c(0, 1)
    )))

# Save plot as PNG
ggsave("14-lm-gg-line.png",
  plot, width = 800, height = 400, units = "px")
```

Before we build the plot, we prepare the stage.
We generate prediction values from our linear model,
and organize both raw data and predicted values,
into proper `data.frame` structures.

```r
x_plot <- seq(
  min(x_values), max(x_values),
  length.out = 100)
y_plot <- predict(
  lm_model,
  newdata = data.frame(x_values = x_plot))

data <- data.frame(x = x_values, y = y_values)
```



Now the real show begins.
Plot using `ggplot2`.
We assemble plot components piece by piece,
using the `+` operator.
As you can see, there is a lot of plus sign here.
This like an object stacked with another object,
all in one `ggplot2` figure.
The statistical version of LEGO bricks.

```r
plot <- ggplot(data, aes(x = x, y = y)) +
  geom_point(aes(color="Data Points"), size = 0.5) +
  geom_line(
    data = data.frame(x = x_plot, y = y_plot),
    aes(x, y, color="Linear Equation"),
    linewidth = 0.2) +
  labs(
    x = "x", y = "y",
    title = "Straight line fitting") +
  theme_minimal() +
  theme(legend.position = "right",
        legend.text = element_text(size = 2),
        text = element_text(size = 4)) +
  scale_color_manual(
    name = "Plot",
    breaks = c(
      "Data Points",
      "Linear Equation"),
    values = c(
      "Data Points"="red",
      "Linear Equation"="black")) +
  guides(
    color = guide_legend(
      override.aes = list(
        shape = c(16, NA), linetype = c(0, 1)
    )))
```



And finally, we save the plot as a `PNG`,
using pixel-perfect dimensions fit for a blog, report,
or that paper we are totally going to submit before the deadline.

```r
# Save plot as PNG
ggsave("14-lm-gg-line.png",
  plot, width = 800, height = 400, units = "px")
```



The plot result can be shown as follows:



You can obtain the interactive `JupyterLab` in this following link:

* **14-lm-gg-line.r**

With `ggplot2`, our plot becomes both readable and customizable.
It gives us control over every element,
ideal when we want clarity without sacrificing style.

#### Quadratic Curve

Now, we raise the degree of complexity, literally.

By tweaking the data, increasing the model's order,
and adjusting the aesthetic elements just a tad,
we can reuse our `ggplot2` structure for a curvier scenario.

* **15-lm-gg-quadratic.r**

```r
# Load required libraries
library(readr)
library(ggplot2)

# Read data from CSV file
data <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Extract x_values and y_values
x_values <- data$xs
y_values <- data$ys2

# Curve Fitting Order
order <- 2

# Perform quadratic regression using lm()
lm_model <- lm(y_values ~
  poly(x_values, order, raw = TRUE))

# Coefficients
coefficients <- coef(lm_model)

# Reverse order to match output
coefficients <- coefficients[
  length(coefficients):1]

# Print coefficients
cat("Coefficients (a, b, c):\n\t",
  coefficients, "\n")

# Generate values for the quadratic curve
x_plot <- seq(
  min(x_values), max(x_values),
  length.out = 100)
y_plot <- predict(
  lm_model,
  newdata = data.frame(x_values = x_plot))

# Create data frame for ggplot2
data <- data.frame(x = x_values, y = y_values)

# Plot using ggplot2
plot <- ggplot(data, aes(x = x, y = y)) +
  geom_point(aes(color="Data Points"), size = 0.5) +
  geom_line(
    data = data.frame(x = x_plot, y = y_plot),
    aes(x, y, color="Quadratic Curve"),
    linewidth = 0.2) +
  labs(
    x = "x", y = "y",
    title = "Quadratic curve fitting") +
  theme_minimal() +
  theme(legend.position = "right",
        legend.text = element_text(size = 2),
        plot.background = element_rect(fill = "white"),
        text = element_text(size = 4)) +
  scale_color_manual(
    name = "Plot",
    breaks = c(
      "Data Points",
      "Quadratic Curve"),
    values = c(
      "Data Points"="red",
      "Quadratic Curve"="black")) +
  guides(
    color = guide_legend(
      override.aes = list(
        shape = c(16, NA), linetype = c(0, 1)
    )))

# Save plot as PNG
ggsave("15-lm-gg-quadratic.png",
  plot, width = 800, height = 400, units = "px")
```

Explanation

```r
order <- 2
```

The plot result can be shown as follows:



You can obtain the interactive `JupyterLab` in this following link:

* **15-lm-gg-quadratic.r**

Real-world data often bends and twists.
Quadratic fits help us capture those subtle curves,
without spiraling into polynomial madness, yet.

#### Cubic Curve

And finally, for datasets with extra flair (or drama),
we apply a cubic fit. Just as before,
we update the order and reuse the same plotting template.

* **16-lm-gg-cubic.r**

```r
# Load required libraries
library(readr)
library(ggplot2)

# Read data from CSV file
data <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Extract x_values and y_values
x_values <- data$xs
y_values <- data$ys3

# Curve Fitting Order
order <- 3

# Perform cubic regression using lm()
lm_model <- lm(y_values ~
  poly(x_values, order, raw = TRUE))

# Coefficients
coefficients <- coef(lm_model)

# Reverse order to match output
coefficients <- coefficients[
  length(coefficients):1]

# Print coefficients
cat("Coefficients (a, b, c, d):\n\t",
  coefficients, "\n")

# Generate values for the regression line
x_plot <- seq(
  min(x_values), max(x_values),
  length.out = 100)
y_plot <- predict(
  lm_model,
  newdata = data.frame(x_values = x_plot))

# Create data frame for ggplot2
data <- data.frame(x = x_values, y = y_values)

# Plot using ggplot2
plot <- ggplot(data, aes(x = x, y = y)) +
  geom_point(aes(color="Data Points"), size = 0.5) +
  geom_line(
    data = data.frame(x = x_plot, y = y_plot),
    aes(x, y, color="Cubic Curve"),
    linewidth = 0.2) +
  labs(
    x = "x", y = "y",
    title = "Cubic curve fitting") +
  theme_minimal() +
  theme(legend.position = "right",
        legend.text = element_text(size = 2),
        plot.background = element_rect(fill = "white"),
        text = element_text(size = 4)) +
  scale_color_manual(
    name = "Plot",
    breaks = c(
      "Data Points",
      "Cubic Curve"),
    values = c(
      "Data Points"="red",
      "Cubic Curve"="black")) +
  guides(
    color = guide_legend(
      override.aes = list(
        shape = c(16, NA), linetype = c(0, 1)
    )))

# Save plot as PNG
ggsave("16-lm-gg-cubic.png",
  plot, width = 800, height = 400, units = "px")
```

Explanation

```r
order <- 3
```

The plot result can be shown as follows:



You can obtain the interactive `JupyterLab` in this following link:

* **16-lm-gg-cubic.r**

Cubic fits let us catch turning points and inflection.
Great for trends that change direction.
But let's not get carried away.
Beyond cubic, it often stops being insight and starts being noise.

Easy peasy?
Quite so, once we see `ggplot2` for what it really is:
not a plotting tool, but a grammar for visual storytelling.
One where each `+` means and also,
and each `aes()` is our secret decoder ring.

-- -- --

### What's the Next Chapter 🤔?

Our `ggplot2` adventure has drawn a neat little line,
or curve, to a temporary stop.
But as statisticians, we know the story doesn't end at a good plot.

Next, we dive into `R`s building models,
that think in terms of classes and distributions.
Yes, it's time for some character development,
where our data points stop being just dots,
and start acting like they belong to something bigger.

Curious about regression's more sociable cousin?
The one that cares about categories and not just numbers?
Then grab a fresh cup of coffee and head over to:
**Trend - Language - R - Part Two**.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Explore R Programming language visualization with ggplot2.
> Providing the data using linear model.

We are back in `R` land, where plots are beautiful,
models are linear, and the coffee is implied.
This time, our journey ventures beyond just fitting lines,
we begin assigning roles to our data.
Who belongs where? 
hat kind of behavior do they exhibit?
Is this point just an outlier or a misunderstood rebel?

Our mission now is to build classes and extract statistical .r.
Think of this as the Hogwarts Sorting Hat but written in tidyverse.

Plotting trends is lovely, but statistical modeling adds meaning.
It’s what turns our colorful dots into interpretable patterns,
allowing us to classify, explain, and even predict.
In short, it’s where data starts earning its keep.

So let us put our lab coats back on,
keep `ggplot2` within reach,
and continue charting the story where our points not only fit in.
They find their purpose.

Let's continue our previous `R` journey,
with building class and statistical .r.

-- -- --

### Trend: Building Class

Real life experience requrie us to manage our code.
This tidying process often be done by creating a class.
This tedious process usually started by making the function first,
then move them to a class.

We cannot afford a spaghetti bowl of copy-pasted code chunks
We need to get civilized.
That means tidying up with functions, and eventually,
wrapping everything into a class.

But of course, like all noble things in statistics,
it starts with a tiny bit of suffering.

#### Refactor to Function

Let's make move the plain code above to a function.
The problem with function is we need a bunch variables,
for input and output between function.

* **17-lm-function.r**

```r
# Load required libraries
library(readr)
library(ggplot2)

generate_regression <- function(x_values, y_values, order) {
  # Perform regression using lm()
  lm_model <- lm(y_values ~ 
    poly(x_values, order, raw = TRUE))
  
  # Generate values for the regression line
  x_plot <- seq(
    min(x_values), max(x_values),
    length.out = 100)
  y_plot <- predict(
    lm_model,
    newdata = data.frame(x_values = x_plot))
  
  # Return a list containing all relevant objects
  return(list(
    order = order,
    x_values = x_values,
    y_values = y_values,
    lm_model = lm_model,
    x_plot = x_plot,
    y_plot = y_plot
  ))
}

show_coeff <- function(regression_data) {
  order    <- regression_data$order
  lm_model <- regression_data$lm_model

  # Define a named vector
  # to map order numbers to curve types
  coeff_text <- c(
    "(a, b)" = 1, "(a, b, c)" = 2, "(a, b, c, d)" = 3)
  order_text <- c(
    "Linear" = 1, "Quadratic" = 2, "Cubic" = 3)

  # Print the curve type
  cat(paste("Using lm_model :",
    names(order_text)[order], "\n"))

  # Coefficients
  coefficients <- coef(lm_model)

  # Reverse order to match output
  coefficients <- coefficients[
    length(coefficients):1]

  # Print coefficients
  cat("Coefficients ",
    names(coeff_text)[order], ":\n\t",
    coefficients, "\n")
}

create_plot <- function(
    regression_data, title, label, pngfile) {

  x_values <- regression_data$x_values
  y_values <- regression_data$y_values
  x_plot   <- regression_data$x_plot
  y_plot   <- regression_data$y_plot

  # Create data frame for ggplot2
  data <- data.frame(x = x_values, y = y_values)

  # Create breaks and values vectors
  breaks <- c("Data Points", "Regression")
  values <- c("Data Points" = "red", "Regression" = "black")

  # Plot using ggplot2
  plot <- ggplot(data, aes(x = x, y = y)) +
    geom_point(aes(color="Data Points"), size = 0.5) +
    geom_line(
      data = data.frame(x = x_plot, y = y_plot),
      aes(x, y, color = "Regression"), linewidth = 0.2) +
    labs(
      x = "x", y = "y", title = title) +
    theme_minimal() +
    theme(legend.position = "right",
        plot.background = element_rect(fill = "white"),
        text = element_text(size = 4)) +
    scale_color_manual(
      name = "Plot",
      breaks = breaks,
      values = values) +
    guides(
      color = guide_legend(
        override.aes = list(
          shape = c(16, NA), linetype = c(0, 1)
      )))

  # Save plot as PNG
  ggsave(pngfile,
    plot, width = 800, height = 400,
    units = "px", device = "png")
}

# Read data from CSV file
series <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Call the function and get regression line data
regress_1 <- generate_regression(
  series$xs, series$ys1, 1)
regress_2 <- generate_regression(
  series$xs, series$ys2, 2)
regress_3 <- generate_regression(
  series$xs, series$ys3, 3)

# Perform linear regression and plot
show_coeff(regress_1)
create_plot(regress_1,
  "Straight line fitting",
  "Linear Equation",
  "14-lm-gg-line.png")

# Perform quadratic regression and plot
show_coeff(regress_2)
create_plot(regress_2,
  "Quadratic curve fitting",
  "Quadratic Curve",
  "15-lm-gg-quadratic.png")

# Perform cubic regression and plot
show_coeff(regress_3)
create_plot(regress_3,
  "Cubic curve fitting",
  "Cubic Curve",
  "16-lm-gg-cubic.png")
```

Let’s load our toolkit first:

```r
library(readr)
library(ggplot2)
```

Then put the code to function one at a time,
for example this `generate_regression` function,
that performing regression using `lm()`,
generate values for the regression line,
and finally return a list containing all relevant objects.

```r
generate_regression <- function(x_values, y_values, order) {
  ...

  return(list(
    order = order,
    x_values = x_values,
    y_values = y_values,
    lm_model = lm_model,
    x_plot = x_plot,
    y_plot = y_plot
  ))
}
```

Then we can use the regression data,
to show the coefficient.

```r
show_coeff <- function(regression_data) {
  order    <- regression_data$order
  lm_model <- regression_data$lm_model

  ...
}
```

And finally, wrap the plot in a `create_plot` function, to do the artistic bit.

```r
create_plot <- function(
    regression_data, title, label, pngfile) {

  x_values <- regression_data$x_values
  y_values <- regression_data$y_values
  x_plot   <- regression_data$x_plot
  y_plot   <- regression_data$y_plot

  ...
}
```



Once we have our function army,
we just call them in order,
in main script, the outer block of the code.
Like conducting a linear symphony:

```r
regress_1 <- generate_regression(
  series$xs, series$ys1, 1)
regress_2 <- generate_regression(
  series$xs, series$ys2, 2)
regress_3 <- generate_regression(
  series$xs, series$ys3, 3)

show_coeff(regress_1)
create_plot(regress_1,
  "Straight line fitting",
  "Linear Equation",
  "14-lm-gg-line.png")

...
```



Want to tinker interactively? Here's the `JupyterLab notebook`:

* **17-lm-function.ipynb**

Functions reduce code duplication,
prevent us from losing our sanity,
and make our scripts more readable.
Even by our future selves.

#### Merging The Plot

Instead of generating separate plots for each regression order,
let’s go full ensemble cast.
Same input, multiple fits, one shared stage.

* **18-lm-merge.r**

```r
# Load required libraries
library(readr)
library(ggplot2)

generate_regressions <- function(x_values, y_values) {
  # Independent x values.
  x_plot <- seq(
    min(x_values), max(x_values),
    length.out = 100)

  print(length(x_values))
  print(length(x_plot))

  # Generate values for the linear regression
  lm_model_1 <- lm(y_values ~ 
    poly(x_values, 1, raw = TRUE))
  y_plot_1 <- predict(
    lm_model_1,
    newdata = data.frame(x_values = x_plot))

  # Generate values for the quadratic regression
  lm_model_2 <- lm(y_values ~ 
    poly(x_values, 2, raw = TRUE))
  y_plot_2 <- predict(
    lm_model_2,
    newdata = data.frame(x_values = x_plot))

  # Generate values for the cubic regression
  lm_model_3 <- lm(y_values ~ 
    poly(x_values, 3, raw = TRUE))
  y_plot_3 <- predict(
    lm_model_3,
    newdata = data.frame(x_values = x_plot))

  # Return a list containing all relevant objects
  return(list(
    x_values = x_values,
    y_values = y_values,
    lm_model_1 = lm_model_1,
    lm_model_2 = lm_model_2,
    lm_model_3 = lm_model_3,
    x_plot   = x_plot,
    y_plot_1 = y_plot_1,
    y_plot_2 = y_plot_2,
    y_plot_3 = y_plot_3
  ))
}

show_coeff <- function(order, lm_model) {
  # Define a named vector
  # to map order numbers to curve types
  coeff_text <- c(
    "(a, b)" = 1, "(a, b, c)" = 2, "(a, b, c, d)" = 3)
  order_text <- c(
    "Linear" = 1, "Quadratic" = 2, "Cubic" = 3)

  # Print the curve type
  cat(paste("Using lm_model :",
    names(order_text)[order], "\n"))

  # Coefficients
  coefficients <- coef(lm_model)

  # Reverse order to match output
  coefficients <- coefficients[
    length(coefficients):1]

  # Print coefficients
  cat("Coefficients ",
    names(coeff_text)[order], ":\n\t",
    coefficients, "\n")
}

create_plot <- function(regression_data) {
  x_values <- regression_data$x_values
  y_values <- regression_data$y_values
  x_plot   <- regression_data$x_plot
  y_plot_1 <- regression_data$y_plot_1
  y_plot_2 <- regression_data$y_plot_2
  y_plot_3 <- regression_data$y_plot_3

  # Create data frame for ggplot2
  data <- data.frame(x = x_values, y = y_values)

  # Plot using ggplot2
  plot <- ggplot(data, aes(x = x, y = y, color = "Data Points")) +
    geom_point(size = 0.5) +
    geom_line(
      data = data.frame(x = x_plot, y = y_plot_1),
      aes(x = x, y = y, color = "Linear Equation"),
      linewidth = 0.2) +
    geom_line(
      data = data.frame(x = x_plot, y = y_plot_2),
      aes(x = x, y = y, color = "Quadratic Curve"),
      linewidth= 0.2) +
    geom_line(
      data = data.frame(x = x_plot, y = y_plot_3),
      aes(x = x, y = y, color = "Cubic Curve"),
      linewidth = 0.2) +
    labs(
      x = "x", y = "y",
      title = "Polynomial Curve Fitting") +
    theme_minimal() +
    theme(legend.position = "right",
          legend.text = element_text(size = 2),
          plot.background = element_rect(fill = "white"),
          text = element_text(size = 4)) +
    scale_color_manual(
      name = "Plot",
      breaks = c(
        "Data Points",
        "Linear Equation",
        "Quadratic Curve",
        "Cubic Curve"),
      values = c(
        "Data Points" = "black",
        "Linear Equation" = "red", 
        "Quadratic Curve" = "green", 
        "Cubic Curve" = "blue")) +
    guides(
      color = guide_legend(
        override.aes = list(
          shape = c(4, NA), linetype = c(0, 1)
        )))

  # Save plot as PNG
  ggsave("18-lm-merge.png", plot,
    width = 800, height = 400, units = "px")
}

# Read data from CSV file
series <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Get regression data
regress <- generate_regressions(
    series$xs, series$ys3)

# Perform linear regression and plot
show_coeff(1, regress$lm_model_1)
show_coeff(2, regress$lm_model_2)
show_coeff(3, regress$lm_model_3)
create_plot(regress)
```

Here’s the new function skeleton:

```r
generate_regressions <- function(x_values, y_values) {
  ...
}

show_coeff <- function(order, lm_model) {
  ...
}

create_plot <- function(regression_data) {
  ...
}
```



Now we can call the function in main script.
Get the regression data.
And perform linear regression and plot.

```r
regress <- generate_regressions(
    series$xs, series$ys3)

show_coeff(1, regress$lm_model_1)
show_coeff(2, regress$lm_model_2)
show_coeff(3, regress$lm_model_3)
plot <- create_plot(regress)
```



This time, we fit linear, quadratic,
and cubic curves and show them all in a single elegant plot.

The plot result can be shown as follows.
You can see that in the legend, it lost one color.
The green one for quadratic curve legend does not shown well.
You can solve this by removing the guides.



Interactive notebook available here:

* **18-lm-merge.ipynb**

The problem with function is we need a bunch variables,
for input and output between function.

#### Using R6 Class

Instead of function me can wrap them all into a class.
`R` has a few kind of class implementation,
one of them is `R6`

* **19-lm-merge.r**

```r
# Load required libraries
library(readr)
library(ggplot2)
library(R6)

CurveFitting <- R6Class("CurveFitting",

  public = list(
    xs  = NULL, ys  = NULL,
    lm1 = NULL, lm2 = NULL, lm3 = NULL,
    xp  = NULL, yp1 = NULL, yp2 = NULL, yp3 = NULL,

    initialize = function(xs, ys) {
      self$xs <- xs
      self$ys <- ys
    },

    generate_regressions = function() {
      # Keep the variable name for data frame
      x_values <- self$xs
    
      # Independent x values.
      self$xp <- seq(
        min(x_values), max(x_values),
        length.out = 100)

      # Generate values for the linear regression
      self$lm1 <- lm(self$ys ~
        poly(x_values, 1, raw = TRUE))
      self$yp1 <- predict(self$lm1,
        newdata = data.frame(x_values = self$xp))

      # Generate values for the quadratic regression
      self$lm2 <- lm(self$ys ~
        poly(x_values, 2, raw = TRUE))
      self$yp2 <- predict(self$lm2,
        newdata = data.frame(x_values = self$xp))

      # Generate values for the cubic regression
      self$lm3 <- lm(self$ys ~
        poly(x_values, 3, raw = TRUE))
      self$yp3 <- predict(self$lm3,
        newdata = data.frame(x_values = self$xp))
    },

    show_coeff = function(order, lm_model) {
      # Define a named vector
      # to map order numbers to curve types
      coeff_text <- c(
        "(a, b)" = 1, "(a, b, c)" = 2,
        "(a, b, c, d)" = 3)
      order_text <- c(
        "Linear" = 1, "Quadratic" = 2, "Cubic" = 3)

      # Print the curve type
      cat(paste("Using lm_model :",
        names(order_text)[order], "\n"))

      # Coefficients
      coefficients <- coef(lm_model)

      # Reverse order to match output
      coefficients <- coefficients[
        length(coefficients):1]

      # Print coefficients
      cat("Coefficients ",
        names(coeff_text)[order], ":\n\t",
        coefficients, "\n")
    },

    show_coeffs = function() {
      self$show_coeff(1, self$lm1)
      self$show_coeff(2, self$lm2)
      self$show_coeff(3, self$lm3)
    },

    create_plot = function() {
      # Create data frame for ggplot2
      data <- data.frame(x = self$xs, y = self$ys)

      # Plot using ggplot2
      plot <- ggplot(data,
          aes(x = x, y = y, color = "Data Points")) +
        geom_point(size = 0.5) +
        geom_line(
          data = data.frame(x = self$xp, y = self$yp1),
          aes(x = x, y = y, color = "Linear Equation"),
          linewidth = 0.2) +
        geom_line(
          data = data.frame(x = self$xp, y = self$yp2),
          aes(x = x, y = y, color = "Quadratic Curve"),
          linewidth = 0.2) +
        geom_line(
          data = data.frame(x = self$xp, y = self$yp3),
          aes(x = x, y = y, color = "Cubic Curve"),
          linewidth = 0.2) +
        labs(
          x = "x", y = "y",
          title = "Polynomial Curve Fitting") +
        theme_minimal() +
        theme(
          legend.position = "right",
          legend.text = element_text(size = 2),
          plot.background = element_rect(fill = "white"),
          text = element_text(size = 4)
        ) +
        scale_color_manual(
          name = "Plot",
          breaks = c(
            "Data Points",
            "Linear Equation",
            "Quadratic Curve",
            "Cubic Curve"),
          values = c(
            "Data Points" = "black",
            "Linear Equation" = "red", 
            "Quadratic Curve" = "green", 
            "Cubic Curve" = "blue"))

      # Save plot as PNG
      ggsave("19-lm-merge.png", plot,
        width = 800, height = 400, units = "px")
    }
  )
)

# Read data from CSV file
series <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Create CurveFitting object
# Perform linear regression, display, and plot
curve_fitting <- CurveFitting$new(
  series$xs, series$ys3)
curve_fitting$generate_regressions()
curve_fitting$show_coeffs()
curve_fitting$create_plot()
```

Here's a trimmed `R6` class skeleton for curve fitting:

```r
CurveFitting <- R6Class("CurveFitting",

  public = list(
    xs  = NULL, ys  = NULL,
    lm1 = NULL, lm2 = NULL, lm3 = NULL,
    xp  = NULL, yp1 = NULL, yp2 = NULL, yp3 = NULL,

    initialize = function(xs, ys) {
      self$xs <- xs
      self$ys <- ys
    },

    generate_regressions = function() {
      ...
    },

    show_coeff = function(order, lm_model) {
      ...
    },

    show_coeffs = function() {
      self$show_coeff(1, self$lm1)
      self$show_coeff(2, self$lm2)
      self$show_coeff(3, self$lm3)
    },

    create_plot = function() {
      ...
    }
  )
)
```



Now our main script is clean, and elegant, become maintainable:
We can instantiate the `CurveFitting` class in main script.
Then perform linear regression, display, finally and create the plot.

```r
curve_fitting <- CurveFitting$new(series$xs, series$ys3)
curve_fitting$generate_regressions()
curve_fitting$show_coeffs()
curve_fitting$create_plot()
```



The plot result can be shown as follows:



You can obtain the interactive `JupyterLab` in this following link:

* **19-lm-merge.ipynb**

Classes let us organize code like grown-ups.
They encapsulate both data and behavior,
letting us focus on logic instead of plumbing.

#### Built in Plot (alternative)

If `ggplot2` feels like overkill for quick-and-dirty plots
we can use `R`'s base plotting system.
Less pretty, but still gets the job done.

* **19-lm-merge-alt.r**

```r
# Load required libraries
library(readr)
library(ggplot2)
library(R6)

CurveFitting <- R6Class("CurveFitting",

  public = list(
    xs  = NULL, ys  = NULL,
    lm1 = NULL, lm2 = NULL, lm3 = NULL,
    xp  = NULL, yp1 = NULL, yp2 = NULL, yp3 = NULL,

    initialize = function(xs, ys) {
      self$xs <- xs
      self$ys <- ys
    },

    generate_regressions = function() {
      # Keep the variable name for data frame
      x_values <- self$xs
    
      # Independent x values.
      self$xp <- seq(
        min(x_values), max(x_values),
        length.out = 100)

      # Generate values for the linear regression
      self$lm1 <- lm(self$ys ~
        poly(x_values, 1, raw = TRUE))
      self$yp1 <- predict(self$lm1,
        newdata = data.frame(x_values = self$xp))

      # Generate values for the quadratic regression
      self$lm2 <- lm(self$ys ~
        poly(x_values, 2, raw = TRUE))
      self$yp2 <- predict(self$lm2,
        newdata = data.frame(x_values = self$xp))

      # Generate values for the cubic regression
      self$lm3 <- lm(self$ys ~
        poly(x_values, 3, raw = TRUE))
      self$yp3 <- predict(self$lm3,
        newdata = data.frame(x_values = self$xp))
    },

    show_coeff = function(order, lm_model) {
      # Define a named vector
      # to map order numbers to curve types
      coeff_text <- c(
        "(a, b)" = 1, "(a, b, c)" = 2,
        "(a, b, c, d)" = 3)
      order_text <- c(
        "Linear" = 1, "Quadratic" = 2, "Cubic" = 3)

      # Print the curve type
      cat(paste("Using lm_model :",
        names(order_text)[order], "\n"))

      # Coefficients
      coefficients <- coef(lm_model)

      # Reverse order to match output
      coefficients <- coefficients[
        length(coefficients):1]

      # Print coefficients
      cat("Coefficients ",
        names(coeff_text)[order], ":\n\t",
        coefficients, "\n")
    },

    show_coeffs = function() {
      self$show_coeff(1, self$lm1)
      self$show_coeff(2, self$lm2)
      self$show_coeff(3, self$lm3)
    },

    create_plot = function() {
      # Open PNG graphics device
      png("19-lm-merge-alt.png",
        width = 800, height = 400)

      # Plot data points
      plot(self$xs, self$ys,
        col = "black", pch = 20,
        xlab = "x", ylab = "y",
        main = "Polynomial Curve Fitting")

      # Plot regression lines
      lines(self$xp, self$yp1, col = "red", lwd = 2)
      lines(self$xp, self$yp2, col = "green", lwd = 2)
      lines(self$xp, self$yp3, col = "blue", lwd = 2)

      # Add legend
      legend("topright",
         legend = c("Data Points", "Linear Equation",
                    "Quadratic Curve", "Cubic Curve"),
         col = c("black", "red", "green", "blue"),
         pch = c(20, NA, NA, NA), lwd = c(NA, 2, 2, 2))
    }
  )
)

# Read data from CSV file
series <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Create CurveFitting object
# Perform linear regression, display, and plot
curve_fitting <- CurveFitting$new(
  series$xs, series$ys3)
curve_fitting$generate_regressions()
curve_fitting$show_coeffs()
curve_fitting$create_plot()
```

Explanation

```r
    create_plot = function() {
      # Open PNG graphics device
      png("19-lm-merge-alt.png",
        width = 800, height = 400)

      # Plot data points
      plot(self$xs, self$ys,
        col = "black", pch = 20,
        xlab = "x", ylab = "y",
        main = "Polynomial Curve Fitting")

      # Plot regression lines
      lines(self$xp, self$yp1, col = "red", lwd = 2)
      lines(self$xp, self$yp2, col = "green", lwd = 2)
      lines(self$xp, self$yp3, col = "blue", lwd = 2)

      # Add legend
      legend("topright",
         legend = c("Data Points", "Linear Equation",
                    "Quadratic Curve", "Cubic Curve"),
         col = c("black", "red", "green", "blue"),
         pch = c(20, NA, NA, NA), lwd = c(NA, 2, 2, 2))
    }
```



The plot result can be shown as follows:



You can obtain the interactive `JupyterLab` in this following link:

* **19-lm-merge-alt.ipynb**

Note that, not everything should be well structured.
Sometimes, fast and messy wins the race.
For simple thing, we'd better use shortcut as possible,
as will be shown in the next `R` article.

-- -- --

### Statistic .r

> A Gentle Madness in Methodology

In this section, we explore how` R` handles statistical .r.
Let's begin with least squares.
It is our trusty wrench for fitting lines through chaos.

#### Manual Calculation

We begin by rolling up our sleeves,
and manually calculating the statistical .r.
This is where we pretend we are living in the 1950s,
and calculators are still furniture.

You can check the code in this classic beauty:

* **51-lq-manual.r**

```r
# Load required library
library(readr)

# Read CSV file
pairCSV <- read.csv("50-samples.csv", header = TRUE)

# Extract x and y values from CSV data
x_observed <- pairCSV[, 1]
y_observed <- pairCSV[, 2]

# Number of data points
n <- length(x_observed)

# Calculate sums
x_sum <- sum(x_observed)
y_sum <- sum(y_observed)

# Calculate means
x_mean <- mean(x_observed)
y_mean <- mean(y_observed)

# Output of basic properties
cat(sprintf("%-10s = %4d\n", "n", n))
cat(sprintf("∑x (total) = %7.2f\n", x_sum))
cat(sprintf("∑y (total) = %7.2f\n", y_sum))
cat(sprintf("x̄ (mean)   = %7.2f\n", x_mean))
cat(sprintf("ȳ (mean)   = %7.2f\n\n", y_mean))

# Calculate deviations
x_deviation <- x_observed - x_mean
y_deviation <- y_observed - y_mean

# Calculate squared deviations
x_sq_deviation <- sum(x_deviation^2)
y_sq_deviation <- sum(y_deviation^2)

# Calculate cross-deviation
xy_cross_deviation <- sum(x_deviation * y_deviation)

# Calculate slope (m) and intercept (b)
m_slope <- xy_cross_deviation / x_sq_deviation
b_intercept <- y_mean - m_slope * x_mean

# Output of least square calculation
cat(sprintf("∑(xᵢ-x̄)    = %9.2f\n", sum(x_deviation)))
cat(sprintf("∑(yᵢ-ȳ)    = %9.2f\n", sum(y_deviation)))
cat(sprintf("∑(xᵢ-x̄)²   = %9.2f\n", x_sq_deviation))
cat(sprintf("∑(yᵢ-ȳ)²   = %9.2f\n", y_sq_deviation))
cat(sprintf("∑(xᵢ-x̄)(yᵢ-ȳ)  = %9.2f\n", xy_cross_deviation))
cat(sprintf("m (slope)      = %9.2f\n", m_slope))
cat(sprintf("b (intercept)  = %9.2f\n\n", b_intercept))

cat(sprintf("Equation     y = %5.2f + %5.2f.x\n\n", b_intercept, m_slope))

# Calculate variance
x_variance <- x_sq_deviation / (n-1)
y_variance <- y_sq_deviation / (n-1)

# Calculate covariance
xy_covariance <- xy_cross_deviation / (n-1)

# Calculate standard deviations
x_std_dev <- sqrt(x_variance)
y_std_dev <- sqrt(y_variance)

# Calculate Pearson correlation coefficient (r)
r <- xy_covariance / (x_std_dev * y_std_dev)

# Calculate R-squared (R²)
r_squared <- r^2

# Output of correlation calculation
cat(sprintf("sₓ² (variance) = %9.2f\n", x_variance))
cat(sprintf("sy² (variance) = %9.2f\n", y_variance))
cat(sprintf("covariance     = %9.2f\n", xy_covariance))
cat(sprintf("sₓ (std dev)   = %9.2f\n", x_std_dev))
cat(sprintf("sy (std dev)   = %9.2f\n", y_std_dev))
cat(sprintf("r (pearson)    = %9.2f\n", r))
cat(sprintf("R²             = %9.2f\n\n", r_squared))

# Create regression line
y_fit <- m_slope * x_observed + b_intercept
y_err <- y_observed - y_fit

# Calculate sum of squared residuals
ss_residuals <- sum(y_err^2)

# Calculate degrees of freedom
df <- n - 2

# Calculate variance of residuals (MSE)
var_residuals <- ss_residuals / df

# Calculate standard error of the slope
std_err_slope <- sqrt(var_residuals / x_sq_deviation)

# Calculate t-value
t_value <- m_slope / std_err_slope

# Output the results
cat(sprintf("SSR = ∑ϵ²           = %9.2f\n", ss_residuals))
cat(sprintf("MSE = ∑ϵ²/(n-2)     = %9.2f\n", var_residuals))
cat(sprintf("SE(β₁)  = √(MSE/sₓ) = %9.2f\n", std_err_slope))
cat(sprintf("t-value = β̅₁/SE(β₁) = %9.2f\n", t_value))
```

Explanation

```r
...
# Calculate deviations
x_deviation <- x_observed - x_mean
y_deviation <- y_observed - y_mean

# Calculate squared deviations
x_sq_deviation <- sum(x_deviation^2)
y_sq_deviation <- sum(y_deviation^2)
...
```



And here’s the interactive `JupyterLab` version,
because typing is cardio:

* **51-lq-manual.ipynb**

Manual calculation forces us to look math in the eye.
It teaches us what each number really means,
before the built-in functions whisk them away.

#### Using Built-in Method

Of course, `R` comes with built-in functions.
Not everyone wants to do math like a statistician in a log cabin.

* **52-lq-built-in.r**

```r
# Read CSV file
pairCSV <- read.csv("50-samples.csv", header = TRUE)

# Extract x and y values from CSV data
x_observed <- pairCSV[, 1]
y_observed <- pairCSV[, 2]

# Number of data points
n <- length(x_observed)

# Calculate sums
x_sum <- sum(x_observed)
y_sum <- sum(y_observed)

# Calculate means
x_mean <- mean(x_observed)
y_mean <- mean(y_observed)

# Output of basic properties
cat(sprintf("%-10s = %4d\n", "n", n))
cat(sprintf("∑x (total) = %7.2f\n", x_sum))
cat(sprintf("∑y (total) = %7.2f\n", y_sum))
cat(sprintf("x̄ (mean)   = %7.2f\n", x_mean))
cat(sprintf("ȳ (mean)   = %7.2f\n\n", y_mean))

# Calculate deviations
x_deviation <- x_observed - x_mean
y_deviation <- y_observed - y_mean

# Calculate squared deviations
x_sq_deviation <- sum(x_deviation^2)
y_sq_deviation <- sum(y_deviation^2)

# Calculate cross-deviation
xy_cross_deviation <- sum(
  x_deviation * y_deviation)

# Calculate slope (m) and intercept (b)
m_slope <- lm(y_observed ~
  x_observed)$coefficients[2]
b_intercept <- lm(y_observed ~
  x_observed)$coefficients[1]

# Output of least square calculation
cat(sprintf("∑(xᵢ-x̄)    = %9.2f\n", sum(x_deviation)))
cat(sprintf("∑(yᵢ-ȳ)    = %9.2f\n", sum(y_deviation)))
cat(sprintf("∑(xᵢ-x̄)²   = %9.2f\n", x_sq_deviation))
cat(sprintf("∑(yᵢ-ȳ)²   = %9.2f\n", y_sq_deviation))
cat(sprintf("∑(xᵢ-x̄)(yᵢ-ȳ)  = %9.2f\n", xy_cross_deviation))
cat(sprintf("m (slope)      = %9.2f\n", m_slope))
cat(sprintf("b (intercept)  = %9.2f\n\n", b_intercept))

cat(sprintf("Equation     y = %5.2f + %5.2f.x\n\n", b_intercept, m_slope))

# Calculate variance
x_variance <- var(x_observed)
y_variance <- var(y_observed)

# Calculate covariance
xy_covariance <- cov(x_observed, y_observed)

# Calculate standard deviations
x_std_dev <- sd(x_observed)
y_std_dev <- sd(y_observed)

# Calculate Pearson correlation coefficient (r)
r <- cor(x_observed, y_observed)

# Calculate R-squared (R²)
r_squared <- r^2

# Output of correlation calculation
cat(sprintf("sₓ² (variance) = %9.2f\n", x_variance))
cat(sprintf("sy² (variance) = %9.2f\n", y_variance))
cat(sprintf("covariance     = %9.2f\n", xy_covariance))
cat(sprintf("sₓ (std dev)   = %9.2f\n", x_std_dev))
cat(sprintf("sy (std dev)   = %9.2f\n", y_std_dev))
cat(sprintf("r (pearson)    = %9.2f\n", r))
cat(sprintf("R²             = %9.2f\n\n", r_squared))

# Calculate residuals
residuals <- residuals(lm(y_observed ~ x_observed))

# Calculate sum of squared residuals
ss_residuals <- sum(residuals^2)

# Calculate degrees of freedom
df <- n - 2

# Calculate variance of residuals (MSE)
var_residuals <- ss_residuals / df

# Calculate standard error of the slope
std_err_slope <- sqrt(var_residuals / x_sq_deviation)

# Calculate t-value
t_value <- m_slope / std_err_slope

# Output the results
cat(sprintf("SSR = ∑ϵ²           = %9.2f\n", ss_residuals))
cat(sprintf("MSE = ∑ϵ²/(n-2)     = %9.2f\n", var_residuals))
cat(sprintf("SE(β₁)  = √(MSE/sₓ) = %9.2f\n", std_err_slope))
cat(sprintf("t-value = β̅₁/SE(β₁) = %9.2f\n", t_value))
```

Explanation

```r
...
# Calculate slope (m) and intercept (b)
m_slope <- lm(y_observed ~
  x_observed)$coefficients[2]
b_intercept <- lm(y_observed ~
  x_observed)$coefficients[1]
...
```



Not everything in `R` has a built-in method shortcut.
And honestly, I must admit I haven’t explored,
every corner of the statistical attic.

However, here is the full summary from the script,
where every Greek letter finds a home:

```output
❯ Rscript 52-lq-built-in.r
n          =   13
∑x (total) =   78.00
∑y (total) = 2327.00
x̄ (mean)   =    6.00
ȳ (mean)   =  179.00

∑(xᵢ-x̄)    =      0.00
∑(yᵢ-ȳ)    =      0.00
∑(xᵢ-x̄)²   =    182.00
∑(yᵢ-ȳ)²   = 309218.00
∑(xᵢ-x̄)(yᵢ-ȳ)  =   7280.00
m (slope)      =     40.00
b (intercept)  =    -61.00

Equation     y = -61.00 + 40.00.x

sₓ² (variance) =     15.17
sy² (variance) =  25768.17
covariance     =    606.67
sₓ (std dev)   =      3.89
sy (std dev)   =    160.52
r (pearson)    =      0.97
R²             =      0.94

SSR = ∑ϵ²           =  18018.00
MSE = ∑ϵ²/(n-2)     =   1638.00
SE(β₁)  = √(MSE/sₓ) =      3.00
t-value = β̅₁/SE(β₁) =     13.33
```

**Fun fact**: a `t-value` above 13 is basically,
statistics yelling “this slope really matters.”

Interactive version? Of course:

* **52-lq-built-in.ipynb**

The result is the same with the python counterpart.

Knowing both manual and automated approaches,
allows us to debug, audit, and impress colleagues at parties.
Annoy people in WhatsApp groups at 2AM with unsolicited regression facts.

#### Visualization

However, I guess the `lm` above is,
enough to calculate regression line.
And then we can combine scatter plot and regression line.

* **53-lq-plot.r**

```r
# Load required libraries
library(ggplot2)

# Read CSV file
pairCSV <- read.csv("50-samples.csv", header = TRUE)

# Extract x and y values from CSV data
x_observed <- pairCSV[, 1]
y_observed <- pairCSV[, 2]

# Create a data frame with x and y observed values
data <- data.frame(x_observed, y_observed)

# Create a scatter plot of the observed data points
scatter_plot <- ggplot(
    data,
    aes(x = x_observed, y = y_observed),
    linewidth = 0.2) +
  geom_point(size = 0.5) +
  labs(x = "x", y = "y",
    title = "Scatter Plot of Observed Data") +
  theme_minimal() +
  theme(
    text = element_text(size = 4),
    plot.background = element_rect(fill = "white")) 

# Calculate slope (m) and intercept (b)
m_slope <- lm(y_observed ~
  x_observed)$coefficients[2]
b_intercept <- lm(y_observed ~
  x_observed)$coefficients[1]

# Calculate regression line
regression_line <- geom_abline(
  intercept = b_intercept, slope = m_slope,
  color = "red")

# Combine scatter plot and regression line
plot <- scatter_plot + regression_line

# Save plot as PNG
ggsave("53-lq-plot.png", plot,
  width = 800, height = 400, units = "px")
```

We can start with usual scatter plot,
always the opening act:

Then add this regression line part the to plot grammar.

```r
regression_line <- geom_abline(
  intercept = b_intercept, slope = m_slope,
  color = "red")

plot <- scatter_plot + regression_line
```



The plot result can be shown as follows:



Interactive version here—click it before your coffee cools:

* **53-lq-plot.ipynb**

Visualizing helps us catch errors, spot patterns, and pretend we are data artists.

#### Additional .r

Beyond the slope and intercept,
there's more personality to explore in our data.
Kurtosis and skewness tell us about tails and symmetry.
Like a weather report for distributions.

To do this, we need the `e1071` package,
which sounds like a robot but computes like a dream.

* **61-additional.r**

```r
# Load required library
library(e1071)

# Read CSV file
pairCSV <- read.csv("50-samples.csv", header = TRUE)

# Extract x and y values from CSV data
x_observed <- pairCSV[[1]]
y_observed <- pairCSV[[2]]

# Number of data points
n <- length(x_observed)

# Calculate maximum, minimum, and range
x_max <- max(x_observed)
x_min <- min(x_observed)
x_range <- x_max - x_min

y_max <- max(y_observed)
y_min <- min(y_observed)
y_range <- y_max - y_min

# Output of maximum, minimum, and range
cat(sprintf('x (max, min, range) = (%7.2f, %7.2f, %7.2f )\n', x_min, x_max, x_range))
cat(sprintf('y (max, min, range) = (%7.2f, %7.2f, %7.2f )\n\n', y_min, y_max, y_range))

x_median <- median(x_observed)
y_median <- median(y_observed)

# Mode
x_mode <- as.numeric(names(which.max(table(x_observed))))
y_mode <- as.numeric(names(which.max(table(y_observed))))

# Output of additional properties
cat(sprintf('x median       = %9.2f\n', x_median))
cat(sprintf('y median       = %9.2f\n', y_median))
cat(sprintf('x mode         = %9.2f\n', x_mode))
cat(sprintf('y mode         = %9.2f\n\n', y_mode))

# Calculate kurtosis and skewness
x_kurtosis <- kurtosis(x_observed)
y_kurtosis <- kurtosis(y_observed)

x_skewness <- skewness(x_observed)
y_skewness <- skewness(y_observed)

cat(sprintf('x kurtosis     = %9.2f\n', x_kurtosis))
cat(sprintf('y kurtosis     = %9.2f\n', y_kurtosis))
cat(sprintf('x skewness     = %9.2f\n', x_skewness))
cat(sprintf('y skewness     = %9.2f\n\n', y_skewness))

# Calculate SE kurtosis and SE skewness
calc_se_kurtosis_gaussian <- function(n) {
  sqrt(4 * n^2 * calc_se_skewness(n)^2 / ((n - 3) * (n + 5)))
}

calc_se_skewness <- function(n) {
  sqrt((6 * n * (n - 1)) / ((n - 2) * (n + 1) * (n + 3)))
}

# Number of data points
x_n <- length(x_observed)
y_n <- length(y_observed)

x_se_kurtosis <- calc_se_kurtosis_gaussian(x_n)
y_se_kurtosis <- calc_se_kurtosis_gaussian(y_n)
x_se_skewness <- calc_se_skewness(x_n)
y_se_skewness <- calc_se_skewness(y_n)

cat(sprintf('x SE kurtosis  = %9.2f\n', x_se_kurtosis))
cat(sprintf('y SE kurtosis  = %9.2f\n', y_se_kurtosis))
cat(sprintf('x SE skewness  = %9.2f\n', x_se_skewness))
cat(sprintf('y SE skewness  = %9.2f\n', y_se_skewness))
```

Explanation

```r
x_kurtosis <- kurtosis(x_observed)
y_kurtosis <- kurtosis(y_observed)

x_skewness <- skewness(x_observed)
y_skewness <- skewness(y_observed)

cat(sprintf('x kurtosis     = %9.2f\n', x_kurtosis))
cat(sprintf('y kurtosis     = %9.2f\n', y_kurtosis))
cat(sprintf('x skewness     = %9.2f\n', x_skewness))
cat(sprintf('y skewness     = %9.2f\n\n', y_skewness))
```



Here’s the statistical gossip.
The result is not really the same with the python counterpart.

```output
❯ Rscript 61-additional.r
x (max, min, range) = (   0.00,   12.00,   12.00 )
y (max, min, range) = (   5.00,  485.00,  480.00 )

x median       =      6.00
y median       =    137.00
x mode         =      0.00
y mode         =      5.00

x kurtosis     =     -1.48
y kurtosis     =     -1.22
x skewness     =      0.00
y skewness     =      0.54

x SE kurtosis  =      1.19
y SE kurtosis  =      1.19
x SE skewness  =      0.62
y SE skewness  =      0.62
```

Skewness and kurtosis help us understand whether our data is chill (normal) or wild (leptokurtic party).
Interactive version available here, for those who love experiments with a safety net:

* **61-additional.ipynb**

Let's be honest,
different tools may give slightly different answers
As you can see, the kurtosis and the skewness is different,
compared with PSPP. Just be aware of it.

I still don't know the reason of this differences.

-- -- --

### What's the Next Chapter 🤔?

If our journey with `ggplot2` so far has felt like,
tuning a well-behaved engine.
One that occasionally leaks warnings
but still gets us beautiful regression lines,
then buckle up. We are just getting started.

We have already explored the manual guts,
and the built-in magic of least squares,
even threw in some skewness and kurtosis for those of us,
who enjoy asymmetric data distributions over symmetrical conversations.

Now would be a great time to continue our exploration with the next chapter:
** [Trend - Language - R - Part Three** ].

👉 **Remember**: mastering both the manual and the automated methods,
not only helps us debug or audit properly.
It also allows us to casually,
drop regression trivia in WhatsApp groups at 2AM.
We may not attend many parties,
but we can dominate a chat thread,
with statistically significant insights.

See you in the next part,
where the lines get smoother and the plots get sassier.

--

Let's continue our previous `ggplot2` journey.

Consider continuing your exploration
with **Trend - Language - R - Part Three**.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Explore R Programming language visualization with ggplot2.
> Provide a bunch of example of plot cases in your fingertip.

We’re back at it with our beloved `ggplot2`.
It is easy if we can embrace the grammar.

Like any well-behaved grammar, once we know the rules,
the plots practically write themselves.
Only here the commas are aesthetics,
the clauses are geoms, 
nd the punchlines are distributions.

Let's keep building our visual intuition.
The more we speak in plots,
the more persuasive we become,
during those impromptu midnight data debates.
And let's be honest, some of us argue better with graphs than with words.

Let’s continue building our visual intuition.
The more we speak in plots,
the more persuasive we sound in late-night data debates.
And let's be honest, some of us argue better with graphs than with words.

_When you have a pet, you can make a poet about it._ \
_When you have a data pet, visualization is the poet._

👉 **Remember**: `ggplot2` is not just a plotting library.
It's a grammar for visual storytelling.
Let's make our data sing, or at least hum with statistical elegance.

-- -- --

### Distribution

Let’s start with the classic, the normal distribution.
Statisticians love it. Students fear it. Algorithms assume it.
We may not always get normally distributed data in real life,
but that does not stop us from dreaming in bell curves.

The `dnorm` method gives us the `y-values` (probability densities)
for each x on the standard normal distribution curve.

```r
y <- dnorm(x)
```

#### Normal Distribution

> geom_line

We start by loading the essential gear (required libraries),
generating `x` values across the curve,
and calculating `y` using `dnorm` method.
Then we wrap it all in a tidy `data.frame`,
so `ggplot2` can do what it does best: turn numbers into art.

```r
library(ggplot2)

x <- seq(-5, 5, length.out = 1000)
y <- dnorm(x)

df <- data.frame(x = x, y = y)
```

Once we have our data frame, we build the plot.
`geom_line()` does the drawing,
and `theme_minimal()` keeps things as clean as our assumptions.
We can add labels and save the output.
This is how we go from raw probability to polished `PNG`.

```r
plot <- ggplot(df, aes(x = x, y = y)) +
  geom_line(color = "black")

plot <- plot +
  theme_minimal() +
  theme(
    text = element_text(size = 4),
    panel.grid = element_blank()) + 

  labs(
    x = "x", y = "Density",
    title = "Standard Normal ",
      "Distribution with Quantiles")

ggsave("63-normal.png", plot,
  width = 800, height = 400, units = "px")
```

#### Normal Distribution with Quantiles

> geom_area

We enhance the normal plot by showing quantiles.
Why? Because sometimes we need to explain to others,
where "_most of the data lives_",
without quoting the full standard deviation manifesto.

* **63-quantiles.r**

```r
# Load required libraries
library(ggplot2)

# Generate data points for x-axis
x <- seq(-5, 5, length.out = 1000)

# Calculate the corresponding y-values
# for a standard normal distribution
y <- dnorm(x)

# Create data frame for plotting
df <- data.frame(x = x, y = y)

# Calculate the percentiles
percentiles <- c(25, 50, 75, 100)
quantiles <- quantile(
  x, probs = percentiles / 100)

# Plot the normal distribution
plot <- ggplot(df, aes(x = x, y = y)) +
  geom_line(color = "black")

# Shade regions corresponding to percentiles
for (i in seq_along(quantiles)) {
  plot <- plot + geom_area(
    data = subset(df,x <= quantiles[i]),
    aes(x = x, y = y),
    fill = i, alpha = 0.3)
}

# Show grid
plot <- plot +
  theme_minimal() +
  theme(
    text = element_text(size = 4),
    plot.background = element_rect(fill = "white"),
    panel.grid = element_blank()) + 

  # Add labels and title
  labs(
    x = "x", y = "Density",
    title = "Standard Normal ",
      "Distribution with Quantiles")

# Save plot as PNG
ggsave("63-quantiles.png", plot,
  width = 800, height = 400, units = "px")
```

We define the percentiles,
then let `quantile()` do the slicing.

```r
percentiles <- c(25, 50, 75, 100)
quantiles <- quantile(x, probs = percentiles / 100)
```



And add this shade regions corresponding to percentiles,
to the plot grammar. This can be done by using `geom_area`.

```r
for (i in seq_along(quantiles)) {
  plot <- plot + geom_area(
    data = subset(df,x <= quantiles[i]),
    aes(x = x, y = y),
    fill = i, alpha = 0.3)
}
```



The plot result can be shown as follows:



👉 Want to play with it interactively?

* **63-quantiles.r**

Adding quantiles makes the plot speak.
Visually hinting where the data clusters.
This is useful for storytelling, teaching, and winning arguments about,
whether someone's test score is "_really above average._"

#### Kurtosis

> The pointiness of our curve

With the `dnorm` method,
we can simulate kurtosis and skewness.

We explore different levels of kurtosis.
Technically it is about tails and peaks,
but informally, it tells us how extreme our data feels.
like comparing drama queens to stoics in distribution form.

* **64-kurtosis.r**

```r
# Load required libraries
library(ggplot2)

# Generate data points for x-axis
x <- seq(-5, 5, length.out = 1000)

# Calculate the corresponding y-values
# for the standard normal distribution
y_standard <- dnorm(x)

# Examples of distributions
# with different levels of kurtosis

# Standard normal distribution (Kurtosis = 0)
y_kurtosis_1 <- dnorm(x, mean = 1, sd = 1)

# Lower kurtosis
y_kurtosis_2 <- dnorm(x, mean = 1, sd = 0.5)

# Higher kurtosis
y_kurtosis_3 <- dnorm(x, mean = 1, sd = 2)

# Create data frames for plotting
df_standard <- data.frame(x = x, y = y_standard)
df_kurtosis_1 <- data.frame(x = x, y = y_kurtosis_1)
df_kurtosis_2 <- data.frame(x = x, y = y_kurtosis_2)
df_kurtosis_3 <- data.frame(x = x, y = y_kurtosis_3)

# Plot the normal distribution and
# distributions with different levels of kurtosis
plot <- ggplot() +
  geom_line(data = df_standard, color = "black",
    aes(x = x, y = y), linewidth = 0.2) +
  geom_line(data = df_kurtosis_1,
    aes(x = x, y = y), color = "red",
    linetype = "dashed", linewidth = 0.2) +
  geom_line(data = df_kurtosis_2,
    aes(x = x, y = y), color = "green",
    linetype = "dashed", linewidth = 0.2) +
  geom_line(data = df_kurtosis_3,
    aes(x = x, y = y), color = "blue",
    linetype = "dashed", linewidth = 0.2) +
  labs(x = "x", y = "Density",
    title = "Normal Distribution ",
      "with Different Kurtosis") +
  scale_linetype_manual(
    values = c("solid", "dashed", "dashed", "dashed"),
    labels = c(
      "Standard Normal", "Standard Kurtosis = 0",
      "Lower Kurtosis", "Higher Kurtosis")) +
  theme_minimal() +
  theme(
    plot.background = element_rect(fill = "white"),
    text = element_text(size = 4))

# Save plot as PNG
ggsave("64-kurtosis.png", plot,
  width = 800, height = 400, units = "px")
```

Let's make examples of distributions
with different levels of kurtosis.
We generate standard, flat, and pointy curves.

1. Standard normal distribution (Kurtosis = 0)
2. Lower kurtosis
3. Higher kurtosis

```r
y_standard <- dnorm(x)
df_standard <- data.frame(x = x, y = y_standard)

y_kurtosis_1 <- dnorm(x, mean = 1, sd = 1)
y_kurtosis_2 <- dnorm(x, mean = 1, sd = 0.5)
y_kurtosis_3 <- dnorm(x, mean = 1, sd = 2)

df_kurtosis_1 <- data.frame(x = x, y = y_kurtosis_1)
df_kurtosis_2 <- data.frame(x = x, y = y_kurtosis_2)
df_kurtosis_3 <- data.frame(x = x, y = y_kurtosis_3)
```



Now we draw them using `geom_line`.
for each different levels of kurtosis to the plot grammar.
Each line shows how the same mean can hide wildly different stories.

```r
plot <- ggplot() +
  geom_line(data = df_standard, color = "black"
    aes(x = x, y = y), linewidth = 0.2) +
  geom_line(data = df_kurtosis_1,
    aes(x = x, y = y), color = "red",
    linetype = "dashed", linewidth = 0.2) +
  geom_line(data = df_kurtosis_2,
    aes(x = x, y = y), color = "green",
    linetype = "dashed", linewidth = 0.2) +
  geom_line(data = df_kurtosis_3,
    aes(x = x, y = y), color = "blue",
    linetype = "dashed", linewidth = 0.2) +
  labs(x = "x", y = "Density",
    title = "Normal Distribution ",
      "with Different Kurtosis") +
  scale_linetype_manual(
    values = c("solid", "dashed", "dashed", "dashed"),
    labels = c(
      "Standard Normal", "Standard Kurtosis = 0",
      "Lower Kurtosis", "Higher Kurtosis")) +
  theme_minimal() +
  theme(
    text = element_text(size = 4))
```



The plot result can be shown as follows:



👉 Want to run the numbers live?

* **64-kurtosis.r**

Why care about kurtosis?
Because reality is messy.
Sometimes data behaves like a chill Gaussian.
Sometimes it spikes like a stressed-out grad student on deadline week.

#### Skewness

> When data leans—left, right, or dramatically off-center

Now let’s shift our focus to skewness.
It tells us whether our data leans like a suspicious p-hacking attempt.

* **65-skewness.r**

```r
# Load required libraries
library(ggplot2)

# Generate data points for x-axis
x <- seq(-5, 5, length.out = 1000)

# Calculate the corresponding y-values
# for the standard normal distribution
y_standard <- dnorm(x)

# Examples of distributions
# with different skewness parameters

# Negative skewness
y_skewed_1 <- dnorm(x) * 2 * pnorm(x)

# Moderate positive skewness
y_skewed_2 <- dnorm(x) * 2 * pnorm(-x)

# High positive skewness
y_skewed_3 <- dnorm(x) * 2 * pnorm(x) * 2

# Create data frames for plotting
df_standard <- data.frame(x = x, y = y_standard)
df_skewed_1 <- data.frame(x = x, y = y_skewed_1)
df_skewed_2 <- data.frame(x = x, y = y_skewed_2)
df_skewed_3 <- data.frame(x = x, y = y_skewed_3)

# Plot the normal distribution and skewed distributions
plot <- ggplot() +
  geom_line(data = df_standard, color = "black",
    aes(x = x, y = y), linewidth = 0.2) +
  geom_line(data = df_skewed_1,
    aes(x = x, y = y), color = "red",
    linetype = "dashed", linewidth = 0.2) +
  geom_line(data = df_skewed_2,
    aes(x = x, y = y), color = "green",
    linetype = "dashed", linewidth = 0.2) +
  geom_line(data = df_skewed_3,
    aes(x = x, y = y), color = "blue",
    linetype = "dashed", linewidth = 0.2) +
  labs(x = "x", y = "Density",
    title = "Normal Distribution with Different Skewness") +
  scale_linetype_manual(
    values = c("solid", "dashed", "dashed", "dashed"),
    labels = c(
      "Standard Normal",
      "Negative Skewness = -4",
      "Moderate Positive Skewness = 2",
      "High Positive Skewness = 6")) +
  theme_minimal() +
  theme(
    plot.background = element_rect(fill = "white"),
    text = element_text(size = 4))

# Save plot as PNG
ggsave("65-skewness.png", plot,
  width = 800, height = 400, units = "px")
```

Let's make examples of distributions
with different skewness parameters.
We simulate several skewness levels:
negative, moderate, and highly positive.

1. Negative skewness
2. Moderate positive skewness
3. High positive skewness

```r
y_standard <- dnorm(x)
df_standard <- data.frame(x = x, y = y_standard)

y_skewed_1 <- dnorm(x) * 2 * pnorm(x)
y_skewed_2 <- dnorm(x) * 2 * pnorm(-x)
y_skewed_3 <- dnorm(x) * 2 * pnorm(x) * 2

df_skewed_1 <- data.frame(x = x, y = y_skewed_1)
df_skewed_2 <- data.frame(x = x, y = y_skewed_2)
df_skewed_3 <- data.frame(x = x, y = y_skewed_3)
```



Then we draw them in context by adding `geom_line` again,
When done right, the plot reveals which side the data whispers its secrets to.
for each different skewed distributions to the plot grammar.

```r
plot <- ggplot() +
  geom_line(data = df_standard, color = "black",
    aes(x = x, y = y), linewidth = 0.2) +
  geom_line(data = df_skewed_1,
    aes(x = x, y = y), color = "red",
    linetype = "dashed", linewidth = 0.2) +
  geom_line(data = df_skewed_2,
    aes(x = x, y = y), color = "green",
    linetype = "dashed", linewidth = 0.2) +
  geom_line(data = df_skewed_3,
    aes(x = x, y = y), color = "blue",
    linetype = "dashed", linewidth = 0.2) +
  labs(x = "x", y = "Density",
    title = "Normal Distribution with Different Skewness") +
  scale_linetype_manual(
    values = c("solid", "dashed", "dashed", "dashed"),
    labels = c(
      "Standard Normal",
      "Negative Skewness = -4",
      "Moderate Positive Skewness = 2",
      "High Positive Skewness = 6")) +
  theme_minimal() +
  theme(
    text = element_text(size = 4))
```



The plot result can be shown as follows:



👉 Try bending the curve yourself:

* **65-skewness.r**

Understanding skewness helps us avoid misleading averages.
Sometimes the "_average_" income includes Jeff Bezos,
and that shifts everything right.

-- -- --

### Trend: Multiple

> When in doubt, regress everything. Then doubt the regression.

Sometimes, we need to show multiple trends at once.
Maybe to compare patterns, maybe to confuse our boss.
Either way, `ggplot2` lets us put several series in one plot,
or spread them neatly across a grid.
It's like choosing between a dinner buffet or a tasting menu.

#### Geom Smooth

> Linear model with standard errors: the tuxedo of trendlines.

Why manually calculate regression when `geom_smooth()` can,
do the heavy lifting and wear a standard error cloak while at it?
Think of it as our personal assistant for drawing statistically proper lines.

Let's begin with a scatter plot using `geom_point()`, 
then let `geom_smooth()` do its thing,
plotting linear fits for [`ys₁`, `ys₂`, and `ys₃`].

* **71-geom-smooth.r**

```r
# Load required libraries
library(readr)
library(ggplot2)
library(ggthemes)

# Read data from CSV file
series <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Extract x and y values from CSV data
xs <- series$xs
ys1 <- series$ys1
ys2 <- series$ys2
ys3 <- series$ys3

# Create a data frame with x and y values
data <- data.frame(
  x = xs, y1 = ys1, y2 = ys2, y3 = ys3)

# Scatter plot with regression lines
plot <- ggplot(data, aes(x = xs)) +
  # Add points for y1,
  # add regression line for y1
  geom_point(
    aes(x = xs, y = ys1),
    size = 0.5, color = "firebrick") +  
  geom_smooth(
    aes(x = xs, y = ys1), method = "lm",
    se = TRUE, color = "firebrick",
    linewidth = 0.2) +  

  # Add points for y2,
  # add quadratic regression line for y2
  geom_point(
    aes(x = xs, y = ys2),
    size = 0.5, color = "forestgreen") +  
  geom_smooth(
    aes(x = xs, y = ys2), method = "lm",
    # formula = y ~ poly(x, 2),
    se = TRUE, color = "forestgreen",
    linewidth = 0.2) +  

  # Add points for y3,
  # add cubic regression line for y3
  geom_point(
    aes(x = xs, y = ys3),
    size = 0.5, color = "royalblue") +  
  geom_smooth(
    aes(x = xs, y = ys3), method = "lm",
    # formula = y ~ poly(x, 3),
    se = TRUE, color = "royalblue",
    linewidth = 0.2) +  

  labs(x = "x", y = "y",
    title = "Scatter Plot with Regression Lines") +
  theme_solarized() +
  scale_color_solarized() +
  theme(
    text = element_text(size = 4))

# Save plot as PNG
ggsave("71-geom-smooth.png", plot,
  width = 800, height = 400, units = "px")
```

Explanation

```r
plot <- ggplot(data, aes(x = xs)) +
  geom_point(
    aes(x = xs, y = ys1),
    size = 0.5, color = "firebrick") +  
  geom_smooth(
    aes(x = xs, y = ys1), method = "lm",
    se = TRUE, color = "firebrick",
    linewidth = 0.2) +  
    text = element_text(size = 4))
  ...
```



To make it visually elegant (and slightly hipster),
we can apply the `solarized` theme from the `ggthemes` library.
Plots deserve style too.

```r
  labs(x = "x", y = "y",
    title = "Scatter Plot with Regression Lines") +
  theme_solarized() +
  scale_color_solarized() +
  theme(
    text = element_text(size = 4))
```



Here’s the final output,
where our data points are loud and the regression lines are proud:



Get interactive and tinker in `JupyterLab`:

* **71-geom-smooth.r**

```r
```

These plots help us compare multiple trend patterns on a single canvas
Regression isn't just prediction, it’s persuasion in visual form.

#### Grid Extra

> Not all trends get along on the same y-axis.

Sometimes plotting everything together makes,
the trends look like they're in a statistical street fight.
When axes clash or y-axis scales diverge,
it's time to separate the series using `gridExtra`.

* **72-grid-extra.r**

```r
# Load required libraries
library(readr)
library(ggplot2)
library(ggthemes)
library(gridExtra)

# Avoid generating Rplots.pdf
pdf(NULL)

# Read data from CSV file
series <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Extract x and y values from CSV data
xs <- series$xs
ys1 <- series$ys1
ys2 <- series$ys2
ys3 <- series$ys3

# Create a data frame with x and y values
data <- data.frame(
  x = xs, y1 = ys1, y2 = ys2, y3 = ys3)

# Scatter plot with regression line for y1
plot_y1 <- ggplot(data, aes(x = xs, y = ys1)) +
  geom_point(
    size = 0.5, color = "indianred") +  
  geom_smooth(
    method = "lm", formula = y ~ poly(x, 1),
    se = TRUE, color = "indianred", linewidth = 0.2) +  
  labs(
    x = "x", y = "y", 
    title = "Regression Line for y1") +
  theme_light() +
  theme(
    text = element_text(size = 2),
    axis.text = element_text(size = 3))

# Scatter plot with quadratic regression line for y2
plot_y2 <- ggplot(data, aes(x = xs, y = ys2)) +
  geom_point(
    size = 0.5, color = "limegreen") +  
  geom_smooth(
    method = "lm", formula = y ~ poly(x, 1),
    se = TRUE, color = "limegreen", linewidth = 0.2) +  
  labs(
    x = "x", y = "y", 
    title = "Quadratic Regression Line for y2") +
  theme_light() +
  theme(
    text = element_text(size = 2),
    axis.text = element_text(size = 3))

# Scatter plot with cubic regression line for y3
plot_y3 <- ggplot(data, aes(x = xs, y = ys3)) +
  geom_point(
    size = 0.5, color = "steelblue") +  
  geom_smooth(
    method = "lm", formula = y ~ poly(x, 1),
    se = TRUE, color = "steelblue", linewidth = 0.2) +  
  labs(
    x = "x", y = "y", 
    title = "Cubic Regression Line for y3") +
  theme_light() +
  theme(
    text = element_text(size = 2),
    axis.text = element_text(size = 3))

# Arrange plots using gridExtra horizontally
grid_plot <- grid.arrange(
  plot_y1, plot_y2, plot_y3, ncol = 3)

# Save the combined grid of plots as PNG
ggsave("72-grid-extra.png", grid_plot,
  width = 800, height = 400, units = "px")
```

Here, we arrange the individual trend plots,
using `gridExtra` side-by-side horizontally with:

```r
grid_plot <- grid.arrange(
  plot_y1, plot_y2, plot_y3, ncol = 3)
```

The result is a civilized separation of trends,
each plot gets its own y-axis,
no need to share or compromise:



The plot result can be shown as follows:



Explore it yourself in `JupyterLab`:

* **72-grid-extra.r**

Multiple trends in one frame are useful,
until the `y-axis` scale distorts the story.
Grid arrangements help us show the data fairly,
without statistical squabbling.

-- -- --

### Statistic Properties: One Axis Plot

> Three series in one axis plot

_Three series walk into a plot… and immediately argue about the median._

Before we start visualizing,
let's remember: statistics are like cats
(cat the pet, not the linux command).
They don't always behave the way we expect,
but with the right box (or violin),
we can get them to show their shape.

In this section, we wrangle multiple y-series,
and explore ways to compare their distributions using one axis.
This is our statistical group therapy session, 
here each series gets a chance to express itself.

As you can see from previous statistical properties.
We can analyze the data for each series.
For example we can just consider just the y-series,
and obtain the `mean`, `median`, `mode`,
and also the `minimum`, `maximum`, `range`, and `quantiles`.

#### Long Format

> Melt

_We melt the data, not the analyst._

When plotting multiple y-series in one go,
we need to reshape the data from wide to long.
Why? Because `ggplot2` prefers tidy data,
each row is one observation, each column one variable.
Wide format is for spreadsheets,
long format is for plots and parties.

We use `gather()` from the `tidyr` package.
Think of it as inviting all your series to one common table.

```r
series_longer <- series %>%
  gather(key = "y", value = "value", -xs)
```



You can check the result by `cat` or `print` the merged series.

Melting lets us treat all y-series equally.
Ideal for side-by-side comparison in single-axis plots.

#### Box Plot

> The box plot: where medians get the spotlight,
> and outliers are gently shamed.

The classic box plot summarizes data with quartiles and outliers.
It's like a résumé for our series:
here's the median, here’s the range, and oh,
those dots? We don’t talk about those.

The most common way to visualize this is the box plot.
We can utilize `geom_boxplot` to get the plot.

* **81a-boxplot.r**

```r
# Load required libraries
library(readr)
library(tidyr)
library(ggplot2)

# Read data from CSV file
series <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Melt the series to long format for boxplot
series_longer <- series %>%
  gather(key = "y", value = "value", -xs)

# Define custom colors (unused)
custom_colors <- c("red", "green", "blue")

# Define softer colors
# Light pink, Sky blue, Gold
soft_colors <- c("#FFB6C1", "#87CEEB", "#FFD700")

# Create boxplot using ggplot2 with custom colors
plot <- ggplot(
    series_longer,
    aes(x = y, y = value, fill = y)) +
  geom_boxplot(color = "black", linewidth= 0.2) +
  scale_fill_manual(values = soft_colors) +
  labs(
    x = "Variable", y = "Value",
    title = "Box Plot for ys1, ys2, and ys3") +
  theme_minimal() +
  theme(
    plot.background = element_rect(fill = "white"),
    text = element_text(size = 4))

# Save plot as PNG
ggsave("81a-boxplot.png", plot,
  width = 800, height = 400, units = "px")
```

Explanation

```r
plot <- ggplot(
    series_longer,
    aes(x = y, y = value, fill = y)) +
  geom_boxplot(color = "black", linewidth= 0.2) +
  ...
```



Let's use custom colors for this example.

```r
  scale_fill_manual(values = soft_colors) +
```

The plot result can be shown as follows:



You can obtain the interactive `JupyterLab` in this following link:

* **81a-boxplot.r**

Box plots are the go-to for comparing distributions.
Quick, informative, and a favorite of statisticians,
who want to look serious.

#### Violin Plot

> When a box plot learns to dance.

Box plots are informative,
but sometimes we want more flair.
Enter the violin plot:
a combination of box plot and kernel density.
Now we get to see the shape of the data,
not just its summary.

The better to visualize is by using violin plot.
We can utilize `geom_violin` to get the plot.

* **81b-violin.r**

```r
# Load required libraries
library(readr)
library(tidyr)
library(ggplot2)

# Read data from CSV file
series <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Melt the series to long format for violinplot
series_longer <- series %>%
  gather(key = "y", value = "value", -xs)

# Define custom colors (unused)
custom_colors <- c("red", "green", "blue")

# Define softer colors
# Light pink, Sky blue, Gold
soft_colors <- c("#FFB6C1", "#87CEEB", "#FFD700")

# Create violinplot using ggplot2 with custom colors
plot <- ggplot(
    series_longer,
    aes(x = y, y = value, fill = y)) +
  geom_violin(color = "black", linewidth= 0.2) +
  scale_fill_manual(values = soft_colors) +
  labs(
    x = "Variable", y = "Value",
    title = "Violin Plot for ys1, ys2, and ys3") +
  theme_minimal() +
  theme(
    plot.background = element_rect(fill = "white"),
    text = element_text(size = 4))

# Save plot as PNG
ggsave("81b-violin.png", plot,
  width = 800, height = 400, units = "px")
```

Explanation

```r
plot <- ggplot(
    series_longer,
    aes(x = y, y = value, fill = y)) +
  geom_violin(color = "black", linewidth= 0.2) +
 ...
```



The plot result can be shown as follows:



You can obtain the interactive `JupyterLab` in this following link:

* **81b-violin.r**

Violin plots show the full distribution.
Great for spotting multimodal patterns or hidden spikes.
Like a box plot with emotional range.

#### Swarm Plot

> Dot by dot, truth emerges.

Sometimes we just want to see all the raw values,
without summarizing them away.
The swarm plot (via `jitter` in `geom_point`),
lets each data point speak for itself.
No data left behind.

This leave us with other option such as swarm plot and strip plot.
We can get swarm plot using `jitter` inside `geom_point`.

* **81c-swarm.r**

```r
# Load required libraries
library(readr)
library(tidyr)
library(ggplot2)

# Read data from CSV file
series <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Melt the series to long format for swarmplot
series_longer <- series %>%
  gather(key = "y", value = "value", -xs)

# Define custom colors (unused)
custom_colors <- c("red", "green", "blue")

# Define softer colors
# Light pink, Sky blue, Gold
soft_colors <- c("#FFB6C1", "#87CEEB", "#FFD700")

# Create swarmplot using ggplot2 with custom colors
plot <- ggplot(
    series_longer,
    aes(x = y, y = value, color = y)) +
  geom_point(
    position = position_jitterdodge(
      jitter.width = 0.3, jitter.height = 0),
    size = 0.5) +
  scale_fill_manual(values = soft_colors) +
  labs(
    x = "Variable", y = "Value",
    title = "Swarm Plot for ys1, ys2, and ys3") +
  theme_minimal() +
  theme(
    plot.background = element_rect(fill = "white"),
    text = element_text(size = 4))

# Save plot as PNG
ggsave("81c-swarm.png", plot,
  width = 800, height = 400, units = "px")
```

Explanation

```r
plot <- ggplot(
    series_longer,
    aes(x = y, y = value, color = y)) +
  geom_point(
    position = position_jitterdodge(
      jitter.width = 0.3, jitter.height = 0),
    size = 0.5) +
  ...
```



And here it is.
The plot result can be shown as follows:



You can obtain the interactive `JupyterLab` in this following link:

* **81c-swarm.r**

Swarm plots are perfect when sample sizes are small,
or distributions are non-traditional.
Plus, it just looks cool.

#### Strip Plot

> Minimalism, but make it jitter.

Strip plots are similar to swarm plots but even simpler.
Here, we use `geom_jitter()` to spread out points horizontally,
so they don't overlap like penguins in a pile.

We can get strip plot using `geom_jitter`.

* **81d-strip.r**

```r
# Load required libraries
library(readr)
library(tidyr)
library(ggplot2)

# Read data from CSV file
series <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Melt the series to long format for stripplot
series_longer <- series %>%
  gather(key = "y", value = "value", -xs)

# Define custom colors (unused)
custom_colors <- c("red", "green", "blue")

# Define softer colors
# Light pink, Sky blue, Gold
soft_colors <- c("#FFB6C1", "#87CEEB", "#FFD700")

# Create stripplot using ggplot2 with custom colors
plot <- ggplot(
    series_longer,
    aes(x = y, y = value, color = y)) +
  geom_jitter(
    width = 0.3, height = 0, size = 0.5) +
  scale_fill_manual(values = soft_colors) +
  labs(
    x = "Variable", y = "Value",
    title = "Strip Plot for ys1, ys2, and ys3") +
  theme_minimal() +
  theme(
    plot.background = element_rect(fill = "white"),
    text = element_text(size = 4))

# Save plot as PNG
ggsave("81d-strip.png", plot,
  width = 800, height = 400, units = "px")
```

Explanation

```r
plot <- ggplot(
    series_longer,
    aes(x = y, y = value, color = y)) +
  geom_jitter(
    width = 0.3, height = 0, size = 0.5) +
  ...
```



The plot result can be shown as follows:



You can obtain the interactive `JupyterLab` in this following link:

* **81d-strip.r**

Strip plots keep it simple.
Good for exploratory views and,
when we want to embrace a bit of chaos,
but still understand the story.

-- -- --

### Statistic Properties: Distribution

> Let there be frequencies, and let them plot themselves.

We've met our y-series in various boxy, violiny, and jittery forms.
Now it's time to ask: how do these values,
distribute themselves along the number line?
Are they huddled near the mean?
Wandering wildly like unsupervised p-values?

We'll explore that with some of,
our favorite tools for visualizing distributions.
Just like previous four, we can analyse the y-axis,
but this time by frequency of each series.

#### KDE Plot

> Kernel Density Estimation

The KDE plot gives us a smoothed-out version of the histogram.
It estimates the probability density function of the variable.
Which sounds fancy, but really just means:
"_Here's where the data likes to hang out._"

And thanks to `geom_density`,
we don't even need to bring calculus to the party.

KDE shown well the distribution of the frequency.
This complex task can be done easily with `geom_density`.

* **82a-kdeplot.r**

```r
# Load required libraries
library(readr)
library(tidyr)
library(ggplot2)

# Read data from CSV file
series <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Melt the series to long format for stripplot
series_longer <- series %>%
  gather(key = "Category", value = "value", -xs)

# Create KDE plot using ggplot2 with custom colors
plot <- ggplot(
    series_longer,
    aes(x = value, fill = Category)) +
  geom_density(alpha = 0.7, color = NA) +
  scale_fill_brewer(palette = "Set1") +
  labs(
    x = "Value", y = "Density",
    title = "KDE Plot for ys1, ys2, and ys3") +
  theme_minimal() +
  theme(
    plot.background = element_rect(fill = "white"),
    text = element_text(size = 4))

# Save plot as PNG
ggsave("82a-kdeplot.png", plot,
  width = 800, height = 400, units = "px")
```

Explanation

```r
plot <- ggplot(
    series_longer,
    aes(x = value, fill = Category)) +
  geom_density(alpha = 0.7, color = NA) +
  ...
```



And here's the resulting plot:



You can obtain the interactive `JupyterLab` in this following link:

* **82a-kdeplot.r**

KDE plots help us compare shapes of distributions,
without worrying about bin size.
They give a smooth overview that highlights trends,
like a box plot with a PhD in smoothness.

#### Rug Plot

The rug plot is about minimalism.
It doesn't summarize, smooth, or bin.
It simply places a tiny tick mark for each observation.
Elegant. Humble. Underrated.

We can also simply show the rug plot using `geom_rug`.

* **83a-rugplot.r**

```r
# Load required libraries
library(readr)
library(tidyr)
library(ggplot2)

# Read data from CSV file
series <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Melt the series to long format for rugplot
series_longer <- series %>%
  gather(key = "Category", value = "value", -xs)

# Create KDE plot using ggplot2 with custom colors
plot <- ggplot(
    series_longer,
    aes(x = value, fill = Category)) +
  geom_rug(alpha = 0.5, sides = "b") +
  scale_fill_brewer(palette = "Set1") +
  labs(
    x = "Value", y = "Density",
    title = "Rug Plot for ys1, ys2, and ys3") +
  theme_minimal() +
  theme(
    plot.background = element_rect(fill = "white"),
    text = element_text(size = 4))

# Save plot as PNG
ggsave("83a-rugplot.png", plot,
  width = 800, height = 400, units = "px")
```

Explanation

```r
plot <- ggplot(
    series_longer,
    aes(x = value, fill = Category)) +
  geom_rug(alpha = 0.5, sides = "b") +
  ...
```



And here’s the tick parade:



You can obtain the interactive `JupyterLab` in this following link:

* **83a-rugplot.r**

Rug plots show the raw locations of all data points.
Great for spotting clustering, gaps,
or if our data has secretly turned binary when we weren't looking.

#### Histogram

> The classic.

Histograms are still one of the clearest ways,
to show frequency distributions.
But `geom_histogram` is more than the basic histogram for beginner.
In `R`, `geom_histogram` lets us tweak bins, colors, and aesthetics
to make our plots look good and tell the truth.
A rare combo.

* **83b-histplot.r**

```r
# Load required libraries
library(readr)
library(tidyr)
library(ggplot2)

# Read data from CSV file
series <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Melt the series to long format for histplot
series_longer <- series %>%
  gather(key = "Category", value = "value", -xs)

# Create KDE plot using ggplot2 with custom colors
plot <- ggplot(
    series_longer,
    aes(x = value, fill = Category)) +
  geom_histogram(
    binwidth = 50, linewidth = 0.2,
    alpha = 0.7, color = "black") +
  scale_fill_brewer(palette = "Set1") +
  labs(
    x = "Value", y = "Density",
    title = "Histogram Plot for ys1, ys2, and ys3") +
  theme_minimal() +
  theme(
    plot.background = element_rect(fill = "white"),
    text = element_text(size = 4))

# Save plot as PNG
ggsave("83b-histplot.png", plot,
  width = 800, height = 400, units = "px")
```

Explanation

```r
plot <- ggplot(
    series_longer,
    aes(x = value, fill = Category)) +
  geom_histogram(
    binwidth = 50, linewidth = 0.2,
    alpha = 0.7, color = "black") +
  ...
```



And here’s the result:



You can obtain the interactive `JupyterLab` in this following link:

* **83b-histplot.r**

Histograms offer a quick glance,
at the frequency of values in intervals.
Perfect for spotting skewness, symmetry,
and when the data is just plain weird.

-- -- --

### Statistic Properties: Marginal

At this point, we have sliced and diced our data in every direction,
except the literal margins. Time to fix that.
Marginal plots allow us to peek at each axis on its own turf.
Think of it as giving the `x` and `y` axes their solo performance,
with `ggMarginal` from the `ggExtra` library as our stage manager.

We can step to analyse each of single axis analysis,
right on its own axis using `ggMarginal` from `ggExtra` library.

#### Density Example

We start with a classic 2D plot.
So far so good.

* **84a-marginal.r**

```r
# Load required libraries
library(readr)
library(ggplot2)
library(ggExtra)

# Avoid generating Rplots.pdf
pdf(NULL)

# Read data from CSV file
series <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Create scatter plot with marginal density plots
p <- ggplot(
    series, linewidth = 0.2,
    aes(x = xs, y = ys3)) +
  geom_point(size = 0.2) +
  geom_smooth(
    method = "lm", formula = y ~ poly(x, 1),
    se = TRUE, color = "blue", linewidth = 0.2) +
  theme_minimal() +
  theme(
    text = element_text(size = 4))

# Add marginal density plots
p_with_margins <- ggMarginal(
  p, type = "density", linewidth = 0.2,)

# Save plot as PNG
ggsave("84a-marginal.png", p_with_margins,
  width = 800, height = 600, units = "px")
```

For example we can add marginal density plot.
Let's start with usual plot.



Now we let each axis whisper its own secrets,
by adding marginal density plots.
This gives a quick glimpse of distribution on both axes,
without adding clutter to the main scene.

```r
p_with_margins <- ggMarginal(
  p, type = "density", linewidth = 0.2,)
```



The final result is a polished plot that combines the big picture with fine details:



Explore the interactive version here:

* **84a-marginal.r**

Marginal plots help us connect the dots,
between joint and marginal distributions.
In other words, we see not just where the points are,
but how they behave on each axis.
For statisticians, that's like switching from grayscale to technicolor.

#### Histogram Example

We're not married to density.
Let's switch it up and try histograms instead.

* **84b-marginal.r**

```r
# Load required libraries
library(readr)
library(ggplot2)
library(ggExtra)

# Avoid generating Rplots.pdf
pdf(NULL)

# Read data from CSV file
series <- read_csv(
  "series.csv",
  show_col_types = FALSE)

# Create scatter plot with marginal histogram plots
p <- ggplot(
    series, linewidth = 0.2,
    aes(x = xs, y = ys3)) +
  geom_point(size = 0.2) +
  geom_smooth(
    method = "lm", formula = y ~ poly(x, 1),
    color = "red", fill = alpha("#87CEEB", 0.1),
    se = TRUE, linewidth = 0.2) +
  theme_minimal() +
  theme(
    text = element_text(size = 4))

# Add marginal histogram plots
p_with_margins <- ggMarginal(
  p, type = "histogram",
  color = "black", fill = alpha("#FFD700", 0.1),
  linewidth = 0.1)

# Save plot as PNG
ggsave("84b-marginal.png", p_with_margins,
  width = 800, height = 600, units = "px")
```

We can use marginal histograms to get a more "_binned_" perspective.
This is the histogram’s time to shine—on the sidelines.

```r
p_with_margins <- ggMarginal(
  p, type = "histogram",
  color = "black", fill = alpha("#FFD700", 0.1),
  linewidth = 0.1)
```



Here's how the final result looks:



And the interactive version is ready for your curiosity:

* **84b-marginal.r**

Sometimes we want to see the raw frequency count.
Histograms add structure to the axis-wise distribution,
making it easier to spot skew, outliers,
or whether the data suffers from
"_the dreaded left shoulder syndrome._"

-- -- --

### What's the Next Chapter 🤔?

So far, we've explored statistical properties with `R`,
sliced data from every angle,
and smoothed it like a well-behaved normal curve.
All in all, not bad for a plotting party hosted by statisticians.

Numbers deserve more than being left alone in a spreadsheet.
We've shown how to visualize data distributions in practical, meaningful ways.
From box plots to violin plots to marginal density overlays,
we now have tools that not only inform,
but also impress during awkward coffee break conversations.

**But where do we go from here?**

While `Python` and `R` are the old reliable friends of the statistical world,
the programming party doesn’t end there.
There's `Julia`, fast, modern, and already practicing its keynote speech for the future.
Then there’s `Typescript` and `Go`, bridging the world of analysis,
with scalable applications that refuse to crash under pressure.

Learning statistical visualization across multiple languages means,
we are not just tool users. We are toolmakers.
We future-proof our workflows and avoid the classic trap:
"_I have this great insight, but it only runs on my laptop._"

So if you're curious what comes next, consider peeking into:
👉 **Trend - Language - Julia - Part One**.

In data science, like in life,
flexibility is the best regression line.
It's time to see how the stats game changes,
when we switch gears.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Explore Julia statistic plot visualization.
> Providing the data using linear model.

Welcome to our Trend meets `Julia` trilogy.

Julia is like the youngest sibling in the programming family.
Fast, smart, and still figuring out where the spoons are.
While I haven't yet studied all of its grammar rules,
or fully learned how to conjugate its macros,
we can already do what truly matters:
plot pretty charts and poke at distributions.

Starting early with Julia means,
we are future proofing our workflow ,
nd catching the train before it becomes the bullet train
It’s okay if we don't understand everything yet.
Plots speak first. Syntax catches up later.

We may not be fluent yet,
but we’re statistically enthusiastic.

-- -- --

### Preparation

All we need is `Julia` installed on our system.
Preferably somewhere we can find it later without using `locate`.

#### Library

The script here begins from the absolute basics.
As with any language trying to be both fast and friendly,
libraries need to be added gradually,
like toppings on statistical pizza.

Use `Julia`'s terminal to install them.
Yes, it talks back.

```julia
add Polynomials
add Plots
add CSV
add Printf
add DataFrames
add GLM
add Distributions
add StatsPlots
add ColorSchemes
add ColorTypes
add Gadfly
add IJulia
import Cairo, Fontconfig
```

These libraries are our statistical toolbox.
GLM for models, Plots for the art,
Distributions for the theory, and ColorSchemes.
Let’s face it, default colors are rarely emotionally fulfilling.

#### Data Series Samples

As is tradition, we begin with minimal cases.
Two datasets to keep things simple.
No fifty-column CSV monsters today.

The first is a multi-series file.
Great for practicing melt operations, 
and pretending we're experts in data tidying:

* 👉 **series.csv**

```csv
xs, ys1, ys2, ys3
0,  5,   5,   5
1,  9,   12,  14
2,  13,  25,  41
3,  17,  44,  98
4,  21,  69,  197
5,  25,  100, 350
6,  29,  137, 569
7,  33,  180, 866
8,  37,  229, 1253
9,  41,  284, 1742
10, 45,  345, 2345
11, 49,  412, 3074
12, 53,  485, 3941
```

The second one is a clean,
focused dataset for statistical modeling like least squares.
Small enough to open in a text editor.

* 👉 **50-samples.csv**

```csv
x,y
0,5
1,12
2,25
3,44
4,69
5,100
6,137
7,180
8,229
9,284
10,345
11,412
12,485
```

These sample files let us skip,
the "_where is my data_" drama ,
nd focus on learning the plotting tools.
Also, note the filename: "_samples_" not "_population_".
Statistically speaking, that’s not a typo, it is a worldview.

-- -- --

### Polynomials Fit

Let's start from simple, just reading data, and interpret.

#### Vector

We begin with simple arrays.
No DataFrame drama. Just pure, honest xs and ys as a source data.
Then use `Polynomials.fit` to get the coefficient of curve fitting
This require `Polynomials`  library.

* **01-poly-vector.jl**

```julia
using Polynomials

# Given data
x_values = [
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_values = [
  5, 9, 13, 17, 21, 25, 29,
  33, 37, 41, 45, 49, 53]

# Curve Fitting Order
order = 1

# Perform linear regression using Polynomials.fit
pf = fit(x_values, y_values, order)
println("Using Polynomials.fit")

# Extract coefficients and reverse them
coeffs_r= reverse(coeffs(pf)) 
println("Coefficients (a, b):")

# Format coefficients
coeffs_fmt = [
  round(c, digits=2) for c in coeffs_r]  
println(coeffs_fmt, "\n")
```

Explanation

```julia
# Given data
x_values = [
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_values = [
  5, 9, 13, 17, 21, 25, 29,
  33, 37, 41, 45, 49, 53]
```



We suspect a linear relationship.
And yes, sometimes data is kind enough not to lie to our faces.

Our target regression model:

$$
y = a + b{x}
$$

Let’s let `Julia` do the math with `Polynomials.fit`:

```julia
using Polynomials

order = 1
pf = fit(x_values, y_values, order)
println("Using Polynomials.fit")

coeffs_r= reverse(coeffs(pf)) 
println("Coefficients (a, b):")

coeffs_fmt = [
  round(c, digits=2) for c in coeffs_r]  
println(coeffs_fmt, "\n")
```

We need to set the curve fitting order,
such as one for straight line.
Then perform linear regression using `Polynomials.fit`.
With the result, we can extract coefficients,
and reverse them to fit the equation above.
And finally printing in rounding decimal format.



We can see the result as follows.

```output
❯ julia 01-poly-vector.jl
Using Polynomials.fit
Coefficients (a, b):
[4.0, 5.0]
```

[401-vim-poly-vector-03]

📓 Jupyter version here: 

* **01-poly-vector.jl**

This is the starting point for understanding,
how our data trends behave over time or iterations.
It helps reveal whether we're dealing with a polite straight line,
or something a bit more rebellious.

#### Dataframe

Ready to scale up?
Let's switch to using DataFrames for better structure and flexibility.

* **02-dataframe.jl**

```julia
using CSV, DataFrames

# Read data from CSV file
# Strip spaces from column names
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

println(last(df,5))
println()
println(names(df))
```

Instead of array, we can read from CSV,
and put the result into dataframe.
First we read data from CSV,
and sanitize the column names by stripping faces.

```julia
using CSV, DataFrames

df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))
```

Check the contents like any cautious statistician would:

```julia
println(last(df,5))
println()
println(names(df))
```



We can see the result as follows.

```output
❯ julia 02-dataframe.jl
5×4 DataFrame
 Row │ xs     ys1    ys2    ys3   
     │ Int64  Int64  Int64  Int64 
─────┼────────────────────────────
   1 │     8     37    229   1253
   2 │     9     41    284   1742
   3 │    10     45    345   2345
   4 │    11     49    412   3074
   5 │    12     53    485   3941

["xs", "ys1", "ys2", "ys3"]
```



📓 Jupyter version here: 

* **02-dataframe.jl**

#### Stack

> Long Format

For some kind of visualization,
we need to melt the DataFrame to long format.

* **03-stack.jl**

```julia
using CSV, DataFrames

# Read data from CSV file
# Strip spaces from column names
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

# Melt the DataFrame to long format
df_long = stack(df, Not(:xs))

show(df_long, allrows=false)
println("\n")

show(names(df_long))
```

Explanation

```julia
df_long = stack(df, Not(:xs))

show(df_long, allrows=false)
println("\n")

show(names(df_long))
```



We can see the result as follows.

```output
❯ julia 03-stack.jl
39×3 DataFrame
 Row │ xs     variable  value 
     │ Int64  String    Int64 
─────┼────────────────────────
   1 │     0  ys1           5
   2 │     1  ys1           9
   3 │     2  ys1          13
   4 │     3  ys1          17
  ⋮  │   ⋮       ⋮        ⋮
  36 │     9  ys3        1742
  37 │    10  ys3        2345
  38 │    11  ys3        3074
  39 │    12  ys3        3941
               31 rows omitted

["xs", "variable", "value"]%  
```



We can see that this dataframe has
three series: [`ys1`, `ys2`, `ys3`].

You can obtain the interactive `JupyterLab` in this following link:

* **03-stack.jl**

Stacked (or melted) data makes it easier,
to feed multiple series into a single plot.
Our charts become neater,
and our code becomes less repetitive.

#### Curve Fitting

Now, the real fun begins.
Let's fit curves of varying orders for our three series.

* **04-poly-fit.jl**

```julia
using CSV, DataFrames, Polynomials, Printf

# Read data from CSV file
# Strip spaces from column names
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

# Extract columns from DataFrame
x_values = df.xs
y_values1 = df.ys1
y_values2 = df.ys2
y_values3 = df.ys3

# Perform linear regression for ys1
pf_1 = fit(x_values, y_values1, 1)

coeffs_r1 = reverse(coeffs(pf_1))
coeffs_fmt_1 = [
  round(c, digits=2) for c in coeffs_r1]

println("Coefficients (a, b) for ys1:")
println(coeffs_fmt_1, "\n")

# Perform quadratic curve fitting for ys2
pf_2 = fit(x_values, y_values2, 2)

coeffs_r2 = reverse(coeffs(pf_2))
coeffs_fmt_2 = [
  round(c, digits=2) for c in coeffs_r2]

println("Coefficients (a, b, c) for ys2:")
println(coeffs_fmt_2, "\n")

# Perform cubic curve fitting for ys3
pf_3 = fit(x_values, y_values3, 3)

coeffs_r3 = reverse(coeffs(pf_3))
coeffs_fmt_3 = [
  round(c, digits=2) for c in coeffs_r3]

println("Coefficients (a, b, c, d) for ys3:")
println(coeffs_fmt_3, "\n")
```

This is how we can define each series.
First, we read data from CSV file,
and also strip spaces from column names.
Then extract columns from DataFrame.

```julia
using CSV, DataFrames, Polynomials, Printf

df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

x_values = df.xs
y_values1 = df.ys1
y_values2 = df.ys2
y_values3 = df.ys3
```



We match each series with a polynomial of suitable ambition.
This is how we can calculate
polynomial coefficient for each series.

* linear regression (order 1) for `ys₁`
* quadratic curve fitting (order 2) for `ys₂`
* cubic curve fitting (order 3) for  `ys₃`

```julia
pf_1 = fit(x_values, y_values1, 1)

coeffs_r1 = reverse(coeffs(pf_1))
coeffs_fmt_1 = [
  round(c, digits=2) for c in coeffs_r1]

println("Coefficients (a, b) for ys1:")
println(coeffs_fmt_1, "\n")
```

... and similarly for pf_2 and pf_3.

```julia
pf_2 = fit(x_values, y_values2, 2)
...

pf_3 = fit(x_values, y_values3, 3)
...
```



We can see the result as follows.

```output
❯ julia 04-poly-fit.jl
Coefficients (a, b) for ys1:
[4.0, 5.0]

Coefficients (a, b, c) for ys2:
[3.0, 4.0, 5.0]

Coefficients (a, b, c, d) for ys3:
[2.0, 3.0, 4.0, 5.0]
```



📓 Jupyter version here: 

* **04-poly-fit.jl**

By fitting different polynomial orders,
we can assess the complexity of each trend.
Are we dealing with a gentle slope or a chaotic rollercoaster?

#### Merge All Series in One Function

Time to refactor.
Let's write a reusable function and pass symbols like pros.

* **05-poly-merge.jl**

```julia
using CSV, DataFrames, Polynomials, Printf

function calc_coeff(df::DataFrame,
    x_col::Symbol, y_col::Symbol, order::Int)

  # Extract x and y values
  xs = df[!, x_col]
  ys = df[!, y_col]

  order_text = Dict(1 => "Linear",
    2 => "Quadratic", 3 => "Cubic")
  coeff_text = Dict(1 => "(a, b)",
    2 => "(a, b, c)", 3 => "(a, b, c, d)")

  # Perform polynomial fitting
  # Reverse coefficients to match output
  # Format coefficients
  pf = fit(xs, ys, order)
  cfs_r = reverse(coeffs(pf))
  cfs_fmt = [round(c, digits=2) for c in cfs_r]

  # Using string interpolation to print the result
  println("Curve type for $y_col: ",
    order_text[order])
  println("Coefficients ",
    "$(coeff_text[order]):\n\t$cfs_fmt\n")
end

# Read data from CSV file
df = CSV.read("series.csv", DataFrame)

# Strip spaces from column names
rename!(df, Symbol.(strip.(string.(names(df)), ' ')))

# Call the function for each y column
# with respective order
println("Using Polynomials.fit\n")
calc_coeff(df, :xs, :ys1, 1)
calc_coeff(df, :xs, :ys2, 2)
calc_coeff(df, :xs, :ys3, 3)
```

With this symbol name,
we can extract x and y values.
Then perform polynomial fitting,
for three kinds of polynomial order.

$$
\begin{array}{|c|c|}
\hline
order = 1 & y = a + b{x}  \\
\hline
order = 2 & y = a + b{x} + c{x}^2 \\
\hline
order = 3 & y = a + b{x} + c{x}^2 + d{x}^3  \\
\hline
\end{array}
$$

With this equation, we need to
reverse coefficients to match output.
We also need to round the coefficients,
and using string interpolation to print the result

```julia
function calc_coeff(df::DataFrame,
    x_col::Symbol, y_col::Symbol, order::Int)

  xs = df[!, x_col]
  ys = df[!, y_col]

  order_text = Dict(1 => "Linear",
    2 => "Quadratic", 3 => "Cubic")
  coeff_text = Dict(1 => "(a, b)",
    2 => "(a, b, c)", 3 => "(a, b, c, d)")

  pf = fit(xs, ys, order)
  cfs_r = reverse(coeffs(pf))
  cfs_fmt = [round(c, digits=2) for c in cfs_r]

  println("Curve type for $y_col: ",
    order_text[order])
  println("Coefficients ",
    "$(coeff_text[order]):\n\t$cfs_fmt\n")
end
```



Let's call the function for each ys series
with respective order.

```julia
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)), ' ')))

println("Using Polynomials.fit\n")
calc_coeff(df, :xs, :ys1, 1)
calc_coeff(df, :xs, :ys2, 2)
calc_coeff(df, :xs, :ys3, 3)
```



We can see the result as follows.

```output
❯ julia 05-poly-merge.jl
Using Polynomials.fit

Curve type for ys1: Linear
Coefficients (a, b):
        [4.0, 5.0]

Curve type for ys2: Quadratic
Coefficients (a, b, c):
        [3.0, 4.0, 5.0]

Curve type for ys3: Cubic
Coefficients (a, b, c, d):
        [2.0, 3.0, 4.0, 5.0]
```



📓 Jupyter version here: 

* **05-poly-merge.jl**

We avoid copy-paste regression,
by turning repeated logic into one elegant function.
Reusability is the hallmark of statistical sanity.

-- -- --

### Plot

> Where regressions meet Renaissance.

Wouldn't it be satisfying,
if we could see the regression we just calculated?
I mean, what's the point of fitting models,
if we don't let them strut their stuff on a plot?

#### Straight Line

Let's start with the most basic of polynomial creatures: the straight line.
No drama, no surprises, just honest-to-goodness linearity.

* **11-poly-linear.jl**

```julia
using CSV, DataFrames, Polynomials, Plots

# Read data from CSV file
# Strip spaces from column names
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)), ' ')))

# Extract columns from DataFrame
xs = df.xs
ys = df.ys1
println(xs, "\n", ys, "\n")

# Perform linear regression for ys
pf = fit(xs, ys, 1)
cfs_r = reverse(coeffs(pf))
cfs_fmt = [
  round(c, digits=2) for c in cfs_r]

println("Coefficients (a, b) for ys:")
println(cfs_fmt, "\n")

# Generate Series for Plotting
xp = range(minimum(xs), maximum(xs), length=100)
yp = pf.(xp)

# Plotting
scatter(xs, ys,
  label="Data Points")
plot!(xp, yp, color=:red,
  label="Linear Equation")
xlabel!("X values")
ylabel!("Y values")
title!("Straight line fitting")

# Save the plot as a PNG file
savefig("11-poly-linear.png")
```

To begin, we bring in our trusty tools.
Think of these as the stat nerd’s brush and palette:
We can install using julia REPL.

```julia
using CSV, DataFrames, Polynomials, Plots
```

As usual, we load the data from CSV and sanitize those column names.
Then extract columns from DataFrame,
like we're preparing them for polite statistical society:

```julia
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)), ' ')))

xs = df.xs
ys = df.ys1
println(xs, "\n", ys, "\n")
```

🖼️ Visual checkpoint

Seeing all fits 

Now we fit a linear model by performing linear regression for ys.
And get a new pair series (xp, yp) for the plot.
We also pretty-print the coefficients because we’re civilised like that:

```julia
pf = fit(xs, ys, 1)
cfs_r = reverse(coeffs(pf))
cfs_fmt = [
  round(c, digits=2) for c in cfs_r]

println("Coefficients (a, b) for ys:")
println(cfs_fmt, "\n")

xp = range(minimum(xs), maximum(xs), length=100)
yp = pf.(xp)
```

📉 Mid-plot drama



And now, the fun part—drawing it.

As you can see the grammar here is interesting.
First we draw the first plot using `scatter`,
then we can add the above plot using other plot parts.
All additional parts use exclamation `!`.

```julia
scatter(xs, ys,
  label="Data Points")
plot!(xp, yp, color=:red,
  label="Linear Equation")
xlabel!("X values")
ylabel!("Y values")
title!("Straight line fitting")
```



💾 Save our masterpiece

Then finally save the plot output,
as a PNG file.

```julia
savefig("11-poly-linear.png")
```

We can see the result as follows.

```output
❯ julia 11-poly-linear.jl
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
[5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53]

Coefficients (a, b) for ys:
[4.0, 5.0]
```

📸 Gallery update

The plot result can be shown as follows:



🧪 Interactive playground:

You can obtain the interactive `JupyterLab` in this following link:

* **11-poly-linear.jl**

Linear fitting is our first statistical hello to data trends.
It tells us if the relationship walks in a straight line or takes a detour.

#### Quadratic Curve

Lines are great.
But sometimes data likes to show off and curve a bit.
Let's adapt code above for second order.
Extract columns from DataFrame,
then perform quadratic regression for ys.

* **12-poly-quadratic.jl**

```julia
using CSV, DataFrames, Polynomials, Plots

# Read data from CSV file
# Strip spaces from column names
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)), ' ')))

# Extract columns from DataFrame
xs = df.xs
ys = df.ys2
println(xs, "\n", ys, "\n")

# Perform quadratic regression for ys
pf = fit(xs, ys, 2)
cfs_r = reverse(coeffs(pf))
cfs_fmt = [
  round(c, digits=2) for c in cfs_r]

println("Coefficients (a, b, c) for ys:")
println(cfs_fmt, "\n")

# Generate Series for Plotting
xp = range(minimum(xs), maximum(xs), length=100)
yp = pf.(xp)

# Plotting
scatter(xs, ys,
  label="Data Points")
plot!(xp, yp, color=:red,
  label="Fitted second-order polynomial")
xlabel!("X values")
ylabel!("Y values")
title!("Quadratic curve fitting")

# Save the plot as a PNG file
savefig("12-poly-quadratic.png")
```

Explanation

```julia
xs = df.xs
ys = df.ys2
println(xs, "\n", ys, "\n")

pf = fit(xs, ys, 2)
cfs_r = reverse(coeffs(pf))
cfs_fmt = [
  round(c, digits=2) for c in cfs_r]

println("Coefficients (a, b, c) for ys:")
println(cfs_fmt, "\n")
```

📸 Quadratic got curves



The plot result can be shown as follows:



📚 Interactive version:

You can obtain the interactive `JupyterLab` in this following link:

* **12-poly-quadratic.jl**

Quadratics help us catch nonlinear patterns,
that a straight line would totally miss.
We're not just drawing curves.
We’re modeling real-world bounce and dip.

#### Cubic Curve

When quadratic still doesn't cut it,
bring in the big polynomial guns: cubic regression.

* **13-poly-cubic.jl**

```julia
using CSV, DataFrames, Polynomials, Plots

# Read data from CSV file
# Strip spaces from column names
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)), ' ')))

# Extract columns from DataFrame
xs = df.xs
ys = df.ys3
println(xs, "\n", ys, "\n")

# Perform cubic regression for ys
pf = fit(xs, ys, 3)
cfs_r = reverse(coeffs(pf))
cfs_fmt = [
  round(c, digits=2) for c in cfs_r]

println("Coefficients (a, b, c, d) for ys:")
println(cfs_fmt, "\n")

# Generate Series for Plotting
xp = range(minimum(xs), maximum(xs), length=100)
yp = pf.(xp)

# Plotting
scatter(xs, ys,
  label="Data Points")
plot!(xp, yp, color=:red,
  label="Fitted third-order polynomial")
xlabel!("X values")
ylabel!("Y values")
title!("Cubic curve fitting")

# Save the plot as a PNG file
savefig("13-poly-cubic.png")
```

Explanation

```julia

xs = df.xs
ys = df.ys3
println(xs, "\n", ys, "\n")

pf = fit(xs, ys, 3)
cfs_r = reverse(coeffs(pf))
cfs_fmt = [
  round(c, digits=2) for c in cfs_r]

println("Coefficients (a, b, c, d) for ys:")
println(cfs_fmt, "\n")
```



🎢 Now that’s a curve

The plot result can be shown as follows:



🧪 Interactive notebook:

You can obtain the interactive `JupyterLab` in this following link:

* **13-poly-cubic.jl**

Cubic fits are flexible. Maybe too flexible. 
ike a statistics student overfitting their final project.
Use with care.

-- -- --

### Merging Plot

Why juggle multiple columns when one will do?
Let's use a single series and fit it using all three orders.
Because comparing fits is our version of competitive curling.

Instead of using three series,
we can analyze only one series,
but using three different orders.

* **15-poly-merge.jl**

```julia
using CSV, DataFrames, Polynomials, Plots, Printf

function calc_coeff(df::DataFrame,
    x_col::Symbol, y_col::Symbol, order::Int)

  # Extract x and y values
  xs = df[!, x_col]
  ys = df[!, y_col]

  order_text = Dict(1 => "Linear",
    2 => "Quadratic", 3 => "Cubic")
  coeff_text = Dict(1 => "(a, b)",
    2 => "(a, b, c)", 3 => "(a, b, c, d)")

  # Perform polynomial fitting
  # Reverse coefficients to match output
  # Format coefficients
  pf = fit(xs, ys, order)
  cfs_r = reverse(coeffs(pf))
  cfs_fmt = [round(c, digits=2) for c in cfs_r]

  # Using string interpolation to print the result
  println("Curve type for $y_col: ",
    order_text[order])
  println("Coefficients ",
    "$(coeff_text[order]):\n\t$cfs_fmt\n")
end

function calc_coeffs(df::DataFrame)
  # Call the function for only ys3 column
  # with respective order
  println("Using Polynomials.fit\n")

  calc_coeff(df, :xs, :ys3, 1)
  calc_coeff(df, :xs, :ys3, 2)
  calc_coeff(df, :xs, :ys3, 3)
end

function calc_plot_all(df::DataFrame,
    x_col::Symbol, y_col::Symbol)

  # Extract x and y values
  xs = df[!, x_col]
  ys = df[!, y_col]

  # Draw Plot
  xp = range(minimum(xs), maximum(xs), length=100)
  yp1 = fit(xs, ys, 1).(xp)
  yp2 = fit(xs, ys, 2).(xp)
  yp3 = fit(xs, ys, 3).(xp)

  # Plotting
  scatter(xs, ys,
    label="Data Points")
  plot!(xp, yp1, color=:red,
    label="Linear Equation")
  plot!(xp, yp2, color=:green,
    label="Fitted second-order polynomial")
  plot!(xp, yp3, color=:blue,
    label="Fitted third-order polynomial")

  # Decoration
  xlabel!("X values")
  ylabel!("Y values")
  title!("Polynomial Curve Fitting")

  # Save the plot as a PNG file
  savefig("15-poly-merge.png")
end

# Read data from CSV file
# Strip spaces from column names
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

# Plot all three series
calc_coeffs(df)
calc_plot_all(df, :xs, :ys3)
```

First, we create function skeletons:

```julia
using CSV, DataFrames, Polynomials, Plots, Printf

function calc_coeff(df::DataFrame,
    x_col::Symbol, y_col::Symbol, order::Int)
  ...
end

function calc_coeffs(df::DataFrame)
  ...
end

function calc_plot_all(df::DataFrame,
    x_col::Symbol, y_col::Symbol)
  ...
end
```



We are still using symbol name as parameter argument.
Form this we extract x and y values.
Then perform polynomial fitting as usual.
Remember that we have three kinds of polynomial order.

$$
\begin{array}{|c|c|}
\hline
order = 1 & y = a + b{x}  \\
\hline
order = 2 & y = a + b{x} + c{x}^2 \\
\hline
order = 3 & y = a + b{x} + c{x}^2 + d{x}^3  \\
\hline
\end{array}
$$

#### Fit and print coefficients:

With this equation, we need to
reverse coefficients to match output.
We also need to round the coefficients,
and using string interpolation to print the result

```julia
function calc_coeff(df::DataFrame,
    x_col::Symbol, y_col::Symbol, order::Int)

  xs = df[!, x_col]
  ys = df[!, y_col]

  order_text = Dict(1 => "Linear",
    2 => "Quadratic", 3 => "Cubic")
  coeff_text = Dict(1 => "(a, b)",
    2 => "(a, b, c)", 3 => "(a, b, c, d)")

  pf = fit(xs, ys, order)
  cfs_r = reverse(coeffs(pf))
  cfs_fmt = [round(c, digits=2) for c in cfs_r]

  println("Curve type for $y_col: ",
    order_text[order])
  println("Coefficients ",
    "$(coeff_text[order]):\n\t$cfs_fmt\n")
end
```



#### Aggregate results:

Beside plotting,
we need to display the coefficient result.
Here we call the function for only ys3 column
with respective order.

```julia
function calc_coeffs(df::DataFrame)
  println("Using Polynomials.fit\n")

  calc_coeff(df, :xs, :ys3, 1)
  calc_coeff(df, :xs, :ys3, 2)
  calc_coeff(df, :xs, :ys3, 3)
end
```



#### Plot them all:

In this function, we calc and plot.
* Calc all three series and
* Plot all three curve fittings.

```julia
function calc_plot_all(df::DataFrame,
    x_col::Symbol, y_col::Symbol)

  # Extract x and y values
  xs = df[!, x_col]
  ys = df[!, y_col]

  # Draw Plot
  xp = range(minimum(xs), maximum(xs), length=100)
  yp1 = fit(xs, ys, 1).(xp)
  yp2 = fit(xs, ys, 2).(xp)
  yp3 = fit(xs, ys, 3).(xp)

  # Plotting
  scatter(xs, ys,
    label="Data Points")
  plot!(xp, yp1, color=:red,
    label="Linear Equation")
  plot!(xp, yp2, color=:green,
    label="Fitted second-order polynomial")
  plot!(xp, yp3, color=:blue,
    label="Fitted third-order polynomial")

  # Decoration
  xlabel!("X values")
  ylabel!("Y values")
  title!("Polynomial Curve Fitting")

  # Save the plot as a PNG file
  savefig("15-poly-merge.png")
end
```



#### Pull it together:

Let's gather it all together.
Plot all three series.

```julia
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

calc_coeffs(df)
calc_plot_all(df, :xs, :ys3)
```



We can see the result as follows.

```output
❯ julia 15-poly-merge.jl
Using Polynomials.fit

Curve type for ys1: Linear
Coefficients (a, b):
        [4.0, 5.0]

Curve type for ys2: Quadratic
Coefficients (a, b, c):
        [3.0, 4.0, 5.0]

Curve type for ys3: Cubic
Coefficients (a, b, c, d):
        [2.0, 3.0, 4.0, 5.0]
```



📸 The whole gallery

The plot result can be shown as follows:



📚 Interactive version:

You can obtain the interactive `JupyterLab` in this following link:

* **15-poly-merge.jl**

Seeing all fits on one canvas,
helps us judge whether our data just wants:
a line, a parabola, or full polynomial dramatics.

-- -- --

### Struct

> Building Class

Julia has unique way to define class.
You can observe the example below.

Structs in Julia are how we create custom data types with methods.
Think of it like classes, but on vacation.
No self, no this, just vibes and clear structure.

It may strange at first.
And I don't know the real reason for not having
common building block for the class.

All I can imagine is working with `jupyter notebook`.
It is easier to write modular code this way,
without the limit of building block issue.

* **16-poly-struct.jl**

```julia
using CSV, DataFrames, Polynomials, Plots, Printf

mutable struct CurveFitter
  df::DataFrame
  x_col::Symbol
  y_col::Symbol

  function CurveFitter(df::DataFrame,
      x_col::Symbol, y_col::Symbol)
    return new(df, x_col, y_col)
  end
end

function calc_coeff(cf::CurveFitter, order::Int)
  # Extract x and y values
  xs = cf.df[!, cf.x_col]
  ys = cf.df[!, cf.y_col]

  order_text = Dict(1 => "Linear",
    2 => "Quadratic", 3 => "Cubic")
  coeff_text = Dict(1 => "(a, b)",
    2 => "(a, b, c)", 3 => "(a, b, c, d)")

  # Perform polynomial fitting
  # Reverse coefficients to match output
  # Format coefficients
  pf = fit(xs, ys, order)
  cfs_r = reverse(coeffs(pf))
  cfs_fmt = [round(c, digits=2) for c in cfs_r]

  # Using string interpolation to print the result
  println("Curve type for $(cf.y_col): ",
    order_text[order])
  println("Coefficients ",
    coeff_text[order], ":\n\t", cfs_fmt, "\n")
end

function calc_coeffs(cf::CurveFitter)
  println("Using Polynomials.fit\n")
  for order in 1:3
    calc_coeff(cf, order)
  end
end

function calc_plot_all(cf::CurveFitter)
  # Extract x and y values
  xs = cf.df[!, cf.x_col]
  ys = cf.df[!, cf.y_col]

  # Generate x values for plotting
  xp = range(minimum(xs), maximum(xs), length=100)

  # Perform polynomial fitting for different orders
  yp1 = fit(xs, ys, 1).(xp)
  yp2 = fit(xs, ys, 2).(xp)
  yp3 = fit(xs, ys, 3).(xp)

  # Plotting
  scatter(xs, ys,
    label="Data Points")
  plot!(xp, yp1, color=:red,
    label="Linear Equation")
  plot!(xp, yp2, color=:green,
    label="Fitted second-order polynomial")
  plot!(xp, yp3, color=:blue,
    label="Fitted third-order polynomial")

  # Decoration
  xlabel!("X values")
  ylabel!("Y values")
  title!("Polynomial Curve Fitting")

  # Save the plot as a PNG file
  savefig("16-poly-struct.png")
end

# Read data from CSV file
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

# Define a CurveFitter object
# Calculate coefficients and plot all three series
cf = CurveFitter(df, :xs, :ys3)
calc_coeffs(cf)
calc_plot_all(cf)
```

Let's see the skeleton first.

```julia
using CSV, DataFrames, Polynomials, Plots, Printf

mutable struct CurveFitter
  ...
end

function calc_coeff(cf::CurveFitter, order::Int)

  ...
end

function calc_coeffs(cf::CurveFitter)
  ...
end

function calc_plot_all(cf::CurveFitter)
  ...
end
```



#### Create our CurveFitter type

Now, let's see this `mutable struct`.

```julia
mutable struct CurveFitter
  df::DataFrame
  x_col::Symbol
  y_col::Symbol

  function CurveFitter(df::DataFrame,
      x_col::Symbol, y_col::Symbol)
    return new(df, x_col, y_col)
  end
end
```



#### Add methods

Now we can define each methods of the class.

```julia
function calc_coeff(cf::CurveFitter, order::Int)
  xs = cf.df[!, cf.x_col]
  ys = cf.df[!, cf.y_col]

  order_text = Dict(1 => "Linear",
    2 => "Quadratic", 3 => "Cubic")
  coeff_text = Dict(1 => "(a, b)",
    2 => "(a, b, c)", 3 => "(a, b, c, d)")

  pf = fit(xs, ys, order)
  cfs_r = reverse(coeffs(pf))
  cfs_fmt = [round(c, digits=2) for c in cfs_r]

  println("Curve type for $(cf.y_col): ",
    order_text[order])
  println("Coefficients ",
    coeff_text[order], ":\n\t", cfs_fmt, "\n")
end
```



> There is no self

Each method use `cf::CurveFitter` as first parameter.

```julia
function calc_coeffs(cf::CurveFitter)
  println("Using Polynomials.fit\n")
  for order in 1:3
    calc_coeff(cf, order)
  end
end
```



This method is very similar with previous function.

```julia
function calc_plot_all(cf::CurveFitter, y_col::Symbol)
  xs = cf.df[!, cf.x_col]
  ys = cf.df[!, cf.y_col]

  xp = range(minimum(xs), maximum(xs), length=100)
  yp1 = fit(xs, ys, 1).(xp)
  yp2 = fit(xs, ys, 2).(xp)
  yp3 = fit(xs, ys, 3).(xp)

  scatter(xs, ys,
    label="Data Points")
  plot!(xp, yp1, color=:red,
    label="Linear Equation")
  plot!(xp, yp2, color=:green,
    label="Fitted second-order polynomial")
  plot!(xp, yp3, color=:blue,
    label="Fitted third-order polynomial")

  xlabel!("X values")
  ylabel!("Y values")
  title!("Polynomial Curve Fitting")

  savefig("16-poly-struct.png")
end
```



Again, let's gather all stuff together.
After reading data from CSV file.
We need to instantiate the class,
and call any necessary method.

This can be done by defining a CurveFitter object.
then calculate coefficients and plot all three series.

```julia
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

cf = CurveFitter(df, :xs, :ys3)
calc_coeffs(cf)
calc_plot_all(cf)
```

We can see the result as follows.

```output
❯ julia 16-poly-struct.jl
Using Polynomials.fit

Curve type for ys1: Linear
Coefficients (a, b):
        [4.0, 5.0]

Curve type for ys2: Quadratic
Coefficients (a, b, c):
        [3.0, 4.0, 5.0]

Curve type for ys3: Cubic
Coefficients (a, b, c, d):
        [2.0, 3.0, 4.0, 5.0]
```



The plot result can be shown as follows:



You can obtain the interactive `JupyterLab` in this following link:

* **16-poly-struct.jl**

Modularizing our work like this makes reuse and experimentation a breeze.
It’s not just tidy. It’s practical.

-- -- --

### What's the Next Chapter 🤔?

We’re back on our noble quest through the kingdom of `Julia`,
armed with semicolons and sharp wits.
This time, we're building classes
(a.k.a. _types_, because _classes_ are so last season),
exploring statistical properties,
and flexing our UTF-8 muscles,
to write equations that look like,
they walked straight out of a LaTeX fashion show.

Why bother? Because writing `μ` and `σ²`,
instead of mean and variance doesn't just make us look smarter,
it reduces cognitive switching between notation and code.
It's like giving our brain better variable names, but in Greek.

Also, this approach bridges the gap ,
etween our code and the math in the textbooks.
Fewer translation errors, fewer headaches.
It's like bringing a fluent interpreter,
to a multilingual statistics conference.

As always, we balance rigor with readability.
And sneak in a pun when least expected.

Consider continuing your `Julia`-verse adventures with
👉 **Trend - Language - Julia - Part Two**.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Explore statistic properties with Julia.
> Providing the data using linear model.

Julia is that one friend,
who not only solves complex math,
but also writes it beautifully in Unicode.
It can express mathematical functions,
in ways that look like they just walked off the page of a textbook.
Seriously, it's like `LaTeX` and `Python` had a mathematically gifted child.



#### Readable Code

However... just because we can write:

$$
\mathbf{y} = X \mathbf{\beta} + \mathbf{\varepsilon}
$$

It doesn't mean we should throw Greek letters everywhere,
like we're decorating a fraternity house.

_Readable code beats aesthetic code in production._ \
_Unicode is a flex, but clarity is a lifeline._

We statisticians know that beauty matters, but so does readability, 
specially when debugging code at 2AM while questioning life choices.
So while Unicode looks gorgeous,
we'll proceed with a conservative coding approach,
that still gets the job done and keeps future us from rage-quitting.

-- -- --

### Statistic Properties

Let's peek under the hood of how `Julia` handles statistical properties.
We'll start with the classic workhorse of regression: least squares.
This is where statisticians get misty-eyed—right,
before they argue about assumptions over coffee.

#### Manual Calculation

> The Spreadsheet Monk Way

Full code available.
You can check the detail of the manual calculation
in the source code below:

* **51-lq-manual.jl**

```julia
using CSV, DataFrames, Printf, Statistics

# Read data from CSV file
pairCSV = CSV.read("50-samples.csv", DataFrame)

# Extract x and y values from CSV data
x_observed = pairCSV.x
y_observed = pairCSV.y

# Number of data points
n = length(x_observed)

# Calculate sums
x_sum = sum(x_observed)
y_sum = sum(y_observed)

# Calculate means
x_mean = mean(x_observed)
y_mean = mean(y_observed)

# Output of basic properties
@printf("%-10s = %4d\n", "n", n)
@printf("∑x (total) = %7.2f\n", x_sum)
@printf("∑y (total) = %7.2f\n", y_sum)
@printf("x̄ (mean)   = %7.2f\n", x_mean)
@printf("ȳ (mean)   = %7.2f\n\n", y_mean)

# Calculate deviations
x_deviation = x_observed .- x_mean
y_deviation = y_observed .- y_mean

# Calculate squared deviations
x_sq_deviation = sum(x_deviation .^ 2)
y_sq_deviation = sum(y_deviation .^ 2)

# Calculate cross-deviation
xy_cross_deviation = sum(x_deviation .* y_deviation)

# Calculate slope (m) and intercept (b)
m_slope = xy_cross_deviation / x_sq_deviation
b_intercept = y_mean - m_slope * x_mean

# Output of least square calculation
@printf("∑(xᵢ-x̄)    = %9.2f\n", sum(x_deviation))
@printf("∑(yᵢ-ȳ)    = %9.2f\n", sum(y_deviation))
@printf("∑(xᵢ-x̄)²   = %9.2f\n", x_sq_deviation)
@printf("∑(yᵢ-ȳ)²   = %9.2f\n", y_sq_deviation)
@printf("∑(xᵢ-x̄)(yᵢ-ȳ)  = %9.2f\n", xy_cross_deviation)
@printf("m (slope)      = %9.2f\n", m_slope)
@printf("b (intercept)  = %9.2f\n\n", b_intercept)

@printf("Equation     y = %.2f + %.2f.x\n\n", b_intercept, m_slope)

# Calculate variance
x_variance = x_sq_deviation / (n-1)
y_variance = y_sq_deviation / (n-1)

# Calculate covariance
xy_covariance = xy_cross_deviation / (n-1)

# Calculate standard deviations
x_std_dev = sqrt(x_variance)
y_std_dev = sqrt(y_variance)

# Calculate Pearson correlation coefficient (r)
r = xy_covariance / (x_std_dev * y_std_dev)

# Calculate R-squared (R²)
r_squared = r^2

# Output of correlation calculation
@printf("sₓ² (variance) = %9.2f\n", x_variance)
@printf("sy² (variance) = %9.2f\n", y_variance)
@printf("covariance     = %9.2f\n", xy_covariance)
@printf("sₓ (std dev)   = %9.2f\n", x_std_dev)
@printf("sy (std dev)   = %9.2f\n", y_std_dev)
@printf("r (pearson)    = %9.2f\n", r)
@printf("R²             = %9.2f\n\n", r_squared)

# Create regression line
y_fit = m_slope .* x_observed .+ b_intercept
y_err = y_observed .- y_fit

# Calculate sum of squared residuals
ss_residuals = sum(y_err .^ 2)

# Calculate degrees of freedom
df = n - 2

# Calculate variance of residuals (MSE)
var_residuals = ss_residuals / df

# Calculate standard error of the slope
std_err_slope = sqrt(var_residuals / x_sq_deviation)

# Calculate t-value
t_value = m_slope / std_err_slope

# Output the results
@printf("SSR = ∑ϵ²           = %9.2f\n", ss_residuals)
@printf("MSE = ∑ϵ²/(n-2)     = %9.2f\n", var_residuals)
@printf("SE(β₁)  = √(MSE/sₓ) = %9.2f\n", std_err_slope)
@printf("t-value = β̅₁/SE(β₁) = %9.2f\n\n", t_value)
```

After reading data from CSV,
we extract our favorite bickering pair: `x` and `y`.

```julia
using CSV, DataFrames, Printf, Statistics

pairCSV = CSV.read("50-samples.csv", DataFrame)
x_observed = pairCSV.x
y_observed = pairCSV.y
```



We compute sample size, totals, and means,
the boring part of any romantic relationship
then printout the basic properties.

```julia
n = length(x_observed)

x_sum = sum(x_observed)
y_sum = sum(y_observed)

x_mean = mean(x_observed)
y_mean = mean(y_observed)

@printf("%-10s = %4d\n", "n", n)
@printf("∑x (total) = %7.2f\n", x_sum)
@printf("∑y (total) = %7.2f\n", y_sum)
@printf("x̄ (mean)   = %7.2f\n", x_mean)
@printf("ȳ (mean)   = %7.2f\n\n", y_mean)
```

These are the building blocks for everything else.
Miss a mean, and the whole regression falls like a badly balanced ANOVA.



Let's take those deviations for a walk:
square them, multiply them,
and mash them into slope (`m`) and intercept (`b`).
The usual statistics hazing ritual.
Then printout the least square calculation.

```julia
x_deviation = x_observed .- x_mean
y_deviation = y_observed .- y_mean

x_sq_deviation = sum(x_deviation .^ 2)
y_sq_deviation = sum(y_deviation .^ 2)
xy_cross_deviation = sum(x_deviation .* y_deviation)

m_slope = xy_cross_deviation / x_sq_deviation
b_intercept = y_mean - m_slope * x_mean

@printf("∑(xᵢ-x̄)    = %9.2f\n", sum(x_deviation))
@printf("∑(yᵢ-ȳ)    = %9.2f\n", sum(y_deviation))
@printf("∑(xᵢ-x̄)²   = %9.2f\n", x_sq_deviation)
@printf("∑(yᵢ-ȳ)²   = %9.2f\n", y_sq_deviation)
@printf("∑(xᵢ-x̄)(yᵢ-ȳ)  = %9.2f\n", xy_cross_deviation)
@printf("m (slope)      = %9.2f\n", m_slope)
@printf("b (intercept)  = %9.2f\n\n", b_intercept)

@printf("Equation     y = %.2f + %.2f.x\n\n", b_intercept, m_slope)
```

We're trying to find the line that best hugs our data.
Mathematically speaking,
least squares is the most socially acceptable line of best fit.



Now we flex our calculator muscles to find:
variance, standard deviation, covariance,
Pearson correlation coefficient (r), and the beloved R-squared (R²).
The crowd cheers.
Then again printout the correlation calculations as usual.

```julia
x_variance = x_sq_deviation / (n-1)
y_variance = y_sq_deviation / (n-1)
xy_covariance = xy_cross_deviation / (n-1)

x_std_dev = sqrt(x_variance)
y_std_dev = sqrt(y_variance)

r = xy_covariance / (x_std_dev * y_std_dev)
r_squared = r^2

@printf("sₓ² (variance) = %9.2f\n", x_variance)
@printf("sy² (variance) = %9.2f\n", y_variance)
@printf("covariance     = %9.2f\n", xy_covariance)
@printf("sₓ (std dev)   = %9.2f\n", x_std_dev)
@printf("sy (std dev)   = %9.2f\n", y_std_dev)
@printf("r (pearson)    = %9.2f\n", r)
@printf("R²             = %9.2f\n\n", r_squared)
```

This tells us how tight the data hugs the trend line.
In statistics, we call this "_relationship goals._"



> Residuals time:

subtract predictions from reality, 
just like grading our expectations after a family reunion.
That gap, between expectations and reality, is like a residual in a regression.

We need to create regression line,
along with residual error, using array operations.
Then calculate sum of squared residuals,
also using array operations.

Based on degrees of freedom,
calculate further from variance of residuals (MSE),
standard error of the slope, and calculate t-value,
then printout the output the results,'
again and again, and again...

```julia
y_fit = m_slope .* x_observed .+ b_intercept
y_err = y_observed .- y_fit

ss_residuals = sum(y_err .^ 2)
df = n - 2

var_residuals = ss_residuals / df
std_err_slope = sqrt(var_residuals / x_sq_deviation)
t_value = m_slope / std_err_slope

@printf("SSR = ∑ϵ²           = %9.2f\n", ss_residuals)
@printf("MSE = ∑ϵ²/(n-2)     = %9.2f\n", var_residuals)
@printf("SE(β₁)  = √(MSE/sₓ) = %9.2f\n", std_err_slope)
@printf("t-value = β̅₁/SE(β₁) = %9.2f\n\n", t_value)
```

This is the beating heart of inference.
We're not just fitting a line.
We're making statistically sound claims.



> Execution result:

```output
❯ julia 51-lq-manual.jl
n          =   13
∑x (total) =   78.00
∑y (total) = 2327.00
x̄ (mean)   =    6.00
ȳ (mean)   =  179.00

∑(xᵢ-x̄)    =      0.00
∑(yᵢ-ȳ)    =      0.00
∑(xᵢ-x̄)²   =    182.00
∑(yᵢ-ȳ)²   = 309218.00
∑(xᵢ-x̄)(yᵢ-ȳ)  =   7280.00
m (slope)      =     40.00
b (intercept)  =    -61.00

Equation     y = -61.00 + 40.00.x

sₓ² (variance) =     15.17
sy² (variance) =  25768.17
covariance     =    606.67
sₓ (std dev)   =      3.89
sy (std dev)   =    160.52
r (pearson)    =      0.97
R²             =      0.94

SSR = ∑ϵ²           =  18018.00
MSE = ∑ϵ²/(n-2)     =   1638.00
SE(β₁)  = √(MSE/sₓ) =      3.00
t-value = β̅₁/SE(β₁) =     13.33
```



📓 Interactive Jupyter version here:

You can obtain the interactive `JupyterLab` in this following link:

* **51-lq-manual.jl**

#### GLM Library

> Using Built-in Method

_Now boarding: the GLM train. All manual passengers, please stay seated._

We can simplified aboce calculation with built-in method.

Link to code:

* **52-lq-built-in.jl**

```julia
using CSV, DataFrames, Printf, Statistics, GLM

# Read data from CSV file
pairCSV = CSV.read("50-samples.csv", DataFrame)

# Extract x and y values from CSV data
x_observed = pairCSV.x
y_observed = pairCSV.y

# Number of data points
n = size(pairCSV, 1)

# Calculate sums
x_sum = sum(x_observed)
y_sum = sum(y_observed)

# Calculate means
x_mean = mean(x_observed)
y_mean = mean(y_observed)

# Output of basic properties
@printf("%-10s = %4d\n", "n", n)
@printf("∑x (total) = %7.2f\n", x_sum)
@printf("∑y (total) = %7.2f\n", y_sum)
@printf("x̄ (mean)   = %7.2f\n", x_mean)
@printf("ȳ (mean)   = %7.2f\n\n", y_mean)

# Fit a linear model
model = lm(@formula(y ~ x), pairCSV)

# Get coefficients
# Extract slope and intercept
coefs = coef(model)
m_slope = coefs[2]
b_intercept = coefs[1]

# Output of least square calculation
@printf("m (slope)      = %9.2f\n", m_slope)
@printf("b (intercept)  = %9.2f\n\n", b_intercept)
@printf("Equation     y = %.2f + %.2f.x\n\n", b_intercept, m_slope)

# Calculate variance
x_variance = var(x_observed)
y_variance = var(y_observed)

# Calculate covariance
xy_covariance = cov(x_observed, y_observed)

# Calculate standard deviations
x_std_dev = std(x_observed)
y_std_dev = std(y_observed)

# Calculate Pearson correlation coefficient (r)
r = cor(x_observed, y_observed)

# Calculate R-squared (R²)
r_squared = r^2

# Output of correlation calculation
@printf("sₓ² (variance) = %9.2f\n", x_variance)
@printf("sy² (variance) = %9.2f\n", y_variance)
@printf("covariance     = %9.2f\n", xy_covariance)
@printf("sₓ (std dev)   = %9.2f\n", x_std_dev)
@printf("sy (std dev)   = %9.2f\n", y_std_dev)
@printf("r (pearson)    = %9.2f\n", r)
@printf("R²             = %9.2f\n\n", r_squared)

# Generate predicted values
# Calculate residuals
y_fit = predict(model)
y_err = residuals(model)

# Calculate sum of squared residuals
ss_residuals = sum(y_err .^ 2)

# Calculate degrees of freedom
df = n - 2

# Calculate variance of residuals (MSE)
var_residuals = ss_residuals / df

# Calculate standard error of the slope
x_deviation = x_observed .- x_mean
x_sq_deviation = sum(x_deviation .^ 2)
std_err_slope = sqrt(var_residuals / x_sq_deviation)

# Calculate t-value
t_value = m_slope / std_err_slope

# Output the results
@printf("SSR = ∑ϵ²           = %9.2f\n", ss_residuals)
@printf("MSE = ∑ϵ²/(n-2)     = %9.2f\n", var_residuals)
@printf("∑(xᵢ-x̄)²            = %9.2f\n", x_sq_deviation)
@printf("SE(β₁)  = √(MSE/sₓ) = %9.2f\n", std_err_slope)
@printf("t-value = β̅₁/SE(β₁) = %9.2f\n\n", t_value)
```

We import `GLM`.
`Julia`'s own statistics power tool.

```julia
using CSV, DataFrames, Printf, Statistics, GLM
```



Like in `R`,
we fit a linear model with `lm()`.
The syntax feels like `R`,
with a fresh paint job and no memory leaks.

```julia
model = lm(@formula(y ~ x), pairCSV)
coefs = coef(model)
m_slope = coefs[2]
b_intercept = coefs[1]

@printf("m (slope)      = %9.2f\n", m_slope)
@printf("b (intercept)  = %9.2f\n\n", b_intercept)
@printf("Equation     y = %.2f + %.2f.x\n\n", b_intercept, m_slope)
```



We still do our ritual variance-covariance dance.
This time, using built-in methods that actually want to be used:
variance, covariance, standard deviations,
and even the pearson correlation coefficient (r).
From this we can manually calculate R-squared (R²).

```julia
x_variance = var(x_observed)
y_variance = var(y_observed)
xy_covariance = cov(x_observed, y_observed)

x_std_dev = std(x_observed)
y_std_dev = std(y_observed)

r = cor(x_observed, y_observed)
r_squared = r^2

@printf("sₓ² (variance) = %9.2f\n", x_variance)
@printf("sy² (variance) = %9.2f\n", y_variance)
@printf("covariance     = %9.2f\n", xy_covariance)
@printf("sₓ (std dev)   = %9.2f\n", x_std_dev)
@printf("sy (std dev)   = %9.2f\n", y_std_dev)
@printf("r (pearson)    = %9.2f\n", r)
@printf("R²             = %9.2f\n\n", r_squared)
```

These are sanity checks.
Even if the model does the heavy lifting,
we still want to peek inside ,
nd make sure it's not drunk on assumptions.



From previous this linear model,
we can generate predicted values along with residuals.
Then we can continue doing our manual calculation.
Just ask politely and `GLM` serves it on a silver platter.

```julia
y_fit = predict(model)
y_err = residuals(model)

df = n - 2
ss_residuals = sum(y_err .^ 2)
var_residuals = ss_residuals / df

x_deviation = x_observed .- x_mean
x_sq_deviation = sum(x_deviation .^ 2)
std_err_slope = sqrt(var_residuals / x_sq_deviation)
t_value = m_slope / std_err_slope

@printf("SSR = ∑ϵ²           = %9.2f\n", ss_residuals)
@printf("MSE = ∑ϵ²/(n-2)     = %9.2f\n", var_residuals)
@printf("∑(xᵢ-x̄)²            = %9.2f\n", x_sq_deviation)
@printf("SE(β₁)  = √(MSE/sₓ) = %9.2f\n", std_err_slope)
@printf("t-value = β̅₁/SE(β₁) = %9.2f\n\n", t_value)
```



> Execution result:

```output
❯ julia 52-lq-built-in.jl
n          =   13
∑x (total) =   78.00
∑y (total) = 2327.00
x̄ (mean)   =    6.00
ȳ (mean)   =  179.00

m (slope)      =     40.00
b (intercept)  =    -61.00

Equation     y = -61.00 + 40.00.x

sₓ² (variance) =     15.17
sy² (variance) =  25768.17
covariance     =    606.67
sₓ (std dev)   =      3.89
sy (std dev)   =    160.52
r (pearson)    =      0.97
R²             =      0.94

SSR = ∑ϵ²           =  18018.00
MSE = ∑ϵ²/(n-2)     =   1638.00
∑(xᵢ-x̄)²            =    182.00
SE(β₁)  = √(MSE/sₓ) =      3.00
t-value = β̅₁/SE(β₁) =     13.33
```



📓 Interactive Jupyter version here:

You can obtain the interactive `JupyterLab` in this following link:

* **52-lq-built-in.jl**

#### Final Thoughts

Whether we go monk-mode and write everything by hand,
or let GLM do the heavy lifting,
`Julia` gives us tools that are not just elegant, but trustworthy.

As long as we understand what's going on under the hood,
we can keep our statistical integrity—,
nd maybe even crack a smile while doing it.

-- -- --

### Unicode Symbols as Variables

> Making Greek Great Again

Let's take a detour from dry regressions,
and dive into something a bit more fun.
Unicode madness.

Julia, unlike our old high-school calculators,
is happy to speak Greek.
This section explores just how readable,
and elegant code can be,
when our variables wear togas and quote Pythagoras.

**In short**: our math professor’s chalkboard now runs `Julia`.

Why should our variables be limited to boring `x` and `y`,
when we could use the entire Greek fraternity?
Let’s treat our dataset like a philosophy class,
with `xᵢ`, `ȳ`, and `∑ϵ²` all mingling like Socratic thinkers.

#### Defining UTF-8 Variables

Yes, Julia lets us use UTF-8 characters for variable names,
no arcane flags, no weird syntax. Just copy-paste the Greek.
Let's have this experiment below:

* **53-lq-utf.jl**

```julia
using CSV, DataFrames, Printf, Statistics, GLM

# Read data from CSV file
df = CSV.read("50-samples.csv", DataFrame)

# Extract x and y values from CSV data
xᵢ = df.x
yᵢ = df.y

# Number of data points
n = length(xᵢ)

# Calculate sums
∑x = sum(xᵢ)
∑y = sum(yᵢ)

# Calculate means
x̄ = mean(xᵢ)
ȳ = mean(yᵢ)

# Output of basic properties
@printf("%-10s = %4d\n", "n", n)
@printf("∑x (total) = %7.2f\n", ∑x)
@printf("∑y (total) = %7.2f\n", ∑y)
@printf("x̄ (mean)   = %7.2f\n", x̄)
@printf("ȳ (mean)   = %7.2f\n\n", ȳ)

# Calculate variance
sₓ² = sum((xᵢ .- x̄).^2) / (n - 1)
sʸ² = sum((yᵢ .- ȳ).^2) / (n - 1)

# Calculate covariance
cov = sum((xᵢ .- x̄) .* (yᵢ .- ȳ)) / (n - 1)

# Calculate standard deviations
sₓ = sqrt(sₓ²)
sʸ = sqrt(sʸ²)

# Calculate Pearson correlation coefficient (r)
r = cov / (sₓ * sʸ)

# Calculate R-squared (R²)
r² = r^2

# Output of correlation calculation
@printf("sₓ² (variance) = %9.2f\n", sₓ²)
@printf("sʸ² (variance) = %9.2f\n", sʸ²)
@printf("covariance     = %9.2f\n", cov)
@printf("sₓ (std dev)   = %9.2f\n", sₓ)
@printf("sʸ (std dev)   = %9.2f\n", sʸ)
@printf("r (pearson)    = %9.2f\n", r)
@printf("R²             = %9.2f\n\n", r²)

# Calculate slope (m) and intercept (b)
mᵣ = sum((xᵢ .- x̄) .* (yᵢ .- ȳ)) / sum((xᵢ .- x̄).^2)
bᵣ = ȳ - mᵣ * x̄

@printf("m (slope)      = %9.2f\n", mᵣ)
@printf("b (intercept)  = %9.2f\n\n", bᵣ)
@printf("Equation     y = %.2f + %.2f.x\n\n", bᵣ, mᵣ)

# Create regression line
ŷᵢ = mᵣ .* xᵢ .+ bᵣ
ϵᵢ = yᵢ .- ŷᵢ

# Calculate sum of squared residuals
∑ϵ² = sum(ϵᵢ .^ 2)

# Calculate degrees of freedom
df = n - 2

# Calculate variance of residuals (MSE)
MSE = ∑ϵ² / df

# Calculate standard error of the slope
SE_β₁ = sqrt(MSE / sum((xᵢ .- x̄).^2))

# Calculate t-value
tᵥ = mᵣ / SE_β₁

# Output the results
@printf("SSR = ∑ϵ²           = %9.2f\n", ∑ϵ²)
@printf("MSE = ∑ϵ²/(n-2)     = %9.2f\n", MSE)
@printf("SE(β₁)  = √(MSE/sₓ) = %9.2f\n", SE_β₁)
@printf("t-value = β̅₁/SE(β₁) = %9.2f\n\n", tᵥ)
```

Let's start by loading data and switching to Greek mode.
First we are going to use `xᵢ` and `yᵢ`.

```julia
using CSV, DataFrames, Printf, Statistics, GLM

df = CSV.read("50-samples.csv", DataFrame)
xᵢ = df.x
yᵢ = df.y
```

Code readability skyrockets when math notation in our code matches the textbook.
It's like translating math into executable form.
No decoder ring required.



Why write `sum_x` when we can just... write `∑x`?
Now let's go full-statistician and summon the ancient symbols:
`∑` for summation and `x̄` for the mean.

```julia
n = length(xᵢ)

∑x = sum(xᵢ)
∑y = sum(yᵢ)

x̄ = mean(xᵢ)
ȳ = mean(yᵢ)

@printf("%-10s = %4d\n", "n", n)
@printf("∑x (total) = %7.2f\n", ∑x)
@printf("∑y (total) = %7.2f\n", ∑y)
@printf("x̄ (mean)   = %7.2f\n", x̄)
@printf("ȳ (mean)   = %7.2f\n\n", ȳ)
```



#### Embracing Variance, Standard Deviation, and Friends

In true academic fashion, we calculate the essentials:
variance, standard deviation, covariance, and Pearson’s r.
All wrapped in tidy UTF-8.

```julia
sₓ² = sum((xᵢ .- x̄).^2) / (n - 1)
sʸ² = sum((yᵢ .- ȳ).^2) / (n - 1)
cov = sum((xᵢ .- x̄) .* (yᵢ .- ȳ)) / (n - 1)

sₓ = sqrt(sₓ²)
sʸ = sqrt(sʸ²)

r = cov / (sₓ * sʸ)
r² = r^2

@printf("sₓ² (variance) = %9.2f\n", sₓ²)
@printf("sʸ² (variance) = %9.2f\n", sʸ²)
@printf("covariance     = %9.2f\n", cov)
@printf("sₓ (std dev)   = %9.2f\n", sₓ)
@printf("sʸ (std dev)   = %9.2f\n", sʸ)
@printf("r (pearson)    = %9.2f\n", r)
@printf("R²             = %9.2f\n\n", r²)
```

Understanding these statistical values is the core of linear regression.
Using intuitive symbols means we see the math as we compute it.
No translation overhead.



Let's now compute our regression line,
in proper Greek attire:

```julia
mᵣ = sum((xᵢ .- x̄) .* (yᵢ .- ȳ)) / sum((xᵢ .- x̄).^2)
bᵣ = ȳ - mᵣ * x̄

@printf("m (slope)      = %9.2f\n", mᵣ)
@printf("b (intercept)  = %9.2f\n\n", bᵣ)
@printf("Equation     y = %.2f + %.2f.x\n\n", bᵣ, mᵣ)
```



#### Residuals and T-Value: Greek Theater Finale

Now for the grand finale,
the residuals (ϵᵢ) and the t-value.
This is the statistical equivalent of checking,
if our theory survived peer review.

```julia
ŷᵢ = mᵣ .* xᵢ .+ bᵣ
ϵᵢ = yᵢ .- ŷᵢ

df = n - 2
∑ϵ² = sum(ϵᵢ .^ 2)

MSE = ∑ϵ² / df
SE_β₁ = sqrt(MSE / sum((xᵢ .- x̄).^2))
tᵥ = mᵣ / SE_β₁

@printf("SSR = ∑ϵ²           = %9.2f\n", ∑ϵ²)
@printf("MSE = ∑ϵ²/(n-2)     = %9.2f\n", MSE)
@printf("SE(β₁)  = √(MSE/sₓ) = %9.2f\n", SE_β₁)
@printf("t-value = β̅₁/SE(β₁) = %9.2f\n\n", tᵥ)
```

 The t-value helps us decide whether the slope matters,
 or whether it's just a line we imagined after too much coffee.



Here's the real output,
complete with statistical drama:

```output
❯ julia 53-lq-utf.jl
n          =   13
∑x (total) =   78.00
∑y (total) = 2327.00
x̄ (mean)   =    6.00
ȳ (mean)   =  179.00

sₓ² (variance) =     15.17
sʸ² (variance) =  25768.17
covariance     =    606.67
sₓ (std dev)   =      3.89
sʸ (std dev)   =    160.52
r (pearson)    =      0.97
R²             =      0.94

m (slope)      =     40.00
b (intercept)  =    -61.00

Equation     y = -61.00 + 40.00.x

SSR = ∑ϵ²           =  18018.00
MSE = ∑ϵ²/(n-2)     =   1638.00
SE(β₁)  = √(MSE/sₓ) =      3.00
t-value = β̅₁/SE(β₁) =     13.33
```



You can also explore this visually using the JupyterLab version:

* **53-lq-utf.jl**

It looks like that it works.

#### Defining Functions in Greek

> Math Equation

Why stop at variables?
Let's name our functions in Greek too.
It's like writing a math paper that runs itself.

* **54-lq-math.jl**

```julia
using CSV, DataFrames, Printf, Statistics, GLM

# Read data from CSV file
df = CSV.read("50-samples.csv", DataFrame)

# Extract x and y values from CSV data
xᵢ = df.x
yᵢ = df.y

# Define symbols for functions
∑(x) = sum(x)   # Summation
√(x) = sqrt(x)  # Square root

# Number of data points
n = length(xᵢ)

# Calculate sums
∑x = ∑(xᵢ)
∑y = ∑(yᵢ)

# Calculate means
x̄ = mean(xᵢ)
ȳ = mean(yᵢ)

# Calculate variance
sₓ² = ∑((xᵢ .- x̄).^2) / (n - 1)
sʸ² = ∑((yᵢ .- ȳ).^2) / (n - 1)

# Calculate covariance
cov = ∑((xᵢ .- x̄) .* (yᵢ .- ȳ)) / (n - 1)

# Calculate standard deviations
sₓ = √(sₓ²)
sʸ = √(sʸ²)

# Calculate Pearson correlation coefficient (r)
r = cov / (sₓ * sʸ)

# Calculate R-squared (R²)
r² = r^2

# Calculate slope (m) and intercept (b)
mᵣ = ∑((xᵢ .- x̄) .* (yᵢ .- ȳ)) / ∑((xᵢ .- x̄).^2)
bᵣ = ȳ - mᵣ * x̄

# Create regression line
ŷᵢ = mᵣ .* xᵢ .+ bᵣ
ϵᵢ = yᵢ .- ŷᵢ

# Calculate sum of squared residuals
∑ϵ² = ∑(ϵᵢ .^ 2)

# Calculate degrees of freedom
df = n - 2

# Calculate variance of residuals (MSE)
MSE = ∑ϵ² / df

# Calculate standard error of the slope
SE_β₁ = √(MSE / ∑((xᵢ .- x̄).^2))

# Calculate t-value
tᵥ = mᵣ / SE_β₁

# Output of basic properties
@printf("%-10s = %4d\n", "n", n)
@printf("∑x (total) = %7.2f\n", ∑x)
@printf("∑y (total) = %7.2f\n", ∑y)
@printf("x̄ (mean)   = %7.2f\n", x̄)
@printf("ȳ (mean)   = %7.2f\n\n", ȳ)

# Output of correlation calculation
@printf("sₓ² (variance) = %9.2f\n", sₓ²)
@printf("sʸ² (variance) = %9.2f\n", sʸ²)
@printf("covariance     = %9.2f\n", cov)
@printf("sₓ (std dev)   = %9.2f\n", sₓ)
@printf("sʸ (std dev)   = %9.2f\n", sʸ)
@printf("r (pearson)    = %9.2f\n", r)
@printf("R²             = %9.2f\n\n", r²)

# Output of regression coefficient
@printf("m (slope)      = %9.2f\n", mᵣ)
@printf("b (intercept)  = %9.2f\n\n", bᵣ)
@printf("Equation     y = %.2f + %.2f.x\n\n", bᵣ, mᵣ)

# Output the results
@printf("SSR = ∑ϵ²           = %9.2f\n", ∑ϵ²)
@printf("MSE = ∑ϵ²/(n-2)     = %9.2f\n", MSE)
@printf("SE(β₁)  = √(MSE/sₓ) = %9.2f\n", SE_β₁)
@printf("t-value = β̅₁/SE(β₁) = %9.2f\n\n", tᵥ)
```

Let's experiment with `∑(x)` and `√(x)`.

```julia
∑(x) = sum(x)   # Summation
√(x) = sqrt(x)  # Square root

n = length(xᵢ)
∑x = ∑(xᵢ)
∑y = ∑(yᵢ)

x̄ = mean(xᵢ)
ȳ = mean(yᵢ)
```

It's just that simple. No plugins.
No special mode. No sacrificing goats..



With this, we can recreate textbook equations nearly line-for-line.

```julia
sₓ² = ∑((xᵢ .- x̄).^2) / (n - 1)
sʸ² = ∑((yᵢ .- ȳ).^2) / (n - 1)
cov = ∑((xᵢ .- x̄) .* (yᵢ .- ȳ)) / (n - 1)

sₓ = √(sₓ²)
sʸ = √(sʸ²)

r = cov / (sₓ * sʸ)
r² = r^2
```

Compare that to the original equation:
It looks like we can put the math equation, right into the code.

$$
\begin{align*}
s_x^2 &= \frac{1}{n-1}\sum\limits_{i=1}^{n} (x_i - \bar{x})^2 \\
\text{Cov}(x,y) &= \frac{1}{n-1}\sum\limits_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) \\
s_x &= \sqrt{s_x^2} \\
r_{x,y} &= \frac{\text{Cov}(x,y)}{s_x s_y} \\
\end{align*}
$$

We can see how close the code looks with the original equation.

We’re not just coding math. We’re living it.



This way, we can see how the code works better.

```julia
mᵣ = ∑((xᵢ .- x̄) .* (yᵢ .- ȳ)) / ∑((xᵢ .- x̄).^2)
bᵣ = ȳ - mᵣ * x̄

ŷᵢ = mᵣ .* xᵢ .+ bᵣ
ϵᵢ = yᵢ .- ŷᵢ
```



And of course, we go all the way to the t-test:

$$
SSE = \sum (y_i - \hat{y}_i)^2 \\
$$

```julia
df = n - 2
∑ϵ² = ∑(ϵᵢ .^ 2)

MSE = ∑ϵ² / df
SE_β₁ = √(MSE / ∑((xᵢ .- x̄).^2))
tᵥ = mᵣ / SE_β₁
```



And finally printout all the statistic properties,
from basic properties, correlation calculation,
regression coefficient until we get the t-value.

```julia
@printf("%-10s = %4d\n", "n", n)
@printf("∑x (total) = %7.2f\n", ∑x)
@printf("∑y (total) = %7.2f\n", ∑y)
@printf("x̄ (mean)   = %7.2f\n", x̄)
@printf("ȳ (mean)   = %7.2f\n\n", ȳ)

@printf("sₓ² (variance) = %9.2f\n", sₓ²)
@printf("sʸ² (variance) = %9.2f\n", sʸ²)
@printf("covariance     = %9.2f\n", cov)
@printf("sₓ (std dev)   = %9.2f\n", sₓ)
@printf("sʸ (std dev)   = %9.2f\n", sʸ)
@printf("r (pearson)    = %9.2f\n", r)
@printf("R²             = %9.2f\n\n", r²)

@printf("m (slope)      = %9.2f\n", mᵣ)
@printf("b (intercept)  = %9.2f\n\n", bᵣ)
@printf("Equation     y = %.2f + %.2f.x\n\n", bᵣ, mᵣ)

@printf("SSR = ∑ϵ²           = %9.2f\n", ∑ϵ²)
@printf("MSE = ∑ϵ²/(n-2)     = %9.2f\n", MSE)
@printf("SE(β₁)  = √(MSE/sₓ) = %9.2f\n", SE_β₁)
@printf("t-value = β̅₁/SE(β₁) = %9.2f\n\n", tᵥ)
```

Again, let's test the result.

```output
❯ julia 54-lq-math.jl
n          =   13
∑x (total) =   78.00
∑y (total) = 2327.00
x̄ (mean)   =    6.00
ȳ (mean)   =  179.00

sₓ² (variance) =     15.17
sʸ² (variance) =  25768.17
covariance     =    606.67
sₓ (std dev)   =      3.89
sʸ (std dev)   =    160.52
r (pearson)    =      0.97
R²             =      0.94

m (slope)      =     40.00
b (intercept)  =    -61.00

Equation     y = -61.00 + 40.00.x

SSR = ∑ϵ²           =  18018.00
MSE = ∑ϵ²/(n-2)     =   1638.00
SE(β₁)  = √(MSE/sₓ) =      3.00
t-value = β̅₁/SE(β₁) =     13.33
```



You can obtain the interactive `JupyterLab` in this following link:

* **54-lq-math.jl**

Embedding math symbols in actual code,
helps students, researchers, and code reviewers alike,
follow logic with less friction.

#### A Final Word of Caution

Yes, we can name our variables `∑`, `√`, and `ϵᵢ`.
These are just utf-8.
Although this works, don't be a fool of the symbol.
You may use apples, fruit, vegetables,
or any smiley faces, instead of greek letter.

Just because we can use Greek doesn't mean we should go full emoji.
`Julia` doesn’t judge if we name our slope `🍕`, but our future selves might.

So, be elegant. Be readable.
And maybe, just maybe,
leave the smiley faces for Slack.

-- -- --

### Visualization 

> A Statistician's Canvas

Time to stop theorizing and start visualizing.
We're entering the _show-don't-tell_ phase of statistics,
where numbers finally admit they have feelings,
and express them in scatter plots.

* **55-lq-plot.jl**

```julia
using CSV, DataFrames, Plots, GLM

# Read data from CSV file
pairCSV = CSV.read("50-samples.csv", DataFrame)

# Extract x and y values from CSV data
x_observed = pairCSV.x
y_observed = pairCSV.y

# Create a scatter plot of the observed data points
scatter_plot = scatter(
  x_observed, y_observed,
  xlabel = "x", ylabel = "y",
  title = "Scatter Plot of Observed Data",
  markersize = 2,
  legend = false,
  color = :blue,
  grid = false,
  size = (800, 400))

# Fit a linear model
model = lm(@formula(y ~ x), pairCSV)

# Get coefficients
# Extract slope and intercept
coefs = coef(model)
m_slope = coefs[2]
b_intercept = coefs[1]

# Calculate regression line
regression_line = plot!(
  x -> m_slope * x + b_intercept,
  xlims = extrema(x_observed),
  color = :red, linewidth = 2)

# Save plot as PNG
savefig("55-lq-plot.png")
```

We begin by importing data from a CSV file.
Think of it as a sociable little matrix,
that prefers to travel in rows and columns.
Then, we extract our `x` and `y` values,
the dynamic duo of regression analysis.

```julia
using CSV, DataFrames, Plots, GLM

pairCSV = CSV.read("50-samples.csv", DataFrame)
x_observed = pairCSV.x
y_observed = pairCSV.y
```



#### Next up: we scatter.

This basic scatter plot displays our observed data.
No lines, no assumptions, just the raw awkwardness of reality.
Every dot is a witness to randomness,
and maybe some underlying structure.
If we’re lucky.

```julia
scatter_plot = scatter(
  x_observed, y_observed,
  xlabel = "x", ylabel = "y",
  title = "Scatter Plot of Observed Data",
  markersize = 2,
  legend = false,
  color = :blue,
  grid = false,
  size = (800, 400))
```



But we're statisticians,
we see lines where others see dots.
It's time to fit a linear model.

Here's where regression enters with a cape.
Using the Generalized Linear Model (`GLM`) package,
we fit a straight line to our data.
That line is our best guess of the trend,
minimizing the squared distance from each point.
In plain English, it's the least embarrassed line our dataset could draw.

```julia
model = lm(@formula(y ~ x), pairCSV)

coefs = coef(model)
m_slope = coefs[2]
b_intercept = coefs[1]
```



With slope and intercept in hand,
two numbers that explain an entire relationship,
we overlay the regression line.

```julia
regression_line = plot!(
  x -> m_slope * x + b_intercept,
  xlims = extrema(x_observed),
  color = :red, linewidth = 2)
```

Before we forget—save the plot.
It didn't struggle through all that math just to be discarded.

```julia
# Save plot as PNG
savefig("55-lq-plot.png")
```



And voilà.
The result is a clean visual:
raw data, elegant line, statistical beauty.
Simple, honest, and useful.
Just like our favorite p-values.



For the hands-on folks,
an interactive `JupyterLab notebook` version is ready for exploration:

* **55-lq-plot.jl**

This line turns scattered noise into insight.
It helps us predict, summarize, and sound wise in meetings.

-- -- --

### Additional Properties

> When Stats Go Beyond the Basics

Once we finish celebrating the mean and standard deviation,
we realize the party's far from over.
There are more statistical snacks on the table,
like median, mode, range,
and their mysterious cousins: skewness and kurtosis.

Let’s dig in.

* **61-additional.jl**

```julia
using CSV, DataFrames, Statistics, Printf, Distributions

# Read CSV file
pairCSV = CSV.read("50-samples.csv", DataFrame)

# Extract x and y values from CSV data
x_observed = pairCSV.x
y_observed = pairCSV.y

# Number of data points
n = length(x_observed)

# Calculate maximum, minimum, and range
x_max = maximum(x_observed)
x_min = minimum(x_observed)
x_range = x_max - x_min

y_max = maximum(y_observed)
y_min = minimum(y_observed)
y_range = y_max - y_min

# Output of maximum, minimum, and range
@printf("x (max, min, range) = (%7.2f, %7.2f, %7.2f)\n",
  x_min, x_max, x_range)
@printf("y (max, min, range) = (%7.2f, %7.2f, %7.2f)\n\n",
  y_min, y_max, y_range)

# Calculate median
x_median = median(x_observed)
y_median = median(y_observed)

# Calculate mode
x_mode = mode(x_observed)
y_mode = mode(y_observed)

# Output of additional properties
@printf("x median         = %9.2f\n", x_median)
@printf("y median         = %9.2f\n", y_median)
@printf("x mode           = %9.2f\n", x_mode)
@printf("y mode           = %9.2f\n\n", y_mode)
```

As always, we begin with our trusted `x` and `y` values,
summoned from the depths of a CSV file.
A good dataset never ghosted anyone.

```julia
using CSV, DataFrames, Statistics, Printf, Distributions

pairCSV = CSV.read("50-samples.csv", DataFrame)
x_observed = pairCSV.x
y_observed = pairCSV.y
```



These values give us a quick scan of the data landscape.
Are we dealing with tight clusters or wild outliers?
Are the y-values scaling mountains while x gently naps?

#### Max, Min, Range

Let's start with the basics of the basics.
We count how many data points we have
(just in case someone snuck in an extra row),
then we grab the max, min, and calculate the range,
the statistical equivalent of measuring the tallest,
and shortest party guests and the gap between them.

```julia
n = length(x_observed)

x_max = maximum(x_observed)
x_min = minimum(x_observed)
x_range = x_max - x_min

y_max = maximum(y_observed)
y_min = minimum(y_observed)
y_range = y_max - y_min

@printf("x (max, min, range) = (%7.2f, %7.2f, %7.2f)\n",
  x_min, x_max, x_range)
@printf("y (max, min, range) = (%7.2f, %7.2f, %7.2f)\n\n",
  y_min, y_max, y_range)
```



#### Median and Mode

Let's move deeper.
The median tells us the middle child of the dataset:
quiet, centered, reliable.
The mode, meanwhile, is the most popular kid on the block.
Together, they help us understand symmetry or the lack thereof.

```julia
# Calculate median
x_median = median(x_observed)
y_median = median(y_observed)

# Calculate mode
x_mode = mode(x_observed)
y_mode = mode(y_observed)

# Output of additional properties
@printf("x median         = %9.2f\n", x_median)
@printf("y median         = %9.2f\n", y_median)
@printf("x mode           = %9.2f\n", x_mode)
@printf("y mode           = %9.2f\n\n", y_mode)
```

Mean gets all the fame,
but median and mode are often better at handling weird data distributions.
They are less swayed by drama, aka outliers.



#### Execute

Let's peek at the result, our data speaks.

```output
❯ julia 61-additional.jl
x (min, max, range) = (   0.00,   12.00,   12.00)
y (min, max, range) = (   5.00,  485.00,  480.00)

x median         =      6.00
y median         =    137.00
x mode           =      0.00
y mode           =      5.00
```

Turns out our y-values are living large,
possibly influenced by a few overachievers.



Curious minds can interact with the dataset directly here:

* **61-additional.jl**

#### Now, a confession.

We could also compute kurtosis and skewness. And I did.
But the numbers refused to match their PSPP counterparts.
At this point, I decided to avoid philosophical debates with statistical libraries.

It is not that I gave up,
It is just that I'm postponing our enlightenment,
until I find the right reference book,
or a kind statistician who explains it with coffee.

-- -- --

### What's the Next Chapter 🤔?

Our Julia journey so far has taken us from the humble CSV,
to a flurry of scatter plots, regression lines, and statistical side quests.
We measured, we modeled, we even met the mode.
Not bad for a bunch of symbols, syntax, and slightly suspicious outliers.

_But we're not done yet. The story continues._

Next up, we'll roll up our sleeves, 
and dive into defining custom types.
A bit like teaching `Julia` how to think like a statistician.
We'll also explore more plotting,
this time featuring our stylish friend: `Gadfly`.
It’s the one with the bowtie that insists on doing things the declarative way.

Defining structures helps us organize data like pros,
and visualizing trends helps us explain it to the rest of the world.
Especially those who don't get excited about variance on a Saturday night.

So if our current chapter felt like snack time at the stats buffet,
the next one is the main course.

Join us for the sequel:
👉 **Trend - Language - Julia - Part Three**.

Bring curiosity, coffee, and possibly a fresh pair of parentheses.

-- -- -- -- -- -- -- -- --

### Preface

> Goal: Explore Julia statistic plot visualization.
> Providing the data using linear model.

In the ever-evolving garden of Julia plotting libraries,
we find ourselves surrounded by exotic species:
`StatPlots`, `Gadfly`, `VegaLite`,
and a few more lurking in the corners.
Think of them as eccentric artists at a statistical gallery,
each with their own brushstroke style,
and very strong opinions on color palettes.

To be honest, I haven't explored them all deeply yet.
Some of them still feel like that unopened drawer in the lab.
Full of potential, mildly intimidating.
But that's alright. We'll begin with a simple mission:
visualizing data from a linear model.

A solid visual is worth a thousand summary statistics.
Whether we're explaining regression to students,
or convincing ourselves the model isn't plotting revenge.
A good plot makes patterns pop and errors harder to ignore.

So let's dip our toes into the world of Julia plotting.
No lab coat required, but we do recommend goggles,
if our data has sharp outliers.

-- -- --

### Distribution

When it comes to statistics,
distributions are like spices in cooking.
The normal distribution?
That's our salt. It's everywhere,
everybody expects it, and things taste weird without it.

Let's start with the classic.
This `pdf` (probabilty density function) can be used to
calculate the corresponding y-values
for the standard normal distribution

#### Normal Distribution

Before we dive into tails and peaks,
we need to make one data series.
Let's generate our star performer:
the standard normal distribution.
This is the one where mean is zero,
standard deviation is one,
and statisticians feel strangely comforted.

* **63-dist.jl**

```julia
using StatsPlots, Distributions

# Generate data points for x-axis
x = range(-5, 5, length=1000)

# Calculate the corresponding y-values
# for a standard normal distribution
y = pdf(Normal(), x)

# Calculate the percentiles
percentiles = [25, 50, 75, 100]
quantiles = quantile.(Normal(), percentiles ./ 100)

# Plot the normal distribution
plot(
  x, y, fillrange = zero(x), fillalpha = 0.35,
  color=:black,
  label="Standard Normal Distribution", lw=1)
 
# Shade regions corresponding to percentiles
for (i, q) in enumerate(quantiles)
  sx = x .<= q
  sy = y[sx]
  # plot!(sx, sy, fillrange = zero(sx), fc=:blues)
  # vline!([q], color=i, alpha=0.3, label="")
end

# Add labels and title
xlabel!("x")
ylabel!("Density")
title!("Standard Normal Distribution with Quantiles")

# Save plot as PNG
savefig("63-quantiles.png")
```

Using Julia's Distributions package,
we can conjure our x-values,
and from those, calculate the corresponding y-values,
using the probability density function.

```julia
using StatsPlots, Distributions

x = range(-5, 5, length=1000)
y = pdf(Normal(), x)
```



Now that we have our `x` and `y` series,
let's wrap them in a warm visualization blanket,
with titles and labels,
so we don't forget what we were plotting after two cups of coffee.

```julia
plot(
  x, y, fillrange = zero(x), fillalpha = 0.35,
  color=:black,
  label="Standard Normal Distribution", lw=1)

xlabel!("x")
ylabel!("Density")
title!("Standard Normal Distribution with Quantiles")
```



The final masterpiece:



Interactive `JupyterLab` version is here for the click-happy:

* **63-dist.jl**

The normal distribution is the reference point,
for a huge range of statistical methods.
Seeing it helps us build visual intuition,
especially when comparing other,
less obedient distributions.

#### Normal Distribution with Quantiles

> No luck 🙃

I've got no luck of visualizing quantiles with Julia.

Despite my best efforts (and one existential tea break),
visualizing quantiles within this distribution didn't pan out.
Some day. Some plugin. Some patch.
Until then, it's just a beautiful bell curve.

#### Kurtosis

With the `pdf` method,
we can simulate kurtosis and skewness.

If the normal distribution is the middle child of stats,
then kurtosis is that weird cousin,
who's always "_too extra_" or "_too chill._"
Kurtosis describes how pointy or flat a distribution is,
basically, how much drama your data brings.

* **64-kurtosis.jl**

```julia
using StatsPlots, Distributions

# Generate data points for x-axis
x = range(-5, 5, length=1000)

# Calculate the corresponding y-values
# for the standard normal distribution
y_standard = pdf.(Normal(), x)

# Examples of distributions
# with different levels of kurtosis

# Standard normal distribution (Kurtosis = 0)
y_kurtosis_1 = pdf.(Normal(1, 1), x)

# Lower kurtosis
y_kurtosis_2 = pdf.(Normal(1, 0.5), x)

# Higher kurtosis
y_kurtosis_3 = pdf.(Normal(1, 2), x)

# Plot the normal distribution and
# distributions with different levels of kurtosis
plot(
  x, y_standard, color=:black,
  label="Standard Normal",
  title = "Normal Distribution "
    * "with Different Kurtosis",
  xlabel = "x", ylabel = "Density",
)

plot!(
  x, y_kurtosis_1, color=:red,
  label="Standard Kurtosis = 0",
  linestyle=:dash, 
)

plot!(
  x, y_kurtosis_2, color=:green,
  label="Lower Kurtosis",
  linestyle=:dash, 
)

plot!(
  x, y_kurtosis_3, color=:blue,
  label="Higher Kurtosis",
  linestyle=:dash, 
)

# Save plot as PNG
savefig("64-kurtosis.png")
```

Let’s simulate a few personalities.
We start with making series by
generating data points for x-axis,
and calculating the corresponding y-values
for the standard normal distribution.

```julia
using StatsPlots, Distributions

x = range(-5, 5, length=1000)
y_standard = pdf.(Normal(), x)
```

We'll now tweak the variance to simulate different levels of kurtosis:

1. Standard normal distribution (Kurtosis = 0)
2. Lower kurtosis
3. Higher kurtosis

```julia
y_kurtosis_1 = pdf.(Normal(1, 1), x)
y_kurtosis_2 = pdf.(Normal(1, 0.5), 
y_kurtosis_3 = pdf.(Normal(1, 2), x)
```



Start with the vanilla plot,
using normal distribution.

```julia
# Plot the normal distribution and
plot(
  x, y_standard, color=:black,
  label="Standard Normal",
  title = "Normal Distribution "
    * "with Different Kurtosis",
  xlabel = "x", ylabel = "Density",
)
```



Then stir in the flavors,
by adding each different levels of kurtosis to the plot grammar.

```julia
# distributions with different levels of kurtosis
plot!(
  x, y_kurtosis_1, color=:red,
  label="Standard Kurtosis = 0",
  linestyle=:dash, 
)

plot!(
  x, y_kurtosis_2, color=:green,
  label="Lower Kurtosis",
  linestyle=:dash, 
)

plot!(
  x, y_kurtosis_3, color=:blue,
  label="Higher Kurtosis",
  linestyle=:dash, 
)
```



Final chart:



Interactive `JupyterLab` version:

* **64-kurtosis.jl**

Understanding kurtosis helps us detect heavy tails,
or overly flat distributions.
Critical for risk analysis, quality control,
and figuring out if our model is secretly partying in the tails.

#### Skewness

Now we move on to skewness,
the measure of symmetry,
or how lopsided a distribution is.
If our data curve leans like it's trying to eavesdrop,
skewness is the gossip it's chasing.

* **65-skewness.jl**

```julia
using StatsPlots, Distributions

# Generate data points for x-axis
x = range(-5, 5, length=1000)

# Calculate the corresponding y-values
# for the standard normal distribution
y_standard = pdf.(Normal(), x)

# Examples of distributions
# with different skewness parameters

# Negative skewness
y_skewed_1 = (2 * pdf.(Normal(), x) 
  .* cdf.(Normal(), x))

# Moderate positive skewness
y_skewed_2 = (2 * pdf.(Normal(), -x) 
  .* cdf.(Normal(), -x))

# High positive skewness
y_skewed_3 = (2 * pdf.(Normal(), x) 
  .* cdf.(Normal(), x) * 2)

# Plot the normal distribution
# and skewed distributions
plot(
  x, y_standard, color=:black,
label="Standard Normal",
  title = "Normal Distribution "
    * "with Different Skewness",
  xlabel = "x", ylabel = "Density",
)

plot!(
  x, y_skewed_1, color=:red,
  label="Negative Skewness = -4",
  linestyle=:dash,
)

plot!(
  x, y_skewed_2, color=:green,
  label="Moderate Positive Skewness = 2",
  linestyle=:dash,
)

plot!(
  x, y_skewed_3, color=:blue,
  label="High Positive Skewness = 6",
  linestyle=:dash,
)

# Save plot as PNG
savefig("65-skewness.png")
```

Explanation

```julia
using StatsPlots, Distributions

x = range(-5, 5, length=1000)
y_standard = pdf.(Normal(), x)
```

Here come the characters.
Let's make examples of distributions
with different skewness parameters.

1. Negative skewness
2. Moderate positive skewness
3. High positive skewness

```julia
y_skewed_1 = (2 * pdf.(Normal(), x) 
  .* cdf.(Normal(), x))
y_skewed_2 = (2 * pdf.(Normal(), -x) 
  .* cdf.(Normal(), -x))
y_skewed_3 = (2 * pdf.(Normal(), x) 
  .* cdf.(Normal(), x) * 2)
```



Plot the symmetrical base,
using normal distribution.

```julia
plot(
  x, y_standard, color=:black,
label="Standard Normal",
  title = "Normal Distribution "
    * "with Different Skewness",
  xlabel = "x", ylabel = "Density",
)
```

Add the drama.
Each distributions with
different skewness parameters to the plot grammar.

```julia
plot!(
  x, y_skewed_1, color=:red,
  label="Negative Skewness = -4",
  linestyle=:dash,
)

plot!(
  x, y_skewed_2, color=:green,
  label="Moderate Positive Skewness = 2",
  linestyle=:dash,
)

plot!(
  x, y_skewed_3, color=:blue,
  label="High Positive Skewness = 6",
  linestyle=:dash,
)
```



Final visual:



Play with the code here:

* **65-skewness.jl**

Skewness affects mean and standard deviation.
If we assume symmetry when it's not there,
we might make decisions that only work for perfectly balanced data worlds.
Which, let’s be honest, almost never happen.

-- -- --

### Multiple Series

When life gives us multiple data series,
we do not complain. We visualize.
This section is all about juggling multiple trends on the same stage,
whether it's in one glorious unified plot or gracefully separated using grid layouts.
Think of it as conducting an orchestra of noisy datasets.

#### Regression Steps

This part is not about passing our thesis defense.
We are just plotting three series, running regressions,
estimating their standard errors,
and wrapping them all in a warm, fuzzy ribbon of confidence.

This can be done by these four steps.

1. Scatter plot for each series.
2. Line plot for each series.
3. Calculate each standard errors.
4. Add shaded region for standard error for each series.

With total plot drawing as 6 plots.

* **71-regression.jl**

```julia
using CSV, DataFrames, Statistics, StatsPlots, ColorSchemes

# Read data from CSV file
df = CSV.read("series.csv", DataFrame, types=Dict())
rename!(df, Symbol.(strip.(string.(names(df)))))

# Extract x and y values from CSV data
xs = df.xs
ys1 = df.ys1
ys2 = df.ys2
ys3 = df.ys3

# Scatter plot without regression lines
scatter(
  xs, ys1, label="ys1", 
  seriestype=:scatter, color=:red, 
  legend=:topright)
scatter!(
  xs, ys2, label="ys2", 
  seriestype=:scatter, color=:green)
scatter!(
  xs, ys3, label="ys3", 
  seriestype=:scatter, color=:blue)

# Calculate standard error for each y series
se1 = std(ys1) / sqrt(length(ys1))
se2 = std(ys2) / sqrt(length(ys2))
se3 = std(ys3) / sqrt(length(ys3))

# Define color scheme for shading
colors = ColorSchemes.magma.colors

# Plot shaded region representing standard error
plot!(
  xs, ys1, label="", color=colors[1],
  ribbon=(se1, se1), fillalpha=0.3)
plot!(
  xs, ys2, label="", color=colors[2],
  ribbon=(se2, se2), fillalpha=0.3)
plot!(
  xs, ys3, label="", color=colors[3],
  ribbon=(se3, se3), fillalpha=0.3)

xlabel!("x")
ylabel!("y")
title!("Scatter Plot with Regression Lines")

# Save plot as PNG
savefig("71-regression.png")
```

We begin, as statisticians often do, by reading a CSV.
This populates our dataframe and separates `x` from the three `y`'s.
They're not siblings, but close enough.

```julia
df = CSV.read("series.csv", DataFrame, types=Dict())
rename!(df, Symbol.(strip.(string.(names(df)))))

xs = df.xs
ys1 = df.ys1
ys2 = df.ys2
ys3 = df.ys3
```



#### Scatter

Scatter plots first, without with regression lines.
This is our baseline before the serious statistical dress-up begins.

```julia
scatter(
  xs, ys1, label="ys1", 
  seriestype=:scatter, color=:red, 
  legend=:topright)
scatter!(
  xs, ys2, label="ys2", 
  seriestype=:scatter, color=:green)
scatter!(
  xs, ys3, label="ys3", 
  seriestype=:scatter, color=:blue)
```



#### Standard Error

Now let's add some statistical seasoning: the standard error.
It tells us how much the data wobbles around the mean.
A lower SE means our trend is a well-behaved intern.
A higher SE means it drinks coffee at midnight.

```julia
se1 = std(ys1) / sqrt(length(ys1))
se2 = std(ys2) / sqrt(length(ys2))
se3 = std(ys3) / sqrt(length(ys3))
```

Let's bring in colors,
because grayscale regression is a mood killer.

```julia
colors = ColorSchemes.magma.colors
```



#### Plot

Plotting time again, line plot for each series,
along with shaded region using ribbon,
representing standard error for each series.
This time with smooth trend lines and shaded error ribbons.
Like giving each line a warm blanket to keep their variability cozy.

```julia
plot!(
  xs, ys1, label="", color=colors[1],
  ribbon=(se1, se1), fillalpha=0.3)
plot!(
  xs, ys2, label="", color=colors[2],
  ribbon=(se2, se2), fillalpha=0.3)
plot!(
  xs, ys3, label="", color=colors[3],
  ribbon=(se3, se3), fillalpha=0.3)
```



Behold the final result. Three trends. Three ribbons. One plot to rule them all.



If you're feeling adventurous (or just hate static images),
the interactive `JupyterLab notebook` is here:

* **71-regression.jl**

Visualizing regression and its uncertainty helps us understand,
both the central trend and how twitchy our estimates are.
Data might lie, but standard error whispers the truth.

#### Combined

Sometimes, throwing everything into one plot is like,
forcing three cats into a bathtub.
Better to give each one its own little space,
especially if their y-axis scales are vastly different.

* **72-combined.jl**

```julia
using CSV, DataFrames, Statistics, StatsPlots, ColorSchemes

# Read data from CSV file
df = CSV.read("series.csv", DataFrame, types=Dict())
rename!(df, Symbol.(strip.(string.(names(df)))))

# Extract x and y values from CSV data
xs = df.xs
ys1 = df.ys1
ys2 = df.ys2
ys3 = df.ys3

# Calculate standard error for each y series
se1 = std(ys1) / sqrt(length(ys1))
se2 = std(ys2) / sqrt(length(ys2))
se3 = std(ys3) / sqrt(length(ys3))

# Define color scheme for shading
colors = ColorSchemes.magma.colors

# Scatter plot with regression line for ys1
plot1 = scatter(
  xs, ys1, label="ys1",
  seriestype=:scatter, color=:red)
scatter!(
  xs, ys1, label="", color=:red)
plot!(
  xs, ys1, label="", color=colors[1],
  ribbon=(se1, se1), fillalpha=0.3)
xlabel!("x")
ylabel!("y")
title!(
  "Regression Line for y1",
  titlefontsize=8)

# Scatter plot with regression line for ys2
plot2 = scatter(
  xs, ys2, label="ys2",
  seriestype=:scatter, color=:green)
scatter!(
  xs, ys2, label="", color=:green)
plot!(
  xs, ys2, label="", color=colors[2],
  ribbon=(se2, se2), fillalpha=0.3)
xlabel!("x")
ylabel!("y")
title!(
  "Quadratic Regression Line for y2",
  titlefontsize=8)

# Scatter plot with regression line for ys3
plot3 = scatter(
  xs, ys3, label="ys3",
  seriestype=:scatter, color=:blue)
scatter!(
  xs, ys3, label="", color=:blue)
plot!(
  xs, ys3, label="", color=colors[3],
  ribbon=(se3, se3), fillalpha=0.3)
xlabel!("x")
ylabel!("y")
title!(
  "Cubic Regression Line for y3",
  titlefontsize=8)

# Combine plots into a single figure
plot_combined = plot(
  plot1, plot2, plot3, layout=(1, 3))

# Save plot as PNG
savefig("72-combined.png")
```

We follow our trusted ritual:
read the CSV, extract the values, calculate standard errors,
and assign color roles like casting a telenovela.

```julia
df = CSV.read("series.csv", DataFrame, types=Dict())
rename!(df, Symbol.(strip.(string.(names(df)))))

xs = df.xs
ys1 = df.ys1
ys2 = df.ys2
ys3 = df.ys3

se1 = std(ys1) / sqrt(length(ys1))
se2 = std(ys2) / sqrt(length(ys2))
se3 = std(ys3) / sqrt(length(ys3))

colors = ColorSchemes.magma.colors
```



Next, we create one plot per series
[``ys₁`, `ys₂`, and `ys₃`.].
Like opening three tabs instead of,
squashing everything into one spreadsheet cell.

```julia
plot1 = scatter(
  xs, ys1, label="ys1",
  seriestype=:scatter, color=:red)
...

plot2 = scatter(
  xs, ys2, label="ys2",
  seriestype=:scatter, color=:green)
...

plot3 = scatter(
  xs, ys3, label="ys3",
  seriestype=:scatter, color=:blue)
...
```



Now it's time to align them neatly,
like well-behaved academic panels at a conference.

```julia
plot_combined = plot(
  plot1, plot2, plot3, layout=(1, 3))
```



TAnd there we have it.
Three subplots, side by side, not yelling over each other.



The interactive version is just a click away.
Because real statisticians always double-check their plots.

* **72-combined.jl**

Separate plots offer clarity when each series tells a very different story.
Think of it as letting each dataset speak without being talked over.

-- -- --

### Statistic Properties: StatsPlot

> Three series. One axis. No mercy.

Previously, we focused on regression and trendlines,
but now we turn our gaze toward the fundamental descriptors of our data
It's time to put those y-series on the therapist's couch and ask:
"_How are you feeling? Centered? Spread out? Any outliers bothering you?_"

As you can see from previous statistical properties.
We can analyze the data for each series.
For example we can just consider just the y-series,
and obtain the `mean`, `median`, `mode`,
and also the `minimum`, `maximum`, `range`, and `quantiles`.

We can use `StatsPlot` for simple `Boxplot` and `Violinplot`.
But we require `Gadfly` to draw `Swarm Plot`.

Understanding statistical properties helps us move,
from "_pretty plots_" to "_actually meaningful insights._"
Boxplots and violin plots summarize shape,
spread, and centrality all in one tidy graphic.

#### StatsPlot: Box Plot

When our inner statistician wants to play minimalist,
the `boxplot`  method from `StatsPlot` steps in.
It shows the median, interquartile range, whiskers, and outliers.
All without saying a word.
It's basically the silent film of data visualization.

* **81a-boxplot.jl**

```julia
using CSV, DataFrames, StatsPlots

# Read data from CSV file
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

# Extract the columns ys1, ys2, and ys3
data = [df.ys1, df.ys2, df.ys3]

# Create a box plot using StatsPlots
boxplot(data, 
  labels = ["ys1", "ys2", "ys3"],
  linecolor = :black,
  legend = false,
  xlabel = "Variable",
  ylabel = "Value",
  title = "Box Plot for ys1, ys2, and ys3",
  grid = false)

# Save plot as PNG
savefig("81a-boxplot.png")
```

We start with the same ritual: read the CSV,
and politely ask for [`ys₁`, `ys₂`, and `ys₃`].
These will be the stars of our plot.

```julia
using CSV, DataFrames, StatsPlots

df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

data = [df.ys1, df.ys2, df.ys3]
```



Now, we summon the mighty `boxplot` function from `StatsPlots`.
It does exactly what it says. No drama, just five-number summaries.

```julia
boxplot(data, 
  labels = ["ys1", "ys2", "ys3"],
  linecolor = :black,
  legend = false,
  xlabel = "Variable",
  ylabel = "Value",
  title = "Box Plot for ys1, ys2, and ys3",
  grid = false)
```



Here's the final plot. 
otice how each box whispers secrets about skewness and variability.
And those dots? Outliers. Every dataset has its rebels.



Need to poke around the data interactively? We've got a Jupyter notebook for that:

* **81a-boxplot.jl**

#### StatsPlot: Violin Plot

If `boxplots` are a bit too uptight for our taste,
we can go with `violins` method from `StatsPlot`.
These plots combine boxplots with kernel density estimates.
Think of it as a plot that went to art school,
and now speaks softly about distribution curves.

* **81b-violin.jl**

```julia
using CSV, DataFrames, StatsPlots

# Read data from CSV file
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

# Extract the columns ys1, ys2, and ys3
data = [df.ys1, df.ys2, df.ys3]

# Create a violin plot using StatsPlots
violin(data, 
  labels = ["ys1", "ys2", "ys3"],
  linecolor = :black,
  legend = false,
  xlabel = "Variable",
  ylabel = "Value",
  title = "Violin Plot for ys1, ys2, and ys3",
  grid = false)

# Save plot as PNG
savefig("81b-violin.png")
```

We use the same data,
but with a more expressive tool.
This time, the violin tells the whole story,
and plays a solo too.

```julia
violin(data, 
  labels = ["ys1", "ys2", "ys3"],
  linecolor = :black,
  legend = false,
  xlabel = "Variable",
  ylabel = "Value",
  title = "Violin Plot for ys1, ys2, and ys3",
  grid = false)
```



And here’s the result: elegant, symmetric violins,
representing how thick or thin the data is across the value range.

If boxplots were terse academic abstracts,
violins are dramatic spoken-word poetry.



Curious to fiddle with the violins yourself? The JupyterLab version awaits:

* **81b-violin.jl**

Violin plots reveal where data clusters within the distribution,
not just the edges.
It's like going from watching shadows on the wall,
to actually seeing the data dance.

Sadly, despite my enthusiasm,
`StatsPlot` is not yet equipped to do swarm plots or strip plots
So I shall go gadget hunting. 
erhaps in the land of `Gadfly`, a new hope awaits.

-- -- --

### Statistic Properties: Gadfly

> Three series. One axis. All beautifully chaotic.

Now that we have dissected our data with `StatsPlot`,
it's time to put on our artsy glasses and give `Gadfly` a spin. 
amed after the philosophical pest Socrates was proud to be,
this library pokes our data just enough to make it confess.

Gadfly brings elegant grammar-of-graphics plotting to Julia,
and it's a great choice when we want flexible yet readable visual output.
Plus, it sounds cool.

#### Gadfly: Box Plot

To let `Gadfly` do this box plot thing,
we must summon its visual spellbook with `Cairo` and `Fontconfig`.

* **82a-boxplot.jl**

```julia
using CSV, DataFrames, Gadfly
import Cairo, Fontconfig

# Read data from CSV file
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

# Melt the DataFrame to long format for boxplot
df_long = stack(df, Not(:xs))

# Create a boxplot using Gadfly
box_plot = Gadfly.plot(
  df_long,
  x=:variable,
  y=:value,
  color=:variable,
  Geom.boxplot(),
  Guide.xlabel("Variable"),
  Guide.ylabel("Value"),
  Guide.title("Box Plot for ys1, ys2, and ys3"),
  Theme(
    key_position = :top,
    boxplot_spacing = 100px,
    background_color = "white",
  )
)

# Save plot as PNG
draw(PNG("82a-boxplot.png", 800px, 400px), box_plot)
```

Explanation

```julia
using CSV, DataFrames, Gadfly
import Cairo, Fontconfig
```

As always, raw data must be reshaped to long format.
Think of it as giving the dataset a good yoga stretch,
before the plotting begins.

```julia
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

df_long = stack(df, Not(:xs))
```



Now comes the visual reveal.
We ask `Gadfly` to plot boxes for each series,
which allows us to judge central tendency, spread, and outlier drama.
Basically the entire personality profile of our variables.

```julia
box_plot = Gadfly.plot(
  df_long,
  x=:variable,
  y=:value,
  color=:variable,
  Geom.boxplot(),
  Guide.xlabel("Variable"),
  Guide.ylabel("Value"),
  Guide.title("Box Plot for ys1, ys2, and ys3"),
  Theme(
    key_position = :top,
    boxplot_spacing = 100px,
    background_color = "white",
  )
)
```



Here's our output: clean lines, expressive boxes,
and a whisper of statistical elegance.
The outliers are still there, silently pleading not to be judged.



Interactive version for plot tinkerers:

* **82a-boxplot.jl**

#### Gadfly: Violin Plot

A violin plot is like a boxplot that listened to too much jazz.
It adds density estimation, giving us not just the notes but the melody of our data.
we also need to import `Cairo` and `Fontconfig`.

* **82b-violin.jl**

```julia
using CSV, DataFrames, Gadfly
import Cairo, Fontconfig

# Read data from CSV file
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

# Melt the DataFrame to long format for violin plot
df_long = stack(df, Not(:xs))

# Create a violin plot using Gadfly
violin_plot = Gadfly.plot(
  df_long,
  x=:variable,
  y=:value,
  color=:variable,
  Geom.violin,
  Guide.xlabel("Variable"),
  Guide.ylabel("Value"),
  Guide.title("Violin Plot for ys1, ys2, and ys3"),
  # Set ymin to 0 to avoid negative values on y-axis
  Coord.cartesian(ymin=0),
  # Set minimum y-axis value to 0
  Scale.y_continuous(minvalue=0),
  Theme(
    key_position=:top,
    default_color="purple", 
    background_color="white",
    panel_stroke=colorant"gray",
    minor_label_font_size=10pt, 
    major_label_font_size=12pt,
  )
)

# Save plot as PNG
draw(PNG("82b-violin.png", 800px, 400px), violin_plot)
```

Same data, but now the rhythm changes.

```julia
violin_plot = Gadfly.plot(
  df_long,
  x=:variable,
  y=:value,
  color=:variable,
  Geom.violin,
  Guide.xlabel("Variable"),
  Guide.ylabel("Value"),
  Guide.title("Violin Plot for ys1, ys2, and ys3"),

  Coord.cartesian(ymin=0),

  Scale.y_continuous(minvalue=0),
  Theme(
    key_position=:top,
    default_color="purple", 
    background_color="white",
    panel_stroke=colorant"gray",
    minor_label_font_size=10pt, 
    major_label_font_size=12pt,
  )
)
```



Behold: violins of data.
Some are chunky, some are skinny,
but all are telling us where the values live, breathe,
and occasionally spike unexpectedly.



Our JupyterLab ensemble is available here:

* **82b-violin.jl**

Where boxplots are terse and strict,
violin plots show distribution nuances.
We get to see whether the data is heavy in the middle,
skewed to the side, or trying to impersonate a bimodal bell curve.

#### Gadfly: Swarm Plot

And now, for the grand finale, bees on a box.
The swarm plot, also known as beeswarm,
shows every single data point while gently nudging them to avoid overlap.
It is as if our data formed a polite crowd at a buffet.

* **82c-swarm.jl**

```julia
using CSV, DataFrames, Gadfly
import Cairo, Fontconfig

# Read data from CSV file
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

# Melt the DataFrame to long format for boxplot
df_long = stack(df, Not(:xs))

# Create a boxplot using Gadfly
box_plot = Gadfly.plot(
  df_long,
  x=:variable,
  y=:value,
  color=:variable,
  Geom.beeswarm(),
  Guide.xlabel("Variable"),
  Guide.ylabel("Value"),
  Guide.title("Swarm Plot for ys1, ys2, and ys3"),
  Theme(
    key_position = :top,
    background_color = "white",
  )
)

# Save plot as PNG
draw(PNG("82c-swarm.png", 800px, 400px), box_plot)
```

To get buzzing, we add `Geom.beeswarm()` to the mix:

```julia
box_plot = Gadfly.plot(
  df_long,
  x=:variable,
  y=:value,
  color=:variable,
  Geom.beeswarm(),
  Guide.xlabel("Variable"),
  Guide.ylabel("Value"),
  Guide.title("Swarm Plot for ys1, ys2, and ys3"),
  Theme(
    key_position = :top,
    background_color = "white",
  )
)
```



Let each dot speak. We no longer summarize. We observe the crowd.
Here it is in all its buzzing glory.:



Interactive swarm fun awaits at:

* **82c-swarm.jl**

Swarm plots highlight distribution
and density without aggregation.
If each data point were a vote,
this would be the fairest election plot in statistics.

-- -- --

### Statistic Properties: Distribution

_From frequencies to densities._ \
_Sometimes the spread tells the whole story._

After giving our data the spa treatment with box plots and violin strokes,
it is time to ask a deeper question: "_How is our data distributed?_"
In this section, we look at the y-axis not just as numbers
but as frequencies and densities.
A true bonding moment between data and probability.

#### KDE Plot

> Kernel Density Estimation

_How to smooth out chaos politely._

A KDE plot gives us a continuous estimate of the distribution.
It answers that ancient question:
"_What would our histogram look like if it were raised by mathematicians?_"

KDE shown well the distribution of the frequency.
This complex task can be done easily
with `kde_plot` from `StatsPlots`.

* **83a-kdeplot.jl**

```julia
using CSV, DataFrames, StatsPlots

# Read data from CSV file
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

# Melt the DataFrame to long format for KDE plot
df_long = stack(df, Not(:xs))

# Create KDE plot using StatsPlots with custom colors
kde_plot = density(
  df_long.value, 
  group = df_long.variable,
  fillalpha = 0.7,
  legend = :topright,
  xlabel = "Value",
  ylabel = "Density",
  title = "KDE Plot for ys1, ys2, and ys3",
  lw = 2, # Line width
  α = 0.5 # Opacity
)

# Save plot as PNG
savefig("83a-kdeplot.png")
```

First, we must prep our data.
Yes, again. The data must be melted.
We need to melt the DataFrame to long format.
Think fondue, but for DataFrames.

```julia
using CSV, DataFrames, StatsPlots

df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

df_long = stack(df, Not(:xs))
```



Now we can create KDE plot using StatsPlots with custom colors

```julia

kde_plot = density(
  df_long.value, 
  group = df_long.variable,
  fillalpha = 0.7,
  legend = :topright,
  xlabel = "Value",
  ylabel = "Density",
  title = "KDE Plot for ys1, ys2, and ys3",
  lw = 2, # Line width
  α = 0.5 # Opacity
)
```



And voilà: a trio of smoothed density curves,
gliding through the value space like they just completed a statistics PhD.



Explore interactively:

* **83a-kdeplot.jl**

Histograms are nice,
but KDE plots let us peek behind the bins,
and reveal the underlying probability whisper.

_Smooth, elegant, and informative._

#### Rug Plot

> No Luck

Despite our best statistical intentions,
the rug plot continues to elude us in Julia.
A perfect example of how even in data science,
some rugs are pulled from under our feet.

You know, I still have no luck, drawing this plot in Julia.
I'd better come back later on.

#### Histogram

> Where it all began—bin by bin.

The humble histogram. A classic.
The visual equivalent of sorting socks by color,
and counting how many of each.
Simple. Satisfying. Slightly obsessive.

This looks like the most common chart for beginner.
This simple task can be done easily
with `hist_plot` from `StatsPlots`.

* **84a-histogram.jl**

```julia
using CSV, DataFrames, StatsPlots

# Read data from CSV file
df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

# Melt the DataFrame to long format for histplot
df_long = stack(df, Not(:xs))

# Create histogram plot using StatsPlots with custom colors
hist_plot = histogram(
    df_long.value,
    group = df_long.variable,
    bins = collect(0:50:maximum(df_long.value)),
    linecolor = :black,
    fillalpha = 0.7,
    color = :Set1,
    xlabel = "Value",
    ylabel = "Density",
    title = "Histogram Plot for ys1, ys2, and ys3",
    legend = :topleft
)

# Save plot as PNG
savefig("84a-histogram.png")
```

Yes, we melt again.
Our DataFrame, that is. Not our .

```julia
using CSV, DataFrames, StatsPlots

df = CSV.read("series.csv", DataFrame)
rename!(df, Symbol.(strip.(string.(names(df)))))

df_long = stack(df, Not(:xs))
```



Now we can create Histogram using StatsPlots with custom colors

```julia
hist_plot = histogram(
    df_long.value,
    group = df_long.variable,
    bins = collect(0:50:maximum(df_long.value)),
    linecolor = :black,
    fillalpha = 0.7,
    color = :Set1,
    xlabel = "Value",
    ylabel = "Density",
    title = "Histogram Plot for ys1, ys2, and ys3",
    legend = :topleft
)
```



A familiar sight: colorful bars rising,
from the axis like a baritone choir,
representing grouped frequencies.



Play with the histogram interactively:

* **84a-histogram.jl**

Histograms give a discrete view of data frequency. 
Great for quick intuition, beginner-friendly,
and surprisingly deep once bin size joins the party.

A small confession: custom color tweaking is still not working as intended.
We will circle back when the Julia gods grant us enlightenment.
For now, we lean on default palettes and optimism.
I'll do it later. When I've got the time.

#### Marginal

> No Luck (Again)

I have to explore more. Unfortunately.

The marginal plot, an elusive unicorn in our Julia zoo.
It waits in the shadows with rug plots,
probably sipping espresso and judging our color palettes.

_I apologize._ \
_This one goes on the **someday** list._

-- -- --

### What's the Next Chapter 🤔?

We have seen how Julia helps us visualize statistical properties.
Not just with style, but with substance.
Whether we box it, violin it, swarm it, or smooth it with KDE,
each plot is a conversation between us and the data.

Statistical visualization is not just for pretty graphs in reports.
It helps us think, to detect patterns, identify outliers,
and avoid the dreaded "_everything looks normal_" fallacy.

Naturally, we've focused on `Python`, `R`, and `Julia`.
Each a different flavor of statistical sorcery.
But we can go further: with `TypeScript` and `Go` on the horizon,
our next frontier might include full-stack statistical integration (just kidding).
Imagine serving insights with both confidence intervals and a REST API. Bliss.

_But for now?_

Well, life's confidence interval is currently skewed right.
Work is calling. To be honest life is pretty demanding.
So we'll hit pause here and return when our time series permits it.

-- -- --

### Conclusion

> Was this fun? Statistically speaking... highly significant.

What do we think?

* Did we melt enough data?
* Plot with enough color?
* Make enough jokes about KDE to summon a Linux mascot?

Farewell for now, fellow data wranglers.
Until the next round of rows, columns, and probability distributions.
Stay curious, stay caffeinated, and never trust a histogram without labels.

We shall meet again.
