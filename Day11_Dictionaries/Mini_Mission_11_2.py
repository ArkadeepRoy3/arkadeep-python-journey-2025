'''
🎯 Mini Mission 2: Emoji Translator 🐍➡️😊
📝 Your Task:
Write a Python program that:

Takes a sentence as input from the user.

Replaces specific words with emojis using a dictionary.

Prints the translated sentence.

🧩 Example:

Input: I love pizza and music
Output: I ❤️ 🍕 and 🎵

emoji_dict = {
    "love": "❤️",
    "pizza": "🍕",
    "music": "🎵",
    "cat": "🐱",
    "dog": "🐶",
    "sun": "☀️",
    "happy": "😊",
    "sad": "😢"
}
'''
def emoji_translator(emoji_dict):
    input_string = input("Welcome to the Emoji Translator! 😄 Type a sentence:").lower().strip().split()
    print(input_string)
    translated = []
    for word in input_string:
        if word in emoji_dict:
            translated.append(emoji_dict[word] + " ")
        else:
            translated.append(word)
    print(" ".join(translated))

emoji_dict = {
    "love": "❤️",
    "pizza": "🍕",
    "music": "🎵",
    "cat": "🐱",
    "dog": "🐶",
    "sun": "☀️",
    "happy": "😊",
    "sad": "😢"
}
emoji_translator(emoji_dict)