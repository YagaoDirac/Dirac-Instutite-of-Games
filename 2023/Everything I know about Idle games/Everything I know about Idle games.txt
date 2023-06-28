Everything I know about Idle games

YagaoDirac

github.com/yagaodirac/Internal-Reference-of-Dirac-Instutite-of-Game\2023

   Recently, I saw people started to make idle games more than 1 or 2 years ago. The pandemic finally left us. But very soon, I started to be aware of the issues in the games people are making. Since 2017, I played almost every idle game I can find, and I almost remember all of them. They are literally hundreds, if not more than a thousand. Most of them are similar, some are in a series, most are individual. 6 years later, people are still making similar games, and making the same mistakes, running into the same problems. Again, the experience in game industry is not accumulated enough. This is why I'm now writing this article, in English.

   Let me write it as short as possible.

======Chapter 1, what is idle game.
   Idle game is a genre, it's similar to managing, clicker, and sometimes it's not possible to distinguish them. The key content is the increasing of numbers. But theorically, it's not about the the increasing of numbers.
   So, what is idla game about.
   In my previous researchment, the result is like, the amount of information corresponds to the lifespan of a video game. Log(amount of content) is proportional to the time people play it.
   Idle game simplified almost everything, which makes it different from clicker, but the theory still holds, the amount of content. Or, how long does it take for someone to learn the game. This duration is the maximun of lifespan of a game, while the actual length is determined by when people are not possible to find new content in the game, it feels like the game stucked. 
If this conclusion is correct enough, button array doesn't have more content amount than a single button, a set of similar upgrades doesn't have more content than a single but individual upgrade.
For example:
Upgrade A: 10 coins to get +1coin/sec
   If A is the first time for such formula, such form to appear in this game, it has information.
Upgrade B: 1000 coins to get +10coin/sec
   If B follows A, then it doesn't have any information with it.
So, if you make a lot upgrades like this, people don't get new content when they only have such upgrades, and if this costs a super long time, people would probably feel stucked, and likely to quit.
   If you question this conclusion, you can make a game where all people can play is 1 array of upgrades, they have the same form, but carefully balanced, with similar formula to determine the numbers. This sounds like an extreme example only for demonstration, but it happens sometimes.

======Chapter 2, how to add new content into a game
   Not only for idle games, for most video games, devs are supposed to add real informations into games, but a lot of times, they don't know they should do this.
   I'm not gonna talk about other genres. So, how to add information/content to a idle game, and really increase its amount of content/information?

   First of all, what can be used to do this? In most idle games, they are resources and upgrades. If the game is multiplayer, then you at least can take use of it, like transaction system, pvp, or something. Very few idle games have test system in which, people try out their ideas and figure out their best way to idle, I'll explain this latter.

   Resource is pretty basic, the only thing you can do is adding more kind of resources to the game, and unlock them early enough. According to my experience, I recommend you try 2~4 resource for the beginning of your game, and unlock 1 new kind a time. The reason is like, 1 is too few, 2 or 3 is just ok. Recently, in idle games, people are tend to start with 2 kinds of resources, but the interaction between them is pretty weak. Years ago, the second resource is basically called prestige score, and is seperated from the forst 1, and only obtained when prestige(resetting the normal progress to get some special cash to buy higher level upgrades which is not reset when resetting the normal progress). It was actually 1 resource for the normal layer, and 1 for the prestige layer, or "global upgrades". If you consider prestige mechanism is only for code/game assets reuse, then it's 1 resource only.
   Recently, I saw some games start with 2 resources, but they are not for interaction, or to support more recipes. I think people will try it.
   If the game starts with only 1 kind of resource, then upgrades, recipes can only consume nothing or this only kind of resource, and generates this only kind of resource. This limits what devs can add and people can play.
   
   Then, upgrades.
   Upgrades can come in a lot forms, upgrades, recipes, challenges, unlocks/achievements, the only difference is if it's repeatable. Basically, they are the same. But remember, the maximun of the duration people play a game, is proportional to the content amount of the game, while, things too similar don't add up to the amount of content, so even though all of them are basically the same, they don't share the same form, so they add up to the amount of content seperately. This is what you can take good advantage of, and you should. 
   I think all idle game designers should know one important difference between resource and upgrades. Most games have 2~5 resources, but most games have at least 15 different form of upgrades, if you add resources to the game, it's always very powerful, unless it's crafting system(pic1.png). But if you add upgrades to the game, even in a good enough way, it's normal. If you happen to add it in a lame way, it doesn't help significantly. So, remember, it's better to design the game with multiple resources from the beginning, and unlock at least 2.
   Now, please look at pic1.png. In the png, I shown a lot of existing way to organize the upgrades. One thing I have to make super clear, is the difference between ingredient and resource. In the crafting system, every ingredient is from 1 or few recipes, usually 1, and goes for 1 or few product, but resources are from at least 10 ways and goes for at least 10 ways. It means, for every resource, you can add at least 20 upgrades to the game, but for every ingredient, it's usually no more than 5 recipes. And also, recipes look similar, but what you can do with a resource is basically everything, upgrades/crafting/challenge/unlocks/achievement and a lot, this is another reason why add resources is always more powerful for a game than adding ingredients.

   For multiplayer idle game, at least 2 thing can be added, transaction, pvp. Transaction and pvp are similar because they allow people to add information to the game on the fly. The content/information amount is quite different for single player and multiply players. If you allow people to add more informations to the game, you may take advantage of the players intelligence. I'm not good at these theory.

   I mentioned test system, let me explain it. In most cases, people know what they are gonna obtain before they decide to buy any upgrades or go for any recipes. But in real world, sometimes we don't know the out come before we really test the ideas. Very few idle games have such systems in them, but such systems contribute to the game massively. It's like a playground, people test out their ideas and see which is the best, and set up as the best one, and then idle, increase. The testing consumes a lot time and let people to think of different ideas, even when the game is closed. You don't have to balance, simply add more choises. And you can add almost infinite layers of complexity in a isolated system. Even you mess, the design never pollutes outside. But the downside is, testing system usually cost more code and polishing, it at least needs an evaluation feature, and an extra feature to let people save their configurations.

