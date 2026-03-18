# Monte Carlo and Credit Analysis

**Source:** https://edbodmer.com/monte-carlo-and-credit-analysis

---

This page demonstrates how Monte Carlo can be used in credit analysis. Some of the subjects covered include what kind of volatility is associated with different DSCR; how different distributions affect the measurement of probability of default; the importance of mean reversion in measuring probability of default; and, application of Monte Carlo simulation in oil price projects. A big conclusion from all of this is that Monte Carlo may be used to illustrate ideas and concepts, but it is not very useful in practice. In particular, the variables that drive Monte Carlo simulation including the distribution; mean reversion; changing volatility; trends in the mean; and other factors.

### Time Series without Mean Reversion and Normal Distribution to Demonstrate Target DSCR’s

The first case demonstrates how to use basic Monte Carlo simulation using a very simple VBA code to illustrate how volatility and the target probability of default can drive theoretical level of the DSCR. To illustrate the idea begin by looking at the cumulative default rates for different bond ratings from Standard and Poors.

![](https://edbodmer.com/wp-content/uploads/2021/01/image.png)

![](https://edbodmer.com/wp-content/uploads/2021/01/image-5.png)

Let’s see if we can simulate these numbers with Monte Carlo simulation. Note the log scale.

![](https://edbodmer.com/wp-content/uploads/2021/01/image-6.png)

![](https://edbodmer.com/wp-content/uploads/2021/01/image-1.png)

![](https://edbodmer.com/wp-content/uploads/2021/01/image-2.png)

![](https://edbodmer.com/wp-content/uploads/2021/01/image-3.png)

![](https://edbodmer.com/wp-content/uploads/2021/01/image-4.png)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=12795&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10324&rand=0.07672640514820672)