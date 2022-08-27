import re
import json

# save the positive words into a list called p_list
with open('positive tweets.txt') as f:
    p_txt = f.read()
    p_txt = re.sub('[,\.()":;!@#$%^&*\d]|\'s|\'', '', p_txt)
    p_list = p_txt.replace('\n',' ').replace('  ',' ').lower().split(' ')
    # test if cool is in the list
    print ('cool is in the postive list: ', 'cool' in p_list )

# save the negative words into a list called n_list
with open('negative tweets.txt') as f:
    n_txt = f.read()
    n_txt = re.sub('[,\.()":;!@#$%^&*\d]|\'s|\'', '', n_txt)
    n_list = n_txt.replace('\n',' ').replace('  ',' ').lower().split(' ')
    # test if abrade is in the list
    print ('abrade is in the negative list: ', 'abrade' in n_list )
    # test if cool is in the list
    print ('cool is in the negative list: ', 'cool' in p_list )

# process the tweets
with open('data.txt') as f:

    txt = f.read()
    txt = re.sub('[,\.()":;!@#$%^&*\d]|\'s|\'', '', txt)
    word_list = txt.replace('\n',' ').replace('  ',' ').lower().split(' ')
    
    # create empty dictionaries
    word_count_dict = {}
    word_count_positive = {}
    word_count_negative= {}
    
    for word in word_list:
		# count all words frequency
        if word in word_count_dict.keys():
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
		# count if it is a positive word
        if word in p_list:
            if word in word_count_positive.keys():
                word_count_positive[word] += 1
            else:
                word_count_positive[word] = 1
		# else see if it is a negative word
        elif word in n_list:
            if word in word_count_negative.keys():
                word_count_negative[word] += 1
            else:
                word_count_negative[word] = 1
			
    list_dict = sorted(word_count_dict.items(), key=lambda x:x[1], reverse=True)
    list_positive = sorted(word_count_positive.items(), key=lambda x:x[1], reverse=True)
    list_negative = sorted(word_count_negative.items(), key=lambda x:x[1], reverse=True)

    with open('word_count.csv', 'w')as f1:
        for i in list_dict:
            f1.write('%s,%s\n' %(i[0],str(i[1])))
    with open('word_positive.csv', 'w')as f1:
        for i in list_positive:
            f1.write('%s,%s\n' %(i[0],str(i[1])))
    with open('word_negative.csv', 'w')as f1:
        for i in list_negative:
            f1.write('%s,%s\n' %(i[0],str(i[1])))
