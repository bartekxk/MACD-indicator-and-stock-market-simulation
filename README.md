<h1>Project description</h1>

The project aimed to write a program that will try to get the most profit from the stock market using the MACD stock index. The program calculates relevant data, creates charts, and then simulates purchases / sales, suggesting the calculated index and using the created algorithm.

<h1>Program structure</h1>

The program was written in Python. At the beginning of the program, two constans MONEY were created - the amount of the initial money to be simulated and DATA_SIZE - the number of samples to be processed. The csvFile variable has been downloaded data from the csv file containing historical data from the stock exchange. The program has created a class that supports the entire problem named MACD. The following class methods are described below:
<ul>
<li>__init__ - class constructor, get data from the csv file as a parameter;</li>
<li>rollingAverage - calculating the moving average, get as parameters: source column, target column, period and size of data;</li>
<li>macd - calculating macd from previously prepared data, get the size of the data as a parameter;</li>
<li>print - print out data and create and draw graphs on the screen;</li>
<li>calculate - performing the calculations we need (ema12, ema26, macd, signal), get the size of the data as a parameter;</li>
<li>simulate - simulation of sale and purchase on the stock exchange, get as the initial parameter the portfolio and the number of days;</li>
<h1>Calculations</h1>
In the program, it was necessary to calculate two rolling averages of periods 26 and 12 from the input data.
<img src="https://i.imgur.com/2UqEIZG.png">
Then calculate the MACD indicator, which is the difference:
<img src="https://i.imgur.com/Y6Cu96l.png">

And calculate the rolling average of MACD at 9 using the previous formula.

<h1>Purchase / sales strategy</h1>

The purchase and sale strategy adopted by me consisted of an appropriate reaction depending on the point where the indicator was cut. The more the signal is below zero, the more significant it is. With stable data, these locations range between -100 and 100, so when you cut in place = <- 100, we buy / sell for all the money / all shares, and at> = 100 we skip the signal. For this purpose, a ratio is calculated (accepting 1.0 for <= - 100 and 0.0 for> = 100):
ratio = ((0-place_curve) +100) / 200)
On the basis of which we calculate the amount we have to buy or sell.

<h1>Usability analysis</h1>
<img src="https://i.imgur.com/GXX363n.png">
<img src="https://i.imgur.com/Pu2DaEP.png">
<img src="https://i.imgur.com/kJ3l1aM.png">
<h1>Doubts and problems noticed</h1>

The algorithm I use together with the MACD indicator makes profits but they are small in long terms, and on the real stock exchange together with commissions could even bring losses.
The algorithm is quite stable for a longer time and we do not suffer too much loss or profits.
