# Sust Global | The financial cost of climate change: using AI to translate climate science into loss models

**Source:** https://www.sustglobal.com/insights/financial-cost-climate-change-ai-modeling

---

The financial cost of climate change: using AI to translate climate science into loss models
--------------------------------------------------------------------------------------------

In the blog below, Matt Cooper - Senior Data Science Engineer at Sust Global - explains the methodological complexity involved in transforming raw climate data into meaningful financial loss models that organizations can actually use. He describes how Sust Global uses novel machine learning techniques to resolve this challenge and enable our clients to accurately identify how and where they are exposed to financial risk from the impacts of climate change.

### How bad will climate change get?

Last year, the Intergovernmental Panel on Climate Change (IPCC) [concluded](https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_Headline_Statements.pdf)
 that human influence had unequivocally ‘warmed the atmosphere, ocean, and land.’ This is already affecting many climate and weather extremes on a global scale, with deadly disasters such as wildfires, droughts, floods and cyclones becoming more intense and frequent.

What is less certain is how much humanity will collectively work together to reduce future warming of the planet. The most common way to [model the future of the climate](https://www.sustglobal.com/wildfire-risk-predicting-unusual-future/#modelling-the-future)
 is to use simulations, which use a whole suite of assumptions about the world to simulate the future – everything from the laws of fluid dynamics and atmospheric chemistry to variables in human behavior. These are not predictions but rather scenarios that give an idea of the range of possible futures.  
With that in mind, how can businesses translate abstract climate science into the actionable financial metrics required to support informed strategic decision making?

At Sust Global we combine AI-enhanced climate simulations with industry-standard loss and damage models used by the insurance sector to tackle this problem. This blog post will outline each of the steps in the process:

*   The raw climate simulations used by the scientific community
    
*   How we derive hazard risk estimates from these simulations using AI
    
*   How we take historic estimates of damages associated with climate impacts to translate hazards into losses
    
*   How we deal with uncertainty at every step of this pipeline.
    

### The science of simulation

The first step in predicting what climate change will be like is to run simulations of the future. These simulations are called Global Climate Models, or GCMs, and they divide the world into grid cells. Then, based on the physical laws of how temperature, sunlight, water, and air interact in the presence of increasing CO2, these models can predict a small step into the future - typically one hour. Run these models long enough, and you have a simulation of a century. Aggregating lots of different models under many different assumptions can give us our best picture of what the future of the world will look like.

While these models can answer important questions about how emitting more CO2 translates into global temperature increases, they aren't quite ready to predict the occurrences of real property-destroying hazards - that's where Sust Global comes in.

The raw data from GCMs needs to be refined to get estimates of hazards. This is in part because GCMs are very coarse - they can simulate weather over a wide area and can make accurate forecasts about the temperatures and rainfall in a region - but they don't make accurate forecasts for things that happen on very local spatial scales.

For example, a GCM can tell us if fire weather will be more likely in Southern California, but it can't forecast accurately if a particular LA neighborhood is at risk, since this depends on things like what kind of forests are nearby. This level of local granularity is too detailed to fit into a global model of the entire earth's climate system.

GCMs can also broadly predict changes in rainfall trends, but whether or not your house is at risk of flooding depends on precise estimates of local topography. GCMs are also inadequate for complex, fine-scale weather phenomena like tropical cyclones (aka hurricanes and typhoons depending on where they form).

To give our customers an accurate picture of the climate hazards, a lot of our work involves taking the fuzzy, imprecise predictions from GCMs and using them to create a crisp, high-resolution picture of the future.

We take future predictions of fire weather, combine it with on-the-ground, satellite-derived data on land cover and on historic fire, and then use AI to make actual, credible forecasts of fire risk. We use similar methods to turn coarse estimates of future flood risk, in combination with thousands of high-resolution geospatial flood maps from FEMA, into highly precise flood estimates probabilities at multiple depths. All of this work adds enormous value to the global forecasts made by the scientific community and gives our customers accurate, validated data on hazards that they care about.

### Quantifying the cost of climate hazards

Predicting the risk of climate hazards in the future is a complex task - one that relies on supercomputer simulations, cutting-edge AI models, and decades of satellite imagery. But this still does not tell us enough about how _bad_ climate change will be - it does not tell us whether a 2-foot flood or a category 4 hurricane winds will do more damage to a house, or whether a week-long heatwave or a season of wildfire smoke will do more damage to public health. For these we need to translate hazards, like hurricanes and floods, into a cross-comparable metric like dollars lost, percentage of homes destroyed, hours of work interrupted, or even lives lost. To do these we need what are called _damage functions_.

A damage function is a mathematical function that takes in some climate hazard and outputs some measure of how bad the damage is. Let's take fires as an example. Let's say that we already have predictions of the risk of fires occurring in the year 2030 in the state of California, but we want to know how many houses they will destroy. So our function would look like:

`fire probability * percent of houses usually destroyed * total number of houses = expected number of houses destroyed`

This will provide us a metric for how many houses could be expected to be lost in a given year - a very important number for everyone from insurance companies and state emergency preparedness agencies to individual homeowners. Typically, the function is derived using historical data. That means that while the _probability_ of future hazards will change in the future and is inferred by complex climate modeling, the _damage_ that those hazards do is assumed to be constant.

So we could look at historic fires in California and say that, when a fire is in a residential area, typically 80% of houses are destroyed. Rough modeling could tell us that, if there are 12 million homes in California, each with 1-in-1000 chance of being in an area hit by wildfires, and we have observed that historically 80% of homes in wildfire-hit areas are destroyed, then we can infer that California will loose about 9,600 homes in a given year. If, however, climate change makes a 1-in-1000 chance of fire increase to a 1-in-100 chance, that would be 96,000 homes destroyed.

In reality, the damage estimation process is much more complicated. For one, most hazards are modeled in terms of both _probability_ and _intensity_. For example, at a given location, a hundred-year flood (i.e. a flood event that has 1 in 100 chance of being equalled or exceeded in a given year) could be 1 foot, but a thousand-year flood could be 10 feet. For hurricanes, there might be a 10% chance of a category 1 (74 mph) hurricane, but a 1% chance of a category 5 (157+ mph) hurricane. So damage functions must be able to predict different levels of damage at different intensities, whether intensity is measured in terms of depths, wind speeds, temperatures, hazard duration, etc.

### Accounting for uncertainty

Another major complexity of damage estimation is that a good model will use different damage functions in different contexts. Building standards often vary widely across geographies, usually accounting for prevalent hazards, so houses in Miami will likely be more resistant to hurricane-force winds than houses in Seattle. A proper damage estimation methodology should account for that and use separate damage functions for houses in Miami vs Seattle.

Another way damage functions can vary is by type of structure, with apartments, residential homes, factories, schools, stadiums, etc., all being damaged differently by a flood of the same depth. A good model of future damages will take all these variables into account, which is why we account for both geography as well as asset type in our Value-at-Risk estimations, with 36 different damage functions for various asset types.

While these methods can give us state-of-the-art estimates of future climate change impacts, it is important to recognize that these estimates come with uncertainty, and accounting for this uncertainty is necessary to create reliable models. Indeed, there is uncertainty in nearly every step of the process. In the first step of climate simulation asking, i.e., how hot will the oceans be in 2050? - different GCMs give different predictions, creating one source of uncertainty.

Following that, converting future climate conditions into hazard probabilities - how likely will a category 3 hurricane be in 2050, given that oceans are 3 degrees C warmer? Finally, there is uncertainty in the damage estimation - what kind of damage does a category 3 hurricane do? This is why most approaches to Value-at-Risk estimation use simulations of thousands of potential futures, under varying assumptions of climate change, hazard frequency, and hazard damages.

### Conclusion

Organizations across every sector struggle with transforming the complexity and uncertainty of climate science into meaningful business metrics and applied industrial practices for things like risk management, asset valuation, and risk pricing. Bridging this gap between science and business is one of the greatest challenges we face as we seek to adapt to a rapidly changing climate.

Using these methodologies and properly accounting for uncertainty, we at Sust Global can give precise and scientifically-validated estimates of the kind of risks your business assets will face under climate change.

* * *

**About the author:** Matt Cooper is the Senior Data Science Engineer at Sust Global, where his work runs the gamut from engineering data pipelines to thinking critically about risk models to improving Sust Global's platform. Before joining our science and product team, Matt was a Data Science Postdoc that Harvard School of Public Health, where he researched the effects of heatwaves and droughts on food security and health. Matt is passionate about making falsifiable predictions about the future, and using new evidence to update his mental and computational models.

_At_ [_Sust Global_](https://www.sustglobal.com/)
_, we are on the mission to transform the latest in machine learning, remote sensing and frontier climate science into the intelligent climate data infrastructure that organizations need to thrive. If_ _you would like to learn more about our financial loss modeling capabilities, fill out the form below and a member of the team will be in touch shortly._

Cookie consent
--------------

We use cookies to give you the best online experience. Please let us know if you agree to all of these cookies.

**Analytics**

Accept all Decline