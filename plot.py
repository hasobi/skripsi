srv_serror_rate = data['srv_serror_rate']
attack = data['type_attack']


data_srv_serror_rate = pd.concat([srv_serror_rate, attack], axis=1)

normal_srv_serror_rate = data_srv_serror_rate[data_srv_serror_rate.type_attack == 'normal']
dos_srv_serror_rate= data_srv_serror_rate[data_srv_serror_rate.type_attack == 'dos']


sort_normal_srv_serror_rate = normal_srv_serror_rate.sort_values('srv_serror_rate', ascending=True)
sort_dos_srv_serror_rate = dos_srv_serror_rate.sort_values('srv_serror_rate', ascending=True)


count_normal_srv_serror_rate = sort_normal_srv_serror_rate['srv_serror_rate'].value_counts()
count_dos_srv_serror_rate = sort_dos_srv_serror_rate['srv_serror_rate'].value_counts()


data_srv_serror_rate2 = pd.concat([count_normal_srv_serror_rate, count_dos_srv_serror_rate], axis = 1)
data_srv_serror_rate2.columns =['normal','dos']


data_srv_serror_rate2 = data_srv_serror_rate2.fillna(0)
index = data_srv_serror_rate2.index.to_frame()
data_srv_serror_rate3 = pd.concat([data_srv_serror_rate2, index], axis=1)


data_srv_serror_rate3 = data_srv_serror_rate3.rename(columns={0: 'value'})


plt.figure(figsize=(20,10))

ax =  sns.kdeplot(data_srv_serror_rate3['normal'], shade=True, color='g')
ax =  sns.kdeplot(data_srv_serror_rate3['dos'], shade=True, color="r")
plt.title('srv_serror_rate')