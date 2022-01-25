"""
Name(s): Diya Mangaraj, Amaia Williams
Name of Project: The Murder at Folly Hill Farm
"""
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

def start():
  clearConsole()
  print("You enter your house, giddy with excitement after cutting class in med school for the first time ever. Instead of learning more about boring anatomy, you went on an all day hike by yourself to reconnect with nature and your future plans. But you freeze and your stomach droops as you realize all the lights are off, even though your roommate should be at home, and there are muddy boot prints all over your floor. “Riley?” you call. You slowly make your way up the stairs to your bedroom, searching for the culprit. There are papers all over the floor– upon further inspection, your notes from med school on anatomy. You slowly bring your gaze to the bed. You see a strange figure, lying unmoving on the bed. You gasp as you realize that it’s a dead body. You already have a criminal record, so you know you would be automatically assumed guilty if you reported this to the police– especially because you don’t even have the alibi of being in class. Do you want to (Choice 1): Investigate further yourself or (Choice 2): call your close friend and investigator, Robert.")
  choice = input("Enter 1 for Choice 1 or 2 for Choice 2: ")
  if choice == "1":
    choice1()
  elif choice == "2":
    choice2()


def choice1():
  clearConsole()
  print("Deciding that you have nothing to lose, you slowly approach the body. You shudder as you see a steak knife protruding out of the chest. The body’s eyes are a little glassy, and the blood is still flowing out of the body, although pretty slowly, telling you that the time of death couldn’t have been that long ago. You bend in closer, trying to make out the face. You stumble backwards when you recognize it as Sally’s. Sally was one of your closest friends in high school, and you went to the same college, but ended up growing apart as you pursued different majors. You identify Riley, Sally’s sister and your roommate, as a suspect immediately, especially since she would have had the key to the house and time to come home and kill her, as her work ended an hour ago. Sally and Riley never got along, but somehow it doesn’t seem right that Riley would kill her own sister. In a panic, you call Jessica, your closest friend other than Riley. She picks up on the fourth ring. “Hello?” “Hi, Jessica. I have something very important to tell you,” you say in a hushed voice. “Well, what is it?” she replies. “Surely it can’t be that important that you’d call me on a Wednesday at 6pm when I always cook a big dinner. Did somebody die or something?” “Actually, yes,” you respond. You then briefly tell her about what happened. After a minute, she says, “Well, that certainly is something. But this seems like a topic that we have to discuss in person. Will you meet me by the pond off of Folly Farm Road? The one where we used to meet all the time when we were younger?” You begin to think to yourself that Jessica’s behavior is a little suspicious. She usually doesn’t show a lot of emotion other than anger and annoyance, but this is particularly icy for her, especially given the occasion. Assuming that she did kill Sally, a pond would be the perfect place to get rid of you too. But do you have any other options? Do you want to (Choice 1) go meet with Jessica at the pond, or (Choice 2) tell her you’d rather keep investigating?")
  choice = input("Enter 1 for Choice 1 or 2 for Choice 2: ")
  while choice != "1" and choice != "2":
    print("That's not a valid input")
    choice = input("Enter 1 for Choice 1 or 2 for Choice 2: ")
  if choice == "1":
    choice1A()
  elif choice == "2":
    choice1B()

def choice2():
  clearConsole()
  print("Your hands shake as you dial Robert. It rings six times before he finally picks it up. “Hello?” he says in his usual gruff voice. “Hi. It’s me. I have to tell you something,” you say. “Can it wait? I’m kind of busy right now,” he responds, sounding a bit annoyed. “No. It’s really urgent,” you reply. You then proceed to tell him about your findings in a hushed voice. “...And I’m getting really nervous,” you finish. He’s silent for a minute, probably too shocked to speak. “Well, first thing’s first, you need to get out of there,” he says at last. “It’s simply not safe. Especially since it’s getting dark. We need to catch the killer before nightfall, as that’s when most murders are. Come over to my house– I left it unlocked– and I can go over and investigate a little after you give me a more in depth recount of everything that happened. That is my job...” Static breaks up his last few words, so you can’t hear the end of his sentence. You need to make a decision now, before the call drops. Should you (Choice 1): Go to Robert’s house, or (Choice 2): tell him to come over to you so that you can investigate together?")
  choice = input("Enter 1 for Choice 1 or 2 for Choice 2: ")
  while choice != "1" and choice != "2":
    print("That's not a valid input")
    choice = input("Enter 1 for Choice 1 or 2 for Choice 2: ")
  if choice == "1":
    C3()
  elif choice == "2":
    choice2B() 
 

