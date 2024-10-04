# MP_BI_Tobias

## MP4:

- Which machine learning methods did you choose to apply in the application?

I used Decistion Tree (with different n_components), Naive Bayes, Random Forest for classification (Supervised training) and a KMeans method for clustering (Unsupervised training).

---
- How accurate is your solution of prediction?

All my classification models had an accuracy score around 8.2 - 8.5. Neither seemed to be significantly better than the other, although the models where only 3-4 features where included instead of almost all the features, were generally scoring around 8.4 - 8.5. Also the Random Forest model had a high score of around 8.5. 

My confusion matrices didn't match the accuracy score. As far as I can tell it's because of the class imbalance in the Attrition feature. 

---
- Which are the most decisive factors for quitting a job?

From the correlation matrix it seems to be working overtime, being single and number of total working years. Working overtime, being single and not having worked that many years will make a little
more likely that an employee quits her job

---
- Which work positions and departments are in higher risk of losing employees?

From the correlation matrix it seems to be the position as Sales Representative and the Sales Department which are in higher risk of losing employees


---
- Are employees of different gender paid equally in all departments?

??? [Didn't have time to investigate this]

---
- Do the family status and the distance from work influence the work-life balance?

??? [Didn't have time to investigate this. The correlation matrix might say a little about this]

---
  
- Does education make people happy (satisfied from the work)?

??? [Didn't have time to investigate this. The correlation matrix might say a little about this]

---
- Which were the challenges in the project development?

It took me a long time to find out why the accuracy scores and the confusion matrices didn't match and I'm not totally sure the class imbalance is the reason why.
I'm unsure about all the models I've used
  

---
---
---
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
