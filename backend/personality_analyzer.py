from typing import List, Dict, Any, Set
import re
import random

trait_indicators = {
    "E": [  # Extraversion
        r'\b(party|social|friends|people|crowd|group|team|together|meet|gathering|extrovert)\b',
        r'\b(love to talk|hanging out|going out|social event|meet new people)\b',
        r'(!)+' 
    ],
    "I": [  # Introversion
        r'\b(quiet|alone|solitude|peace|book|reading|reflect|think|contemplate|introvert)\b',
        r'\b(need space|personal time|by myself|staying in|home body|deep thought)\b',
        r'\b(few close friends|quality over quantity|meaningful conversation)\b'
    ],
    "S": [  # Sensing
        r'\b(fact|detail|practical|realistic|actual|concrete|specific|exact|precise)\b',
        r'\b(experience|observation|present|now|today|current|notice|see|hear|touch)\b',
        r'\b(what happened|what is|in reality|actually|in fact|in detail)\b'
    ],
    "N": [  # Intuition
        r'\b(idea|concept|theory|abstract|imagine|possibility|future|potential|vision)\b',
        r'\b(wonder|what if|could be|might be|someday|envision|big picture|meaning)\b',
        r'\b(connection|pattern|insight|inspiration|innovate|creative|novel|new approach)\b'
    ],
    "T": [  # Thinking
        r'\b(logic|analyze|objective|rational|reason|principle|system|efficiency|effective)\b',
        r'\b(truth|fair|justice|critical|evaluate|assess|measure|problem solve|therefore)\b',
        r'\b(pros and cons|decision matrix|logical conclusion|objective view)\b'
    ],
    "F": [  # Feeling
        r'\b(feel|emotion|care|value|appreciate|heart|compassion|empathy|harmony)\b',
        r'\b(happy|sad|love|like|dislike|hurt|enjoy|pleasure|pain|sentiment|personal)\b',
        r'\b(what matters|important to me|I care about|means a lot|touched|moved)\b'
    ],
    "J": [  # Judging
        r'\b(plan|schedule|organize|decide|goal|achievement|complete|finish|deadline)\b',
        r'\b(structure|order|system|routine|regular|consistent|punctual|reliable)\b',
        r'\b(should|must|have to|need to|responsibility|obligation|duty|commit)\b'
    ],
    "P": [  # Perceiving
        r'\b(spontaneous|flexible|adapt|option|possibility|explore|discover|change)\b',
        r'\b(maybe|perhaps|whatever|whenever|play it by ear|go with the flow|improvise)\b',
        r'\b(open-ended|undecided|postpone|procrastinate|last minute|spontaneity)\b'
    ]
}

def analyze_tweets(tweets: List[str]) -> Dict[str, int]:


    trait_counts = {trait: 0 for trait in "EISNTFJP"}
    

    for tweet in tweets:
        tweet_lower = tweet.lower()
      
        for trait, patterns in trait_indicators.items():
            for pattern in patterns:
                if re.search(pattern, tweet_lower, re.IGNORECASE):
                    trait_counts[trait] += 1
                    break 
    
    return trait_counts

def analyze_tweet_for_traits(tweet: str) -> Set[str]:

    tweet_lower = tweet.lower()
    found_traits = set()
    
    for trait, patterns in trait_indicators.items():
        for pattern in patterns:
            if re.search(pattern, tweet_lower, re.IGNORECASE):
                found_traits.add(trait)
                break 
    
    return found_traits

def get_trait_words(trait: str) -> List[str]:

    trait_words = {
        "E": ["Extraverted", "Outgoing", "Social", "Expressive", "Enthusiastic"],
        "I": ["Introverted", "Reserved", "Reflective", "Private", "Thoughtful"],
        "S": ["Sensing", "Practical", "Detail-oriented", "Factual", "Realistic"],
        "N": ["Intuitive", "Conceptual", "Imaginative", "Theoretical", "Abstract"],
        "T": ["Thinking", "Logical", "Analytical", "Objective", "Principled"],
        "F": ["Feeling", "Empathetic", "Compassionate", "Value-driven", "Harmonious"],
        "J": ["Judging", "Organized", "Planned", "Decisive", "Structured"],
        "P": ["Perceiving", "Adaptable", "Flexible", "Spontaneous", "Open-ended"]
    }
    
    return trait_words.get(trait, ["Unknown"])

def get_trait_percentage(counts: Dict[str, int], trait1: str, trait2: str) -> Dict[str, float]:

    total = counts[trait1] + counts[trait2]
    
    if total == 0:
        
        if random.random() > 0.5:
            return {trait1: 55.0, trait2: 45.0}
        else:
            return {trait1: 45.0, trait2: 55.0}
    
  
    percent1 = (counts[trait1] / total) * 100
    percent2 = (counts[trait2] / total) * 100
    
    noise = random.uniform(-5, 5)
    percent1 += noise
    percent2 -= noise
    
    percent1 = max(min(percent1, 95), 5)  
    percent2 = 100 - percent1
    
    return {trait1: percent1, trait2: percent2}