# Train Scrapy
to crawl items you need use: `scrapy crawl bookspider -o SITE_DATA.CSV -t headless`

# Test Pandas
 include /test
1. Run fetchexternal.py; "fetch df from external database"
2. Run addheaders.py;  "add headers to our df"
3. Run BOOK.py; "create BOOK.CSV"
4. Run AUTHORS.py; "create AUTHORS.py"
5. Run AUTHORS_BOOK.py; "create BOOK_AUTHORS"
`6. Run new_nentioned.py; "fetch author name for our title from BOOK_AUTHORS"`
7. Run MENTIONED.py; "snippet of text (2-3 meaningful sentences around matched author name)"
8. Run MENTIONED_AUTHORS.py; (create MENTIONED_AUTHORS.CSV)
9. Run FREQUENT_AUTHOR.py; (show most frequent author of the site)
10. Run missing_books.py; (books from the site are missing in the BOOKS.CSV)
11. Run most_frequent_words.py; (shows top 10 most frequent meaningful words from the title)
12. Run BOOK_DESC.py; (create BOOK_DESCRIPTION.CSV)