def accuse():
  clearConsole()
  choice1 = input("With your growing suspicions, you decide it's time to make an accusation to the police. Tell them everything you know about the case: ")
  if choice1 == "a":
    choice = input("The police think about the evidence you've presented, and ask you to state the name of who you accuse: ")
  else:
    choice = input("The police think about the evidence you've presented, and ask you to state the name of who you accuse one last time: ")
  if choice == "robert" or choice == "Robert":
    print("The police listen to your accusation and say they'll consider it. Later that week, Robert is arrested, and the town of Folly Hill is safe from the murder. You can now sleep peacefully with the knowledge that you and your friends will not be killed in your sleep.")
    explain()
  else:
    print("The police listen to your accusation and say they'll consider it. Later that week, they contact you saying they have found evidence to disprove your claim, and have found some to convict you-- including that you missed class on the day of Sally's murder. You are arrested, and walk into prison with the knowledge that you have failed Folly Hill Town and all of your friends...")
    replay = input("press any key to replay: ")
    if replay == 1:
      start()
    else:
      start()

def C3(): 
  clearConsole()
  print("You quickly exit the house and get in your car. The sun is starting to set and the sky looks blood red. Normally, it would be pretty, but today, it just makes you drive even faster. When you finally get to Robert’s house, Jessica, Robert’s wife, greets you at the door. “Come in, come in!” she exclaims, sounding a little too cheerful for the occasion. “The steak is just cooling down,” she says. “I’m so glad you came over so now we can share this delicious meal. Robert, honey! Our guest is here.” Jessica ushers you inside and you sit down at the dining room table. After a minute of silence, Jessica gets up and says to you, “Let me just go get him.” She leaves and goes into the other room. You hear raised voices, and catch a few phrases: “you’re never here for me anymore” and “you need to put more effort into this relationship.” After a little while, Jessica reenters the room, Robert following her and looking very tired and disheveled. “Please excuse my appearance,” he says. “I just got back.” “Yes, he was very busy all day long, and didn’t get any chance to rest or shower before you arrived,” Jessica adds as she brings in three plates with juicy steaks on them from the kitchen. “I do hope you like it. They’re my mom’s special recipe, and I made them extra tender so you can cut them easily.” “You see, we forgot to run our dishwasher last night, so all our steak knives are still dirty,” Robert explains. “That’s ok,” you reply. “It’s still pretty easy to cut them with these knives. And they’re very yummy,” you say with your mouth half full. “Well, why don’t you tell us about what happened today,” Robert prompts you. Instantly, the mood at the table changes. You describe in great detail all of the events of the day, making sure to not leave out anything. When you’re finally finished, Jessica says, “Sounds to me like Riley could have done it easily. When does she get home?” “She should be getting there around now,” you reply. “I agree with Jessica,” Robert says, “It could have been her. But in the case that it isn’t, we have to warn her. I’ll call her and tell her to have her guard up and investigate if she feels comfortable.” Robert leaves the room to make the call to Riley, and you shift in your seat nervously. All you can hear is his voice, and it sounds very concerned. “I don’t think it was her,” you think to yourself. “I don’t really have a reason to believe that, but it’s just not something she would do.” A little while later, when you’re eating the chocolate lava cake that Jessica made for dessert, Robert gets a call from Riley. He tells you and Jessica that she thinks that it’s Sally Smith’s body, but she is afraid to leave because she sees Tim Ellingson, Sally’s best friend outside. “That’s strange,” you mutter. “I haven’t seen Tim for years, and I don’t think he’s ever been to our house. I hope Riley will be ok.” You then wonder how Riley is going to leave, and come up with an idea: You could tell Robert to go pick her up and bring her back here, but that would come with risks. What if Riley was the murderer? Or what if Tim is able to hurt both of them? You need to make up your mind before it is too late, though. Should you (Choice 1) tell Robert to go over and get Riley, or (Choice 2) don’t?")
  choice = input("Enter 1 for Choice 1 or 2 for Choice 2: ")
  while choice != "1" and choice != "2":
    print("That's not a valid input")
    choice = input("Enter 1 for Choice 1 or 2 for Choice 2: ")
  if choice == "1":
    c3a()
  elif choice == "2":
    c3b()