======Chapter 3, progressive speed
   Before we dive into this topic, if you feel like, "should I speed the game up a bit so it's not so boring/slow", and on the other hand, "If I speed the game up a bit, it's too short.". If this is the case, then you need more content/information for your game. Read chapter 2.
   Now I assume your game have enough content, or it's supposed to be short, or it's ok for you for any reason, then, what is a good speed to unlock the content for players.
   Is unlocking content too fast bad? I don't think so. People still have to spend enough time to learn these content, then get used to it. This duration is basically constant for a person. If a lot content are dumped to the person, it simply consume them one by one. So the total time is still constant, if ignore the details.
   Is unlocking all the content right from the beginning a good idea? The answer is likely to be no. If the game is small, short, with only limited amount of content, it's still ok. The issue comes as, if a lot late game content are unlocked too early, people will find it's super hard to figure out what to do. It means, the proportion of "playable"/"unlocked" at any given moment is the key, if it's too low, people spend a lot time figuring out "ok, Im not supposed to touch this, and this, and that right now". If your game lacks of complexity, this is still a tool which may help, but if your game is already complex enough, this can be an issue.
   What happens if content is unlocked too slow? People feel stucked, and quit. Theorically, they don't see new content at a specific moment, and they don't expect to see enough new content, they quit. This quiting moment is the minimun duration people play a game.
   How to measure the amount of content? I didn't mention how to do this quantitatively, because it was in my previous paper <<Surprise is all you need>>. It's now only in Chinese language, if really a lot people read my papers, I'll translate it into English, or simply try out Google translation.
   Again, similar content doesn't contribute to the amount of content/information. If in a period of time, the game only unlocks similar content, it may release too little amount of information, people would probably feel the game is repeating or simply stucked, and quit.
   By far, almost all the idle games start from 0 progress or nearly 0. Many years ago, this was a good design, at that time, people have very limited idea of how a game works. But now, people are more experienced, skilled at playing games, so starting from 0 looks lame now. The issue is like, the very beginning 15 minutes are usually very slow and sh*tty. I've seen people conplain about this in a lot of games. Consider unlock more than 1 content in the beginning, this can help attacting the experienced players, and they are probably the majority of your users.

======Chapter 4, game content/assets reuse
   According to convention, video games have plot(剧情), so the game progresses in a line. This causes some issue for games without plot. If a video game doesn't have any plot or is not stage based, it doesn't have to progress from the beginning to the end. Content/assets don't have to be organized in a line.
   From 2016, idle games use a prestige method to let people reset progress while obtain some global boost. In such a way, the early game content is reused, which is good, but late game content doesn't benifit from this. 
   In pic2.png, I shown some estimated reuse of content for different kind of games. The last one, idle game with random consquence of progress, doesn't exist for now. Someone please try it out. The basic idea is, the content is organised in phases, and every time a phase is finished, a random phase is unlocked for player. Or it's like, from stage x to stage y, where x and y are random numbers. And phases can be duplicated, or overlapped, or anything. This trich helps late game content reuse. In fact, in such a way, there's no way to say if some content is early or late, they come randomly.

