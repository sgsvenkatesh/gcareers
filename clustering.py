import json

def get_words_count(word):
    return len(word.split(" "))

def run_analytics(top_tech_list, stats):
    identifiers = [ "uniwords", "dualwords", "triwords" ]
    results = []

    for tech in top_tech_list:
        this_count = 0
        keywords = []

        for item in tech:
            word_count = get_words_count(item)
            list_to_search = stats[identifiers[word_count - 1]]

            if len(item) <= 3:
                if list_to_search.get(item):
                    keywords.append(item)
                    this_count += list_to_search[item]
            else:
                for key in list_to_search.keys():
                    if item in key:
                        keywords.append(key)
                        this_count += list_to_search[key]
        
        if keywords:
            results.append({ "keywords": keywords, "count": this_count })

    print("done with clustering. writing to file ")

    with open("./results/analytics/clustered-stats.json", "w") as clustered_stats:
        json.dump(results, clustered_stats, indent = 4)
        print("saved results to file ./results/analytics/clustered-stats.json")

def load_stats_run_analytics():
    # TODO: replace with promise architecture
    with open("./tech-list.json") as top_tech_list_obj:
        top_tech_list = json.load(top_tech_list_obj)
        stats = {}

        with open("./results/uniword/stats-full-uniword.json") as uniwords_list_object:
            stats["uniwords"] = json.load(uniwords_list_object)

            with open("./results/dualword/stats-full-dualword.json") as dualwords_list_object:
                stats["dualwords"] = json.load(dualwords_list_object)

                with open("./results/triword/stats-full-triword.json") as triwords_list_object:
                    stats["triwords"] = json.load(triwords_list_object)

                    print("data fetched. starting analytics")
                    run_analytics(top_tech_list, stats)

load_stats_run_analytics()