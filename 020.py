# Perform a Google search and return top 5 results.

from googlesearch import search

query = "Python tips"
for result in search(query, num_results=5):
    print(result)
