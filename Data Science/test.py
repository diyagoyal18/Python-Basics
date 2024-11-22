•
Importing all the required libraries

Reading the city dataset file

Reading the global dataset file
Displaying the datasets:

Selecting the required global data frame

Checking the missing values;

Calculating the mean of the city dataset and filling the missing values :

DATA MERGING: Merge the city and global datasets on the 'year' column for direct comparison.

Calculating Moving Average for City and Global data

• Calculated the Moving Average (MA) for both city and global data by taking an interval of 15 years MA_city,MA_global=moving_average(city_data['clean_avg_temp'],new_global_df['Avg_temp'],15) df=pd.DataFrame({'year':np.linspace(1796,2013,len(MA_city)),'MA_city':MA_city}) df2=pd.DataFrame({'year':np.linspace(1796,2013,len(MA_global),dtype=int),'MA_global':MA_global})
•
Printing the new data-frame 2
• df2
•
Lengths of data
• len(MA_city),len(MA_global)
•
Plotting the original data of city
• sns.set_style(style='darkgrid')
• plt.figure(figsize=(16,10))
• plt.plot(city_data['year'],city_data['clean_avg_temp'],label='New Delhi average temperature change from 1796-2013')
• plt.xlabel('Year',fontdict={'size':25})
• plt.ylabel('Avg. Temperature',fontdict={'size':25})
• plt.legend(fontsize='xx-large')
• plt.title('Trend before calculating moving average',fontdict={'size':25})
• plt.show()
•
After calculating moving average for city
• sns.set_style('darkgrid')
• plt.figure(figsize=(20,10))
• plt.plot(df['year'],df['MA_city'],color='blue',label='New Delhi average temperature change from 1796-2013',marker='o',linestyle='dashed',markerfacecolor='black',linewidth=2,markersize=6)
• plt.xlabel('Year',fontdict={'size':25})
• plt.ylabel('Moving Avg. Temperature',fontdict={'size':25})
• plt.legend(fontsize='xx-large')
• plt.title('Trend after calculating moving average',fontdict={'size':25})
• plt.show()
•
Plotting the global original data
• sns.set_style(style='darkgrid')
• plt.figure(figsize=(16,10))
• plt.plot(new_global_df['Year'],new_global_df['Avg_temp'],label='Global average temperature change from 1796-2013')
• plt.xlabel('Year',fontdict={'size':25})
• plt.ylabel('Avg. Temperature',fontdict={'size':25})
• plt.legend(fontsize='xx-large')
• plt.title('Global Trend before calculating moving average',fontdict={'size':25})
• plt.show()
26 | P a g e
•
After calculating global moving average
• sns.set_style(style='darkgrid')
• plt.figure(figsize=(16,10))
• plt.plot(df2['year'],df2['MA_global'],label='Global average temperature change from 1796-2013',marker='o',linestyle='dashed',markerfacecolor='black',linewidth=2,markersize=5)
• plt.xlabel('Year',fontdict={'size':25})
• plt.ylabel('Moving Avg. Temperature',fontdict={'size':25})
• plt.legend(fontsize='xx-large')
• plt.title('Global Trend after calculating moving average',fontdict={'size':25})
• plt.show()
•
Is your city hotter or cooler on average compared to the global average? Has the difference been consistent over time?
• print ('The average temperature of New Delhi is {:.2f}°C'.format(city_data['clean_avg_temp'].mean()))
•
• print ('The average global temperature is {:.2f}°C'.format(new_global_df['Avg_temp'].mean()))
•
Differences of moving average temperature of New Delhi and Global from 1796 to 2013' df3=pd.DataFrame({'MA_city':MA_city,'MA_global':MA_global,'Difference avg temp':np.array(MA_city)-np.array(MA_global),'year':df['year']}) df3 plt.figure(figsize=(20,10)) plt.plot(df3['year'],df3['Difference avg temp'],marker='o',linestyle='dashed',markerfacecolor='black',linewidth=2,markersize=2) plt.xlabel('Years',fontdict={'size':25}) plt.ylabel('Difference between avg. temperature',fontdict={'size':15}) plt.title(',fontdict={'size':20}) plt.show()Differences of moving average temperature of New Delhi and Global from 1796 to 2013'
•
How do the changes in your city’s temperatures over time compare to the changes in the global average?
• fig=plt.figure()
• plt1=fig.add_subplot(211)
• plt2=fig.add_subplot(212)
• plt1.plot(df['year'],df['MA_city'],color='blue',label='New Delhi average temperature change from 1796-2013')
• plt2.plot(df2['year'],df2['MA_global'],color='r',label='Global average temperature change from 1796-2013')
27 | P a g e
• plt.xlabel('year',fontdict={'size':15})
• plt1.legend()
• plt2.legend()
•
What does the overall trend look like? Is the world getting hotter or cooler? Has the trend been consistent over the last few hundred years?
• sns.lmplot(y='MA_city',x='year',data=df,height=7,scatter_kws={'marker':0,'color':'indianred'},line_kws={'linewidth':1,'color':'blue'},order=2)
• plt.gca().spines['top'].set_visible(False)
• plt.gca().spines['right'].set_visible(False)
• plt.title('Trend Analysis of avg. temperature change in New Delhi',fontsize='xx-large')
• plt.xlabel('Year (1796-2013)',fontdict={'size':20})
• plt.ylabel('Moving Average Temperature',fontdict={'size':20})
• sns.lmplot(y='MA_global',x='year',data=df3,height=7,scatter_kws={'marker':0,'color':'green'},line_kws={'linewidth':1,'color':'blue'},order=2)
• plt.title('Trend Analysis of avg. temperature change Globally',fontsize='xx-large')
• plt.xlabel('Year (1796-2013)',fontdict={'size':20})
• plt.ylabel('Moving Average Temperature',fontdict={'size':20})
• plt.show()
•
How bad is the condition in New Delhi and globally?
• plt.figure(figsize=(20,10))
• plt.plot(df3['year'],df3['Difference avg temp'],linestyle='dashed',label='Difference between city and global avg. temperature')
• plt.ylabel('Difference between avg. temperature',fontdict={'size':20})
• plt.xlabel('Year',fontdict={'size':20})
• plt.legend(fontsize='xx-large')
• plt.title('Differences of moving average temperature of New Delhi and Global from 1796 to 2013',fontdict={'size':20})
• plt.show()
•
Differnces of moving average temperature of New Delhi and Global fig=plt.figure(figsize=(20,10)) ax=fig.add_subplot(111) ax.plot(df3['year'],df3['Difference avg temp'],marker='o',linestyle='dashed',markerfacecolor='black',linewidth=2,markersize=2) rect1 = matplotlib.patches.Rectangle((1808, 17.1),10,-0.49, color ='green',alpha=0.3) plt.xlabel('Years',fontdict={'size':25}) ax.add_patch(rect1) plt.ylabel('Difference between avg. temperature',fontdict={'size':20})
28 | P a g e
plt.title('Differences of moving average temperature of New Delhi and Global from 1796 to 2013',fontdict={'size':20}) plt.show()
•
New Delhi’s moving average temperature over recent 15 years
• fig=plt.figure(figsize=(20,10))
• ax=fig.add_subplot(111)
• plt.plot(df['year'],df['MA_city'],color='blue',label='New Delhi average temperature change from 1796-2013',marker='o',linestyle='dashed',markerfacecolor='black',linewidth=2,markersize=6)
• rect1 = matplotlib.patches.Rectangle((1993, 25.60),40,0.6, color ='red',alpha=0.3)
• ax.add_patch(rect1)
• plt.xlabel('Year',fontdict={'size':25})
• plt.ylabel('Moving Avg. Temperature',fontdict={'size':25})
• plt.legend(fontsize='xx-large')
• plt.title("New Delhi's moving average temperature (15 years)",fontdict={'size':25})
• plt.show()
•
Correlation Analysis:
• # Calculate the correlation between New Delhi and global temperatures
• correlation = merged_data['avg_temp_x'].corr(merged_data['avg_temp_y'])
•
• print(f"Correlation between New Delhi and Global Temperatures: {correlation:.2f}")
X = df.drop(columns='year', axis=1) Y = df['year']
TRAINING AND TESTING SETS IN RATIO 20:80 X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2) print(X.shape, X_train.shape, X_test.shape)
TRAINING AND TESTING SETS IN RATIO 30:70 X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=2) print(X.shape, X_train.shape, X_test.shape)
TRAINING AND TESTING SETS IN RATIO 30:70 X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=2) print(X.shape, X_train.shape, X_test.shape)
29 | P a g e
LINEAR REGRESSION : lr = LinearRegression()
lr.fit(X_train, Y_train) lr.score(X_train,Y_train)
lr_Y_pred = lr.predict(X_test)
POLYNOMIMAL REGRESSION: poly_reg = PolynomialFeatures(degree=2) poly_reg
#transforming the features to higher degree X_train_poly = poly_reg.fit_transform(X_train) #splitting the data plr_X_train, plr_X_test, plr_Y_train, plr_Y_test = train_test_split(X_train_poly, Y_train, test_size=0.2, random_state=2)
plr = LinearRegression() #model training plr.fit(plr_X_train,plr_Y_train) #model accuracy plr.score(plr_X_train,plr_Y_train)
plr_Y_pred = plr.predict(plr_X_test)
DECISION TREE REGRESSION: dtree = DecisionTreeRegressor() dtree
#model training dtree.fit(X_train,Y_train) #model accuracy dtree.score(X_train,Y_train)
dtree_pred = dtree.predict(X_test)
RANDOM FOREST REGRESSION: rf = RandomForestRegressor(n_estimators=100) rf
#model training
30 | P a g e
rf.fit(X_train,Y_train) #model accuracy rf.score(X_train,Y_train)
rf_pred = rf.predict(X_test)
MODEL EVALUATION: #evaluation Metrics # Mean Absolute Error (MAE) mae_linear = mean_absolute_error(Y_test, lr_Y_pred) mae_polynomial = mean_absolute_error(plr_Y_test, plr_Y_pred) mae_tree = mean_absolute_error(Y_test, dtree_pred) mae_rf = mean_absolute_error(Y_test, rf_pred) # Root Mean Squared Error (RMSE) rms_linear = mean_squared_error(Y_test, lr_Y_pred, squared=False) rms_polynomial = mean_squared_error(plr_Y_test, plr_Y_pred, squared=False) rms_tree = mean_squared_error(Y_test, dtree_pred, squared=False) rms_rf = mean_squared_error(Y_test, rf_pred, squared=False) # R-squared (R2) r2_linear = r2_score(Y_test, lr_Y_pred) r2_polynomial = r2_score(plr_Y_test, plr_Y_pred) r2_tree = r2_score(Y_test, dtree_pred) r2_rf = r2_score(Y_test, rf_pred) # Mean square error mse_linear = mean_squared_error(Y_test, lr_Y_pred) mse_polynomial = mean_squared_error(plr_Y_test, plr_Y_pred) mse_tree = mean_squared_error(Y_test, dtree_pred) mse_rf = mean_squared_error(Y_test, rf_pred)
# Print or use the metrics as needed print("Mean Absolute Error:") print(f"Linear Regression:", {mae_linear}) print(f"Logistic Regression:", {mae_polynomial}) print(f"Decision Tree:", {mae_tree}) print(f"Random Forest Tree:", {mae_rf}) print("\nRoot Mean Squared Error:") print(f"Linear Regression:, {rms_linear}")
31 | P a g e
print(f"Logistic Regression:", {rms_polynomial}) print(f"Decision Tree:, {rms_tree}") print(f"Random Forest Tree:", {rms_rf}) print("\nR-squared (R2):") print(f"Linear Regression:, {r2_linear}") print(f"Logistic Regression:", {r2_polynomial}) print(f"Decision Tree:, {r2_tree}") print(f"Random Forest Tree:", {r2_rf}) print("\n Mean square error:") print(f"Linear Regression:, {mse_linear}") print(f"Logistic Regression:", {mse_polynomial}) print(f"Decision Tree:, {mse_tree}") print(f"Random Forest Tree:", {mse_rf})
# Assuming you have performance metrics for each algorithm[20%test] r2_scores = [r2_linear, r2_polynomial, r2_tree, r2_rf] mae_scores = [mae_linear/100, mae_polynomial/100,mae_tree/100,mae_rf/100] mse_scores = [mse_linear/10000,mse_polynomial/10000,mse_tree/10000 ,mse_rf/10000] rmse_scores = [rms_linear/100, rms_polynomial/100,rms_tree/100, rms_rf/100] # List of algorithms algorithms = ['Linear regression', 'Polynomial', 'Decision', 'Random Forest Tree'] # Set the width of the bars bar_width = 0.15 # Set the position of each bar on X-axis r1 = np.arange(len(algorithms)) r2 = [x + bar_width for x in r1] r3 = [x + bar_width for x in r2] r4 = [x + bar_width for x in r3] r5 = [x + bar_width for x in r4] # Create bar plot plt.bar(r2, r2_scores, width=bar_width, label='R2 Score') plt.bar(r3, mae_scores, width=bar_width, label='MAE') plt.bar(r4, mse_scores, width=bar_width, label='MSE') plt.bar(r5, rmse_scores, width=bar_width, label='RMSE')
32 | P a g e
# Add labels to the chart plt.xlabel('Algorithms', fontweight='bold') plt.xticks([r + 2*bar_width for r in range(len(algorithms))], algorithms) plt.ylabel('Scores') plt.title('Performance Comparison of ML Algorithms[20% test]') # Show legend plt.legend() # Show the plot plt.show()
SPLITTING THE DATA IINTO 70% TRAINING DATA AND 30% TESTING DATA: X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=2) lr = LinearRegression()
lr.fit(X_train, Y_train) lr.score(X_train,Y_train)
lr_Y_pred = lr.predict(X_test)
poly_reg = PolynomialFeatures(degree=2) poly_reg
#transforming the features to higher degree X_train_poly = poly_reg.fit_transform(X_train) #splitting the data plr_X_train, plr_X_test, plr_Y_train, plr_Y_test = train_test_split(X_train_poly, Y_train, test_size=0.3, random_state=2)
plr = LinearRegression() #model training plr.fit(plr_X_train,plr_Y_train) #model accuracy plr.score(plr_X_train,plr_Y_train)
plr_Y_pred = plr.predict(plr_X_test)
dtree = DecisionTreeRegressor() dtree
33 | P a g e
#model training dtree.fit(X_train,Y_train) #model accuracy dtree.score(X_train,Y_train)
dtree_pred = dtree.predict(X_test) rf = RandomForestRegressor(n_estimators=100) rf
#model training rf.fit(X_train,Y_train) #model accuracy rf.score(X_train,Y_train)
rf_pred = rf.predict(X_test)
#evaluation Metrics # Mean Absolute Error (MAE) mae_linear = mean_absolute_error(Y_test, lr_Y_pred) mae_polynomial = mean_absolute_error(plr_Y_test, plr_Y_pred) mae_tree = mean_absolute_error(Y_test, dtree_pred) mae_rf = mean_absolute_error(Y_test, rf_pred) # Root Mean Squared Error (RMSE) rms_linear = mean_squared_error(Y_test, lr_Y_pred, squared=False) rms_polynomial = mean_squared_error(plr_Y_test, plr_Y_pred, squared=False) rms_tree = mean_squared_error(Y_test, dtree_pred, squared=False) rms_rf = mean_squared_error(Y_test, rf_pred, squared=False) # R-squared (R2) r2_linear = r2_score(Y_test, lr_Y_pred) r2_polynomial = r2_score(plr_Y_test, plr_Y_pred) r2_tree = r2_score(Y_test, dtree_pred) r2_rf = r2_score(Y_test, rf_pred) # Mean square error mse_linear = mean_squared_error(Y_test, lr_Y_pred) mse_polynomial = mean_squared_error(plr_Y_test, plr_Y_pred) mse_tree = mean_squared_error(Y_test, dtree_pred)
34 | P a g e
mse_rf = mean_squared_error(Y_test, rf_pred)
# Print or use the metrics as needed print("Mean Absolute Error:") print(f"Linear Regression:", {mae_linear}) print(f"Logistic Regression:", {mae_polynomial}) print(f"Decision Tree:", {mae_tree}) print(f"Random Forest Tree:", {mae_rf}) print("\nRoot Mean Squared Error:") print(f"Linear Regression:, {rms_linear}") print(f"Logistic Regression:", {rms_polynomial}) print(f"Decision Tree:, {rms_tree}") print(f"Random Forest Tree:", {rms_rf}) print("\nR-squared (R2):") print(f"Linear Regression:, {r2_linear}") print(f"Logistic Regression:", {r2_polynomial}) print(f"Decision Tree:, {r2_tree}") print(f"Random Forest Tree:", {r2_rf}) print("\n Mean square error:") print(f"Linear Regression:, {mse_linear}") print(f"Logistic Regression:", {mse_polynomial}) print(f"Decision Tree:, {mse_tree}") print(f"Random Forest Tree:", {mse_rf})
# Assuming you have performance metrics for each algorithm[20%test] r2_scores = [r2_linear, r2_polynomial, r2_tree, r2_rf] mae_scores = [mae_linear/100, mae_polynomial/100,mae_tree/100,mae_rf/100] mse_scores = [mse_linear/10000,mse_polynomial/10000,mse_tree/10000 ,mse_rf/10000] rmse_scores = [rms_linear/100, rms_polynomial/100,rms_tree/100, rms_rf/100] # List of algorithms algorithms = ['Linear regression', 'Polynomial', 'Decision', 'Random Forest Tree'] # Set the width of the bars bar_width = 0.15 # Set the position of each bar on X-axis r1 = np.arange(len(algorithms))
35 | P a g e
r2 = [x + bar_width for x in r1] r3 = [x + bar_width for x in r2] r4 = [x + bar_width for x in r3] r5 = [x + bar_width for x in r4] # Create bar plot plt.bar(r2, r2_scores, width=bar_width, label='R2 Score') plt.bar(r3, mae_scores, width=bar_width, label='MAE') plt.bar(r4, mse_scores, width=bar_width, label='MSE') plt.bar(r5, rmse_scores, width=bar_width, label='RMSE') # Add labels to the chart plt.xlabel('Algorithms', fontweight='bold') plt.xticks([r + 2*bar_width for r in range(len(algorithms))], algorithms) plt.ylabel('Scores') plt.title('Performance Comparison of ML Algorithms[30% test]') # Show legend plt.legend() # Show the plot plt.show()
SPLITTING THE DATA IINTO 60% TRAINING DATA AND 40% TESTING DATA: X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=2) lr = LinearRegression()
lr.fit(X_train, Y_train) lr.score(X_train,Y_train)
lr_Y_pred = lr.predict(X_test)
poly_reg = PolynomialFeatures(degree=2) poly_reg
#transforming the features to higher degree X_train_poly = poly_reg.fit_transform(X_train) #splitting the data plr_X_train, plr_X_test, plr_Y_train, plr_Y_test = train_test_split(X_train_poly, Y_train, test_size=0.4, random_state=2)
36 | P a g e
plr = LinearRegression() #model training plr.fit(plr_X_train,plr_Y_train) #model accuracy plr.score(plr_X_train,plr_Y_train)
plr_Y_pred = plr.predict(plr_X_test)
dtree = DecisionTreeRegressor() dtree
#model training dtree.fit(X_train,Y_train) #model accuracy dtree.score(X_train,Y_train)
dtree_pred = dtree.predict(X_test) rf = RandomForestRegressor(n_estimators=100) rf
#model training rf.fit(X_train,Y_train) #model accuracy rf.score(X_train,Y_train)
rf_pred = rf.predict(X_test)
#evaluation Metrics # Mean Absolute Error (MAE) mae_linear = mean_absolute_error(Y_test, lr_Y_pred) mae_polynomial = mean_absolute_error(plr_Y_test, plr_Y_pred) mae_tree = mean_absolute_error(Y_test, dtree_pred) mae_rf = mean_absolute_error(Y_test, rf_pred) # Root Mean Squared Error (RMSE) rms_linear = mean_squared_error(Y_test, lr_Y_pred, squared=False) rms_polynomial = mean_squared_error(plr_Y_test, plr_Y_pred, squared=False) rms_tree = mean_squared_error(Y_test, dtree_pred, squared=False) rms_rf = mean_squared_error(Y_test, rf_pred, squared=False) # R-squared (R2) r2_linear = r2_score(Y_test, lr_Y_pred)
37 | P a g e
r2_polynomial = r2_score(plr_Y_test, plr_Y_pred) r2_tree = r2_score(Y_test, dtree_pred) r2_rf = r2_score(Y_test, rf_pred) # Mean square error mse_linear = mean_squared_error(Y_test, lr_Y_pred) mse_polynomial = mean_squared_error(plr_Y_test, plr_Y_pred) mse_tree = mean_squared_error(Y_test, dtree_pred) mse_rf = mean_squared_error(Y_test, rf_pred)
# Print or use the metrics as needed print("Mean Absolute Error:") print(f"Linear Regression:", {mae_linear}) print(f"Logistic Regression:", {mae_polynomial}) print(f"Decision Tree:", {mae_tree}) print(f"Random Forest Tree:", {mae_rf}) print("\nRoot Mean Squared Error:") print(f"Linear Regression:, {rms_linear}") print(f"Logistic Regression:", {rms_polynomial}) print(f"Decision Tree:, {rms_tree}") print(f"Random Forest Tree:", {rms_rf}) print("\nR-squared (R2):") print(f"Linear Regression:, {r2_linear}") print(f"Logistic Regression:", {r2_polynomial}) print(f"Decision Tree:, {r2_tree}") print(f"Random Forest Tree:", {r2_rf}) print("\n Mean square error:") print(f"Linear Regression:, {mse_linear}") print(f"Logistic Regression:", {mse_polynomial}) print(f"Decision Tree:, {mse_tree}") print(f"Random Forest Tree:", {mse_rf})
# Assuming you have performance metrics for each algorithm[20%test] r2_scores = [r2_linear, r2_polynomial, r2_tree, r2_rf] mae_scores = [mae_linear/100, mae_polynomial/100,mae_tree/100,mae_rf/100] mse_scores = [mse_linear/10000,mse_polynomial/10000,mse_tree/10000 ,mse_rf/10000]
38 | P a g e
rmse_scores = [rms_linear/100, rms_polynomial/100,rms_tree/100, rms_rf/100] # List of algorithms algorithms = ['Linear regression', 'Polynomial', 'Decision', 'Random Forest Tree'] # Set the width of the bars bar_width = 0.15 # Set the position of each bar on X-axis r1 = np.arange(len(algorithms)) r2 = [x + bar_width for x in r1] r3 = [x + bar_width for x in r2] r4 = [x + bar_width for x in r3] r5 = [x + bar_width for x in r4] # Create bar plot plt.bar(r2, r2_scores, width=bar_width, label='R2 Score') plt.bar(r3, mae_scores, width=bar_width, label='MAE') plt.bar(r4, mse_scores, width=bar_width, label='MSE') plt.bar(r5, rmse_scores, width=bar_width, label='RMSE') # Add labels to the chart plt.xlabel('Algorithms', fontweight='bold') plt.xticks([r + 2*bar_width for r in range(len(algorithms))], algorithms) plt.ylabel('Scores') plt.title('Performance Comparison of ML Algorithms[30% test]') # Show legend plt.legend() # Show the plot plt.show()