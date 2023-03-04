# What's In This Folder?
<br></br>

-------------------------------------------------------------------------------------------------------------------------------------------------------------

## Calculating Stock Returns Jupyter Notebook
<br></br>
<b>The Calculating Stock Returns Jupyter Notebook is a Jupyter Notebook that calculates stock returns for Virtu Financial.<b>
  
-------------------------------------------------------------------------------------------------------------------------------------------------------------

<br></br>

-------------------------------------------------------------------------------------------------------------------------------------------------------------

## Estimating Portfolio Risk (Multiple Assets).py
<br></br>
<b>The file estimates portfolio risk (multiple assets) - using a list of weights and the df.cov() method to estimate the covariance matrix as:</b>
<div>&nbsp;</div>
<b>vcv_matrix = returns_df.cov() <- This pretty much just does returns_df = prices_df.pct_change(1)</b>
<div>&nbsp;</div>
<b> Then the .py file calculates the variance of a k asset portfolio as:</b>
<b>var_p = np.dot(np.transpose(weights), np.dot(vcv_matrix, weights))</b>
<div>&nbsp;</div>
  
  
### What does the last line above do?
  
  
<div>&nbsp;</div>
<b>If I'm not mistaken, it will multiply the np.dot() for vcv_matrix & weights together and then add it to weights in np.transpose(). 
Then the biggest np.dot() will multiple the two together and produce a result.



-------------------------------------------------------------------------------------------------------------------------------------------------------------
