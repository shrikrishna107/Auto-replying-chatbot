import pyautogui
import pyperclip
import time
from google import genai

# Small delay to give you time to switch to the correct screen
# time.sleep(3)

client = genai.Client(api_key="AIzaSyDtUJ5FindZad_r9KlIhIgGtqmYtYhpJfg")

def is_the_last_message_from_sender(chat_history, sender_name = "Belle"):
    messages = chat_history.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True
    return False

# Step 1: Click on the icon at (1265, 1045)
pyautogui.click(995, 1049)
time.sleep(1)
while True:
    # Step 2: Drag from (696, 437) to (1858, 897) to select text
    pyautogui.moveTo(682, 236, duration=0.5)
    pyautogui.dragTo(950, 950, duration=1, button='left')
    time.sleep(3)

    # Step 3: Copy selected text (Ctrl + C)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(697, 262)
    time.sleep(0.5)

    # Step 4: Get text from clipboard
    chat_history = pyperclip.paste()

    print("Copied text:")
    print(chat_history)
    
    if is_the_last_message_from_sender(chat_history):
        response = client.models.generate_content( 
            model="gemini-2.5-flash",
            contents=[ 
                { "role": "user", "parts":
                 [{ "text": (   "You are Shri Krishna Pandey, a BCA final year student from India. "
                                "You speak in a mix of Hindi and English. "
                                "Analyze the following chat history and respond in character. "
                                "The Output should be the next chat response as Shri Krishna Pandey. "
                                "Try to keep the text responses short, not too short that it starts to seem rude, but not too long to seem annoying. Keep them at the exact lenght. Not too short, not too long. "
                                "Add emojis in the response, and try not to bold any word, phrase or sentance in the response:\n\n" + chat_history ) }] } ] )

        print(response.text)
        pyperclip.copy(response.text)

        # Step 5: Click on the text area
        pyautogui.click(846, 975)
        time.sleep(1) #Wait for 1 second to ensure that the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')

        # Step 7: Press Enter
        pyautogui.press('enter')