# Remaining Depreciation on Existing Assets

**Source:** https://edbodmer.com/depreciation-with-different-asset-vintages-and-rates-using-udf

---

A classic problem in corporate modelling involves modelling future depreciation and in particular the depreciation expense on existing assets. As explained in the previous section, you can model future depreciation that results from new capital expenditures in a straightforward manner when you build up a table of gross plant. While you can use future capital expenditures and the gross depreciation rate to model depreciation on new assets, unless you have been given information on the asset retirements, modelling the depreciation on remaining assets is a much more complex problem. The problem is that it would be rare for you to obtain a forecast of retirements where the sum of the retirements is equivalent to the gross plant balance (when an asset is retired, the gross plant balance as well as the accumulated depreciation is reduced).

This section describes a process that can be used to compute existing depreciation which can be combined with depreciation on new capital expenditures to derive total forecasted depreciation. Two cases are described below. In the first case it is assumed that you have information on the gross plant balance at the end of the historic period as well as the plant life. In the second case it is assumed you only have information on the net plant balance in the last historic period and the plant life. All of the analysis is based on straight line depreciation. The discussion may seem long and complex, but you can implement the method easily in corporate models and once the basic mechanics are established the technique can easily be copied to other models. In other words it is not that complex. An integrated financial model that includes the techniques is attached to the button below.

.

 **[Excel File with Projects Consolidating to Portfolio Demonstrating Returns and Financial Ratios](https://edbodmer.com/wp-content/uploads/2025/04/Portfolio-Consolidation.xlsm)
**

.

#### Theory of Existing Depreciation and Adjustment to Stable Growth Model

The continual growth analysis discussed in the prior section for straight line depreciation expense can be used to demonstrate how depreciation on remaining existing assets can be modelled. To do this one can construct a long-term model that continues until after the ratios stabalize in the model of stable depreciation rates. Then one can simply stop the capital expenditures at a defined point. In the population example, you would stop any new births and see what the remaining population is (the remaining gross plant). You could also measure how fast people are depreciating until they die (the depreciation rate or depreciation expense). You could measure the amout of deaths for each year (the retirements). If there was a higher growth rate in the population before the births stopped, the population would remain at a higher level for longer. If the life expectency of the population is longer then then there would be more people for a longer period.

In the stable depreciation model, after the capital expenditures are stopped, you can see the level and more imporantly the pattern of depreciation expense on the remaining assets without future capital expenditures. This is the remaining depreciation for assets that are on the balance sheet as of the stop date. Note that this analysis assumes that the capital expenditures were initially made with constant growth over time (not in a lumpy manner).

The screenshot below illustrates how you can add a flag for the end of the capital expenditure period and see how the remaining depreciation moves over time (it is always straight line depreciation). In the case shown on the screenshot a life of 8 years and a growth rate of 11% are used. If you use a different growth rate or plant life, the remaining straight line depreciation that is computed on the existing assets will be different. The depreciation expense declines after the capital expenditures stop because the older capital expenditures are retiring over the remaining life. Note in the excerpt below that the depreciation on existing assets adds to the net plant balance at the date that capital expenditures are stopped. In the example, the capital expenditures are stopped in year 50 (presumably that is long enough so that plants with different lives will stabalize from having a life of less than 50 years). Then, after the expenditures are stopped retirements continue to occur and the gross plant balance declines. Eventually at the end of the plant life after 50 years, the asset is fully retired. The retirements increase because of the assumption of constant growth that occured earlier. As with all cases, the depreciation expense is computed from the gross plant. But net plant is also computed and the depreciation can be expresses as

.

![](https://edbodmer.com/wp-content/uploads/2025/02/image-8.png)

.

Once the remaining depreciation is simulated in this manner, you can compute the depreciation rate divided by the gross or net plant and then try to come up with a method to match this rate (that is what is demonstrated below). Evenutally, the depreciation expense sums to the remaining net plant (not the gross plant as some depreciation on the existing plant has already been recorded). The screenshot below shows that the depreciation rate on net plant that sums to 100%.

.

![](https://edbodmer.com/wp-content/uploads/2025/02/image-9.png)

.

#### Illustration of Remaining Straight Line Depreciation on Existing Assets with Different Assumptions

To demonstrate what happens to depreciation expense on existing assets, a few different cases with different lives and different growth rates are shown below. The graphs show the straight line depreciation divided by the net plant at the date capital expenditures stop. The graph uses the depreciation rate on net plant shown in the excerpt of the excel sheet above. Even though the depreciation rates are declining, the depreciation is always straight line. The depreciation is declining because assets are being retired and they eventually all are retired and the depreciation expense that is straight line, falls to zero. The first case assumes a 10 year life and a growth rate of 5%. Other cases adjust the growth rate and the plant life from this intial case with the 10 year life and the 5% growth.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-32.png)

.

When the growth rate increases, there are more retirements from the existing asset base later on (recall the screenshot above that shows how retirements are increasing). In this case the depreciation on exiting plant still sums to 100% and is flatter because of the higher growth rate.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-33.png)

.

The third scenario assumes a longer life and a low growth rate. In this case, the depreciation rate declines at a relatively steep rate and the depreciation on the existing assets continues for a longer period.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-34.png)

