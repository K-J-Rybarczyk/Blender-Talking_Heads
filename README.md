#Talking Heads - Blender Addon
----

###What it is?

This is an addon for Blender of course (and part of my thesis). This is a pack of simple tools to make work with lip-sync easier. Currently Blender don't have any 100% working automatic lip-sync system like Voice-o-Matic for example. No, no, no, this plugin is not a 100% working tool too. This is rather a basic equipment to develop in the future. I have hope that maybe someone will interest in subject and we will have some true, big, one in million system of automatic lip-sync in Blender in some time. Now, we have THIS! :D Talking Heads!

Ah, you ask, why "Talking Heads"? It is in a memory of victim of my hard work with this addon - Head.blend. You can find her here too, she is especially good, when you want to try how my plugin works - she was made mainly with my addon. The name is in a memory of Talking Heads from Fallouts games too - If you have ever play Fallout 1 or 2, you know what I talking about.

But now, go on to important things.



###How work with this?

![panel.png](https://raw.githubusercontent.com/K-J-Rybarczyk/Blender-Talking_Heads/master/Screens/panel.png "Panel")

Here you see a panel of my addon. You can find it in Tool Bar in Animation tab. Now, what is what...

**Addres of dictionary file** - This addon work with dictionary file (file like this you can find in repository too, now only with 3082 most common words but in the future it will be bigger). In this field you write, where is dictionary file, for example: "C:\MyFiles\MyBlenderWork\Animation\dictionary".

**Apply dictionary** - You must press this to remake file to dictionary working in Blender.

**Add Phoneme Armature** - First true Blender option. Adding special armature that my plugin use to animate.

**Add Phoneme Shapekeys** - Adding empty phoneme shape keys that my plugin use, to selected mesh.

**Armature to link name** - If you want (of course you want) to link armature to mesh, here you write name of armature for a model.

**Link Shape Keys to Armature** - First, select your mesh with phoneme shape keys that you want link with armature in "Armature to link name", then just press this button. Voilà! If you do everything alright then now you should have beauty drivers on all phoneme shape keys. Nice. Now your model is ready to animate!

**Text to animation** - I think this is self explanatory. This is what your model will talking.

**Animation starting frame** - Again, easy like you see. After makeing animation value will be the same like the end of animation - you don't want to overwrite your animation by accident.

**Apply animation** - Magic button, that create animation from your text.