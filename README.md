# google-careers
_(data updated as on 19th March 2019)_

Python scripts to generate insights on tech trends at Google North America.  
_Thanks to [Hemanth Malla](https://github.com/hemanthmalla) for the idea._

This repository is aimed to get an overview of the tech skills that Google is looking for. The scripts crawl the [Google Careers website](https://careers.google.com/jobs/results/?company=Google&company=YouTube&employment_type=FULL_TIME&hl=en_US&jlo=en_US&q=&sort_by=relevance) and counts of frequency of the keywords listed at [tech-list.json](https://github.com/sgsvenkatesh/gcareers/blob/master/tech-list.json) on the Google Careers website. 

Below is a short description of the functionality of each of the files.

`__init__.py` gives an overview of the flow and the order in which the files are executed. You may use this a module if needed.  
`crawl_list.py` fetches all the jobs listed at Google and YouTube  
`crawl_full_desc.py` fetches full job description for each of the job listing from the previous step  
`get_stats.py` sanitizes the crawled descriptions and counts the frequency of words of lengths 1, 2 and 3. Stores the results at `./results/`.  
`clustering.py` finds the occurence of each of the skills mentioned at [tech-list.json](https://github.com/sgsvenkatesh/gcareers/blob/master/tech-list.json) in the results obtained from previous step. Stores the results at `./results/analytics/`.

### Results

Below are the results we got on analyzing over 2200 job descriptions, as we found on _19th March 2019_.

| Skill                                 | Frequency         |
| ------------------------------------- | :---------------: |
| Artificial Intelligence               | 388               |
| Machine Learning                      | 539               |
| Deep Learning                         | 68                |
| **Cloud**                             | **4729**          |
| Blockchain                            | 1                 |
| Internet of Things                    | 61                |
| JavaScript                            | 494               |
| Python                                | 840               |
| Java                                  | 646               |
| Natural Language Processing           | 273               |
| Computer Vision                       | 48                |
| Chatbots                              | 2                 |
| Devops                                | 63                |
| Augmented Reality / Virtual Reality   | 93                |
| Robotic Process Automation            | 0                 |
| Augmented Analytics                   | 0                 |
| **Cyber Security**                    | **2061**          |
| Network Security                      | 41                |
| Quantum Computing                     | 0                 |
| Privacy                               | 448               |
| **Search and Information Retrieval**  | **1356**          |
| Data Mining, BigData                  | 356               |
| E-commerce                            | 43                |
| **Computer Networks**                 | **3644**          |
| Databases                             | 628               |
| Compilers                             | 77                |
| Distributed Systems                   | 224               |
| Virtualization                        | 74                |
| Operating Systems                     | 221               |
| Algorithms & Data Structures          | 343               |
| Cryptography                          | 74                |
| Computer Architecture                 | 61                |
| Robotics                              | 220               |
| **Mobile (Android, iOS)**             | **2234**          |
| BioInformatics                        | 21                |
| HCI                                   | 275               |
| Containers (K8s, Docker)              | 154               |

### Takeaways

* As you would be expecting, Cloud-related skills seem to be in great demand, with a whopping count of ~4700. Further to this, Security, Networks, Mobile, Search seem to be the most sought out fields at Google. 
* It was interesting to see that there are negligible or no occurences of popular topics like Quantum Computing and BioInformatics. 
* Besides this, keywords like Computer Vision, Computer Architecture, Cryptography, Virtualization, Compilers, E-commerce Devops, Internet of Things, BlockChain have really low number of occurences compared to that of Cloud, Search and others.
* Also, Algorithms & Data Structures keywords were observed to occur only ~350 times. From the above data, it appears to me that being able to [invert a binary tree](https://twitter.com/mxcl/status/608682016205344768?lang=en) may not be as important to Google today as it is at excelling in one field.  
__@Students__, now you know not to miss your classes for Leetcode! 😛

__@Others__, you have more insights or ideas, happy to collaborate over a PR or a git-issue. 😀
