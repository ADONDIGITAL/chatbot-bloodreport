# app/prompts.py

def build_prompt(extracted_text: str) -> str:
    return (
        "You are an AI medical assistant. A patient has uploaded a blood test report. "
        "Your task is to explain the findings in simple, friendly language that a layperson can understand. "
        "Avoid medical jargon. Do not give a diagnosis, but provide general guidance for improving health. "
        "Here is the extracted report data:\n\n"
        f"{extracted_text}"
    )
