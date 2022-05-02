
def predictRuns(file):
              import pandas as pd
              import numpy as np
              from sklearn.neighbors import KNeighborsRegressor

              df_new= pd.read_csv('IPL_train.csv')
              encoded_df = pd.get_dummies(data=df_new, columns=['batting_team', 'bowling_team',"venue",'innings'])


              encoded_df = encoded_df[['batting_team_Chennai Super Kings',
                     'batting_team_Delhi Daredevils', 'batting_team_Kings XI Punjab',
                     'batting_team_Kolkata Knight Riders', 'batting_team_Mumbai Indians',
                     'batting_team_Rajasthan Royals',
                     'batting_team_Royal Challengers Bangalore',
                     'batting_team_Sunrisers Hyderabad', 'bowling_team_Chennai Super Kings',
                     'bowling_team_Delhi Daredevils', 'bowling_team_Kings XI Punjab',
                     'bowling_team_Kolkata Knight Riders', 'bowling_team_Mumbai Indians',
                     'bowling_team_Rajasthan Royals',
                     'bowling_team_Royal Challengers Bangalore',
                     'bowling_team_Sunrisers Hyderabad', 'venue_Arun Jaitley Stadium',
                     'venue_Eden Gardens', 'venue_M.Chinnaswamy Stadium',
                     'venue_MA Chidambaram Stadium, Chepauk, Chennai',
                     'venue_Narendra Modi Stadium, Ahmedabad', 'venue_Wankhede Stadium',
                     'innings_1', 'innings_2','runs_6_overs' ]]

              X_train = encoded_df.drop(labels='runs_6_overs', axis=1)
              y_train = encoded_df['runs_6_overs'].values


              regr = KNeighborsRegressor()
              regr.fit(X_train,y_train)


              X_test=pd.read_csv(file)


              batting_team = X_test['batting_team'][0]
              bowling_team = X_test['bowling_team'][0]
              venue = X_test['venue'][0]
              innings = X_test['innings'][0]
              X_test.drop(labels=['batsmen','bowlers'],axis=1, inplace=True)

              temp_array = []

              if batting_team == 'Chennai Super Kings':
                  temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
              elif batting_team == 'Delhi Daredevils':
                  temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
              elif batting_team == 'Kings XI Punjab':
                  temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
              elif batting_team == 'Kolkata Knight Riders':
                  temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
              elif batting_team == 'Mumbai Indians':
                  temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
              elif batting_team == 'Rajasthan Royals':
                  temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
              elif batting_team == 'Royal Challengers Bangalore':
                  temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
              elif batting_team == 'Sunrisers Hyderabad':
                  temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

              if bowling_team == 'Chennai Super Kings':
                  temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
              elif bowling_team == 'Delhi Daredevils':
                  temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
              elif bowling_team == 'Kings XI Punjab':
                  temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
              elif bowling_team == 'Kolkata Knight Riders':
                  temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
              elif bowling_team == 'Mumbai Indians':
                  temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
              elif bowling_team == 'Rajasthan Royals':
                  temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
              elif bowling_team == 'Royal Challengers Bangalore':
                  temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
              elif bowling_team == 'Sunrisers Hyderabad':
                  temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

              if venue == 'Arun Jaitley Stadium':
                  temp_array = temp_array + [1, 0, 0, 0, 0, 0]
              elif venue == 'Eden Gardens':
                  temp_array = temp_array + [0, 1, 0, 0, 0, 0]
              elif venue == 'M.Chinnaswamy Stadium':
                  temp_array = temp_array + [0, 0, 1, 0, 0, 0]
              elif venue == 'MA Chidambaram Stadium, Chepauk, Chennai':
                  temp_array = temp_array + [0, 0, 0, 1, 0, 0]
              elif venue == 'Narendra Modi Stadium, Ahmedabad':
                  temp_array = temp_array + [0, 0, 0, 0, 1, 0]
              elif venue == 'Wankhede Stadium':
                  temp_array = temp_array + [0, 0, 0, 0, 0, 1]

              if innings == 1:
                  temp_array = temp_array + [1, 0]
              elif innings == 2:
                  temp_array = temp_array + [0, 1]

              print(df_new['venue'].unique())

              data = np.array([temp_array])
              my_prediction = int(regr.predict(data))

              return my_prediction