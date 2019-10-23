data_duration = data[['duration', 'type_attack']]

normal_duration = data_duration[data_duration.type_attack == 'normal']
dos_duration= data_duration[data_duration.type_attack == 'dos']


sort_normal_duration = normal_duration.sort_values('duration', ascending=True)
sort_dos_duration = dos_duration.sort_values('duration', ascending=True)


count_normal_duration = sort_normal_duration['duration'].value_counts()
count_dos_duration = sort_dos_duration['duration'].value_counts()


data_duration2 = pd.concat([count_normal_duration, count_dos_duration], axis = 1)
data_duration2.columns =['normal','dos']


data_duration2 = data_duration2.fillna(0)
index = data_duration2.index.to_frame()
data_duration3 = pd.concat([data_duration2, index], axis=1)


data_duration3 = data_duration3.rename(columns={0: 'value'})


plt.figure(figsize=(20,10))

ax =  sns.kdeplot(data_duration3['normal'], shade=True, color='g')
ax =  sns.kdeplot(data_duration3['dos'], shade=True, color="r")
plt.title('duration')