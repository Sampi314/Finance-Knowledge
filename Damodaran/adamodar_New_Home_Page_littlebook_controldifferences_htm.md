# Controlling for differences in relative valuation

**Source:** https://pages.stern.nyu.edu/~adamodar/New_Home_Page/littlebook/controldifferences.htm

---

 [![littlebook](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/Budimage/littlebook.gif)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/littlebook.htm)
 The Little Book of Valuation
===============================================================================================================================================================================================

Controlling for Differences across Firms
========================================

            No matter how carefully we construct our list of comparable firms, we will end up with firms that are different from the firm we are valuing. The differences may be small on some variables and large on others and we will have to control for these differences in a relative valuation. There are three ways of controlling for these differences:

1\. Subjective Adjustments
--------------------------

Relative valuation begins with two choices - the multiple used in the analysis and the group of firms that comprises the comparable firms. In many relative valuation, the multiple is calculated for each of the comparable firms and the average is computed. To evaluate an individual firm, the analyst then compare the multiple it trades at to the average computed; if it is significantly different, the analyst can make a subjective judgment about whether the firm’s individual characteristics (growth, risk or cash flows) may explain the difference. Thus, a firm may have a PE ratio of 22 in a sector where the average PE is only 15, but the analyst may conclude that this difference can be justified because the firm has higher growth potential than the average firm in the industry. If, in the judgment of the analyst, the difference on the multiple cannot be explained by the fundamentals, the firm will be viewed as over valued (if its multiple is higher than the average) or undervalued (if its multiple is lower than the average).

The weakness in this approach is not that analysts are called upon to make subjective judgments, but that the judgments are often based upon little more than guesswork. All too often, these judgments confirm their biases about companies.

2\. Modified Multiples
----------------------

            In this approach, we modify the multiple to take into account the most important variable determining it – the companion variable. To provide an illustration, analysts who compare PE ratios across companies with very different growth rates often divide the PE ratio by the expected growth rate in EPS to determine a growth-adjusted PE ratio or the PEG ratio. This ratio is then compared across companies with different growth rates to find under and over valued companies.

There are two implicit assumptions that we make when using these modified multiples. The first is that these firms are comparable on all the other measures of value, other than the one being controlled for. In other words, when comparing PEG ratios across companies, we are assuming that they are all of equivalent risk. The other assumption generally made is that that the relationship between the multiples and fundamentals is linear. Again, using PEG ratios to illustrate the point, we are assuming that as growth doubles, the PE ratio will double; if this assumption does not hold up and PE ratios do not increase proportional to growth, companies with high growth rates will look cheap on a PEG ratio basis.

3\. Statistical Techniques
--------------------------

            Subjective adjustments and modified multiples are difficult to use when the relationship between multiples and the fundamental variables that determine them becomes complex. There are statistical techniques that offer promise, when this happens. In this section, we will consider the advantages of these approaches and potential concerns.

### Sector Regressions

In a regression, we attempt to explain a dependent variable by using independent variables that we believe influence the dependent variable. This mirrors what we are attempting to do in relative valuation, where we try to explain differences across firms on a multiple (PE ratio, EV/EBITDA) using fundamental variables (such as risk, growth and cash flows). Regressions offer three advantages over the subjective approach:

a.     The output from the regression gives us a measure of how strong the relationship is between the multiple and the variable being used. Thus, if we are contending that higher growth companies have higher PE ratios, the regression should yield clues to both how growth and PE ratios are related (through the coefficient on growth as an independent variable) and how strong the relationship is (through the t statistics and R squared).

b.     If the relationship between a multiple and the fundamental we are using to explain it is non-linear, the regression can be modified to allow for the relationship.

c.     Unlike the modified multiple approach, where we were able to control for differences on only one variable, a regression can be extended to allow for more than one variable and even for cross effects across these variables.

In general, regressions seem particularly suited to our task in relative valuation, which is to make sense of voluminous and sometimes contradictory data. There are two key questions that we face when running sector regressions:

·     The first relates to how we define the sector. If we define sectors too narrowly, we run the risk of having small sample sizes, which undercut the usefulness of the regression. Defining sectors broadly entails fewer risks. While there may be large differences across firms when we do this, we can control for those differences in the regression.