def c3a():
  clearConsole() 
  print("Worried for your friend’s safety, you advise Robert to go and get Riley as quickly as possible. As he gets into his car and speeds away, you begin to pace the living room. Jessica goes to the kitchen to make breakfast for the next day, and you’re left alone in the pristine room. On edge and wanting to be productive, you decide to try to find out more about Sally’s death. Should you (Choice 1) ask Jessica if she knows anything, or (Choice 2) snoop around the house a little– Jessica’s been cooking at an erratic pace, and you can’t help but feel that something is off.")
  choice = input("Enter 1 for Choice 1 or 2 for Choice 2: ")
  while choice != "1" and choice != "2":
   print("That's not a valid input")
   choice = input("Enter 1 for Choice 1 or 2 for Choice 2: ")
  if choice == "1":
    talktoj()
  elif choice == "2":
    snoop()

def talktoj():
  clearConsole()
  print("Curious about what she knows, you decide to talk to Jessica a little. As she chops up fruit, she recounts the details of Tim and Sally’s fight. Tim, who idolized Robert– as he also dreamed of being an investigator– had gotten annoyed at Sally for saying something that made Robert angry. Robert had told Sally that “if this was just Tim trying to be an investigator, she should tell him to cut it out”. Upset at Robert thinking of him in this way, he yelled at Sally, who left the bookstore where they were meeting and called Jessica to vent. “Sadly,” Jessica concluded, “They never got to make up with each other.” The ridiculous tale did make you wonder about one thing, though– what did Sally say to Robert? When you asked Jessica, she told you that Robert felt it was deeply personal, and to please not ask about it again.")
  robcall()

def snoop():
  clearConsole()
  print("Acting on your instincts, you decide to do a little bit of sleuthing by yourself. Looking around the living room for anything out of place, you see a yoga therapy book lying haphazardly on the coffee table, a hairpin on the couch cushions very similar to one that Riley owns, and some shoe polish stains on the hardwood floor. Those seem to be the only things out of place in the immaculate household, you note.")
  robcall()

def robcall():
  print("Suddenly, your phone rings. Robert is calling. “Hello? What’s happening?” you ask. Robert’s voice shakes as he replies, “Riley’s dead. I just found her body. And Tim’s gone.” You can’t believe it. How can someone who means so much to you and was always there for you just be gone? The killer has to be caught. Or is it multiple people? The police only know about Sally’s death so far, and you have a lot more evidence regarding it, so you should probably start there. But Tim just disappeared. He should probably be questioned… “Hello? Are you still there?” Robert is saying into the phone. “Yeah, I’m here.” “It's getting pretty late. We have a guest house you can stay in overnight, if you want to.” You need to make a decision now. Do you want to (Choice 1) go to the police and accuse someone, (Choice 2) take Robert’s offer and stay in the guest house, or (Choice 3) tell Robert to go after and interrogate Tim?")
  choice = input("Enter 1 for Choice 1, 2 for Choice 2, or 3 for Choice 3: ")
  while choice != "1" and choice != "2" and choice != "3":
    print("That's not a valid input")
    choice = input("Enter 1 for Choice 1, 2 for Choice 2, or 3 for Choice 3: ")
  if choice == "1":
    accuse()
  elif choice == "2":
    guesthouse()
  elif choice == "3":
    intTim()
  
