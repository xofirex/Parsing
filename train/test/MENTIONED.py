import pandas as pd
import nltk.data

nltk.download('punkt')
#
#
file1 = r"C:\test\train\SITE_DATA.CSV"
file2 = r"C:\test\train\AUTHORS.CSV"
df1 = pd.read_csv(file1, usecols=["description"])
df3 = df1.convert_dtypes()
# all_name = set(["James Patterson", "Kei Nagai", "Ichigo Kurosaki", "Justice Lonesome", "Stephen King"])
all_name = set()
csv = pd.read_csv(file2, usecols=["author_name"])
csv = csv.convert_dtypes()
all_name.update(csv['author_name'])
desc = set()
csv = pd.read_csv(file1, usecols=["description"])
desc.update(csv['description'])
aut_name = set()
list_author = list()
author_sentence = set()

for one_author_name in all_name:
    for one_desc in desc:
        aut_name.discard(one_author_name)
        author_sentence.discard(one_author_name)
        if str(one_author_name) in str(one_desc) and str(one_author_name) not in aut_name:
            aut_name.add(one_author_name)
            a_list = nltk.tokenize.sent_tokenize(one_desc)
            for x in a_list:
                if one_author_name in x and one_author_name not in author_sentence:
                    sentence_index = a_list.index(x)
                    author_sentence.add(one_author_name)
                    if sentence_index == len(a_list)-1:
                        meaningful = a_list[sentence_index - 1] + " " + a_list[sentence_index]
                        list_author.append(
                            {"author_name": one_author_name, "description": one_desc, "meaningful_sentences": meaningful})
                    # if a_list.index(x) == 0 and len(a_list) != 1:
                    #     meaningful = a_list[sentence_index] + " " + a_list[sentence_index + 1]
                    #     list_author.append(
                    #         {"author_name": one_author_name, "description": one_desc, "meaningful_sentences": meaningful})
                    else:
                        meaningful = a_list[sentence_index] + " " + a_list[sentence_index + 1]
                        list_author.append(
                            {"author_name": one_author_name, "description": one_desc, "meaningful_sentences": meaningful})
df = pd.DataFrame(list_author)
df.to_csv(r'C:\test\train\MENTIONED.csv', index=False)
