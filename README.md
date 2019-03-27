# gcareers
_(data updated as on 19th March 2019)_

Python scripts to generate insights on tech trends at Google. Thanks to [Hemanth Malla](https://github.com/hemanthmalla) for the idea.

This repository is aimed to get an overview of the tech skills that Google is looking for. The scripts crawl the [Google Careers website](https://careers.google.com/jobs/results/?company=Google&company=YouTube&employment_type=FULL_TIME&hl=en_US&jlo=en_US&q=&sort_by=relevance) and counts of frequency of the keywords listed at [tech-list.json](https://github.com/sgsvenkatesh/gcareers/blob/master/tech-list.json) on the Google Careers website. 

Below is a short description of the functionality of each of the files.

`__init__.py` gives an overview of the flow and the order in which the files are executed. You may use this a module if needed.  
`crawl_list.py` fetches all the jobs listed at Google and YouTube  
`crawl_full_desc.py` fetches full job description for each of the job listing from the previous step  
`get_stats.py` sanitizes the crawled descriptions and counts the frequency of words of lengths 1, 2 and 3. Stores the results at `./results/`.  
`clustering.py` finds the occurence of each of the skills mentioned at [tech-list.json](https://github.com/sgsvenkatesh/gcareers/blob/master/tech-list.json) in the results obtained from previous step. Stores the results at `./results/analytics/`.

### Results

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
| Data Mining, BigData                  | 212               |
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
| HCI                                   | 275               |
| Containers (K8s, Docker)              | 154               |