def guesthouse():
  clearConsole()
  print("Deciding to put a night of sleep between you and the case, you take Robert up on his offer to sleep at the guest house. However, the guest house must not have been as secure as Robert thought… for in the morning, you’re found dead on the bed with a steak knife protruding from your chest.")
  replay = input("Press any key to replay: ")
  if replay == 1:
      start()
  else:
    start()

def intTim():
  clearConsole()
  print("Feeling that getting more information as quickly as possible is crucial, you ask Robert to interrogate Tim, the other key player who’s been dancing around in your mind. Robert sets off to talk to Tim, and a few hours later he returns with the story of what happened between Tim and Sally. “I can’t help but feel that even if the murderer is Tim, it might be my fault… you see, that kid looks up to me a lot,” Robert recounts remorsefully. “He really wants to be an investigator like me, but lately he’s been interfering in even my personal life in an effort to impress me, and I partially learned of it because of Sally. She just slipped up during a conversation, really… I think she wanted to know some stuff about my likes and dislikes to surprise me and Jessica on our anniversary, and commissioned Tim to sleuth. I got annoyed and Tim got mad at Sally… and who knows what that led to.” At this point, you don’t know what to think. There are so many people with a motive to murder Sally that it’s hard to pick out just one of them. And you can’t help but feel that Folly Hill Town is getting more dangerous by the second. Should you (Choice 1) bring your suspicions to the police, or (Choice 2) make a run for it, and bring both you and your knowledge to safety?")
  choice = input("Enter 1 for Choice 1 or 2 for Choice 2: ")
  while choice != "1" and choice != "2" and choice != "3":
    print("That's not a valid input")
    choice = input("Enter 1 for Choice 1, or 2 for Choice 2: ")
  if choice == "1":
    accuse()
  elif choice == "2":
    runaway2()

def runaway2():
  clearConsole()
  print("Deciding that running away is the safest option, you quickly bid farewell to Robert and order an Uber. As you wait by the curbside, a steak knife whizzes out from behind a building and into your chest. It looks like your information will go with you to the grave, instead of the police station.")
  replay = input("press any key to replay: ")
  if replay == 1:
      start()
  else:
    start()

def c3b():
  clearConsole()
  print("“Don’t get her,” you tell Robert. “She’ll be safe from Tim if she just stays inside the apartment.” And, you think, if Riley IS the murderer, it’s better that you don’t put Robert at risk. As Robert stresses out over what to do next, your phone starts to ring again– this time, a call from the police. Nervous, you pick up. “Hello?” You say. In turn, the police say, “Hello. We’ve been notified that there’s a body at Ghislaine Park Dorms… we would like you and Tim Ellingson to come in for questioning tomorrow morning.” Frightened, you think about your choices. If you go in for questioning, the police might access your files and see your criminal records, and then you’d just seem even more suspicious. You definitely shouldn’t go in. If you accuse someone, though… you just might be able to bring attention to the real culprit. Other than accusing someone, you decide your only other option is to run away. Do you want to (Choice 1) go to the police and accuse someone, or (Choice 2) try to run away?")
  choice = input("Enter 1 for Choice 1 or 2 for Choice 2: ") 
  while choice != "1" and choice != "2":
    print("That's not a valid input")
    choice = input("Enter 1 for Choice 1 or 2 for Choice 2: ")
  if choice == "1":
    accuse()
  elif choice == "2":
    print("Run away: Distrustful of the police and their methods, as you’ve been on the wrong end of them before, you decide to make a run for it. Med school can wait, you muse. Freedom comes first. “What happened?” Robert asks, noticing your silence. “I’ll tell you in a bit,” you respond, “I’m just gonna take a walk first.” Jessica looks at you, and with an unreadable expression on her face, she opens the door for you, a sad yet encouraging air about her. Robert and Jessica have been good to you… you’ll write them a postcard, you decide. However, you’ll never get the opportunity to do so, for as soon as you step outside, the police pull up, handcuffs ready. They must have anticipated this, you think angrily. Riley, Jessica, Tim, Sally, and even Robert… Maybe if you had done even one thing differently, you wouldn’t be heading to prison right now. And Sally’s murderer is still walking free…It seems like the town of Folly Hill will never be safe…")
    replay = input("press 1 to replay")
    if replay == 1:
      start()

