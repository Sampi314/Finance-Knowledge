# Market Price C++ Model

**Source:** https://edbodmer.com/market-price-c-model

---

In the past, I programmed an electricity market price model that dispatches units, builds new plants, accepts different fuel prices and forecasts the market price of electricity. I had some clients who used my market model for many years but these days I have been working on different projects. I wanted to sell this model to people interested in forecasting power prices and making detailed electricity analysis but I have long given up on this idea.

Even though it is not at a all my main business, for some applications the model may be still useful and I have put instructions on how to implement and run the model. I wrote the dispatch model in C++ The model accepts databases of power plants, loads, fuel prices, renewable resources and other factors and then makes a price forecast. Some of menus are old fashion but the idea is to do just about all of your in excel and get the outputs also to excel. The case study shown below demonstrates how you can quickly build a forecast, benchmark it to actual prices and then evaluate different supply and demand alternatives including construction of new capacity, sensitivity to fuel prices, demand management and many other issues. I am working on how you can run the model from the internet (I am not an expert at all in this however).

You could make a model like this completely in excel, but it would requires so much data in different formats it may be slow and clumsy.

**Case Study on Building Electricity Market Price Forecast**

Introduction
============

To illustrate how to make an electricity marke price forecast, I have set-up a case study using data from the New England market. The New England market is heavly dependent on natural gas. The good news about this marke is that the ISO New England publishes convienent data on individual power plants, hourly loads, actual market prices, plant outages, renewable generation and other items that allows you to make a forecast. In this case study I walk you through setting up excel files, benchmarking the model and performing analysis with the model.

Virtually all of the work you would do to create a case is in excel. But when you are finished with the excel analysis you need to upload text files into the simulation model that I refer to as the C++ model. The uploading process all works with macros and all you have to do is press a button once things are formatted consistent with the explanation below.

**Step 1: Opening C++ Model and Setting-up a New Model Run with New Data**

To set-up the model first you can go to the “Model Input” spreadsheet listed as part of Step 2 below. On the first page of this spreadsheet there is a button that runs a macro called “Activate Market Model.” If the model is correctly installed, then you can press the macro button and a menu for the model will appear (installing the model can be a bit tricky and you may have to call me).

From the model menu (shown on the screen shot below), go to the “Define Project” menu. Here you can put in new file names for the five different files (load file, plant file, shape file, monthly file, annual file). Once you enter the new file names, you should also define a base year which is the first year of the model. I think it is a good idea to allow for a couple of historic years in the model so that you can benchmark actual market on-peak and off-peak prices with prices that are forecast by the model.

