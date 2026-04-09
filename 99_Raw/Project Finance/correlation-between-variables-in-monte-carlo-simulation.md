# Correlation in Monte Carlo and Cholesky Function

**Source:** https://edbodmer.com/correlation-between-variables-in-monte-carlo-simulation

---

This page addresses the case that occurs for many real world applications of Monte Carlo simulation where there is more than one variable and/or some or all of the variables have correlation. If the variables do not have mean reversion, the Cholesky function can be used.  But in other cases where the time series does not follow a random walk the Cholesky function does not work as demonstrated below.  Monte Carlo simulation is also use do demonstrate how the means square error works when there are multiple variables.

Mechanics of Cholesky Function with Random Walk

*   Step 1:  Simulate Variable 1 and use NORMINV of random 0-1
*   Step 2: Create Time Series with starting Point and volatility
*   Step 3: Simulate Variable 2 using NORMINV like Step 1
*   Step 4: Correlation \* Step 1 + ((1-Correlation^2 \* Step 3))^.5
*   Step 5: Create Time Series with Starting Point Using Adjusted Random Variable in Step 4

Alternative Tests of Process
----------------------------

.

The screenshots below demonstrate results of testing the process with different scenarios. The first case simulates the same volatility for the two series. The average correlation computes the average of the resulting correlation statistics for all of the statistics. In this case the average of the correlations is a little below the input of 25%.

.

The graph of shown in the screenshot is for one scenario. You can press the F9 key and see different scenarios with different random draws.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-60.png)

.

When I experiment with different volatilities for the two series the process tends to underestimate the input correlation. An example of this is shown below.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-61.png)

.

Correlation with Mean Reversion
-------------------------------

When experimenting with mean reversion in the equations and running the simulation, I have observed a downward bias in the simulation of correlation. This means if we put an input of 50% as the true correlation, when we apply the process of adjusting the random variable and then running the simulation, the average of the simulated correlation is less than the input. One of the cases is demonstrated below.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-62.png)

.

When the mean reversion is 80%, the process is still biased.

![](https://edbodmer.com/wp-content/uploads/2025/05/image-1.png)

.

The file attached to the button below includes the simulation exercise shown in the screenshots. The file includes a macro that shows the progress of moving through the simulation process. The loop with the progress page can be copied into your simulation file.

.

 **[Excel File with Monte Carlo Simulation Using Cholesky Process to Model the Correlation Between Different Variables](https://edbodmer.com/wp-content/uploads/2025/05/Cholesky-Factors-Proofs.xlsm)
**

.

    Sub simulate1()
    
    Application.ScreenUpdating = False
    
    For Row = 20 To 4020
    
    Cells(Row, 4) = Range("Computed_correlation")
    
    ' Application.StatusBar = " Iteration " & Row - 6
    
        
        test = Row Mod 100
                
        If test = 0 Then
        
        UserForm2.Label1 = "Scenario " & Row - 20 & Chr(10) & "Percent " & Format(Row / 402000, "00.00%" & Chr(10) & "Correlation " & Format([Corr_result], "##.00%"))
        
            DoEvents
            UserForm2.Show vbModeless
        
        End If
    
    Next Row
    
    Unload UserForm2
    
    End Sub
    
    

Demonstration of Mean Squared Error when Variables are Independent
------------------------------------------------------------------

If you have multiple variables and want to compute the standard deviation, you cannot simply add-up the standard deviation and come up with the total standard deviation for the series. Instead, you can compute the variation of each series, then add-up the variation (the square of the standard deviation) and finally, you compute the square root of the sum of the standard deviations.

The file below demonstrates how you can prove that the MSE equation works using Monte Carlo Simulation.

[Cholesky Exercise.xls](http://edbodmer.wikispaces.com/file/view/Cholesky%20Exercise.xls/272113320/Cholesky%20Exercise.xls)

[Cholesky Function.xls](http://edbodmer.wikispaces.com/file/view/Cholesky%20Function.xls/272113542/Cholesky%20Function.xls)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=3755&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=8396&rand=0.6252598294667776)