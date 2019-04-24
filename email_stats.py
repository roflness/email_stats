import sys
import csv
import pandas as pd
import numpy as np
import re
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("Error: %s needs to include name of csv file" % (sys.argv[0],))
    sys.exit()

df = pd.read_csv(filename+'.csv', thousands=',')

df.columns = ['filter_set', 'message_name', 'message_subject', 'matched', 'refunded', 'refunded_pct', 'emails_sent', 'emails_opened', 'emails_opened_pct', 'emails_clicked', 'emails_clicked_pct', 'emails_marked_spam_pct', 'emails_bounced_pct', 'emails_unsubscribed_pct', 'revenue', 'revenue_from_emails', 'emails_cost', 'profit_from_emails']


df['emails_sent'] = pd.to_numeric(df['emails_sent'], errors='coerce')
df['emails_opened'] = pd.to_numeric(df['emails_opened'], errors='coerce')
df['emails_clicked'] = pd.to_numeric(df['emails_clicked'], errors='coerce')


df['message_count'] = df['message_subject'].str.count(' ') + 1

# print(df['emails_opened'])
# # print(df['emails_sent'])
# print(df['emails_sent'].mean())
# print(df['emails_sent'].sum())


df2 = df.drop_duplicates(subset ="message_subject", keep='first')

print(df2.message_subject)
# print(df.groupby('message_count')['emails_opened_pct'].mean())
# print(df.groupby('message_count')['emails_opened_pct'].std())

# # df2 = pd.DataFrame()

# # df2 = df.iloc[0:, 1:]


# corr = df['emails_opened_pct'].corr(df['message_count'])

# plt.scatter(df['emails_opened_pct'], df['message_count'])
# plt.show()


# print(corr)