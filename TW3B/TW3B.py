import numpy as np
import pandas as pd

emails = pd.read_csv('/home/lab2/Downloads/emails.csv')

def process_email(text):
    text = text.lower()
    return list(set(text.split()))

emails['words'] = emails['text'].apply(process_email)
num_emails = len(emails)
num_spam = sum(emails['spam'])

print('Number of emails:', num_emails)
print('Number of spam emails:', num_spam)
print()

print('probability of spam:', num_spam/num_emails)
print()

model = {}

for index, email in emails.iterrows():
    for word in email['words']:
        if word not in model:
            model[word] = {'spam': 1, 'ham': 1}

        if word not in model:
            if email['spam']:
                model[word]['spam'] += 1

            else:
                model[word]['ham'] +1


def predict_bayes(word):
    word = word.lower()
    num_spam_with_word = model[word]['spam']
    num_ham_with_word = model[word]['ham']
    return 1.0*num_spam_with_word/(num_spam_with_word + num_ham_with_word)

print('Prediction using Bayes for word sale', predict_bayes('sale'))
print('Prediction using bayes for word lottery', predict_bayes('lottery'))


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


print('Prodication using NaiveBayes for word lottery sale', predict_naive_bayes('lottery sale'))
print('Prodication using NaiveBayes for word lottery sale', predict_naive_bayes('asdfgh'))
print('Prodication using NaiveBayes for word lottery sale', predict_naive_bayes('Hi Mom, How are you?'))
