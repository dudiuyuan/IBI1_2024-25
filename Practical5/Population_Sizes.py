uk_countries_population=[57.11,3.13,1.91,5.45]
china_province_population=[65.77,41.88,45.28,61.27,85.15]
import matplotlib.pyplot as plt     #importing the matplotlib 
uk_countries= ['England', 'Wales', 'Northern Ireland', 'Scotland']
china_province=["Zhejiang","Fujian","Jiangxi","Anhui","Jiangsu"]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.pie(uk_countries_population, labels=uk_countries,autopct='%1.1f%%',startangle=90)
ax1.axis('equal')
ax2.pie(china_province_population, labels=china_province,autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
plt.show()