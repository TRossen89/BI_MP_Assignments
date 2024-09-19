# MP_BI_Tobias
---
## MP3:  

### Types of regression:
- I have trained and tested a simple linear regression model with sqft_living as the feature/the x
- I have then trained and tested a couple of multiple linear models with different train sets (with different house features, with and without outliers, one hot encoding and/or scaling)
- I have also trained and tested a polynomial regression model without the least informative features, with one hot encoding of zipcode but with no scaling of the values

I have stored 2 models which were the best fitted models:  
1) A multiple linear model where I have removed features with multicollinearity, used one hot encoding on zipcodes and I have scaled all the values
2) The polynomial model

I did create a better fitted multiple linear model where I calculated and removed outliers of some features, but the outliers where also  
removed in the test set, which I think is misleading because in the real world there is outliers

---
### The challenges:

- One challenge was to figure out how the date of the house sales could be used. I didn't manage to find a solution to that
- Another challenge was to figure out whether the outliers should be included or not and what outliers I should remove if I should remove any
- A third challenge was that when I scaled the values for my polynomial regression model the R-Squared values was well above 1, so I guess something has gone wrong and I don't know what.
  But the polynomial model was the best fitted model when I didn't scale the values

  
---
 ### Accuracy of my solutions:

 - When tested on the test set, the multiple linear model that I stored, got an R-Squared of: 0.796
   which means r = 0.892
 - When tested on the test set, the polynomial model that I stored, got an R-Squared of: 0.850
   which means r = 0.922

   
---

### Further improvements:

- I guess I could do some feature engineering with the date feature. For example I could extract the months and see if there is some linear or non-linear correlation
  between the price and the month a house is sold
- I haven't used the lat or long. I don't know if they could be engineered so that they could give some information of the prices
- Maybe I could do some feature engineering with the yr_built and date feature. For example I could calculate the age of the houses from the year-built and date features
  and create a feature called age_of_house which could be a numeric value indicating how many days old the house is 
