import os
import json
import aiohttp
import asyncio
from typing import List, Dict, Any, Optional

sample_tweets = {
    "elonmusk": [
        "Humanity is underrated.",
        "Some people use their hair to express themselves. I use Twitter.",
        "I think the biggest problem with today's world is that smart people spend too much time convincing others and not enough time creating things.",
        "When something is important enough, you do it even if the odds are not in your favor.",
        "If you get up in the morning and think the future is going to be better, it is a bright day.",
        "I'd rather be optimistic and wrong than pessimistic and right.",
        "I want to die on Mars. Just not on impact.",
        "Engineering is the closest thing to magic that exists in the world.",
        "Great companies are built on great products.",
        "It's very important to have a feedback loop, where you're constantly thinking about what you've done and how you could be doing it better."
    ],
    "BillGates": [
        "Success is a lousy teacher. It seduces smart people into thinking they can't lose.",
        "Your most unhappy customers are your greatest source of learning.",
        "We all need people who will give us feedback. That's how we improve.",
        "It's fine to celebrate success but it is more important to heed the lessons of failure.",
        "I choose a lazy person to do a hard job. Because a lazy person will find an easy way to do it.",
        "Life is not fair; get used to it.",
        "If you can't make it good, at least make it look good.",
        "Patience is a key element of success.",
        "I really had a lot of dreams when I was a kid. And I think a great deal of that grew out of the fact that I had a chance to read a lot.",
        "The Internet is becoming the town square for the global village of tomorrow."
    ],
    "timcook": [
        "I think the most diverse group will produce the best product; I firmly believe that.",
        "You want to be the pebble in the pond that creates the ripple for change.",
        "We see that privacy is a fundamental human right that people have.",
        "Life is fragile. We're not guaranteed a tomorrow so give it everything you've got.",
        "The sidelines are not where you want to live your life.",
        "The best things I did in life were when I expected nothing in return.",
        "I've learned that life is fragile, and tomorrow is never guaranteed.",
        "I think you should calmly explain what you're doing and why you're doing it. Focus on things where you have a difference of view, but do it in a way that's collaborative.",
        "To whom much is given, much is expected.",
        "When we work on making our devices accessible by the blind, I don't consider the bloody ROI."
    ]
}

sample_tweets["narendramodi"] = [
    "Shaanti ka maarg bhi Shakti se hokar jaata hai. On Buddha Purnima, we reaffirm our commitment to peace and strength.",
    "Operation Sindoor is India's new normal in our fight against terrorism. We will not tolerate nuclear blackmail.",
    "I convey sincere felicitations and best wishes from the people of India to His Holiness Pope Leo XIV.",
    "I strongly condemn the terror attack in Pahalgam, Jammu and Kashmir. Condolences to those who have lost their loved ones.",
    "Spoke to @elonmusk and talked about various issues, including the topics we covered during our meeting in Washington DC earlier this year.",
    "I look forward to strengthening ties with Spain under the leadership of Prime Minister Pedro Sánchez.",
    "Congratulations to the Indian cricket team for their victory in the T20 World Cup 2024. The nation is proud of your achievement.",
    "Mission Divyastra's successful test is a testament to our scientists' hard work and dedication. India is proud!",
    "On Maharana Pratap Jayanti, we remember his courage and dedication to the motherland.",
    "Rabindranath Tagore's thoughts continue to inspire generations. On his birth anniversary, we pay homage to the great poet."
]


sample_tweets["BarackObama"] = [
    "Change will not come if we wait for some other person or some other time.",
    "The best way to not feel hopeless is to get up and do something.",
    "We are the change that we seek.",
    "A change is brought about because ordinary people do extraordinary things.",
    "There's not a liberal America and a conservative America - there's the United States of America.",
    "We don't ask you to believe in our ability to bring change, rather, we ask you to believe in yours.",
    "Where we are met with cynicism and doubt and those who tell us that we can't, we will respond with that timeless creed that sums up the spirit of a people: Yes, we can.",
    "The future rewards those who press on.",
    "We need to steer clear of this poverty of ambition, where people want to drive fancy cars and wear nice clothes and live in nice apartments but don't want to work hard to accomplish these things.",
    "If you're walking down the right path and you're willing to keep walking, eventually you'll make progress."
]

sample_tweets["JeffBezos"] = [
    "Life's too short to hang out with people who aren't resourceful.",
    "If you double the number of experiments you do per year, you're going to double your inventiveness.",
    "The common question that gets asked in business is, 'why?' That's a good question, but an equally valid question is, 'why not?'",
    "If you're competitor-focused, you have to wait until there is a competitor doing something. Being customer-focused allows you to be more pioneering.",
    "A brand for a company is like a reputation for a person. You earn reputation by trying to do hard things well.",
    "I knew that if I failed I wouldn't regret that, but I knew the one thing I might regret is not trying.",
    "The best customer service is if the customer doesn't need to call you, doesn't need to talk to you. It just works.",
    "Work hard, have fun, make history.",
    "If you never want to be criticized, for goodness' sake don't do anything new.",
    "What we need to do is always lean into the future; when the world changes around you and when it changes against you - what used to be a tail wind is now a head wind - you have to lean into that and figure out what to do because complaining isn't a strategy."
]

random_tweets = [
    "Just finished a great book! Highly recommend it.",
    "Can't wait for the weekend to start!",
    "This weather is driving me crazy...",
    "Had the best coffee this morning!",
    "Working on a new project. So excited!",
    "Thinking about what to have for dinner.",
    "Just watched an amazing movie!",
    "Missing the good old days...",
    "Anyone else having trouble sleeping lately?",
    "Just booked tickets for my next vacation!"
]

async def get_user_tweets(username: str) -> List[str]:

    username_lower = username.lower()
    
    if username_lower in sample_tweets:
        return sample_tweets[username_lower]
    return random_tweets