import sys
import csv
import pandas as pd
import numpy as np
import re


df = pd.read_csv(sys.argv[1]+'.csv')

df.columns = ['filter_set', 'message_name', 'message_subject', 'matched', 'refunded', 'refunded_pct', 'emails_sent', 'emails_opened', 'emails_opened_pct', 'emails_clicked', 'emails_clicked_pct', 'emails_marked_spam_pct', 'emails_bounced_pct', 'emails_unsubscribed_pct', 'revenue', 'revenue_from_emails', 'emails_cost', 'profit_from_emails']

# df['emails_sent'] = int(float(df['emails_sent']))

# df['emails_sent'] = pd.to_numeric(df['emails_sent'], errors='coerce')

df['emails_opened'] = pd.to_numeric(df['emails_opened'], errors='coerce')

print(df['emails_opened'].sum())
# print(df['emails_sent'])
# print(df['emails_sent'].mean())
# print(df['emails_sent'].sum())
