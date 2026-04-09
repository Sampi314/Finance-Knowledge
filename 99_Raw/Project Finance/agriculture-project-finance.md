# Agriculture Project Finance

**Source:** https://edbodmer.com/agriculture-project-finance

---

This webpage describes project financing of agricultural projects. The page contains a few examples of financial models for both livestock and crop cultivation.  Items to consider in the evaluation of agriculture projects are the price and volatility of various agricultural commodities; the productivity of land; the gestation period and pregnancy period of animals that are held to be slaughtered in an abattoir; and the cost structure of a farm including staff costs, costs of equipment, costs of seeds, costs of fertilizer and other factors. In the model that you can download below I show how to set up accounts for different types of animals with growth in weight form feed.

**[Excel File with Project Finance of Agriculture Project in Africa including Balances for Different Livestock](https://edbodmer.com/wp-content/uploads/2020/10/Abbatoir-Project-Inputs_Grupo-Lider.xlsm)
**

![](https://edbodmer.com/wp-content/uploads/2020/10/image-51.png)

Model of Integrated Farm
------------------------

The model that you can download below is for a large integrated farm in Africa that involves agriculture.  The farm employees many people and includes raising a number of different products. The analysis evaluates the effects of increasing productivity of land and expenditures from developing a farm.  The analysis also includes the effects of different commodity prices.  Part of the above model addresses and abattoir which requires capital expenditures, acquisition of animals and the cost of increasing the size of animals. Unfortunately I have not bothered to clean up the file very well, but I hope you can find some of the analysis and presentation useful.

**[Financial Model of an Integrated Farm with Productivty Changes and Commodity Price Analysis](https://edbodmer.com/wp-content/uploads/2018/09/Augusto-Financial-Model_ver3.xlsm)
**

Comprehensive Model of an Abattoir Project
------------------------------------------

Evaluating the risks and returns from an abattoir can be quite difficult because you must evaluate the life cycle of animals including the time to slaughter, the time of gestation and many other factors.  A model that includes analysis of the life cycle of animals is available for download below.

**[Financial Model of Abattoir that Includes Life Cycle of Different Animals, Cost of Daily Rations and Alternative Pricing](https://edbodmer.com/wp-content/uploads/2018/09/Abbatoir-Project-Inputs_Grupo-Lider.xlsm)
**

In making a model of an abattoir (a slaughterhouse), the following steps can be taken

1.  Establish the animal balance that works through the gestion and the life cycle of different animal types. It also establishes the amount of animals slaughtered.
2.  Work through the margin of each animal type using assumptions for animal weight, cost of feed, feed ratios, selling prices and other factors.
3.  Work through a financial model with capital expenditures revenues and expenses
4.  Add financing to the model
5.  Make a nice presentation of the model

An illustration of the various sections of the model is shown in the screenshot below.  The screenshot is of the table of contents for the model.  You can make these table of contents sheets with the generic macros file.

![](https://edbodmer.com/wp-content/uploads/2018/09/Agri-Model-Structure.jpg)

The summary page or the abbatoir  model and the cash flow waterfall is shown below.  The page allows you to change the price of various animals and the amount of the feed required.  The graph shows the amount of debt required that is affected by the amount of cash equity invested.  You should carefully look at the project IRR to evaluate the competitive position of the project.  The IRR looks high which should make you ask why others will not enter the market.

![](https://edbodmer.com/wp-content/uploads/2018/10/Agri-Summary.jpg)

The cash flow waterfall that has a lot of MIN and MAX functions including investing equity before debt and then putting in debt up to a commitment level is show below.  When the cash flow is positive, the debt is paid before equity.

![](https://edbodmer.com/wp-content/uploads/2018/10/Agri-Cash-Flow.jpg)

The annual cash flow that is computed with the SUMIF function is shown in the screenshot below.  This is taken from the periodic model.

![](https://edbodmer.com/wp-content/uploads/2018/10/Agri-Annual.jpg)

Establishing Animal Balances
----------------------------

In the case of raising animals for slaughter and purchasing an abattoir, the amount of animals for feeding must be tracked and the amount of animals for slaughter must be established.  The screenshot below illustrates the type of table you can create to establish these numbers. Once the inputs for the gestation period, the pregnancy period, the required number of maternal animals and the number for termination, you can use the OFFSET function a lot to find when animals will be born and when they will terminate.  The screenshots below illustrate inputs and creating a table of the balance of animals.  Note that you could create a vintage table like a vintage table for the asset age if you want to get more detailed with respect to the cost of feeding animals at different ages.  In modelling the life cycle I think it is good to separate maternal breeds balance and terminal balance.

![](https://edbodmer.com/wp-content/uploads/2018/09/Agri-Animal-Assumptions-1.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/09/Agri-Gestation-1.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/09/Agri-Offset.jpg)

The screenshots below illustrate use of the OFFSET function to model the lifespan of animals.

![](https://edbodmer.com/wp-content/uploads/2018/09/Agri-Offset-1.jpg)

Modelling Capacity Constraints
------------------------------

In addition to modelling the gestion cycle of animals, capacity constraints of the abattoir should be reflected.  As with other models that involve capacity limits, the MIN function can be used and deferred balances can be maintained.  The screenshot below demonstrates how the capacity constraint can be modelled in an agricultural model.

![](https://edbodmer.com/wp-content/uploads/2018/09/Agri-Min.jpg)

Modelling Animal Rations and the Cost of Getting Animals Fat
------------------------------------------------------------

The cost of raising animals depends on the balance of animals, the amount of ration required to make the animals fat and the cost of the feed.  There may be different feeding strategies and the percent of hay, corn, soybeans, wheat and other nutrients can change. The screenshot below illustrates some assumptions with respect to rations and modelling costs.

![](https://edbodmer.com/wp-content/uploads/2018/09/Agri-Cost.jpg)

Rice Farm
---------

The file that you can download below contains some of the type of inputs you could use for evaluating a rice farm.  I have included this so you can see the kind of inputs and example of the structure of expenses and the way in which costs are structured.

**[Project Finance Model of Rice Project with Detailed Inputs and Calculations of Operating Cost and Capital Expenditures](https://edbodmer.com/wp-content/uploads/2019/01/Senegal-Rice-Project.xlsm)
**

![](https://edbodmer.com/wp-content/uploads/2019/01/Rice.png)

Pricing Data for Agriculture
----------------------------

You can get indicative pricing of agriculture commodities from FRED (Federal Reserve Economic Database) and from the the world bank Pink Data.  Analysis of data with these files demonstrates the variability of prices over time.  In the two different files below you can use the commodity price databases I develop and press the buttons to download current data.  Alternatively you can use the comprehensive stock price database file.  The files for downloading are available for download below.

**[File that Contains Monthly Commodity Price History and World Bank Commodity Price Forecasts with Automatic Updates](https://edbodmer.com/wp-content/uploads/2021/09/Commodity-Price-Analysis.xlsm)
**

**[Comprehensive Stock Price, Commodity Price, and Economic Series Database with Monthly Prices](https://edbodmer.com/wp-content/uploads/2022/08/Comprehensive-Stock-Analysis-Utility-Companies.xlsm)
**

The screenshots illustrate the type of pricing data and the volatility of the agricultural prices.

![](https://edbodmer.com/wp-content/uploads/2018/09/Agri-Commodity-3-1.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/09/Agri-Commodity-Price-Fred-1.jpg)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=3449&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=8204&rand=0.9534981323815049)