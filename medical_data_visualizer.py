import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = None
mask_overweight = df.weight.divide(np.square(df.height/100))>25
df.loc[mask_overweight,'overweight']=1
df.loc[df.overweight.isnull(),'overweight'] = 0

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df.cholesterol <= 1,'cholesterol'] = 0 
df.loc[df.gluc <= 1, 'gluc'] = 0
df.loc[df.cholesterol > 0 ,'cholesterol'] = 1
df.loc[df.gluc > 0, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(frame = df[['cholesterol','gluc', 'smoke', 'alco', 'active', 'overweight','cardio']] , id_vars = 'cardio')

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  df_cat = df_cat.groupby(['cardio','variable','value']).value.count()
  df_cat = df_cat.to_frame()
  df_cat.rename(columns= {'value':'total'}, inplace=True)
  df_cat.reset_index(inplace=True)

    # Draw the catplot with 'sns.catplot()'
  fig = sns.catplot(data= df_cat,y='total',x='variable', hue='value', kind = 'bar',col = 'cardio' ).fig
    # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
  # Clean the data
  mask_dia_higher_syst = (df['ap_lo']<=df['ap_hi'])
  mask_height_1 = (df['height'] >= df['height'].quantile(0.025))
  mask_height_2 = (df['height'] <= df['height'].quantile(0.975))
  mask_weight_1 = (df['weight'] >= df['weight'].quantile(0.025))
  mask_weight_2 = (df['weight'] <= df['weight'].quantile(0.975))
  

  df.overweight = df.overweight.astype(int)
  
  df_heat = df[mask_dia_higher_syst & mask_height_1 & mask_height_2 & mask_weight_1 & mask_weight_2]

  # Calculate the correlation matrix
  corr = df_heat.corr()

  # Generate a mask for the upper triangle
  mask = np.triu(corr,0)

  # Set up the matplotlib figure
  fig, ax= plt.subplots(1,1)

  # Draw the heatmap with 'sns.heatmap()'
  ax = sns.heatmap(corr, mask=mask,annot=True, fmt =  '.1f',linewidths=1 )
  # Do not modify the next two lines
  fig.figure.savefig('heatmap.png')
  return fig
