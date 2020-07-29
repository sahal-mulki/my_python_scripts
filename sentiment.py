from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

one_star_data = ["I wish I could give this more than one star, but I can’t. It looked good, and it was free, but there’s just no flow or organization. It’s like a bunch of blog posts thrown together.", "I was shocked by the author’s lack of research. The story starts out great, and I was expecting more of the same. But the veterinarian’s treatment of the dog is totally wrong. I’m a vet technician, so I know what I’m talking about. And the way her boyfriend treats the dog—forget it. It’s abuse, and I couldn’t go on after that.", "This is more of a marketing technique to buy the author’s courses than an informational book. I thought it would be good, but there’s very little to it.", "This book seriously needs a spelling and grammar check. Impossible to read."]
two_star_data = ["I’m only giving this novel two-stars because some parts were great, but other parts were like a self-help book. I didn’t finish it because I didn’t need the advice. I think two different books would work better.", "This was a fast read and a basically good story. But the characters didn’t have depth or personality. Everything was just too easy for them, and there wasn’t any moral of the story or something beyond what happened.", "This has great potential, but I couldn’t finish because of all the typos. I’m willing to forgive a few, but this has so many I moved on to something else.", "I found this book somewhat helpful, but I’m leery of the advice because there’s no documentation or references to the studies the author mentions. The description hyped it up, but now that I’ve read it, I’m disappointed."]
three_star_data = ["This was pretty good. But I had a hard time liking the main character (I thought she’d change), and I wished she had solved the crime instead of her partner.", "Great story overall, but there weren’t enough details and too much blood and gore. It also seems written for kids because it’s so simple (it doesn’t say), and I almost didn’t finish it.", "I thought this book would provide more exact information. I already knew about most of this stuff, but the blog post I read made it seem like a lot more. Some of the information was new, though, and I can definitely use it.", "Loved the story. Didn’t love the grammar errors and typos."]
four_star_data = ["This novel was great. I just couldn’t put it down. But some parts were confusing, and I had to re-read a few times until I could figure out what the author meant. Other than that, super!", "Great story. I gave it only four stars because I felt the lovey-dovey scenes were too much. Just my preference. My favorite part is the ending, and I admit I cried. Keep up the good work! Hoping you’ll tone it down though.", "This was really good, and I’ll mention it to friends. But I thought the style, especially some odd punctuation, made it hard to read at times.", "I am deeply grateful for this book. It opened my eyes to different ways I can trim my constantly overbooked lifestyle and get my sanity and my health back. Thank you! PS I would have given it 5 stars but some sections didn’t have the details I wanted."]
five_star_data = ["I loved this! I could totally relate to the main character, and I loved the ending. Can’t wait for the next one!", "This was just beautiful. The story warmed my heart, and I plan on reading it all over again starting tonight.", "I really appreciate the detailed advice, tips, and instructions in this book. And the worksheets are great. It’s exactly what I need to make my business a success!", "Good story. Held my interest throughout."]

print("By Sahal Mulki")
print("Ps. I didnt make the frame work for this")

for x in one_star_data:
    print("One star data:")
    sentiment = analyzer.polarity_scores(x)
    print(x)
    print(sentiment)
    print(  )
    print(  )

for x in two_star_data:
    print("Two star data:")
    sentiment = analyzer.polarity_scores(x)
    print(x)
    print(sentiment)
    print(  )
    print(  )

for x in three_star_data:
    print("Three star data:")
    sentiment = analyzer.polarity_scores(x)
    print(x)
    print(sentiment)
    print(  )
    print(  )

for x in four_star_data:
    print("Four star data:")
    sentiment = analyzer.polarity_scores(x)
    print(x)
    print(sentiment)
    print(  )
    print(  )

for x in five_star_data:
    print("Five star data:")
    sentiment = analyzer.polarity_scores(x)
    print(x)
    print(sentiment)
    print(  )
    print(  )
