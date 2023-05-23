import openai
import tiktoken
import prompts as pr

selected_model = "gpt-3.5-turbo"
openai.api_key = "sk-XXXX"


def generate_text_with_openai(user_prompt):
    try:
        completion = openai.ChatCompletion.create(
            model=selected_model,  # you can replace this with your prefered model
            messages=[{"role": "user", "content": user_prompt}],
        )
        return completion.choices[0].message.content
    except:
        return ""


def count_tokens(text):
    try:
        encoding = tiktoken.encoding_for_model(selected_model)
        num_tokens = encoding.encode(text)
        return len(num_tokens)
    except:
        return 0


def blog_post_to_bullet_points(blog_content):
    # Ask LLM for a Summary
    summary_prompt = pr.blog_bullet_summary_prompt.format(InputText=blog_content)
    summary = generate_text_with_openai(summary_prompt)

    return summary


def generate_content_ideas(blog_bullet_points):
    ideas_prompt = pr.bullet_points_content_ideas_prompt.format(
        InputText=blog_bullet_points
    )
    ideas = generate_text_with_openai(ideas_prompt)

    return ideas


def generate_tweets(blog_bullet_points):
    tweets_prompt = pr.bullet_points_to_tweets_prompt.format(
        InputText=blog_bullet_points
    )
    tweets = generate_text_with_openai(tweets_prompt)

    return tweets
