<!--
Filename: 	note.md
Project: 	/Users/shume/Developer/DEDSIC/01
Author: 	shumez <https://github.com/shumez>
Created: 	2019-04-30 16:42:8
Modified: 	2019-04-30 20:55:36
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


##

<!-- ref -->

<!-- fig -->

<!-- <style type="text/css">
	img{width: 51%; float: right;}
</style> -->