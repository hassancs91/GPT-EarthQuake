
import scraper as sc
import report as rp
import ai as ai


topic = input("Please enter a topic: ")

print("Searching....")
#scrape top 100 google results for each topic
google_results = sc.perform_google_search(topic)


links_list = []
bullet_summaries = []
content_ideas = []
twitter_tweets = []
total_token_count = 0

print()
print("--------------------------")
print("Results Found: " + str(len(google_results)))
print()
for result in google_results:
    
    #create a list of websites
    links_list.append(result["url"])
    
    print("Result: " + result["url"])
    print("--------------------------")
    
    
    #check brand mentions
    article  = sc.get_article_from_url(result["url"])
    
    #generate bullet summary
    print("Reading...")
    total_token_count = total_token_count + ai.count_tokens(article)
    bullet_summary = ai.blog_post_to_bullet_points(article)
    if bullet_summary:
        print("Summary:")
        print(bullet_summary)
        print("")
        bullet_summaries.append(bullet_summary)
        total_token_count = total_token_count + ai.count_tokens(bullet_summary)
    
        #generate contnet ideas
        print("Generating Conent Ideas...")
        total_token_count = total_token_count + ai.count_tokens(bullet_summary)
        ideas = ai.generate_content_ideas(bullet_summary)
        print("Content Ideas")
        print (ideas)
        print("")
        content_ideas.append(ideas)
        total_token_count = total_token_count + ai.count_tokens(ideas)
    
        #generate tweets
        print("Generating Tweets...")
        total_token_count = total_token_count + ai.count_tokens(bullet_summary)
        tweets = ai.generate_tweets(bullet_summary)
        total_token_count = total_token_count + ai.count_tokens(tweets)
        print("Tweets")
        print (tweets)
        print("")
        twitter_tweets.append(tweets)
        print("--------------------------")
    else:
        print("Unable To Read!")


#calculate the estimate cost (gpt-3-turbo only)
thousands_chunks = total_token_count / 1000
estimate_cost = thousands_chunks * 0.002
 
#save results as pdf
rp.generate_pdf_report(topic,bullet_summaries,content_ideas,twitter_tweets,estimate_cost,total_token_count)
print("PDF Report Created!")