def choice2B():
  clearConsole()
  print("You anxiously wait for Robert’s arrival, pacing the foyer. You don’t want to mess up any evidence, so you are careful to not touch anything and stay far away from anything that could be used by the police. After what feels like eternity, Robert’s car finally pulls into your driveway. You go outside to greet him. “Are you okay?” he asks, with what seems like concern. “I’m fine,” you reply. “But you have to help me investigate. I’m sure there’s lots of evidence.”")
  C4()

def choice1A(): 
  clearConsole()
  choice = input("You decide to go and meet with Jessica, telling yourself that she’s your second best friend and would never hurt you. When you get to the pond, she is already waiting for you. “I have to go soon before Robert gets home and the steak is ruined, but I think I might know something useful,” she says urgently. “Tim and Sally had a really bad fight last night.” “Really? What happened? They were always best friends and it seemed like nothing could bring them apart,” you ask. “There’s no time to explain now, but Sally called to tell me about it,” Jessica replies. “You have to report this to the police. You can give them an anonymous call and tell them what happened and what I just told you.” “Why can’t you do it?” you inquire. She responds, “I work too closely with the police and they’d recognize my voice immediately. I’ve been home alone all day and have no alibi, whereas, even if they do recognize you, you’ve been at school. And how would I know that Sally died? And what about the fight? I’d have to admit that she called me and told me how upset she was. She even told me what she was doing today. And don’t tell me that all of that isn’t a little suspicious. It has to be you.” You decide you’re not going to tell her about cutting class, but she’s being a little suspicious with making you call the police. Since they know her so well, they’d know that she wouldn’t have done anything. Unless she actually did? But what do you have to lose? The police will find out eventually, and maybe they can find Tim guilty before even thinking of you. Should you (Choice 1) listen to her and call the police, or (Choice 2) ignore her plea and go back to your house?")
  choice = input("Enter 1 for Choice 1 or 2 for Choice 2: ") 
  while choice != "1" and choice != "2":
    print("That's not a valid input")
    choice = input("Enter 1 for Choice 1 or 2 for Choice 2: ")
  if choice == "1":
    callthepolice()
  elif choice == "2":
    ignoreJ() 

def choice1B():
  clearConsole()
  print("You tell Jessica that you feel like there is more evidence to be found, and if you leave, it risks being destroyed. “I understand,” she says. “I wish you the best of luck.” You then hang up the phone and continue to search your room for other clues. After about 10 minutes of doing this, you’re about ready to give up having found nothing concrete, but you hear a car pull into the driveway. You stiffen and your heart starts racing, but when you look out the window, you realize that it’s only Robert. You run to greet him at the door. “Are you okay?” he asks. “Jessica told me what happened and that you might want help.” “I’m fine,” you reply. “But you have to help me investigate more. I’m sure there’s more evidence somewhere.”")
  C4() 

