#Talking Heads - Blender Addon
----

###What it is?

This is an addon for Blender of course (and part of my thesis). This is a pack of simple tools to make work with lip-sync easier. Currently Blender don't have any 100% working automatic lip-sync system like Voice-o-Matic for example. No, no, no, this plugin is not a 100% working tool too. This is rather a basic equipment to develop in the future. I sincerely hope that maybe someone will express an interest in this subject, and we will finally create a true, unique, one in a million system designed for automatic lip-sync for Blender in the future. For now, we have THIS! Talking Heads!

Ah, you ask, why "Talking Heads"? This name is in memory of victim of my hard work with this addon - Head.blend. You can find her here too, and she is especially good if you want to check out my plugin - she was made mainly with my addon. The name is in a memory of Talking Heads from Fallout games too - If you have ever played Fallout 1 or 2, you know what I'm talking about.

But now, go on to important things.



###How to use it?

![panel.png](https://raw.githubusercontent.com/K-J-Rybarczyk/Blender-Talking_Heads/master/Screens/panel.png "Panel")

Here you see a panel of my addon. You can find it in Tool Bar in Animation tab.

**Addres of dictionary file** - This addon works with a dictionary file (file like this you can find in repository too, now only with 3082 most common words but in the future it will be bigger). In this field you write, where is dictionary file, for example: "C:\MyFiles\MyBlenderWork\Animation\dictionary".

**Apply dictionary** - You must press this to create dictionary working with Blender. Your dictionary file will be used to do this.

**Add Phoneme Armature** - First true Blender option. Adding special armature that my plugin use to animate.

**Add Phoneme Shapekeys** - Adding empty phoneme shape keys that my plugin use to selected mesh.

**Armature to link name** - If you want (of course you want) to link armature to mesh, here you write name of armature for a model.

**Link Shape Keys to Armature** - First, select your mesh with phoneme shape keys that you want to link with armature in "Armature to link name", then just press this button. Voilà! If you do everything alright then now you should have beauty drivers on all phoneme shape keys. Nice. Now your model is ready to animate!

**Text to animation** - I think this is self explanatory. This is what your model will be talking.

**Animation starting frame** - Again, easy like you see. After making animation value will be the same as the end of animation - you don't want to overwrite your animation by accident.

**Apply animation** - Magic button, that creates animation from your text.



###Any warnings?

Unfortunately: yes. First of all - how I said earlier, this addon must have a special dictionary. Without this, nothing will work. What if you want to use words that are not in dictionary? I predicted such a possibility. My animation algorithm will leave empty space in place of such words, so you can easily create animation on your own.
Second important thing - automatic animation sometimes can be little... Twitchy. Yeah, that's a good word. A lot depends on the shape keys appearance. I tried as best to choose the duration of the individual phonemes, but still, this is an automat. I cannot promise too much at the moment.

Currently, this plugin only facilitates the work with lip-sync, doesn't do everything for us. At the end manual fixes are required.