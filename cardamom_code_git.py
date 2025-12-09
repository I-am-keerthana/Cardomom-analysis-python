from selenium import webdriver
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import calendar
import numpy as np

from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

DRIVER_PATH='C:\\Users\\keerthana\\Downloads\\chromedriver_win32\\chromedriver\\Downloads\\chromedriver_win32\\chromedriver.exe'
final_list=[]
url = 'http://www.indianspices.com/marketing/price/domestic/daily-price8de9.html?v=archive&category=small'
driver.get(url)
new_url=url
while True:
    try:
    
        driver.get(new_url)
        date=driver.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div[2]/div[3]/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]')
        auctioneer_name=driver.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div[2]/div[3]/div/div[3]/div/div/div[4]/table/tbody/tr/td[3]')
        quantity_sold=driver.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div[2]/div[3]/div/div[3]/div/div/div[4]/table/tbody/tr/td[5]')
        price=driver.find_elements_by_xpath('/html/body/div[2]/div/div[3]/div[2]/div[3]/div/div[3]/div/div/div[4]/table/tbody/tr/td[8]')
        for j in range(len(auctioneer_name)):
            temp_data={
               'Date':date[j].text,
               'auctioneer':auctioneer_name[j].text,
               'Quantity':quantity_sold[j].text,
               'price':price[j].text}
            final_list.append(temp_data)
        #print(final_list)
        df_frame=pd.DataFrame(final_list).drop_duplicates()
        n=1
        df2=df_frame.iloc[n:]
   
        df2.to_excel('selenium_card.xlsx',index=False)
   
        driver.find_element(By.CLASS_NAME,'pager-next').click()
        present_url=driver.current_url
        new_url=present_url
    except NoSuchElementException:
        break
        print("end of the page")
all_data=pd.read_excel('selenium_card.xlsx')
all_data.head()
all_data['month']=all_data['Date'].str[3:5]
final_year=all_data['Date'].str[6:10]
#df_year=pd.DataFrame(final_year)
#print(type(df_year))
final_months = all_data['month'].astype('int32')
#print(final_months)
months_names= final_months.apply(lambda x: calendar.month_abbr[x])
month_array=np.array(months_names)


final_revenue=(all_data['price']/all_data['Quantity'])*1000
revenue_array=np.array(final_revenue)


final_quantity=all_data['Quantity']

final_price=all_data['price']
auctioneer=all_data['auctioneer']
hhh=all_data.groupby(final_year)['auctioneer']
#print(type(hhh))



all_data.groupby(final_year)['Quantity'].sum().plot(kind='bar',yticks=[],color="pink",xlabel="years",title="Overall Yearwise Quantity sold")

pvt=pd.pivot_table(all_data,columns=final_year,index=months_names,aggfunc='sum',values='Quantity')
pvt.plot(subplots=True,use_index=True,yticks=[],xlabel='comparision of Yearly monthwise Quantity of cardomom sold ')
xpoints=np.array(final_quantity)
ypoints=np.array(final_price)
#fig = plt.subplots(figsize =(7, 7))


fig,ax=plt.subplots(1,1)
ax.hist(xpoints,color="yellow")
ax.set_title("Max and Min Quantity sold overall")
ax.set_xlabel("Quantity of cardomom sold")
plt.show()
all_data.groupby(final_year)['price'].sum().plot(kind='line',xlabel='prices',ylabel='sales',color="green")
plt.show()
all_data.groupby(months_names)['Quantity'].sum().plot(kind='bar',yticks=[],xlabel="Months",color="orange",title="Overall Monthwise Quantity sold")




               
        

        

    
    

