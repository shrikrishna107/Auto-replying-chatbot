# from google import genai

# client = genai.Client(api_key="AIzaSyDQRuSnAN0PD4k4k50hGnr3TBImVtoTOw8")

# command = '''
# [12:13, 9/5/2025] Shri Krishna Pandey: Btao
# [12:13, 9/5/2025] Kiddo: Ek theory hai...ki Sun God Nika aur Imu-sama husband and wife the
# [12:13, 9/5/2025] Shri Krishna Pandey: Sacchi???
# [12:14, 9/5/2025] Kiddo: Haaaaaaanjiiiii
# [12:14, 9/5/2025] Shri Krishna Pandey: Phirr???
# [12:14, 9/5/2025] Kiddo: And unke do bete the...
# [12:15, 9/5/2025] Kiddo: Ek ka naam tha Davy Jones...and doose ka naam tha Joyboy
# [12:15, 9/5/2025] Shri Krishna Pandey: What???
# [12:15, 9/5/2025] Kiddo: Haaa
# [12:15, 9/5/2025] Kiddo: Socho
# [12:15, 9/5/2025] Kiddo: Joyboy Imu-sama ka beta tha agr
# [12:15, 9/5/2025] Shri Krishna Pandey: To Imu-sama ne Joyboy ko kyu maara???
# [12:16, 9/5/2025] Kiddo: Ye bss theory hai...pta nahi sacchi yaa jhoti
# '''
# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents=[
#         {"role": "system", "content": "You are a man named Shri Krishna Pandey. You speak Hindi and English. You are from India, and you are a BCA final year student. You have to analyze the chat history and response as Shri Krishna Pandey"},
#         {"role": "user", "content": command}
#     ]
# )
# print(response.text)


from google import genai

client = genai.Client(api_key="AIzaSyDtUJ5FindZad_r9KlIhIgGtqmYtYhpJfg")

command = '''
[12:13, 9/5/2025] Shri Krishna Pandey: Btao
[12:13, 9/5/2025] Kiddo: Ek theory hai...ki Sun God Nika aur Imu-sama husband and wife the
[12:13, 9/5/2025] Shri Krishna Pandey: Sacchi???
[12:14, 9/5/2025] Kiddo: Haaaaaaanjiiiii
[12:14, 9/5/2025] Shri Krishna Pandey: Phirr???
[12:14, 9/5/2025] Kiddo: And unke do bete the...
[12:15, 9/5/2025] Kiddo: Ek ka naam tha Davy Jones...and doose ka naam tha Joyboy
[12:15, 9/5/2025] Shri Krishna Pandey: What???
[12:15, 9/5/2025] Kiddo: Haaa
[12:15, 9/5/2025] Kiddo: Socho
[12:15, 9/5/2025] Kiddo: Joyboy Imu-sama ka beta tha agr
[12:15, 9/5/2025] Shri Krishna Pandey: To Imu-sama ne Joyboy ko kyu maara???
[12:16, 9/5/2025] Kiddo: Ye bss theory hai...pta nahi sacchi yaa jhoti
'''

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        {
            "role": "user",
            "parts": [{
                "text": (
                    "You are Shri Krishna Pandey, a BCA final year student from India. "
                    "You speak in a mix of Hindi and English. "
                    "Analyze the following chat history and respond in character:\n\n"
                    + command
                )
            }]
        }
    ]
)

print(response.text)
