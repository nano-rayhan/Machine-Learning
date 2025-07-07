import pandas as pd

df_customers = pd.DataFrame({
    "Name" : ['ashik','Rayhan','Sahed','Robin','Niran'],
    "CustomerId" : [1, 2,3,4,5],
    
})

df_order = pd.DataFrame({
    "CustomerId" : [1, 2,3,6,7],
    "OrderAmount" : [240,400,350,480,440]
})

df_concate = pd.concat([df_customers, df_order], axis=0, ignore_index=True)
print(df_concate)