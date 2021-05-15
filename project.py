import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

#Let's have a look at the data
df_listings = pd.read_csv('./listings.csv')
df_listings.head()
df_reviews = pd.read_csv('./reviews.csv')
df_reviews.head()
df_calendar= pd.read_csv('./calendar.csv')
df_calendar.head()


no_nulls=set(df_listings.columns[df_listings.isnull().mean() == 0 ])
print(no_nulls)

#The listing with most reviews 

listings=df_reviews['listing_id'].value_counts().reset_index()
listings.rename(columns={"index":"id",'listing_id':'count'},inplace=True)
print(listings)
df2=df_listings[['id','name']]
print(df2)

result=pd.merge(df2,listings,on="id")
print(result.sort_values(by=['count'], ascending=False))


#Max Price variation

# lets remove the null values first
df_price=df_calendar[df_calendar['price'].notna()]
print(df_calendar.shape[0])
print(df_price.shape[0])

df_price=df_price.drop(['available', 'listing_id'], axis=1)
df_price['price'] = df_price['price'].str.replace('$','')
df_price['price'] = df_price['price'].str.replace(',','')

df_price[['price']] = df_price[['price']].apply(pd.to_numeric)
df_price=df_price.sort_values(by=['date'], ascending=True)
df_price_most_busy=df_price.loc[df_price.groupby('date')['price'].idxmax()]
print(df_price_most_busy)
df_price_most_busy.plot(x="date",y="price", kind="line",figsize=(400, 100),color='red')
plt.xlabel("Date Range")
plt.ylabel("Price ( $)")
plt.legend(labelspacing = 13)
plt.show()

#most busisiest day

df_busy=df_calendar[df_calendar['price'].isna()]
df_most_busy=df_busy['date'].value_counts()
df_most_busy.plot(figsize=(200, 100),color='blue', kind="bar")
plt.xlabel("Date Range")
plt.ylabel("Number of Bookings")
plt.legend(labelspacing = 13)
plt.show()

#taking stock of property type
df_listings_propety_type_count=df_listings['property_type'].value_counts()
print(df_listings_propety_type_count)
df_listings_propety_type_count.plot(kind="pie",figsize=(50,50))
plt.show()
