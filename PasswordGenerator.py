from ast import For
from password_generator import PasswordGenerator
import pandas as pd

df = pd.DataFrame(columns = ['Password'])


def CreatePassword():
    pwo = PasswordGenerator()
    
    pwd = pwo.shuffle_password('2345679ACEFGHJKLMNPRSTUWXYZacdefghkmnopqrstuwxyz', 7)
    return pwd

for x in range(450):
    y = CreatePassword()
   
    pwd = {'Password': y}
    print(pwd)
    df.loc[x] = pwd

df.reset_index(drop=True)
print(df)
df.to_csv('passwords1.csv')