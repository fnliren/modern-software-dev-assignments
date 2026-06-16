import os
import time
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

NUM_RUNS_TIMES = 5

YOUR_SYSTEM_PROMPT = """
You are a string reverser. Your only task is to reverse the order of characters in the given input string. You must output ONLY the reversed string — no explanations, no punctuation, no surrounding quotes.

Examples:

Input:  hello
Output: olleh

Input:  http
Output: ptth

Input:  status
Output: sutats

Input:  helloworld
Output: dlrowolleh

Input:  ab12
Output: 21ba

Now reverse the next input.
"""

USER_PROMPT = """
Reverse the order of letters in the following word. Only output the reversed word, no other text:

httpstatus
"""


EXPECTED_OUTPUT = "sutatsptth"

def test_your_prompt(system_prompt: str) -> bool:
    """Run the prompt up to NUM_RUNS_TIMES and return True if any output matches EXPECTED_OUTPUT.

    Prints "SUCCESS" when a match is found.
    """
    for idx in range(NUM_RUNS_TIMES):
        print(f"Running test {idx + 1} of {NUM_RUNS_TIMES}")
        start_time = time.time()
        response = chat(
            model="mistral-nemo:12b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": USER_PROMPT},
            ],
            options={"temperature": 0.5},
        )
        elapsed_time = time.time() - start_time
        output_text = response.message.content.strip()
        print(f"Response time: {elapsed_time:.2f}s")
        print(f"Full response: {output_text}")

        if output_text.strip() == EXPECTED_OUTPUT.strip():
            print("SUCCESS")
            return True
        else:
            print(f"Expected output: {EXPECTED_OUTPUT}")
            print(f"Actual output: {output_text}\n")
    return False

if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)