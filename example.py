from pocketsphinx import LiveSpeech
for phrase in LiveSpeech():
    print("Interpreted word: \t" + str(phrase))
    if "hello" in str(phrase):
        print("You're saluting me! =)")
    else:
        print("That's not a salutation! =(")