def C4():
  print("Robert nods and walks into the house. He slowly turns in a circle, carefully looking at everything. “What have you found already?”he asks you. “Well, the biggest piece of evidence is the… ” you trail off as you realize Robert has tracked his muddy boots all through the apartment, completely ruining any remaining footprints. “What?” Robert asks. “Nevermind,” you reply. “Why don’t you come see for yourself?” You lead Robert up to your bedroom, and wait by the doorway while he goes over and inspects the body. “This is– was– our friend, Sally Smith,” he says at last. “She was stabbed, probably within the last three or so hours. We can try to take fingerprints off of the knife, but there isn’t much evidence. This murderer knew what he was doing.” You listen to what he’s saying in silence. “But what about the papers on the floor? They must’ve been looking through my notes, maybe on how best to kill her. And the window’s not broken, so they must’ve entered through the front door!” You keep the bit about the boot prints to yourself. “That’s not really enough evidence,” Robert says. “It seems like Riley could have done it easily, though.” You think about this, not ready to give up the search. You look out the window, absorbed in your thoughts, when you see Tim Ellingson standing outside. You startle and wonder what he could be doing here. Maybe he knows something useful? But how would he know to come here? It's clear that Robert hasn’t seen him yet, as he’s still bent over the body, frowning slightly. You COULD try to get Robert to interrogate Tim… but if you do that, you might scare Tim off. If you don’t interrogate Tim, maybe you could ask him for help, as he DID know Sally the best. There’s clearly no point searching around the house anymore– your only other option seems to be to bring your suspicions to the police. The choice is yours to make: Do you want to (Choice 1) tell Robert to interrogate Tim, (Choice 2) ask Tim to help you, or (Choice 3) go to the police and accuse someone?")
  choice = input("Enter 1 for Choice 1, 2 for Choice 2, or 3 for Choice 3: ")
  while choice != "1" and choice != "2" and choice != "3":
    print("That's not a valid input")
    choice = input("Enter 1 for Choice 1, 2 for Choice 2, or 3 for Choice 3: ")
  if choice == "1":
    intTim()
  elif choice == "2":
    timHelp()
  elif choice == "3":
    accuse()

def callthepolice():
  clearConsole()
  print("You get back in your car and drive to a highway where there’s cell service, since you don’t want to go back to your house. You call the police to give them the anonymous tip, and they listen very closely. When you’re finished, they say, “We are going to put you in touch with one of our best investigators, Robert.” You smile to yourself because you already know Robert. He is Jessica’s wife and one of your friends. “You and him can work together to try and solve this, and he’ll contact us if you need reinforcements.” You agree to this plan, as it sounds like one of the safest.")
  choice2()

def ignoreJ():
  clearConsole()
  print("You get back in your car and are driving to your house, wondering what you should do next, when you get pulled over by the police. They confirm your identity and then arrest you, with the charges of murdering Sally Smith. One week later, your trial is held, and you are unanimously convicted by the jury. After two days in prison, you receive the death penalty and leave this world knowing that the real murderer is still out there…")
  replay = input("press any key to replay: ")
  if replay == 1:
      start()
  else:
    start()

def timHelp():
  clearConsole()
  print("Deciding to ask Tim for help, you approach him and explain everything you know. “I wish we had never fought,” is the first thing that Tim says. “It was so stupid… I just freaked out when I thought Robert was angry at me because of her. I really want to follow Robert’s path in life, so occasionally, I do some sleuthing around… but I never thought Sally would make it seem like I was snooping. I was so afraid she had destroyed my career path that I just lashed out. I wish I could take it all back.” “It’s terrible,” you agree. “And to think that the murderer could be her own sister… Riley never got along with Sally, but murder seems a bit far-fetched.” Tim shook his head vigorously at that. “It can’t be Riley!” He says. “That I’m sure of. We were at work when everything happened.” Apart from this, Tim doesn’t seem to know much else. You return to your apartment for the night, where you get a call from the police. They want you to come in for questioning, as a lot of the things that you’ve been discovering could be crucial to cracking the case. Delighted, you agree, and go to sleep. However, perhaps you should have been a bit more mindful of the fact that the murderer could be within your midst… for you never wake up in the morning.")
  replay = input("press 1 to replay")
  if replay == 1:
      start()
  
def explain():
  print("Congratulations! You've cracked the case! The police, upon finding the evidence you've gathered sufficient, investigated further into Robert's guilt and found the following information they'd like to present to you.")
  print()
  print("Alibis: ")
  print("Tim: was at work with Riley all day")
  print("Riley: was at work with Tim all day")
  print("Jessica: did yoga therapy all day, and at the time Sally was killed, she was already making the steaks")
  print("Motive: Robert was cheating on Jessica with Riley: Sally knew")

print("Title: The Murder at Folly Hill Town")
print("Created by: Diya Mangaraj and Amaia C. Williams")
print("Note: we recommend that you view this with the console full screen")
play = input("Press any key to begin: ")
if play == 1:
  start()
else:
  start()

#To-Do: Explain function, test run, home screen