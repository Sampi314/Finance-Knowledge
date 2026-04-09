# Using Python with Excel - Part Two - Lentran Modelling Solutions

**Source:** http://www.lentransolutions.com/using-python-with-excel-part-2

---

Using Python with Excel – Part Two
==================================

April 29, 2019[No Comments](http://www.lentransolutions.com/using-python-with-excel-part-2#respond)
[Theo West](http://www.lentransolutions.com/author/theowest/)

### Using Python with Excel for Powerful Financial Modelling Solutions

#### A practical guide to Python

This article provides an overview on how we at Lentran Modelling Solutions use Python in conjunction with Excel in our financial models.

Excel’s strengths are its interface, establishment in the business world and being able to analyse, manipulate and present data without any need for programming. Major pitfalls are a relatively low number of mathematical and statistical tools, difficulty in storing and calculating large data sets (the program commonly crashes with larger workbooks) and slow execution compared to advanced programming software. This is where Python comes into play, which is currently together with R among the most popular programming languages, especially for data analysis. It includes a huge number of packages for manipulating big data, scientific computing, machine learning & artificial intelligence methods, making graphics, exploring data, creating statistical models and performing statistical tests.

At Lentran Modelling Solutions we regularly combine Excel and Python as it enables us to have the best of both worlds. This combination enabled us to develop powerful solutions that would not have been possible with each program on its own.

#### Applications

In the past LMS utilised Python in conjunction with Excel for various projects:

1.  One of our clients stored project data in an SQL database, which was regularly updated. We required an Excel financial model, which based on user-specified settings in the model would load and filter data from SQL into the Excel model. Doing this with only VBA would have been too slow, error prone and complex. We integrated Python’s programming power to directly access, filter and analyse the SQL data and efficiently upload the data to our Excel model.
2.  Aggregating and manipulating data from multiple workbooks containing millions of data points.
3.  We utilised machine learning for recognizing patterns containing more than 5 million individual loan repayments covering 100,000 debtors over a time frame of 25 years. Each debtor was characterised with 15 properties. Based on past repayments we deployed multiple machine learning techniques to derive an algorithm for predicting the probability of future cash flows based on debtor characteristics. In turn we were able to develop a powerful forecasting model in Excel with these Python generated probability results.
4.  Use a variety of machine learning models to make predictions regarding future price of financial instruments based on prior price behaviour. Machine learning algorithms selected indicators for identifying and optimising buy and sell signals to maximise trading profits giving the current market state.

#### Case Study 1

###### Client

The project was conducted in cooperation with a global investment management and data science firm. The company is heavily invested in a variety of financial instruments and securities. At its beginnings the firm’s investment decisions were largely based on their traders’ subjective judgement. Traders heavily relied on analysis of fundamental data including revenues, growth rates, overall market direction and profits to determine which assets to buy or sell. In recent years the firm has increasingly focused on developing new, innovative investment strategies based on scientific research and analysis.

###### Purpose

As the behaviour of financial markets changes through time, we designed an intelligent investment system that evolves with the market. Over long periods of time economies tend to follow a pattern of expansion and contraction, which is caused by complex interactions between market-influencing factors and unknown random processes. Companies are traded within this overarching environment and are heavily influenced by the current cycle.

A system had to be developed that was able to forecast future price direction and make automated investment decisions with the aim of maximising medium to long term profits. The trading strategy had to solely base its decisions on historical asset prices. Machine learning was utilised to detect price patterns in the context of the fluctuating economic and business environment.

*   A system had to be developed that was able to forecast future price direction and make automated investment decisions with the aim of maximising medium to long term profits. The trading strategy had to solely base its decisions on historical asset prices.
*   A machine learning algorithm had to be developed to dynamically combine and adjust indicators with the highest forecast accuracy during the prevailing market environment.
*   Data connection between the Excel / Python financial model with a SQL database containing historical prices.
*   Live data connection with model and exchange to download and display current prices.
*   Allow users to filter, reshape, clean and visualise data. Change of system parameter inputs through the Excel interface.

###### Approach

The initial model was based on predicting returns in the S&P 500 stock index and later expanded onto other markets to prove out its forecasting power. The development process was split into distinct stages:

*   Setup of a connection between Excel / Python and the SQL database.
*   Manual cleaning of the outlier prices and creation of algorithms to automatically clean and reshape data.
*   Data visualisation to better understand the data
*   Decomposition of price time series into trend, seasonality and noise.
*   Programming of multiple systems for predicting price.
*   Use of machine learning algorithms to dynamically select the system with the highest likelihood for profit during a given time period and the prevalent market regime.
*   Introduction of statistical tests to determine whether signals have significant forecasting power.
*   Historical testing to determine the profitability of the model.
*   Setting up the model for live trading.

###### Outcome

The trading model allowed the firm to utilise a systemic approach to investing that does not rely on subjective judgements of individual traders. The model has been able to deliver positive returns trading live, which match the historical backtests performed. Due to the dynamic selection of trading algorithms by the implemented machine learning techniques little maintenance is required. The firm added further markets to the portfolio and the investment system has been able to achieve profits.

Due to its data acquisition, cleaning and visualisation capabilities the model has been become a central point of focus for the finance, analytics and trading team.

#### Case Study 2

###### Client

The project was conducted for major project advisory and specialist finance arranging company. The client worked in conjunction with a leading debt collection agency operating in multiple areas including credit cards, mortgages, consumer travel, insurance and energy. They are renown for providing innovative solutions to complex project requirements, which creates competitive advantages and enhances returns for their customers.

###### Purpose

The client required a pricing and profitability model to estimate future financial returns for the bid process of secondary debt and a model for predicting future returns from their loans.

*   Loan repayment behaviour modelling to enable users to forecast loan repayments of a given debtor dataset.
*   Multiple machine learning algorithms that created forecast curves based on debtor characteristics and past behaviour.
*   Determination of NPV of secondary debt for bid processes.
*   Time-series forecasting of the secondary loans owned by the client. Users to be able to adjust assumptions of the dataset and to run multiple scenarios over different time periods.
*   Connection of the Excel model with a SQL database through Python. Users are able to pre-process and filter data for visualisation and adjustment of the machine learning algorithms.
*   Utilisation of a dashboard, which allows users of the model to collect results and to draw inferences based on changing assumptions.

###### Approach

The development of the model was separated into data connection and pre-processing, valuation of a debtor dataset for the bidding process and time-series forecasting of loan repayments of secondary loans owned by the client. Valuation and time-series forecasting were both performed by the machine learning algorithms. The algorithms automatically update their inputs based on changing data. To assess the accuracy of the algorithms for valuations past predictions were compared with actual repayments over time. The time-series forecasts were continually compared with updated actuals.

###### Outcome

The model has enabled the client to make more accurate valuations during the bid stage of secondary debt and helped to estimate expected revenue from their currently owned debt.

The user-friendly Excel front-end interface of the model has also enabled users to analyse and visualise data fast and efficiently.

[](javascript:void(0) "Share this")
[](javascript:void(0) "Tweet this")
[](javascript:void(0) "Share this")
[](javascript:void(0) "Share this")
[](javascript:void(0) "Pin this")

[Previous post Using Python with Excel – Part One](http://www.lentransolutions.com/using-python-with-excel-part-1/)
 [Next post Using Python with Excel – Part Three](http://www.lentransolutions.com/using-python-with-excel-part-3/)

### Leave a Reply [Cancel reply](http://www.lentransolutions.com/using-python-with-excel-part-2#respond)

Your email address will not be published. Required fields are marked \*

  

[](javascript:void(0);)
[](http://www.lentransolutions.com/using-python-with-excel-part-2# "Back to top")