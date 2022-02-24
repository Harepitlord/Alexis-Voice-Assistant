import asyncio
import speech_recognition as sr
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS
from PIL import Image


async def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        audio = r.listen(source, timeout=5, phrase_time_limit=7)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print('Recognizing....')
            print("USER:" + voice_data)
        except sr.UnknownValueError:
            await alexa_speak('Sorry I did not get that')
        except sr.RequestError:
            await alexa_speak('Sorry,my speech server is down')
        return voice_data


async def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en-in')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print("HEALTH-BOT:" + audio_string)
    os.remove(audio_file)


async def respond(voice_data):
    im = Image.open("headache.jpg")
    im2 = Image.open("point.png")
    if 'what is your name' in voice_data:
        await alexa_speak('My name is Alexis')
    if 'what is the time now' in voice_data:
        await alexa_speak(ctime())
    if 'headache' in voice_data:
        await alexa_speak('There a various types of headache\n What kind do you think you have?')
        im.show()
    if 'migraine' in voice_data:
        await alexa_speak(
            "Ginger tea can help\nPreparation\nThinly slice your fresh ginger after cleaning\nBoil it in hot water for nearly 2 to 3 "
            "minutes\nIf you want to add some lemon first remove the rind as it will make the tea bitter\nStir them together\nBring "
            "the water to boil over medium high heat\n Reduce to heat to low simmer and leave this for 5 minutes\nStrain the tea "
            "into a cup and stir it with a drizzle of honey \nDrink it warm ")
        await alexa_speak('or')
        await alexa_speak(
            'Peppermint tea can ease your pain\nPreparation:\nBoil four cups of water\nAdd 15-20 fresh peppermint leaves\nTurn off '
            'the heat and set it aside for 5 minutes\nAdd honey or jaggery if like your tea sweet ')
    if ('stress' or 'tension') in voice_data:
        await alexa_speak('Get some sleep\nDrink a lot of water')
    if 'sinus' in voice_data:
        await alexa_speak('Apply warm compress to the area to relieve pain')
        await alexa_speak('or')
        await alexa_speak('Drink hot water with lemon, honey or ginger')
        await alexa_speak('or')
        await alexa_speak('Drink the cinnamon water, which you boil after you put the cinnamon in the water')
    if 'cluster' in voice_data:
        await alexa_speak('Drink warm tea or coffee to relax the pain')
        await alexa_speak('or')
        await alexa_speak(
            'Grind mustard and pack a paste and apply on your forehead, leave for few minutes and rinse off if your pain subsides ')
    if ("don't have" or 'nothing') in voice_data:
        im2.show()
        await alexa_speak(
            '1.Find pressure point LI-4 by placing your thumb in the space between the base of your thumb and index finger.\n2.Press '
            'down on this point for 5 minutes. Move your thumb in a circle while applying pressure.Be firm, but don’t press so hard '
            'that it hurts.\n3.Repeat the process on your other hand.')
    if 'cough' in voice_data:
        await alexa_speak('Grind Indian nettle and drink its juice,it helps')
        await alexa_speak('or')
        await alexa_speak('Mix a spoon of pepper powder and honey in warm water and drink it ')
    if 'fever' in voice_data:
        await alexa_speak(
            'Tulsi tea is helpful\nPreparation:\nClean the tulsi leaves\nHeat water and tulsi\nMix and let it boil for 10 '
            'minutes\nThen strain it and add lemon juice\nDrink it warm')
        await alexa_speak('or')
        await alexa_speak(
            'Garlic Lemon tea is very effective \nPreparation:\nBoil three cups of water and add three cloves of peeled garlic\nTurn '
            'off after boiling and add half cup of honey\nAdd half cup of lemon juice and mix them well')
    if 'lemon' in voice_data:
        await alexa_speak('Menstrual cramps - Mix lemon juice and one tablespoon of honey to warm glass of water')
        await alexa_speak('Headache - Add a few slices of lemon in your drink or tea')
        await alexa_speak('Fever - Add lemon juice with warm water and honey')
        await alexa_speak('Cold & Flu - Add two tablespoon of honey, and lemon juice to tea')
        await alexa_speak('Upset stomach - Suck on a lemon to gain relief')
        await alexa_speak('Sore throat or Bad Breath - Gargle with lemon juice')
    if 'go offline' in voice_data:
        await alexa_speak('I am going offline,Take care of your health.See you later.Bye')
        exit()