·     The second involves the independent variables that we use in the regression. While the focus in statistics classes is increasing the explanatory power of the regression (through the R-squared) and including any variables that accomplish this, the focus of regressions in relative valuations is narrower. Since our objective is not to explain away all differences in pricing across firms but only those differences that are explained by fundamentals, we will use only those variables that are related to those fundamentals. The last section where we analyzed multiples using DCF models should yield valuable clues. As an example, consider the PE ratio. Since it is determined by the payout ratio, expected growth and risk, we will include only those variables in the regression. We will not add other variables to this regression, even if doing so increases the explanatory power, if there is no fundamental reason why these variables should be related to PE ratios.

### Market Regression

            Searching for comparable firms within the sector in which a firm operates is fairly restrictive, especially when there are relatively few firms in the sector or when a firm operates in more than one sector. Since the definition of a comparable firm is not one that is in the same business but one that has the same growth, risk and cash flow characteristics as the firm being analyzed, we need not restrict our choice of comparable firms to those in the same industry. The regression introduced in the previous section controls for differences on those variables that we believe cause multiples to vary across firms. Based upon the variables that determine each multiple, we should be able to regress PE, PBV and PS ratios against the variables that should affect them. As shown in the last section the fundamentals that determine each multiple are summarized in table 7.5:

_Table 7.5: Fundamentals Determining Equity Multiples_

|     |     |
| --- | --- |
| _Multiple_ | _Fundamental Determinants_ |

|     |     |
| --- | --- |
| Price Earnings Ratio | Expected Growth, Payout, Risk |
| Price to Book Equity Ratio | Expected Growth, Payout, Risk, ROE |
| Price to Sales Ratio | Expected Growth, Payout, Risk, Net Margin |

It is, however, possible that the proxies that we use for risk (beta), growth (expected growth rate in earnings per share), and cash flow (payout) may be imperfect and that the relationship may not be linear. To deal with these limitations, we can add more variables to the regression - e.g., the size of the firm may operate as a good proxy for risk.

            The first advantage of this market-wide approach over the “subjective” comparison across firms in the same sector, described in the previous section, is that it does quantify, based upon actual market data, the degree to which higher growth or risk should affect the multiples. It is true that these estimates can contain errors, but those errors are a reflection of the reality that many analysts choose not to face when they make subjective judgments. Second, by looking at all firms in the market, this approach allows us to make more meaningful comparisons of firms that operate in industries with relatively few firms. Third, it allows us to examine whether all firms in an industry are under- or overvalued, by estimating their values relative to other firms in the market.

### Limitations of Statistical Techniques

            Statistical techniques are not a panacea for research or for qualitative analysis. They are tools that every analyst should have access to, but they should remain tools. In particular, when applying regression techniques to multiples, we need to be aware of both the distributional properties of multiples that we talked about earlier in the chapter and the relationship among and with the independent variables used in the regression.

·     The fact that multiples are not normally distributed can pose problems when using standard regression techniques. These problems are accentuated with small samples, where the asymmetry in the distribution can be magnified by the existences of a few large outliers.

·     In a multiple regression, the independent variables are themselves supposed to be independent of each other. Consider, however, the independent variables that we have used to explain valuation multiples – cash flow potential or payout ratio, expected growth and risk. Across a sector and over the market, it is quite clear that high growth companies will tend to be risky and have low payout. This correlation across independent variables creates “multicollinearity” which can undercut the explanatory power of the regression.

·     Earlier in the chapter, we noted how much the distributions for multiples changed over time, making comparisons of PE ratios or EV/EBITDA multiples across time problematic. By the same token, a multiple regression where we explain differences in a multiple across companies at a point in time will itself lose predictive power as it ages. A regression of PE ratios against growth rates in early 2005 may therefore not be very useful in valuing stocks in early 2006.

·     As a final note of caution, the R-squared on relative valuation regressions will almost never be higher than 70% and it is common to see them drop to 30 or 35%. Rather than ask the question of how high an R-squared has to be to be meaningful, we would focus on the predictive power of the regression. When the R-squared decreases, the ranges on the forecasts from the regression will increase. As an example, the beverage sector regression (from illustration 7.3) yields a forecasted PE of 32.97 but the R-squared of 51% generates a range of 27.11 to 38.83 for the forecast with 95% accuracy; if the R-squared had been higher the range would have been tighter.

* * *