.

#### Simulating the Depreciation Rate on Existing Assets

Once the depreciation is computed on the net plant using the simulation, the question is how to estimate this rate when there are different plant lives and different growth rates in a financial model. If it is assumed that the depreciation life is given, and the growth rate is known, then two methods for computing the projected rate are a variable declining method (this method computes straight line depreciation on the base that is retiring). Alternatively, a intercept and negative slope can be estimated from a simulation. In the VDB case, the initial declining balance factor that evaluates straight line depreciation on the retiring plant can be estimated. The slope and intercept can be computed from a simple regression (regressing the depreciation rate aginst time) while the VDB factor can be computed from the intial depreciation rate as a percent of net plant relative to a flat depreciation rate over the remaining life. The graphs shown below show how the slope and intercept method project depreciation rates relative to the simulated rates that are computed from the spreadsheet that had a long simulation and stopped the capital expenditures after a certain period (50 years in the example).

The first case shows a simulations of the depreciation rates using the two methods in the 10 year life and 5% growth growth case. The simulation shows that the slope and intercept method produces a close approximation but does not capture the curvature of the line. The VDB method produces a reasonable result with somewhat higher depreciation rates in the final periods. The simulations are computed in the slope and intercept method through applying the intercept in the first year and then multiplying the year for the remaining life by the slope for later years. For the VDB method, the rates are computed through applying the VDB function in excel.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-35.png)

.

The second case assumes a higher growth rate which produces a flatter line. In this case the line is steeper and the slope and intercept method produces a closer result.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-36.png)

.

For the third case, the life is longer and the growth rate is lower. This produces a steeper decline in the straight line depreciation rate. The forecasts are still reasonable with the slope and intercept method producing a more accurate forecast. In each case the growth rate is assumed to be constant. If the historic growth rate was not constant, the forecasts would not be different.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-37.png)

.

#### Data Tables for VDB and Slope/Interecept

To make the process applicable in actual models, data tables with different growth rates and depreciation lives can be computed. These data tables can be derived from the spreadsheet that is based on the stable growth analysis discussed above where you change inputs for growth and for plant life. As the method is for straight line depreciation, these data tables do not vary with different corporate models. If the growth rate and the depreciation life is given, the slope, intercept and the VDB factor can be looked up. The slope and intercept or the VDB factor can be computed for a large number of different growth rates and depreciation lives using a data table similar to the data table shown in the earlier table for the accumulated depreciation divided by gross plant for many different growth and depreciation live scenarios (computed with a data table in excel).

The table below shows and excerpt from the data table for the slope. The slope as a function of growth and life. As the growth rate is bigger, the slope is a smaller negative number. This is expected as the slope is steeper with a shorter life because of less growth in capital expenditures. As the plant life is longer the slope is a smaller negative number and flatter. The idea is that if you know the growth rate and the plant life as inputs in a corporate model, you can then derive the slope from this fixed data table. You would copy this data table into your model with fixed values and then use an INDEX function to find the value.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-38.png)

.

The second table shows the intercept in a similar manner. In this case the intercept is strongly affected by the plant life and to a lesser extent by the growth rate. As the plant life is longer the starting point of the the depreciation rate graph is less. As with the slope value, if you know the growth rate and the plant life as inputs in a corporate model, you can then find the intercept from the fixed data table. You can copy this data table into your model with fixed values and then use an INDEX function to find the value.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-40.png)

.

