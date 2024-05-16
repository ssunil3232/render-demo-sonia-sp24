import pandas as pd

file_path = './sleeping_data.csv'
try:
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='ISO-8859-1')

columns_to_drop = ["StartDate","Unnamed: 19", "EndDate", "When you're not sleeping in the same bed as your partner, where do you typically sleep?", "Unnamed: 6","When you're not sleeping in the same bed, where does your partner typically sleep?","When was the first time you slept in separate beds?", "Unnamed: 8", "Which of the following best describes your current occupation?","Unnamed: 25", "Household Income", "Education"]
df = df.drop(columns_to_drop, axis=1)

rename_dict = {
    'Location (Census Region)': "location",
    'When both you and your partner are at home, how often do you sleep in separate beds?': "sleep_freq",
    'How long have you been in your current relationship? If you are not currently in a relationship, please answer according to your last relationship.':"relationship_years",
    'Which of the following best describes your current relationship status?':"relationship_status",
    'What are the reasons that you sleep in separate beds? Please select all that apply.': "snores",
    'Unnamed: 10': "frequent bathroom trips in the night",
    'Unnamed: 11': "sick",
    'Unnamed: 12': "no longer physically intimate",
    'Unnamed: 13': "different temperature preferences for the room",
    'Unnamed: 14': "argument/fight",
    'Unnamed: 15': "not enough space",
    'Unnamed: 16': "do not want to share the covers",
    'Unnamed: 17': "needs to sleep with a child",
    'Unnamed: 18': "night working/very different sleeping times",
    'To what extent do you agree with the following statement:ë_"our sex life has improved as a result of sleeping in separate beds."ë_': "our sex life has improved as a result of sleeping in separate beds.",
    'To what extent do you agree with the following statement: "sleeping in separate beds helps us to stay together."': "sleeping in separate beds helps us to stay together.",
    'To what extent do you agree with the following statement: "we sleep better when we sleep in separate beds."':"we sleep better when we sleep in separate beds."
}

df.rename(columns=rename_dict, inplace=True)
df.rename(columns={'To what extent do you agree with the following statement:"our sex life has improved as a result of sleeping in separate beds."': 'our sex life has improved as a result of sleeping in separate beds.'}, inplace=True)


df = df.iloc[1:]
df = df[(df["location"] != "Response") & (df["location"] != "Mountain") & (df["location"] != "")& df["location"].notna()]
df = df[(df["relationship_status"] != "Response") & (df["relationship_status"] != "Divorced") & (df["relationship_status"] != "Widowed") & (df["relationship_status"] != "Separated")]
#df = df[(df['sleeping in separate beds helps us to stay together.'].notna())]
#df = df[(df['we sleep better when we sleep in separate beds.'].notna())]
#df = df[(df['our sex life has improved as a result of sleeping in separate beds.'].notna())]

columns_to_assign = ['snores', 'frequent bathroom trips in the night', 'sick','no longer physically intimate', 'different temperature preferences for the room','argument/fight','not enough space','do not want to share the covers','needs to sleep with a child','night working/very different sleeping times']

for col in columns_to_assign:
    if col in df.columns:
        df[col] = df[col].apply(lambda x: False if pd.isna(x) else True)
        

df.to_csv('./sleeping-pattern-formatted.csv', encoding='utf-8', index=False)