async def main():
    time.sleep(1)
    await alexa_speak('I am Alexis your health assistant!How can I help you?')
    while 1:
        voice_data = await record_audio()
        await respond(voice_data)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


def server_respond(voice_data: str):
    # im = Image.open("headache.jpg")
    # im2 = Image.open("point.png")
    if 'what is your name' in voice_data:
        return ['My name is Alexis', ]
    if 'what is the time now' in voice_data:
        return [ctime(), ]
    if 'headache' in voice_data:
        return ['There a various types of headache\n What kind do you think you have?', ]
        # im.show()
    if 'migraine' in voice_data:
        return [
            "Ginger tea can help\nPreparation\nThinly slice your fresh ginger after cleaning\nBoil it in hot water for nearly 2 to 3 "
            "minutes\nIf you want to add some lemon first remove the rind as it will make the tea bitter\nStir them together\nBring "
            "the water to boil over medium high heat\n Reduce to heat to low simmer and leave this for 5 minutes\nStrain the tea "
            "into a cup and stir it with a drizzle of honey \nDrink it warm ",
            'or',
            'Peppermint tea can ease your pain\nPreparation:\nBoil four cups of water\nAdd 15-20 fresh peppermint leaves\nTurn off '
            'the heat and set it aside for 5 minutes\nAdd honey or jaggery if like your tea sweet ', ]
    if ('stress' or 'tension') in voice_data:
        return ['Get some sleep\nDrink a lot of water', ]
    if 'sinus' in voice_data:
        return ['Apply warm compress to the area to relieve pain', 'or',
                'Drink hot water with lemon, honey or ginger', 'or',
                'Drink the cinnamon water, which you boil after you put the cinnamon in the water']
    if 'cluster' in voice_data:
        return ['Drink warm tea or coffee to relax the pain', 'or',
                'Grind mustard and pack a paste and apply on your forehead, leave for few minutes and rinse off if your pain subsides', ]
    if ("don't have" or 'nothing') in voice_data:
        # im2.show()
        return [
            '1.Find pressure point LI-4 by placing your thumb in the space between the base of your thumb and index finger.\n2.Press '
            'down on this point for 5 minutes. Move your thumb in a circle while applying pressure.Be firm, but don’t press so hard '
            'that it hurts.\n3.Repeat the process on your other hand.']
    if 'cough' in voice_data:
        return ['Grind Indian nettle and drink its juice,it helps', 'or',
                'Mix a spoon of pepper powder and honey in warm water and drink it ', ]
    if 'fever' in voice_data:
        return [
            'Tulsi tea is helpful\nPreparation:\nClean the tulsi leaves\nHeat water and tulsi\nMix and let it boil for 10 '
            'minutes\nThen strain it and add lemon juice\nDrink it warm',
            'or',
            'Garlic Lemon tea is very effective \nPreparation:\nBoil three cups of water and add three cloves of peeled garlic\nTurn '
            'off after boiling and add half cup of honey\nAdd half cup of lemon juice and mix them well']
    if 'lemon' in voice_data:
        return ['Menstrual cramps - Mix lemon juice and one tablespoon of honey to warm glass of water',
                'Headache - Add a few slices of lemon in your drink or tea',
                'Fever - Add lemon juice with warm water and honey',
                'Cold & Flu - Add two tablespoon of honey, and lemon juice to tea',
                'Upset stomach - Suck on a lemon to gain relief',
                'Sore throat or Bad Breath - Gargle with lemon juice']
    if 'go offline' in voice_data:
        return ['I am going offline,Take care of your health.See you later.Bye']