As shown above, the VDB factor is the value of the first years depreciation. By using the simulation model you can change the life and the growth rate and compute a data table for the VDB factor. An excerpt for this data table is shown in the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-41.png)

.

#### Implementing Depreciation on Existing Assets in a Corporate Model with Information on Gross Plant and Accumulated Depreciation

If you have information on the gross plant and accumulated depreciation then you can implement the depreciation on new capital expenditures using gross plant accumulation and you can separately compute the depreciation on existing assets. For existing depreciation you need the growth rate on historical assets and the plant life. With these two variables you can compute the depreciation rate and then the existing depreciation amount. The difficult part is to first compute the growth rate from the accumulated depreciation divided by the gross plant.

Computing the depreciation on existing assets and new assets in a financial model is illustrated in the screenshot below. The top part with the numbers in blue are the key inputs for the computation. This includes the plant life of 7.5 years, the growth rate derived from the analysis of accumulated depreciation to net plant and the factors for intercept, slope and VDB that are derived from the data tables discussed above. Once the inputs are collected, the depreciation rate on the remaining net plant is derived from either the slope and intercept method or the VDB method. It is emphasized again that the depreciation rate is straight line and the reason for the declining rate is the retirement of existing assets. With the existing depreciation rate the amount of depreciation is computed from the balance of net plant at the start of the period.

The screenshot below shows the calculation of depreciation on new capital expenditures as well. This calculation includes a half year assumption for the year in which the assets are placed in service and a half year convention for the year of retirement. The capital expenditures and retirements are used to compute the balance of gross plant with in turn is used to compute the depreciation expense. The final row in screenshot shows the total depreciation expense which is the sum of the depreciation expense on existing assets plus the depreciation expense on new assets.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-42.png)

.

The remaining discussion explains in more detail how to derive the growth rate, the slope and intercept and the final depreciation expense calculations in more detail on a step by step basis.

#### Step 1: Copy large data tables from the model of stable depreciation

The analysis of stable depreciation rates that is modelled in a spreadsheet includes large data tables, excerpts of which are shown above. These data tables are large with many rows and columns for the growth rate and the plant life. While the data tables can slow down excel, if straight line depreciation is used (which is the basis for this discussion), the ratios and factors do not change other than based on the plant life and the growth rate. This means you can copy and paste special the depreciation factors into a page of your financial model and you will not have to change the copied data data tables. The data tables that you need are the tables for accumulated depreciation as a percent of gross plant, the slope, the intercept and the VDB factor. All of these tables are structured with sensitivity analysis for growth rate and plant life.

#### Step 2: Find the Implied Growth Rate from the Ratio of Accumulated Depreciation to Gross Plant and from the Plant Life

If you are given the plant life and the ratio of accumulated depreciation to net plant you can theoretically derive the growth rate. As one of the large data table produces the accumulated depreciation to net plant ratio, you can start with the plant life and then look in the table until you find the growth rate that matches the given accumulated depreciation to gross plant ratio. Note that the accumulated depreciation to net plant should come from the balance sheet when the company reports these statistics (sometimes you will only get the net plant which renders this method impossible as explained below). There is not an easy excel function to walk to the plant life and then lookup a value from the accumulated depreciation to gross plant. A function has been created to do this automatically as shown below. The function below can be copied into a corporate model without difficulty.

.

The data table and the function to find the growth rate is illustrated below. Once again it is emphasized that while this may seem complicated, if you have the tables in your corporate model, the process is automatic and easy to copy.

.

![](https://edbodmer.com/wp-content/uploads/2025/02/image-7.png)

.

    Function Table_Look_up(Lookup_Table, Lookup_Column, Table_Value)
    
    Dim Index_Array(1000) As Double
    Dim First_Column(1000) As Double
    Dim Rows_in_Table As Single
    
    test_index = WorksheetFunction.Index(Lookup_Table, 10, 4)
    
    Rows_in_Table = Lookup_Table.Rows.Count
    
    '
    ' First, compute the index
    '
    
    For i = 1 To Rows_in_Table
    
        Index_Array(i) = WorksheetFunction.Index(Lookup_Table, i, Lookup_Column)
         First_Column(i) = WorksheetFunction.Index(Lookup_Table, i, 1)
    
    Next i
    
    final_value = WorksheetFunction.XLookup(Table_Value, Index_Array, First_Column, 0, 1, -1)
    
    Table_Look_up = final_value
    
    End Function

.

#### Step 3: Find the Slope/Intercept or the VDB factor from Data Tables

Once you have the growth rate and the plant life (the plant life can be found from annual reports or assumed), you can use the data tables and get the factors for the depreciation rate on net plant for the existing plant as described above. As this process uses the growth and the plant life and as the data tables are fixed (it is best to put them in a separate sheet), the factors — slope, intercept, VDB — can be found using the INDEX function. This use of the index function is illustrated in the screenshot below. The rounded depreciation life defines the column number and the match function can be used to get the column number for the data table. With the column number and row number defined you can extract the factors necessary to compute the depreciation rate on existing assets that retire.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-45.png)

