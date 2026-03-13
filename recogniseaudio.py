import speech_recognition as sr

def record_and_transcribe():
    # 1. Initialize the Recognizer
    recognizer = sr.Recognizer()
    
    # 2. Configure the Microphone
    with sr.Microphone() as source:
        print("Adjusting for noise... please wait.")
        # Adjust for background noise for better accuracy
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Speak now!")
        
        # 3. Capture audio in a loop
        audio = ''
        recording_active = True
        
        while recording_active:
            try:
                with sr.Microphone(device_index=source.device_index) as mic:
                    print("Listening...")
                    audio = recognizer.listen(mic)
                
            except:
                print("No speech detected. Stopping...")
                break
            
            if recording_active:
                try:
                    result = recognizer.recognize_google(audio)
                    if result:
                        return result
                    else:
                        print("Could not understand speech")
                except:
                    print('could not understand audio. please try again. ')
        return None # Return None if recording didn't happen
    
