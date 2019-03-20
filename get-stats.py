import json
import nltk
from nltk.corpus import stopwords
import os

UNIWORD = "uniword"
DUALWORD = "dualword"

def get_stats(token_length):
    directory = "./raw-data/full-desc/"
    tokens = []
    repl_str_space = [ "<li>", "</li>", "</ li>", "<ul>", "</ul>", "</ ul>", "\n", ".", ",", "<p>", "</p>", "</ p>", "#39;s", "#39;", "\u2019", "\u2014", "&", ":", "/", "<i>", "</i>", "</ i>", "<br>", "<br/>", "<br />", "(", ")", ">", "<"]

    for filename in os.listdir(directory):
        if filename.startswith("job") and filename.endswith(".json"):
            
            with open(directory + filename) as result_obj:
                result = json.load(result_obj)

                desc = result.get("description")
                qual = result.get("qualifications")
                respb = result.get("responsibilities")

                if desc:
                    for s in repl_str_space:
                        desc = desc.replace(s, " ")
                        qual = qual.replace(s, " ")
                        respb = respb.replace(s, " ")

                    desc_tokens = list(filter(None, desc.split(" ")))
                    qual_tokens = list(filter(None, qual.split(" ")))
                    respb_tokens = list(filter(None, respb.split(" ")))

                    if token_length == UNIWORD:
                        tokens += desc_tokens
                        tokens += qual_tokens
                        tokens += respb_tokens

                    elif token_length == DUALWORD:
                        tokens += [ " ".join(desc_tokens[i:i+2]) for i in range(len(desc_tokens) - 1) ]
                        tokens += [ " ".join(qual_tokens[i:i+2]) for i in range(len(qual_tokens) - 1) ]
                        tokens += [ " ".join(respb_tokens[i:i+2]) for i in range(len(respb_tokens) - 1) ]

    with open("./results/" + token_length + "/tokens-full-" + token_length + ".json", "w") as outfile:
        json.dump(tokens, outfile, indent = 4)

    stats = {}
    eng_stop_words = set(stopwords.words('english'))

    for token in tokens:
        token = token.lower()

        if token in eng_stop_words:
            continue

        stats[token] = stats.get(token, 0) + 1

    with open("./results/" + token_length + "/stats-full-" + token_length + ".json", "w") as outfile:
        json.dump(stats, outfile, indent = 4)

    sorted_by_value = sorted(stats.items(), key=lambda kv: kv[1], reverse=True)
    with open("./results/" + token_length + "/./sorted-full-" + token_length + ".json", "w") as outfile:
        json.dump(sorted_by_value, outfile, indent = 4)

get_stats(UNIWORD)
get_stats(DUALWORD)