# Methodology & Processes in Wind Forecasting

**Source:** https://pivotal180.com/wind-forecasting-video

---

[Skip to content](https://pivotal180.com/wind-forecasting-video/#fl-main-content)

Methodology & Processes in Wind Forecasting
===========================================

By Daniel Gross | July 14, 2020

**Methodology & Processes in Wind Forecasting**
-----------------------------------------------

This is an extract from our [Renewable Energy Project Finance Modeling Course](https://pivotal180.com/courses/renewable-energy-project-finance-modeling/)
.

**Video Transcript** 

This lesson covers the methodology and process that’s used by wind engineering firms when forecasting a project net capacity factor. The forecast is important to a financial modeler because it’s the source of the assumptions that we use about the energy output of the project to calculate the revenue for a project we need to predict the number of megawatt hours that the wind farm is going to produce in a given period of time and this process is exactly how the engineers come up with that prediction.

The standard forecasting methodology involves five steps, measure, correlate, predict, optimize and sensitize, but more simply the methodology is generally known as MCP, Measure Correlate Predict. As we walk through this MCP process, we’ll keep you oriented by using call-outs up here. And those call outs will indicate which step we’re on.

So let’s get started with the first step, with measurement. This is an image of a meteorological mast, which is commonly called a met mast. It’s basically just a tall pole supporting different kinds of sensors at different elevations. Long before a project reaches financial close and begins construction. The developer will usually install a met mast to collect weather data on the proposed project site. While some met masts only hold measurement equipment to the very top. It’s quite common for certain sensors to be placed at three different Heights on the mast. Ideally you want to collect wind data at or near the plant hub height of the wind turbine, but it’s possible to interpolate or extrapolate if the mast and the turbine hub are at different Heights. It’s also valuable to collect data at the the height where the blade tip is closest to the ground. And this is because the blades on modern wind turbines are often over 45 meters in length or 148 feet. And the wind characteristics are different at different elevations due to a phenomenon known as wind shear.

Just so you know the latest generation offshore wind turbines have blades in excess of 100 meters or 328 feet for those living in the US. So the rotor is the equivalent of two football fields suspend in air spinning.

Oh my God, that’s huge. Haydn, sometimes I think you tell me things just to make me feel even shorter than I already am. Don’t forget I have feelings too.

Now let’s take a closer look at the instruments that sit on a met mast. This is called an anemometer. It’s a very simple device. It has three cups that are attached to a vertical shaft, and it spins whenever the wind blows because at least one cup is always facing into the wind. The speed of each rotation enables the device to measure the horizontal wind speed in meters per second, or in miles per hour. If you’re in one of the three countries that still refuses to adopt the metric system,

Really no metric system, come on, join the modern world already.

This is a wind vane, essentially a fin attached to a vertical shaft, which pivots across all 360 degrees of a compass to measure the direction from which the wind is blowing. In addition to the anemometer and the wind vane, met masts, usually hold other devices like a thermometer to measure temperature and a barometer to measure air pressure and sensors for relative humidity. Temperature, pressure, and humidity data is necessary to calculate the density of the air, which is important because denser air carries more power. So if the air is less dense at high altitudes, does that mean that wind turbines would have less output the higher they are installed above sea level? That’s great insight. A wind turbine up high in the Rocky mountains would generate significantly less energy than a turbine installed in the lowlands of Holland. Even if the wind speed and the temperature are identical on both sites. All of the devices on a met mast are attached to a data logger, which typically records the data in 10 minute increments. The raw data is then fed into a computer model, which generates outputs such as the mean and standard deviation of wind speed, the wind direction, the turbulence, and the maximum gust observed during the measurement period.

So Dan, how many met masts are required for a single wind project?

Good question, in an ideal world, you’d collect data at the location and hub height of every proposed wind turbine, but we don’t live in an ideal world and we don’t have an unlimited budget for data collection. So we do the best that we can within reason. The number of masks required really comes down to the size of the project and the complexity of the terrain, where the project is going to be built. In areas with Hills and valleys and Ridge lines. You’ll need to install more met masks because the wind characteristics can vary significantly over small distances. So with highly complex topography, I’d probably feel comfortable with about two kilometers of distance between a wind turbine and a met mast data collection site. But with very simple terrain, I’d probably be comfortable with about 10 kilometers of distance, but these are just my own basic rules. Just promise me that you won’t rely on my judgment here. Always hire an expert in wind forecasting.

Don’t worry, I’d never trust him with something like this, or actually with pretty much anything else that involves math. It’s just too important to risk getting wrong.

I find your lack of faith disturbing. At least I gave thoughtful guidance. A lot of people say use three met masks and they leave it at that.

No, I trust you a judgment most of the time. So how long would you recommend that data be collected from the met mast?

Project developers will typically collect data for a minimum of 12 months. As an investor I prefer to rely on a about three years of onsite measurement, and I feel much better if there’s even more.

Me too, I mean, I’ll take five years if I can get it.

Once we’ve collected measurements, we need to find a longterm reference data set that has a high correlation to the short term data observed on our project site. Typically the data used for correlation is from airports or from meteorological stations administered by the national weather service and while you might expect the strength of the correlation between the reference site and the target site to be a function of how close they are geographically, that’s actually not always the case. If there’s a big mountain between the project site and the nearest weather station, those two locations may have entirely different wind regimes. So it’s important to acquire data from a variety of reference sites and then rely on the statistical analysis to tell you which one is the best match.

Wind engineers have to do a lot of work to achieve a strong correlation. It’s not as simple as running a linear regression of two datasets. It’s common to divide the distribution of wind speed observations from the met masts into a series of what are called bins based upon the direction from which the wind was blowing. And then each directional bin is separately analyzed against the corresponding directional bin from the reference dataset and maybe time lags can be introduced between the project site and the reference site to compensate for the time that it takes for the wind to propagate from one location to the other. Sometimes averaging the data over different time intervals can also improve the correlation. 10 minute intervals may correlate nicely for one project while six hour intervals might correlate well for another. Basically you just wanna do whatever it takes to find the strongest correlation possible.

In the future I suspect that neural networks and machine learning will actually enhance our ability to find correlations by incorporating things like seasonal adjustments or nonlinear and data pairs from more than one reference site.

Since we’re going to rely on that correlation to forecast the amount of energy generated by our project, it’s probably important to look at the correlation coefficient. So Dan, as we try to R squared value, we need to achieve for the analysis to be reliable?

You should feel good about the quality of the relationship to the reference site if the R squared value is above 0.8 and you should feel very good about an R squared above 0.9 at lower R-squared values, you risk overestimating the amount of wind power that can be produced by the project, and that can have disastrous implications on your financial returns.

So where do people tend to get it wrong?

There are two areas where I’ve seen investors get very badly burned from this process. The first is poor correlation to a longterm reference dataset. This can happen when the onsite data collection is for too short a period of time and ultimately it proves to be unrepresentative. I was serious when I said that I like to see three years of onsite data collection and a high R squared value. As an investor it’s usually better to walk away than to try to convince yourself that questionable wind forecasting is good enough.

The second major failure that I’ve seen is on sites with complex topography, unless the terrain is flat, don’t assume that all of the turbines will correlate equally well to the longterm reference data. So don’t be cheap on data collection. You’re doing yourself a tremendous disservice, unless you set up more met masts to make sure that you understand the variation in the wind characteristics across the entire project site. Using software, the wind engineer develops an equation that characterizes the relationship observed during the relatively short period of overlap between the reference site and our target project site. Wind at the met mast is a function of wind at the reference site and from this function, we can use longterm data from the reference site to extrapolate the wind characteristics that we would expect to observe at our wind project over a long period of time on our site. What do I mean by long term, this would typically be for 10 years of data from the national weather station.

If we take that longterm forecast of wind speed at our project site and plot a histogram, we can see the amount of time that the wind is forecast to blow at different wind speeds over the course of an average year. In this graph along the horizontal axis is wind speed measured in meters per second. and along the vertical axis is time.

This looks weird. Something’s not normal.

You’re probably accustomed to seeing the bell shaped curve of a normal distribution function with two symmetrical tales, but as you can see, wind speed is not normally distributed. There is a long tail off to the right indicating that we anticipate very high wind speeds for only a small fraction of the year. We anticipate more moderate wind speeds for a larger fraction of the year. Of course, it’s absolutely impossible for the wind speed to be less than zero meters per second. So the distribution has no tail off to the left because the wind speed can’t go below zero. A distribution with this shape is called a viable distribution. Here’s another way of thinking about this chart, that sum total of the area under the wind speed curve is equal to the number of hours in the period. So if the period is one year, the area under that curve equals the number of hours in a year or 8760.

To forecast the number of megawatt hours of energy generation from our wind turbine. We need to understand the relationship between the wind speed and the capacity of the wind turbine to generate energy. And this information is contained in a power curve specific to each model of wind turbine.

Dan, I know that I’m supposed to pretend, that I don’t know what a power curve is so I can ask you to explain it to me, but I studied to be an engineer. So I’m just going to present the section.

A power curve is a graph showing the capacity of a wind turbine to generate energy at different wind speeds. As you can see, the wind speed is shown on the horizontal access measured in meters per second, and generation capacity is shown on the vertical access in kilowatts by taking the forecast of wind speed as measured an hours per year and aligning it with the power curve as measured in kilowatts, we can easily forecast the total kilowatt hours per year that can be generated by the turbine. Here’s the idea. Imagine that we build a wind turbine at the exact same location as the met mast from our forecast. If the wind is expected to blow for one hour at 12 meters per second, the turbine would generate 1.5 megawatt hours of electricity. So then we just repeat the process over the course of the entire year, we divide up the wind speed distribution into different bins showing how many hours per year the wind is expected to blow within each range of speed. And then we run each bin through the power curve to calculate megawatt hours and if we do that for each bin, we end up with a forecast for annual energy output, which can be used in the financial model

Before we move on I’d like to point out a couple of things you should know about the power curve, which may help you better understand how much energy you can expect to get from a wind turbine. The first is this point right here called the cut-in speed. This is the speed at which the turbine starts generating power. The cut-in speed is especially important in low wind sites because you need to select a turbine that captures as much wind as possible. In recent years reductions in cut-in speed have been achieved largely through increasing the length of the blade. Longer blades increase the rotor swept area. That’s the circle of air from which the turbine captures energy. While longer plates don’t make the turbine spin faster. They extract more energy from the wind. Increasing the height of the tower can also increase the energy output from low wind science because wind speeds tend to be faster at higher elevations.

The second important point on this power curve is where it flattens out starting at 11 or 12 meters per second, this flat part corresponds to the maximum capacity of the generator, which is called the nameplate capacity for the turbine. As you can see, this turbine only operates at its nameplate capacity at relatively high wind speeds on low wind speed sites, a lower cut-in speed, maybe much more valuable to the project than a higher nameplate capacity.

Well, Dan, stop, let me continue with the technical presentation. You know I’m an engineer, right?

Yes, Haydn you’ve told me you’re an engineer about a thousand times before

Finally, where the power curve ends is the cut-out speed of the turbine. If wind speeds exceed about 25 meters per second, for this turbine model, the equipment needs to be shut down for safety and you won’t get any power generation at all. The takeaway here is that even though this turbine has a nameplate capacity of 1.5 megawatts, it only operates at 1.5 megawatts. When the wind speed is between 11 and 25 meters per second, which is a relatively small fraction of the year. For much of the time, the turbine is operating below 1.5 megawatts. And a lot of the time, the turbine isn’t generating energy at all. Each turbine model has pros and cons and only a subset of the turbines on the market will be suitable for the specific characteristics of our proposed development site. Once the distribution of the wind speed is forecasted, the developer will ask the wind engineer to evaluate multiple turbine models. The best economic result is not always from the turbine, which generates the most energy. You need to weigh the cost of the equipment against the forecast energy output, and then optimize the financial return subject to the constraints of the site.

Let’s recap quickly what we’ve done so far. First, we took measurements at the proposed project site for several years in order to understand the wind speed and other characteristics. Then we compared some key characteristics to a reference data set, to find longer term data that was highly correlated to our sample. And then we used the correlated data to predict the longterm annual distribution of wind speed on our site, which approximated that viable distribution. And finally, we modeled the energy output for a variety of potential turbine models in order to find the optimal equipment for the project, given the cost and other constraints.

So what’s next?

To estimate energy generation across the whole site we need to look beyond the hypothetical turbine on the footprint of the met mast and understand the impact of site topography and roughness. Here you see a topographical map of our project in which the contours represent elevation beside it is a wind speed map in which the contours represent average wind speed. Wind is just like any other fluid. So the wind speed map is created with a fluid dynamics simulation model, in our experience this mapping process can be a tremendous source of forecasting error. So as the financial modeler, you may want to consider running more extreme downside sensitivity cases on projects with complex terrain.

Pushing forward once we have a model for showing wind speeds across the entire site, we can use that model to optimize the placement of the turbines subject to site constraints such as accessibility.

Wind direction is one of the most important variables in turbine layout to minimize wake effects between turbines, developers place turbines so that they won’t be directly behind each other when the wind is blowing from its predominant direction. So you can think of it like the wake of a boat, even in rough water. The area in the motorboats wake is typically quite calm and this same phenomenon happens with wind turbines. So relative positioning of those turbines is extremely important. One of the best ways to visualize the wind direction is called a wind Rose. A wind Rose is a map of the direction, frequency and speed of the wind typically measured over the course of a year. The compass Rose is divided into 16 slices with the length of each spoke, telling us the percentage of time, the wind is blowing from a given direction. The colors on each spoke indicate the wind speed. And so these concentric circles each represent a percentage of the year telling us what percent of the time the wind is blowing from a certain direction at a certain speed. For instance, in this example, we can see that the wind blows from the Southwest for about 12% of the time. And based on the color legend, we can see that this Southwesterly wind is between 8.8 and 11.1 meters per second, for only one or two percent of the time, the wind engineer will use the topographic map, the wind speed map, and the wind rose to experiment with different placements of the turbines on the site until arriving at something that seems optimal. But before we can put a certain number of megawatt hours per year into the financial model, we need to refine the gross estimates of energy generation to net numbers after considering a variety of loss factors,

The adjustments from gross generation to net generation will be provided by the wind engineer. And these adjustments might include items such as topography of the site, wake effects, concept court availability, which we will talk about later in the course, icing conditions, performance of the power curve and curtailment of the grid. One thing to keep in mind with all of these adjustments is that the loss effects are multiplicative, not additive. This is because they are independent events that can occur simultaneously. For example, the wind may be blowing from the direction that causes the most extreme wake effects, but it won’t reduce the net generation if the turbine is coincidentally down for routine maintenance at the same time, therefore you should take each loss factor, subtract the percentage from 100% and then multiply all the results together to see the overall adjustment from gross to net generation.

All right, so now we have completed each step of the measure, correlate, predict process, and we’ve also optimized the layout of our wind turbines. Additionally, we’ve applied the adjustment factors that took us from gross generation to net generation. And now finally, we have a net capacity factor or a net number of megawatt hours that we can put into our financial model if only it were that simple because our forecast was based upon a regression analysis of longterm wind data.

We know that no two years in the past looked exactly the same and therefore we don’t have a precise forecast for how many megawatt hours we will get from our project every year. Instead we have a probability distribution function showing a range of potential outcomes.

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fwind-forecasting-video%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fwind-forecasting-video%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fwind-forecasting-video%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#b18ed3ded5c88cd9c5c5c1c29482f09483f79483f7c1d8c7dec5d0dd8089819fd2dedc9483f7c6d8dfd59cd7dec3d4d2d0c2c5d8dfd69cc7d8d5d4de9483f7)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Daniel Gross

[https://www.linkedin.com/in/daniel-gross-081237b/](https://www.linkedin.com/in/daniel-gross-081237b/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/wind-forecasting-video/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA