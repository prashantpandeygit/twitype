from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
from typing import List, Dict, Any, Optional
from twitter_api import get_user_tweets
from personality_analyzer import analyze_tweets
from mbti_classifier import classify_personality

app = FastAPI(
    title="Twitter MBTI Personality Analyzer",
    description="API for analyzing Twitter users' personality based on their tweets",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://xpersonalitypredictor.vercel.app"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TweetEvidence(BaseModel):
    text: str
    traits: List[str]

class TraitScores(BaseModel):
    extraversion: float
    introversion: float
    sensing: float
    intuition: float
    thinking: float
    feeling: float
    judging: float
    perceiving: float

class PersonalityAnalysisResponse(BaseModel):
    username: str
    personality_type: str
    traits: TraitScores
    tweet_evidence: List[TweetEvidence]

class PersonalityTypeResponse(BaseModel):
    type: str
    title: str
    description: str
    traits: List[str]


mbti_types = {
    "INTJ": {
        "title": "The Architect",
        "description": "INTJs are analytical problem-solvers, innovative and independent. They drive to implement their ideas and achieve their goals.",
        "traits": ["Analytical", "Logical", "Strategic", "Independent", "Perfectionist"]
    },
    "INTP": {
        "title": "The Logician",
        "description": "INTPs are logical, original, creative thinkers. They seek to develop logical explanations for everything that interests them.",
        "traits": ["Inventive", "Logical", "Contemplative", "Theoretical", "Objective"]
    },

}

@app.get("/")
def read_root():
    return {"message": "Twitter MBTI Personality Analyzer API"}

@app.get("/analyze/{username}", response_model=PersonalityAnalysisResponse)
async def analyze_personality(username: str):
    try:
        tweets = await get_user_tweets(username)
        
        if not tweets:
            raise HTTPException(status_code=404, detail=f"No tweets found for user @{username}")
        
        trait_indicators = analyze_tweets(tweets)
        
        personality_type, trait_scores = classify_personality(trait_indicators)
        
      
        tweet_evidence = []
        for tweet in tweets[:5]:  
            tweet_traits = []
            if "I" in personality_type:
                tweet_traits.append("Introversion")
            if "N" in personality_type:
                tweet_traits.append("Intuition")
            
            tweet_evidence.append(TweetEvidence(
                text=tweet,
                traits=tweet_traits[:2] 
            ))
        
        response = PersonalityAnalysisResponse(
            username=username,
            personality_type=personality_type,
            traits=TraitScores(
                extraversion=trait_scores["E"],
                introversion=trait_scores["I"],
                sensing=trait_scores["S"],
                intuition=trait_scores["N"],
                thinking=trait_scores["T"],
                feeling=trait_scores["F"],
                judging=trait_scores["J"],
                perceiving=trait_scores["P"]
            ),
            tweet_evidence=tweet_evidence
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/personality-type/{type}", response_model=PersonalityTypeResponse)
async def get_personality_type(type: str):
    type_upper = type.upper()
    if type_upper not in mbti_types:
        raise HTTPException(status_code=404, detail=f"Personality type {type_upper} not found")
    
    type_data = mbti_types[type_upper]
    
    return PersonalityTypeResponse(
        type=type_upper,
        title=type_data["title"],
        description=type_data["description"],
        traits=type_data["traits"]
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)