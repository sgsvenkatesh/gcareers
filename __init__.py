from crawl_list import crawl_list
from crawl_full_desc import crawl_full_desc
from get_stats import get_stats
from clustering import load_stats_run_analytics

if __name__ == "__main__":
    crawl_list()
    crawl_full_desc()

    get_stats(1)
    get_stats(2)
    get_stats(3)
    
    load_stats_run_analytics()