======Chapter 5, progression isolation
   Progression isolation tackles the issue of "if people stay in a phase/stage/something for longer than they are supposed to, they accumulate more resource/upgrades/something than they are supposed to, they feel too easy in the up coming part/phase/stage/a period of time." If different parts are isolated somehow, somewhat heavily, this issue can be decreased, or solved almost totally.
   Let me describe it a bit more. Let's say, in phase 1, people are supposed to have 1000 coins to unlock phase 2. According to test, if people are fimiliar with the game enough, they should finish the phase 1 phase in 5 hours and buy the critical unlock, and enter the phase 2 and have a lot new content. But someone stayed in phase 1 for 10 hours(for any reason I don't care), and had like 5000 coins, and spent 1000 coins for the critical unlock. When that guy entered the phase 2, it starts with 4000 coins, not 0 coins, and the early part of phase 2 of it is super easy. This example shows what happens if the game lacks progress isolation.
   So, how to do progress isolation? At least we can have 3 ways, by spacial, resource, and number.
   Spacial isolation is very intuitive. Some critical unlocks unlock corresponding space/maps. But if your game doesn't have any map system, like most idle games do, this doesn't work for your game.
   Resource isolation always work in idle games but it's not the only way. Resource isolation is pretty hard, before a resource is unlocked, no matter what people do, they don't get it. It's not about time or anything, it's simply not possible. It feels like stage based style.
   Number isolation is a soft way, and yeah, it always works for all the idle games. It feels like, if the resource 2 is 1000 times expensive than resource 1, so people can accumulate more to get a slightly easier start of next phase, but it's controllable. The example is like: someone stayed in phase 1 for longer than expected and accumulated 5000 coins. It spent 1000 coins for the critical unlock and unlocked a lot new content. In the new content, the cheapest upgrade is around 500 coins, others are all above 1000 coins. It only had 4000 coins left, so only can afford of few upgrades. The very beginning of phase 2 was in fact easier for it, but the difficulty recovers to the design level after 1 or 2 minutes, which is great.
   If the isolation is considered with the relationship between resources/ingredients, it looks like pic3.png. Most idle games don't have any space/maps system, even they have, the structure is similar. For resource based cases, both isolations are possible. For crafting cases, it's a bit messy. Crafting chain, or sometimes we call it pipeline managing, doesn't support resource isolation. Crafting tree doesn't support number isolation well enough. Crafting graph supports both but only normally, I personally don't recommend a super big system in crafting graph style.
   pic4.png shows what happens when isolation combines with reusing. But actually you can do almost anything. A simple trick is like, if the game resets progression of any parts, simply keep some global upgrades/boots, make sure people feel their progress is saved somehow and actually contributes at least a bit.
   pic4.png only shows 3 layers, but in fact you can stack more. In this way, all the job you put in the game contributes to new layers. If my previous researchment is correct enough, the information is multiplied to what you already added into the game. It looks like, from 10*10*10 to 10*10*10*2. If you add more mutually exclusive content, it looks like, from log(100)*log(100), to log(100)*log(100+20)

======Chapter 6, balancing in idle games, and what can be done with imbalance
   Balancing in idle games is quite different from it in other kind of video games. Let's say in a shooting game, I mean whatever shooting game, if dev decide to make 3 weapons, and if they want people to use them evenly, they have to balance them. The reason is usually, every weapon is not cheap to implement. But in most idle games, every item is simply an icon with very few code. They can be very cheap. In such a case, imbalance maybe can help the game.
   In fact I recommend reasonable amount of imbalance. In other words, don't balance idle game too much. If an idle game is perfectly balanced, people simply click on random upgrade, and wait for the numbers to increase, this decreases the content people really care. If an idle game is not balanced(at least not ridiculously), people can have some fun figuring out the best progressing path. This also helps even the idle game is co-op or pvp.

======Chapter 7, is random upgrade/recipe generator a good idea?
   First of all, this random gen system is super hard to implement. The math needed is crazy. If you are not ready for this, skip this chapter.
   I've tried once, the project was called random upgrade generator. It's based on algorithm and math heavily. The project is abandoned. No plan to resume it.
   I haven't seen any idle game with this system, but it's absolutely a cool idea. Also, remember, you don't have to balance the generator too much, simply make sure it's not too ridiculous.
   Again, someone please try this in your project.

======Chapter 8, some details about GUI
   I don't plan to explain any theory of GUI too much. But I still would say some of them here.
   For a rectangle button, its actual size is evaluated as a 1 direction result. The formula is like: ln(max(width, height)). Or, step 1, figure out the max between width and height, step 2, calculate the ln(or any logrithm of it). It mean, with the same area, circular buttons have the greatest actual size. Among rect buttons, square is best, thin while long is the worst.
   The second thing I would say, is the length of total cursor path. Don't make people move cursor too much, in fact you should try minimize this total length. Keep in mind how people actually use the gui, and based on this, optimize it.
   Put ui of related informations in the same screen at the same time as possible, unless people can toggle between them, and while toggling, no vision help is needed. Basically, if there's no keyboard shortcut to help toggle, it's bad design.
   When to automate a button? Theoritically, I recommend the moment people are estimated as already know every detail about this button. It mean, if some content is consumed by the player, don't force it to use it any more. But before that, it's safe not to automate it. 
   
======Chapter 9, game recommendation
   Idle defender series, by Barbasu. I think at least v2 and new beginning are good enough. The 2 versions both have multiple resources, massive information, in game testing system. 
   Synergism, by plactonic. In fact this project is contributed by a lot people, really a lot. But now they speeded up the early game too much. When it was firstly released, it was way slower. It has cascade resources for isolation, tons of upgrades and enough imbalance, in late game it has a testing system. It's like a puzzling game based on idle game.




