.

#### Step 4: Compute the Existing Depreciation from the Net Plant

With the slope and intercept established, you can compute the depreciation rate and then multiply the depreciation rate by the net plant at the base period or the last historic year. To do this there should be a counter variable in the model that counts from 1 to the number of forecast years. When using the slope and intercept method, the depreciation rate is computed from this counter using the formula:

Deprecation Rate (t) = Intercept – Slope x t

Once the depreciation rate is established that varies over time, the depreciation amount is computed as the net plant in the final historic year multiplied by the depreciation rate using the formula:

Depreciation on Existing Assets (t) = Net Plant in Base Period x Depreciation Rate (t)

These formulas are illustrated in the screenshot below.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-43.png)

  
.

#### Step 5: Compute Depreciation on New Capital Expenditures

As already explained, the depreciation on new capital expenditures is much simpler. In this case the capital expenditures are computed with a half year convention where the depreciation assumes that the depreciation occurs with a 1/2 year assumption. The division of the capital expenditures into two parts allows the retirements to also occur in the middle of the year. Computation of capital expenditures for new capital expenditures are illustrated on the screenshot below. In this screenshot the accumulated depreciation on new plant is shown as is the net plant. On the bottom of the screenshot the total of

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-47.png)

.

Case Where Gross Plant and Accumlated Depreciation Are Not Available
--------------------------------------------------------------------

In some situations the net plant property and equipment is presented on the balance sheet and information on the gross plant and accumulated depreciation is not available. In this case you can use the net plant and compute the slope and intercept as explained above. However without the ratio of accumulated depreciation to net plant statistic, computing the the implied growth rate is not possible. In the case without the ability to compute the implied growth in an objective way, the historic growth can be directly input. Calculation of the existing depreciation without information for the gross plant and the accumulated depreciation is illustrated in the screenshot below. Note that there is a TRUE/FALSE switch that allows the direct input of growth rate to be input.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-48.png)

.

General Issues in Modelling Depreciation
----------------------------------------

The video below demonstrates how to deal with depreciation and taxes in a leveraged buyout model.

.

.

Vintage Depreciation
====================

The set of videos first address how to compute prospective depreciation in the case of straight line depreciation rates. In this case without growth, the problem is demonstrated to be an easy one. In the case of growth of capital expenditures, the use of the OFFSET function is demonstrated for straight line depreciation. The second file demonstrates how the problem gets messy when there is a changing depreciation rate. The third video explains how do create a function that first works through the capital expenditure array in a loop and then works through the projection model in a second loop. The age of each vintage is computed and a variable with two dimensions is maintained to keep track of the depreciation rate that is a function of the age and the depreciation amount that must sum across different vintages.

Depreciation Expense from Continuing Capital Expenditures and Changing Depreciation Rates
-----------------------------------------------------------------------------------------

The function for a depreciation vintage is demonstrated below. You need to make two loops. First loop around each capital expenditure that is input by year. Then, once the loop for the capital expenditure is made, within the loop, make a loop around the lifetime of each asset. The depreciation moves forward from the date at which asset is placed in service. Note in the excerpt below the model year is the first loop and then within the loop is another loop for the vintage. As long as the computed age is positive, the depreciation for the incremented by the cap exp for the period.  

**[Excel File that Illustrates Stable Ratios for Depreciation and Deferred Tax that Depend on Growth and Depreciation Rate](https://edbodmer.com/wp-content/uploads/2019/03/Exercise-13-Stable-Depreciaton-and-Deferred-Tax.xls)
**

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=2434&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9172&rand=0.011946735209720116)