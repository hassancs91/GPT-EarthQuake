blog_bullet_summary_prompt = """\
In the following input, I am going to give you a text you should summarize for me a bullet points format.
I will give you a maximum and a minimum amount of bullet points you should use for the summary.
I am also going to give you the text itself after that.
The language of the text you get should define in which language you write the summary.
For Example, if the text is German the summary should be in German too.
This goes for every language. While writing the summary I want you to remember the following information: When it comes to writing content,
two factors are crucial, "perplexity" and "burstiness."
Perplexity measures the complexity of text. Separately,
burstiness compares the variations of sentences.
Humans tend to write with great burstiness, for example,
with some longer or complex sentences alongside shorter sentences.
AI sentences tend to be more uniform. Therefore,
when writing the following content I am going to ask you to create,
I need it to have a good amount of perplexity and burstiness.
Keep that information in mind while writing.
Maximum: [10], Minimum[5], Text: {InputText} """








bullet_points_to_tweets_prompt = """Generate 5-10 tweets based on the following bullet points [{InputText}]"""

bullet_points_content_ideas_prompt = """Generate Content Ideas based on the following bullet points [{InputText}]"""