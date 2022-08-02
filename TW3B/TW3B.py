import numpy as np
import pandas as pd

emails = pd.read_csv('D:/New folder/6th sem/AIML lab/TW3B/emails.csv')
emails.drop_duplicates(inplace=True)

def process_email(text):
    text = text.lower()
    return list(set(text.split()))

def predict_bayes(word):
    word = word.lower()
    num_spam_with_word = model[word]['spam']
    num_ham_with_word = model[word]['ham']
    return num_spam_with_word/(num_spam_with_word + num_ham_with_word)

def predict_naive_bayes(email):
    total = len(emails)
    num_spam = sum(emails['spam'])
    num_ham = total - num_spam
    email = email.lower()
    words = set(email.split())
    spams = [1.0]
    hams = [1.0]
    for word in words:
        if word in model:
            spams.append(model[word]['spam']/num_spam*total)
            hams.append(model[word]['ham']/num_ham*total)
    prod_spams = np.compat.long(np.prod(spams)*num_spam)
    prod_hams = np.compat.long(np.prod(hams)*num_ham)
    return prod_spams/(prod_spams + prod_hams)

emails['words'] = emails['text'].apply(process_email)
num_emails = len(emails)
num_spam = sum(emails['spam'])

print('Number of emails:', num_emails)
print('Number of spam emails:', num_spam)
print('Probability of spam:', num_spam/num_emails)

model = {}
for index, email in emails.iterrows():
    for word in email['words']:
        if word not in model:
            model[word] = {'spam': 1, 'ham': 1}
        if email['spam']:
            model[word]['spam'] += 1
        else:
            model[word]['ham'] +=1

print('Prediction using Bayes for word sale', predict_bayes('sale'))
print('Prediction using bayes for word lottery', predict_bayes('lottery'))
print('Predication using NaiveBayes for word lottery sale', predict_naive_bayes('lottery sale'))
print('Predication using NaiveBayes for word asfgf', predict_naive_bayes('asfgf'))
print('Predication using NaiveBayes for word Hello Mom, I am here at home', predict_naive_bayes('Hello Mom, I am here at home'))
