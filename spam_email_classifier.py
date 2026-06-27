# Spam Email Classifier
# A simple program that checks if an email's content contains spam-related keywords.

print("---- Spam Emali Checker ----")

# Take email content from user
# .lower() converts text to lowercase so the word check below isn't case-sensitive
# (e.g. "Winner", "WINNER", and "winner" are all treated the same)
email = input("Enter user email: ").lower()

# Dictionary of suspicious words/phrases mapped to a "spam weight"
# Higher weight = stronger spam signal (e.g. "winner" is more suspicious than "top")
spam_words = {
    "winner": 3,
    "prize": 3,
    "lottery": 3,
    "act now": 3,
    "free": 2,
    "urgent": 2,
    "cash": 2,
    "credit card": 2,
    "limited time": 2,
    "click here": 2,
    "pool": 1,
    "top": 1
}

# Total score above which the email is treated as spam
SPAM_THRESHOLD = 3

# Running total of matched weights and a list of which words matched (for display)
score = 0
matched_words = []

# Check every word/phrase in the dictionary against the email
for word, weight in spam_words.items():
    if word in email:
        score += weight          # add this word's weight to the total score
        matched_words.append(word)

# Classify based on the total score instead of a single match
if score >= SPAM_THRESHOLD:
    print(f"This is a spam mail (score: {score}) : {email}")
    print(f"Matched spam words: {matched_words}")
else:
    print(f"Valid email (score: {score}) : {email}")
