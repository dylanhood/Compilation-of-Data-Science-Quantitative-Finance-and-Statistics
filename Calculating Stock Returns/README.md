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
<b> var_p = np.dot(np.transpose(weights), np.dot(vcv_matrix, weights))</b>
<div>&nbsp;</div>
  
  
### What does the last line above do?
  
  
<div>&nbsp;</div>
<b>If I'm not mistaken, np.transpose() will convert weights from rows to columns and columns to rows. The smaller np.dot() will matrix multiply (rows to columns and columns to rows) vcv_matrix & weights together.
Then the biggest np.dot() will matrix multiply the np.transpose and the smaller np.dot together and produce a result.



-------------------------------------------------------------------------------------------------------------------------------------------------------------

<br></br>

-------------------------------------------------------------------------------------------------------------------------------------------------------------

## Acknowledgements

<b>Fervent Learning</b> - [Udemy Course](https://www.udemy.com/course/data-driven-investing-with-python-financial-data-science/)



-------------------------------------------------------------------------------------------------------------------------------------------------------------
