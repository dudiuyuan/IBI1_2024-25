# save the population sizes of the countries in the UK and the provinces in China in two lists.
# Sort the lists in descending order and print them.
# import matplotlib.pyplot as plt
# generate two sub windows
# Create a pie chart for the population sizes of the countries in the UK and the provinces in China.
# The pie chart should have the names of the countries/provinces as labels and the population sizes as the values.

uk_countries_population=[57.11,3.13,1.91,5.45]
china_province_population=[65.77,41.88,45.28,61.27,85.15]
st_uk=sorted (uk_countries_population,reverse=True)
st_ch=sorted (china_province_population,reverse=True)
print(st_uk)
print(st_ch)
import matplotlib.pyplot as plt     #importing the matplotlib 
uk_countries= ['England', 'Wales', 'Northern Ireland', 'Scotland']
china_province=["Zhejiang","Fujian","Jiangxi","Anhui","Jiangsu"]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.pie(uk_countries_population, labels=uk_countries,autopct='%1.1f%%',startangle=90)
ax2.pie(china_province_population, labels=china_province,autopct='%1.1f%%', startangle=90)
plt.show()
