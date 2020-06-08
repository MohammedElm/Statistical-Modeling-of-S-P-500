# Statistical-Modeling-of-S-P-500


In this report, we will work on S&P 500 index.  Using YahooStockDataSource Python module, we scrapped its values from 2000 to 2019.


First, we will apply Linear Time Series and GARCH model to its attribute:Open. We will implement a methodology to fit and to find the best ARIMA model by minimizing AIC over a non-trivial combinations of parameters.


Then, we will use this selected ARIMA model to fita GARCH model. This methodolody gives residuals that looks like descrete white noise and models well the Volatility Clustering phenomenon. 


Second, we will implement a simple trading strategy using ARIMA-GARCH models andcompare its results to a naive "Hold and Buy" strategy. This methods seems to perform well on periods of high volatility. This is due to the very definition of GARCH model which takes into account the conditional volatility phenomenon.


Finally, we will work on the daily Volumes of trades associated to S&P 500. We will fit a Univariate Hawkes model on Extreme volumes of trading events. The fitting will be usedby the classical MLE approach. We will also validate our modeling using the Ogata’s test onresiduals (By QQ plot of residuals Vs Exp(1) distribution)
