<!--
Filename: 	note.md
Project: 	/Users/shume/Developer/DEDSIC/01
Author: 	shumez <https://github.com/shumez>
Created: 	2019-04-30 16:42:8
Modified: 	2019-05-07 17:40:44
-----
Copyright (c) 2019 shumez
-->

# 01. First-Order Equations

## ToC

* [01.01. The Simplest Example](#0101_the_simplest_example)
* [01.02. The Logistic Population Model](#0102_the_logistic_population_model)



## 01.01. The Simplest Example

\[ \frac{dx}{dt} = ax \]

\[ x'(t) = ax(t) \]

obtained from calculus  
real num \( k \), \( x(t) = ke^{at} \) is solution

\[ x'(t) = ake^{at} = ax(t) \]

let \( u(t) \) be any solution, compute the derivertiev of \( u(t) e^{-at} \)

\[ 
    \begin{align*}
        \frac{d}{dt} ( u(t)e^{-at} ) 
        &= u'(t) e^{-at} + u(t) (-a e^{-at}) \\
        &= a u(t) e^{-at} - a u(t) e^{-at} &= 0
    \end{align*}
\]

**initial condition** \( x(t_0) = u_0 \)

in the form of an *initial valuee problem*

\[ x' = ax, \, x(0) = u_0 \]

when \( k = 0 \), constant solution \( x(t) \equiv 0 \)  
**equilibrium solution**, **equilibrium point**

* if \( a > 0 \), 
    \[ 
        \lim_{t\rightarrow\infty}{ke^{at}} = 
        \begin{cases} 
            \infty &\text{when } k > 0 \\ 
            -\infty &\text{when } k < 0 
        \end{cases} 
    \]
* if \( a = 0 \), 
    \[ k e^{at} = \text{constant} \]
* if \( a < 0 \),
    \[ \lim_{t \rightarrow \infty} k e^{at} = 0 \]

[![Fig.1.1][fig0101]][fig0101]

* **source**: away from it
* **sink**: toward it

**phase plane**

**bifurcation** at \( a = 0 \)


## 01.02. The Logistic Population Model

\( x' = ax \) when \( a > 0 \)

**Logistic population growth model**

\[ x' = ax (1 - \frac{x}{N}) \]

\( a \), \( N \): positive param

\[ x' = f_a(x) = ax(1 - x) \]

**first order**

**autnomous**: depends on \( x \) alone not \( t \)

\[ 
    \begin{align*}
        \int{\frac{dx}{x(1-x)}} &= \int{a} \, dt \\
        \int{\Big( \frac{1}{x} + \frac{1}{1-x} \Big)} \, dx &= \int{a} \, dt \\
        \log{x} - \log{(1-x)} &= at \\
        \log{\frac{x}{1-x}} &= at \\
        \frac{x}{1-x} &= e^{at} \\
        (1 + e^{at}) x &= e^{at} \\
        x &= \frac{e^{at}}{1 + e^{at}} \\
        x(t) &= \frac{K e^{at}}{1 + K e^{at}}
    \end{align*}
\]

\( t = 0 \), 

\[ K = \frac{x(0)}{1 - x(0)} \]

rewrite

\[ x(t) = \frac{x(0) e^{at}}{1 - x(0) + x(0) e^{at}} \]

[![Fig.1.3][fig0103]][fig0103]

**slope field**

###### Exmaple 

\[ x' = g(x) = x - x^3 \]

[![Figure.1.5][fig0105]][fig0105]

##

<!-- ref -->

<!-- fig -->
[fig0101]: https://raw.githubusercontent.com/shumez/DEDSIC/master/01/fig/fig0101.png
[fig0103]: https://raw.githubusercontent.com/shumez/DEDSIC/master/01/fig/fig0103.png
[fig0105]: https://raw.githubusercontent.com/shumez/DEDSIC/master/01/fig/fig0105.png

<!-- https://raw.githubusercontent.com/shumez/DEDSIC/master/01/ -->

<style type="text/css">
	img{width: 51%; float: right;}
</style>