![Prd1.PNG](https://edbodmer.wikispaces.com/file/view/Prd1.PNG/602899598/350x265/Prd1.PNG "Prd1.PNG")

After you have decided on the base year and the file names, make sure to click the save button.

[![Model Inputs.xlsm](https://c1.wikicdn.com/i/mime/32/empty.png)](http://edbodmer.wikispaces.com/file/view/Model%20Inputs.xlsm/602899662/Model%20Inputs.xlsm)

[Model Inputs.xlsm](http://edbodmer.wikispaces.com/file/view/Model%20Inputs.xlsm/602899662/Model%20Inputs.xlsm "Model Inputs.xlsm")

*   [Details](http://edbodmer.wikispaces.com/file/detail/Model%20Inputs.xlsm)
    
*   [Download](http://edbodmer.wikispaces.com/file/view/Model%20Inputs.xlsm/602899662/Model%20Inputs.xlsm)
    
*   9 MB

**Step 2: Importing Historic and Future Hourly Loads into the Model**

The general process of entering hourly load data is to first download horly loads that are hardly ever in a simple flat file that is arranged from 1 to 8760. Then you set-up a spread sheet file to convert the data using MATCH and INDEX (see the example below). Once you have the data in a flat format, you can copy and paste it to the Model Input File. Next, you can run the maco Edit Files and Open Load File  
Go to Load File Page

Go to ISO New England Website and search for EEI Loads  
[https://www.iso-ne.com/system-planning/system-forecasting/load-forecast](https://www.iso-ne.com/system-planning/system-forecasting/load-forecast)

Open the C++ model and go to Edit Tools window and import excel

The historic loads are there an Download Text

Go to Blank Excel File  
Data From Text — Fixed Width — Click to get

Open the Load Data and then Tools to Read File

[![Re-format Hourly Loads.xlsx](https://c1.wikicdn.com/i/mime/32/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.png)](http://edbodmer.wikispaces.com/file/view/Re-format%20Hourly%20Loads.xlsx/602899684/Re-format%20Hourly%20Loads.xlsx)

[Re-format Hourly Loads.xlsx](http://edbodmer.wikispaces.com/file/view/Re-format%20Hourly%20Loads.xlsx/602899684/Re-format%20Hourly%20Loads.xlsx "Re-format Hourly Loads.xlsx")

*   [Details](http://edbodmer.wikispaces.com/file/detail/Re-format%20Hourly%20Loads.xlsx)
    
*   [Download](http://edbodmer.wikispaces.com/file/view/Re-format%20Hourly%20Loads.xlsx/602899684/Re-format%20Hourly%20Loads.xlsx)
    
*   11 MB

**Step 3: Importing Historic and Future Hourly Loads into the Model**

The general process of entering hourly load data is to first download horly loads that are hardly ever in a simple flat file. Then you set-up a spread sheet file to convert the data using MATCH and INDEX (see the example below). Once you have the data in a flat format, you can copy and paste it to the Model Input File. Next, you can run the maco Edit Files and Open Load File.

Press the button that creates the file and then upload it into the C++ model

Next, Activate the model. and go to New and Existing Plant Facilities Page  
Then tool and press the “Import Data from Excel”

Adjusting for Capacity Outages
==============================

The first step in evaluating outages is to put in large outages such as outages for nuclear plants. For these plants it is a good idea to put in specific start and end dates which is an option in the model.

We are trying to get the month by month average outage (non-numclear) divided by the average capacity (non nuclear) per month. The first step is to read in a report published by the ISO that contains data on all of the plant outages on a daily basis. Then you can use the AVERAGEIF function to find the average outages by month. This report can be found at the following link:

[https://www.iso-ne.com/isoexpress/web/reports/operations/-/tree/daily-capacity-status](https://www.iso-ne.com/isoexpress/web/reports/operations/-/tree/daily-capacity-status)

There is worksheet that demonstrates this process and illustrates the amount of plant outages in a real system with data on daily and monthly plant outages (the model uses monthly plant outages). You can observe variation in the outages by year in total and the way the variation changed on a month by month basis. The file uses the INDIRECT function combined with the AVERAGEIF function to evaluate the month by month outages.

When you are fininshed, you use the macro in the Plant Read Sheet to create a (set of) files that are read into the C++ model.

Running the Model (Dispatching, Computing Prices, Output to Reports)
====================================================================

Open the file

Go to the Montly File and Adjust the Switch to Generate Detail  
Go to the Montly File and Adjust the Switch to Turn off Dispacth

Then Run Simulation — Use a single simulation and then press “Run Model”

When finished running the model, get the read output sheet.

In the read

Then press the “Grow Continual”

There is a column that contains the total outages  
and make new file name

Step 1: Load Data

Go to www.iso-ne and find the CELT report. Available with excel and pdf.

To create new file

Videos associated with Lesson Set 3: Comprehensive Sculpting Analysis
=====================================================================

Step 2: Plant Data

Go to www.iso-ne and find the CELT report. Available with excel and pdf.

**Installing and Implementing the Market Price Model**

Introduction
============

[![PRDfix_Instructions.docx](https://c1.wikicdn.com/i/mime/32/application/vnd.openxmlformats-officedocument.wordprocessingml.document.png)](http://edbodmer.wikispaces.com/file/view/PRDfix_Instructions.docx/480410884/PRDfix_Instructions.docx)

[PRDfix\_Instructions.docx](http://edbodmer.wikispaces.com/file/view/PRDfix_Instructions.docx/480410884/PRDfix_Instructions.docx "PRDfix_Instructions.docx")

*   [Details](http://edbodmer.wikispaces.com/file/detail/PRDfix_Instructions.docx)
    
*   [Download](http://edbodmer.wikispaces.com/file/view/PRDfix_Instructions.docx/480410884/PRDfix_Instructions.docx)
    
*   774 KB

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1284&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11180&rand=0.41164176286762244)