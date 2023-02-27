from . import TextGenerator
from classes.processed_text import ProcessedText
import random

class reponse_question(TextGenerator):
    """
    Fallback text generator, in case we're really at a loss.
    Doesn't care about user input; just dismisses whatever
    they have to say.
    """

    # The default `__init__` should be everything we need.a
    # General rule: don't override it unless you're sure
    # you should.

    def rate(self, in_text: ProcessedText) -> float:
        # Arbitrarily low, but not -∞.
        if (in_text.og_text[in_text.og_text.length()-1] == '?'):
            return 9.9
    ## FIX THIS WITH SMARTER THINKING
    
    def respond(self, in_text: ProcessedText) -> str:
        response = []
        dont_use = ["who","what", "where", "when", "how", "why"]
        i = random.randint(1,in_text.words.length()-1)
        for word, tag in zip (in_text.words, in_text.tags):
            if (word not in dont_use):
                if "who" in in_text.words:
                    if input_tag == 'VBD':
                        response.append("Who is doing " + word + ", why are you doing BLANK?")
                        response.append("Who would honestly do " + word + "? Kinda cringe")
                        response.append("Who is doing that? Why are they doing " + word + "")
                        break
                    elif input_tag == 'NNS':
                        response.append("Who are the " + word + "?.... Oh I'm sorry, didn't really care")
                        response.append("Who had the " + word + ", again?")
                        response.append("Do you really think I care about the " + word + "?")
                        break
                    elif input_tag == 'NN':
                        response.append("Who really thinks about " + word + "?")
                        response.append("Hmmm, I'm not really sure who would be related to those, but what else do you know about that?")
                        response.append("I didn't know they were related to that, please tell me more actually. I really do care about knowing this.")
                        break
                    else:
                        break
                elif "what" in in_text.words:
                    if input_tag == 'VBD':
                        response.append("To " + word + " or not to " + word + ".. That really wasn't ever the question")
                        response.append("You really don't know how to do " + word + "? What kind o- That's fine, we can just move on from this.")
                        response.append("How do you actually do " + word + "?........")
                        break
                    elif input_tag == 'NNS':
                        response.append("Your guess about " + word + " are about the same as me.")
                        response.append("You really don't know what " + word + " is? What kind o- That's fine, we can just move on from this.")
                        response.append("")
                        break
                    elif input_tag == 'NN':
                        response.append("What the freakin heck is a " + word )
                        response.append("Please tell me everything you know about " + word + ". Then I will consider telling you more")
                        response.append("I think its best you consider what you just asked about what " + word + " is... Then come talk to me again")
                        break
                    else:
                        break
                elif "where" in in_text.words:
                    if input_tag == 'VBD':
                        response.append("Where do you usually " + word + " at?")
                        response.append("Have you really thought where people really " + word + " at?")
                        response.append("I actually did some " + word + " on vacation in the past, I know you don't care but I just wanted to share.")
                        break
                    elif input_tag == 'NNS':
                        response.append("Where do you find all the " + word + " of the world?")
                        response.append("I never actually thought about where you would find all the " + word + " in the world")
                        response.append("Maybe you should consider reading a book instead of your phone, cause who really doesn't know really to find these.")
                        break
                    elif input_tag == 'NN':
                        response.append("Didn't you just find one of those " + word + "?")
                        response.append("How the heck do you not know where to find a " + word + "?")
                        response.append("Oh it's literally just down the road from where you live.")
                        break
                    else:
                        break
                elif "when" in in_text.words:
                    if input_tag == 'VBD':
                        response.append("When do you " + word + "? Just asking to get through this conversation.")
                        response.append("Most commonly, people tend to " + word + " when you aren't around.... Cause otherwise, you'd know when")
                        response.append("I actually never thought about when people do that... I'd have to think about this, bring it up tomorrow or something")
                        break
                    elif input_tag == 'NNS':
                        response.append("I'm not an expert on BLANKS but I'd say to just look it up. There's plenty of info.")
                        response.append("I never thought about when to look for " + word + ".")
                        response.append("Oh, I never thought about to think about WHEN something would happen to " + word + "... Please tell me more.")
                        break
                    elif input_tag == 'NN':
                        response.append("Hm, hm, hm, hm...... I didn't think about when we would chat about this really... Check back later?")
                        response.append("I dunno, tbh, probably during a time that makes sense. Ya know?")
                        response.append("I didn't think about when that might happen with " + word + ".")
                        break
                    else:
                        break
                elif "why" in in_text.words:
                    if input_tag == 'VBD':
                        response.append("Why would you realistically wanna " + word + "?")
                        response.append("Why do you BLANK? Cause I know why I " + word + "..")
                        response.append("I never really thought about why  someone would want to to " + word + ". What do you think?")
                        break
                    elif input_tag == 'NNS':
                        response.append("Why " + word + " would do something is quite... Fascinating to think about, don't you think?")
                        response.append("Why do you think that about " + word + "?")
                        response.append("Hm... Quite an interesting thought.. Especially for someone like you, I suppose.")
                        break
                    elif input_tag == 'NN':
                        response.append("Do you actually think about " + word + " that much that you need to talk about it?")
                        response.append("Oh please, tell me why you wanna keep talking about " + word + "? It's truly fascinating, isn't it?")
                        response.append("Mhm.. Mhm... Mhmmmm... I really don't know why you would think that tbh.")
                        break
                    else:
                        break
                elif "how" in in_text.words:
                    if input_tag == 'VBD':
                        response.append("How do you " + word + "? Pft, and here I thought YOU were the expert on " + word + ".")
                        response.append("While I am the local expert on how to BLANK, I did find using youtube to learn more a lot easier... Plus, I don't need to explain further.")
                        response.append("I mean, I know how to do " + word + " but.. Go ahead and explain what you know, and I will tell you when you are wrong.")
                        break
                    elif input_tag == 'NNS':
                        response.append("How do you think " + word + " work? Aren't you the local expert? Why ask me?")
                        response.append("Do you really think thats a good question to see how " + word + " works? Anyone could figure it out... right?")
                        response.append("Ya know, to explain how " + word + " work, in conjunction with your understanding of the situation, is not feasible.. Sorry.")
                        break
                    elif input_tag == 'NN':
                        response.append("I.. I know how to explain how " + word + " works, but even then, it'd probably go over your head")
                        response.append("Honestly, I really don't have the time to explain all the complexities of " + word + ", so I'd just Wikipedia it.. That's some wisdom of the ages.")
                        response.append("Please don't ask me how " + word + " works.. It's too much to explain.")
                        break
                    else:
                        break

        responses.append("Who...? Who asked?")
        response.append("Did you really think I would have an answer to that? I'm not ChatGPT... I actually have an idea of what you are trying to do.")
        response.append("I never really thought about that question, I will have to think about that and get back to you once I come up with an answer.")

        
        return response[random.randint(0,len(reponse)-1)]

                    
                    
