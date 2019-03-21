import json
import nltk
from nltk.corpus import stopwords
import os

def get_token_type(token_length):
    token_type = [ "uniword", "dualword", "triword" ]
    
    return token_type[token_length - 1]

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

                    if token_length == 1:
                        tokens += desc_tokens
                        tokens += qual_tokens
                        tokens += respb_tokens

                    else:
                        tokens += [ " ".join(desc_tokens[i : i + token_length]) for i in range(len(desc_tokens) - token_length + 1) ]
                        tokens += [ " ".join(qual_tokens[i : i + token_length]) for i in range(len(qual_tokens) - token_length + 1) ]
                        tokens += [ " ".join(respb_tokens[i : i + token_length]) for i in range(len(respb_tokens) - token_length + 1) ]

    with open("./results/" + get_token_type(token_length) + "/tokens-full-" + get_token_type(token_length) + ".json", "w") as outfile:
        json.dump(tokens, outfile, indent = 4)

    stats = {}
    eng_stop_words = set(stopwords.words('english'))

    for token in tokens:
        token = token.lower()

        if token in eng_stop_words:
            continue

        stats[token] = stats.get(token, 0) + 1

    with open("./results/" + get_token_type(token_length) + "/stats-full-" + get_token_type(token_length) + ".json", "w") as outfile:
        json.dump(stats, outfile, indent = 4)

    sorted_by_value = sorted(stats.items(), key=lambda kv: kv[1], reverse=True)
    with open("./results/" + get_token_type(token_length) + "/./sorted-full-" + get_token_type(token_length) + ".json", "w") as outfile:
        json.dump(sorted_by_value, outfile, indent = 4)

get_stats(1)
get_stats(2)
get_stats(3)