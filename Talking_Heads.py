bl_info = {
	"name": "Talking Heads",
	"author": "Karolina Jolanta Rybarczyk",
	"version": (0, 1),
	"blender": (2, 74, 0),
	"location": "Tool bar > Animation tab > Talking Heads",
	"description": "Tool for automatic lip-sync",
	"category": "Animation",
}


import bpy
import string
from bpy.props import *


##############################Lists for armature create##############################

phonemes_vowel=['i','ee','oo','ue','o','e','a','u','ar','er','ur','au','ie','ear','air','ow','ae','oi','oe','ure']
phonemes_vowel_MCH=['i_f.MCH','i_s.MCH','oo_f.MCH','oo_s.MCH','e_f.MCH','ar_f.MCH','er_f.MCH','er_s.MCH','au_f.MCH']
phonemes_consonant=['b','p','t','d','h','y','k','l','r','n','m','f','v','g','s','w','z','j','th','wh','ch','sh','zh','ng']

phonemes_all=phonemes_vowel+phonemes_consonant
phonemes_all.append('rest')

shapekeys_list=list(phonemes_all)
shapekeys_list.remove('ie')
shapekeys_list.remove('ear')
shapekeys_list.remove('air')
shapekeys_list.remove('ow')
shapekeys_list.remove('ae')
shapekeys_list.remove('oi')
shapekeys_list.remove('oe')
shapekeys_list.remove('ure')

##############################Lists for armature create##############################



##############################Panel##############################

class Talking_Heads_Panel(bpy.types.Panel):

	bl_label = 'Talking Heads'
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = "Animation"

	dictionary_adress = StringProperty(name="Addres of dictionary file")
	armature_name = StringProperty(name="Armature to link name") 
	anim_text = StringProperty(name="Text to animation")
	starting_frame = IntProperty(name="Animation starting frame", default=(1))



	def draw(self, context):

		layout = self.layout

		layout.prop(context.scene, "dictionary_adress")
		layout.operator("mesh.dictionary_apply", text = "Apply dictionary")
		layout.operator("mesh.add_phoneme_armature", text = "Add Phoneme Armature")
		layout.operator("mesh.add_phoneme_shapekeys", text = "Add Phoneme Shapekeys")
		layout.prop(context.scene, "armature_name")
		layout.operator("mesh.link", text = "Link Shape Keys to Armature")
		layout.prop(context.scene, "anim_text")
		layout.prop(context.scene, "starting_frame")
		layout.operator("mesh.anim_apply", text = "Apply animation")

##############################Panel##############################



##############################Adding Dictionary##############################

class Adding_Dictionary(bpy.types.Operator) :

	bl_idname = 'mesh.dictionary_apply'
	bl_label = 'Apply dictionary'

	def execute(self, context):				#creating dictionary from file

		file_addres=context.scene.dictionary_adress
		Adding_Dictionary.dictionary={}

		text1 = open(file_addres, 'r')
	
		for line in text1:
			x=line.split(";")
			a=x[0].lower()
			b=x[1]

			b=b.rstrip()
			b=b.split('\t');
			b.remove('')

			Adding_Dictionary.dictionary[a]=b

		text1.close()

		return{'FINISHED'}

##############################Adding Dictionary##############################



##############################Phoneme Armature##############################

class Phoneme_Armature(bpy.types.Operator) :

	bl_idname = 'mesh.add_phoneme_armature'
	bl_label = 'Add Phoneme Armature'

	def execute(self, context):

		bpy.ops.object.armature_add()
		bpy.context.object.name = "Phonemes"
		active_ob = bpy.context.active_object
		phonemes_armature = active_ob.data
		bpy.context.object.data.draw_type = 'BBONE'
		bpy.context.object.data.show_names = True
		bpy.context.object.show_x_ray = True
		bpy.ops.object.mode_set(mode='EDIT')



		for i in range(len(phonemes_all)):
			bpy.ops.armature.bone_primitive_add(name=phonemes_all[i])
			pa = phonemes_armature.edit_bones[i]
			pa_name = phonemes_all[i]

			bpy.ops.object.mode_set(mode='POSE')
			bpy.data.objects[active_ob.name].pose.bones[pa_name].rotation_mode = 'XYZ'
			bpy.data.objects[active_ob.name].pose.bones[pa_name].lock_rotation[0] = True
			bpy.data.objects[active_ob.name].pose.bones[pa_name].lock_rotation[1] = True
			bpy.data.objects[active_ob.name].pose.bones[pa_name].lock_rotation[2] = True
			bpy.data.objects[active_ob.name].pose.bones[pa_name].lock_location[0] = True
			bpy.data.objects[active_ob.name].pose.bones[pa_name].lock_location[1] = True
			bpy.data.objects[active_ob.name].pose.bones[pa_name].lock_location[2] = True
			bpy.data.objects[active_ob.name].pose.bones[pa_name].lock_scale[0] = True
			bpy.data.objects[active_ob.name].pose.bones[pa_name].lock_scale[2] = True
			bpy.data.objects[active_ob.name].pose.bones[pa_name].constraints.new('LIMIT_SCALE')
			bpy.context.object.pose.bones[pa_name].constraints["Limit Scale"].use_min_y = True
			bpy.context.object.pose.bones[pa_name].constraints["Limit Scale"].min_y = 0.5
			bpy.context.object.pose.bones[pa_name].constraints["Limit Scale"].use_max_y = True
			bpy.context.object.pose.bones[pa_name].constraints["Limit Scale"].max_y = 1
			bpy.context.object.pose.bones[pa_name].constraints["Limit Scale"].owner_space = 'LOCAL'

			bpy.data.objects[active_ob.name].pose.bones[pa_name].constraints.new('LIMIT_ROTATION')
			bpy.context.object.pose.bones[pa_name].constraints["Limit Rotation"].use_limit_x = True
			bpy.context.object.pose.bones[pa_name].constraints["Limit Rotation"].min_x = 0
			bpy.context.object.pose.bones[pa_name].constraints["Limit Rotation"].use_limit_x = True
			bpy.context.object.pose.bones[pa_name].constraints["Limit Rotation"].max_x = 0
			bpy.context.object.pose.bones[pa_name].constraints["Limit Rotation"].use_limit_y = True
			bpy.context.object.pose.bones[pa_name].constraints["Limit Rotation"].min_y = 0
			bpy.context.object.pose.bones[pa_name].constraints["Limit Rotation"].use_limit_y = True
			bpy.context.object.pose.bones[pa_name].constraints["Limit Rotation"].max_y = 0
			bpy.context.object.pose.bones[pa_name].constraints["Limit Rotation"].use_limit_z = True
			bpy.context.object.pose.bones[pa_name].constraints["Limit Rotation"].min_z = 0
			bpy.context.object.pose.bones[pa_name].constraints["Limit Rotation"].use_limit_z = True
			bpy.context.object.pose.bones[pa_name].constraints["Limit Rotation"].max_z = 0
			bpy.context.object.pose.bones[pa_name].constraints["Limit Rotation"].owner_space = 'LOCAL'

			bpy.data.objects[active_ob.name].pose.bones[pa_name].scale[1]=0.5

			bpy.ops.object.mode_set(mode='EDIT')



#Vowels

		for i in range(len(phonemes_vowel)):
			pv = phonemes_armature.edit_bones[phonemes_vowel[i]]
			pv.head = (i*0.5, 0, 0)
			pv.tail = (i*0.5, 0, 1)



#Consonants

		for i in range(len(phonemes_consonant)):
			pc = phonemes_armature.edit_bones[phonemes_consonant[i]]
			pc.head = (i*0.5, 0, -1)
			pc.tail = (i*0.5, 0, 0)



#Rest

		for i in range(0,1):
			pr = phonemes_armature.edit_bones['rest']
			pr.head = (i*0.5, 0, -2)
			pr.tail = (i*0.5, 0, -1)



#Delete one error bone

		phonemes_armature.edit_bones['Bone'].select = True
		bpy.ops.armature.delete()



#Vowels_MCH

		bpy.context.object.data.layers[1] = True
		bpy.context.object.data.layers[0] = False

		for i in range(len(phonemes_vowel_MCH)):
			bpy.ops.armature.bone_primitive_add(name=phonemes_vowel_MCH[i])
			pv_MCH = phonemes_armature.edit_bones[phonemes_vowel_MCH[i]]
			pv_MCH.head = (i*0.5, 0, 1)
			pv_MCH.tail = (i*0.5, 0, 2)
			pv_MCH_name = phonemes_vowel_MCH[i]

			bpy.ops.object.mode_set(mode='POSE')
			bpy.data.objects[active_ob.name].pose.bones[pv_MCH_name].rotation_mode = 'XYZ'
			bpy.data.objects[active_ob.name].pose.bones[pv_MCH_name].lock_rotation[0] = True
			bpy.data.objects[active_ob.name].pose.bones[pv_MCH_name].lock_rotation[1] = True
			bpy.data.objects[active_ob.name].pose.bones[pv_MCH_name].lock_rotation[2] = True
			bpy.data.objects[active_ob.name].pose.bones[pv_MCH_name].lock_location[0] = True
			bpy.data.objects[active_ob.name].pose.bones[pv_MCH_name].lock_location[1] = True
			bpy.data.objects[active_ob.name].pose.bones[pv_MCH_name].lock_location[2] = True
			bpy.data.objects[active_ob.name].pose.bones[pv_MCH_name].lock_scale[0] = True
			bpy.data.objects[active_ob.name].pose.bones[pv_MCH_name].lock_scale[2] = True
			bpy.data.objects[active_ob.name].pose.bones[pv_MCH_name].constraints.new('LIMIT_SCALE')
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Scale"].use_min_y = True
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Scale"].min_y = 0.5
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Scale"].use_max_y = True
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Scale"].max_y = 1
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Scale"].owner_space = 'LOCAL'

			bpy.data.objects[active_ob.name].pose.bones[pv_MCH_name].constraints.new('LIMIT_ROTATION')
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Rotation"].use_limit_x = True
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Rotation"].min_x = 0
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Rotation"].use_limit_x = True
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Rotation"].max_x = 0
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Rotation"].use_limit_y = True
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Rotation"].min_y = 0
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Rotation"].use_limit_y = True
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Rotation"].max_y = 0
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Rotation"].use_limit_z = True
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Rotation"].min_z = 0
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Rotation"].use_limit_z = True
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Rotation"].max_z = 0
			bpy.context.object.pose.bones[pv_MCH_name].constraints["Limit Rotation"].owner_space = 'LOCAL'

			bpy.data.objects[active_ob.name].pose.bones[pv_MCH_name].scale[1]=0.5

			bpy.ops.object.mode_set(mode='EDIT')

		bpy.context.object.data.layers[0] = True
		bpy.context.object.data.layers[1] = False


#drivers

#i_f.MCH

		i_f_MCH_driver = bpy.context.object.pose.bones["i_f.MCH"].driver_add('scale', 1)
		driver_options = i_f_MCH_driver.driver
		driver_options.type = 'MAX'

		driver_var=driver_options.variables.new()
		driver_var.name = 'ear'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "ear"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		modifier = i_f_MCH_driver.modifiers[0]
		modifier.mode = 'POLYNOMIAL'
		modifier.poly_order = 2
		modifier.coefficients = (-3.5, 12, -8)



#i_s.MCH

		i_s_MCH_driver = bpy.context.object.pose.bones["i_s.MCH"].driver_add('scale', 1)
		driver_options = i_s_MCH_driver.driver
		driver_options.type = 'MAX'

		driver_var=driver_options.variables.new()
		driver_var.name = 'ie'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "ie"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		driver_var=driver_options.variables.new()
		driver_var.name = 'ae'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "ae"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		driver_var=driver_options.variables.new()
		driver_var.name = 'oi'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "oi"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		modifier = i_s_MCH_driver.modifiers[0]
		modifier.mode = 'POLYNOMIAL'
		modifier.poly_order = 2
		modifier.coefficients = (2, -5, 4)



#oo_f.MCH

		oo_f_MCH_driver = bpy.context.object.pose.bones["oo_f.MCH"].driver_add('scale', 1)
		driver_options = oo_f_MCH_driver.driver
		driver_options.type = 'MAX'

		driver_var=driver_options.variables.new()
		driver_var.name = 'ure'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "ure"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		modifier = oo_f_MCH_driver.modifiers[0]
		modifier.mode = 'POLYNOMIAL'
		modifier.poly_order = 2
		modifier.coefficients = (-3.5, 12, -8)



#oo_s.MCH

		oo_s_MCH_driver = bpy.context.object.pose.bones["oo_s.MCH"].driver_add('scale', 1)
		driver_options = oo_s_MCH_driver.driver
		driver_options.type = 'MAX'

		driver_var=driver_options.variables.new()
		driver_var.name = 'ow'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "ow"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		driver_var=driver_options.variables.new()
		driver_var.name = 'oe'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "oe"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		modifier = oo_s_MCH_driver.modifiers[0]
		modifier.mode = 'POLYNOMIAL'
		modifier.poly_order = 2
		modifier.coefficients = (2, -5, 4)



#e_f.MCH

		e_f_MCH_driver = bpy.context.object.pose.bones["e_f.MCH"].driver_add('scale', 1)
		driver_options = e_f_MCH_driver.driver
		driver_options.type = 'MAX'

		driver_var=driver_options.variables.new()
		driver_var.name = 'air'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "air"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		driver_var=driver_options.variables.new()
		driver_var.name = 'ae'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "ae"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		modifier = e_f_MCH_driver.modifiers[0]
		modifier.mode = 'POLYNOMIAL'
		modifier.poly_order = 2
		modifier.coefficients = (-3.5, 12, -8)



#ar_f.MCH

		ar_f_MCH_driver = bpy.context.object.pose.bones["ar_f.MCH"].driver_add('scale', 1)
		driver_options = ar_f_MCH_driver.driver
		driver_options.type = 'MAX'

		driver_var=driver_options.variables.new()
		driver_var.name = 'ie'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "ie"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		driver_var=driver_options.variables.new()
		driver_var.name = 'ow'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "ow"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		modifier = ar_f_MCH_driver.modifiers[0]
		modifier.mode = 'POLYNOMIAL'
		modifier.poly_order = 2
		modifier.coefficients = (-3.5, 12, -8)



#er_f.MCH

		er_f_MCH_driver = bpy.context.object.pose.bones["er_f.MCH"].driver_add('scale', 1)
		driver_options = er_f_MCH_driver.driver
		driver_options.type = 'MAX'

		driver_var=driver_options.variables.new()
		driver_var.name = 'oe'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "oe"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		modifier = er_f_MCH_driver.modifiers[0]
		modifier.mode = 'POLYNOMIAL'
		modifier.poly_order = 2
		modifier.coefficients = (-3.5, 12, -8)



#er_s.MCH

		er_s_MCH_driver = bpy.context.object.pose.bones["er_s.MCH"].driver_add('scale', 1)
		driver_options = er_s_MCH_driver.driver
		driver_options.type = 'MAX'

		driver_var=driver_options.variables.new()
		driver_var.name = 'ear'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "ear"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		driver_var=driver_options.variables.new()
		driver_var.name = 'air'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "air"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		driver_var=driver_options.variables.new()
		driver_var.name = 'ure'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "ure"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		modifier = er_s_MCH_driver.modifiers[0]
		modifier.mode = 'POLYNOMIAL'
		modifier.poly_order = 2
		modifier.coefficients = (2, -5, 4)



#au_f.MCH

		au_f_MCH_driver = bpy.context.object.pose.bones["au_f.MCH"].driver_add('scale', 1)
		driver_options = au_f_MCH_driver.driver
		driver_options.type = 'MAX'

		driver_var=driver_options.variables.new()
		driver_var.name = 'oi'
		driver_var.type = 'TRANSFORMS'

		target = driver_var.targets[0]
		target.id = bpy.data.objects[active_ob.name].id_data
		target.bone_target = "oi"
		target.transform_type = 'SCALE_Y'
		target.transform_space = 'LOCAL_SPACE'

		modifier = au_f_MCH_driver.modifiers[0]
		modifier.mode = 'POLYNOMIAL'
		modifier.poly_order = 2
		modifier.coefficients = (-3.5, 12, -8)



		return{'FINISHED'}

##############################Phoneme Armature##############################



##############################Phoneme Shape Keys##############################

class Phoneme_ShapeKeys(bpy.types.Operator) :

	bl_idname = 'mesh.add_phoneme_shapekeys'
	bl_label = 'Add Phoneme Shape Keys'

	def execute(self, context):
		active_ob = bpy.context.active_object
		active_key = bpy.data.objects[active_ob.name].data.shape_keys

		if not active_key:
			bpy.ops.object.shape_key_add(from_mix=False)
			active_key = bpy.data.objects[active_ob.name].data.shape_keys

		for i in range(len(shapekeys_list)):
			#creating and name empty shapekeys
			bpy.ops.object.shape_key_add(from_mix=False)
			key_number=bpy.context.object.active_shape_key_index
			bpy.data.shape_keys[active_key.name].key_blocks['Key %s'%key_number].name = shapekeys_list[i]

		return{'FINISHED'}

##############################Phoneme Shape Keys##############################



##############################Link Shape Keys to Armature##############################

class Link_ShapeKeys(bpy.types.Operator) :

	bl_idname = 'mesh.link'
	bl_label = 'Link Shape Keys to Armature'

	def execute(self, context):
		active_ob = bpy.context.active_object
		linked_armature=context.scene.armature_name
		active_key = bpy.data.objects[active_ob.name].data.shape_keys

		if context.scene.armature_name=='':
			print("There is no name")

		else:
	
#basic drivers
			
			for i in range (len(shapekeys_list)):
				driver = bpy.data.shape_keys[active_key.name].key_blocks[shapekeys_list[i]].driver_add('value', -1)
				driver_options = driver.driver
				driver_options.type = 'MAX'

				driver_var=driver_options.variables.new()
				driver_var.name = shapekeys_list[i]
				driver_var.type = 'TRANSFORMS'

				target = driver_var.targets[0]
				target.id = bpy.data.objects[linked_armature].id_data
				target.bone_target = shapekeys_list[i]
				target.transform_type = 'SCALE_Y'
				target.transform_space = 'LOCAL_SPACE'

				modifier = driver.modifiers[0]
				modifier.mode = 'POLYNOMIAL'
				modifier.poly_order = 2
				modifier.coefficients = (-0.5, 0, 2)

#additional drivers
		
		#i

			i_driver = bpy.data.shape_keys[active_key.name].key_blocks["i"].driver_add('value', -1)
			driver_options = i_driver.driver
			driver_options.type = 'MAX'

			driver_var=driver_options.variables.new()
			driver_var.name = 'i_f.MCH'
			driver_var.type = 'TRANSFORMS'

			target = driver_var.targets[0]
			target.id = bpy.data.objects[linked_armature].id_data
			target.bone_target = "i_f.MCH"
			target.transform_type = 'SCALE_Y'
			target.transform_space = 'LOCAL_SPACE'

			driver_var=driver_options.variables.new()
			driver_var.name = 'i_s.MCH'
			driver_var.type = 'TRANSFORMS'

			target = driver_var.targets[0]
			target.id = bpy.data.objects[linked_armature].id_data
			target.bone_target = "i_s.MCH"
			target.transform_type = 'SCALE_Y'
			target.transform_space = 'LOCAL_SPACE'



		#oo

			oo_driver = bpy.data.shape_keys[active_key.name].key_blocks["oo"].driver_add('value', -1)
			driver_options = oo_driver.driver
			driver_options.type = 'MAX'

			driver_var=driver_options.variables.new()
			driver_var.name = 'oo_f.MCH'
			driver_var.type = 'TRANSFORMS'

			target = driver_var.targets[0]
			target.id = bpy.data.objects[linked_armature].id_data
			target.bone_target = "oo_f.MCH"
			target.transform_type = 'SCALE_Y'
			target.transform_space = 'LOCAL_SPACE'

			driver_var=driver_options.variables.new()
			driver_var.name = 'oo_s.MCH'
			driver_var.type = 'TRANSFORMS'

			target = driver_var.targets[0]
			target.id = bpy.data.objects[linked_armature].id_data
			target.bone_target = "oo_s.MCH"
			target.transform_type = 'SCALE_Y'
			target.transform_space = 'LOCAL_SPACE'



		#e

			e_driver = bpy.data.shape_keys[active_key.name].key_blocks["e"].driver_add('value', -1)
			driver_options = e_driver.driver
			driver_options.type = 'MAX'

			driver_var=driver_options.variables.new()
			driver_var.name = 'e_f.MCH'
			driver_var.type = 'TRANSFORMS'

			target = driver_var.targets[0]
			target.id = bpy.data.objects[linked_armature].id_data
			target.bone_target = "e_f.MCH"
			target.transform_type = 'SCALE_Y'
			target.transform_space = 'LOCAL_SPACE'



		#ar

			ar_driver = bpy.data.shape_keys[active_key.name].key_blocks["ar"].driver_add('value', -1)
			driver_options = ar_driver.driver
			driver_options.type = 'MAX'

			driver_var=driver_options.variables.new()
			driver_var.name = 'ar_f.MCH'
			driver_var.type = 'TRANSFORMS'

			target = driver_var.targets[0]
			target.id = bpy.data.objects[linked_armature].id_data
			target.bone_target = "ar_f.MCH"
			target.transform_type = 'SCALE_Y'
			target.transform_space = 'LOCAL_SPACE'



		#er

			er_driver = bpy.data.shape_keys[active_key.name].key_blocks["er"].driver_add('value', -1)
			driver_options = er_driver.driver
			driver_options.type = 'MAX'

			driver_var=driver_options.variables.new()
			driver_var.name = 'er_f.MCH'
			driver_var.type = 'TRANSFORMS'

			target = driver_var.targets[0]
			target.id = bpy.data.objects[linked_armature].id_data
			target.bone_target = "er_f.MCH"
			target.transform_type = 'SCALE_Y'
			target.transform_space = 'LOCAL_SPACE'

			driver_var=driver_options.variables.new()
			driver_var.name = 'er_s.MCH'
			driver_var.type = 'TRANSFORMS'

			target = driver_var.targets[0]
			target.id = bpy.data.objects[linked_armature].id_data
			target.bone_target = "er_s.MCH"
			target.transform_type = 'SCALE_Y'
			target.transform_space = 'LOCAL_SPACE'



		#au

			au_driver = bpy.data.shape_keys[active_key.name].key_blocks["au"].driver_add('value', -1)
			driver_options = au_driver.driver
			driver_options.type = 'MAX'

			driver_var=driver_options.variables.new()
			driver_var.name = 'au_f.MCH'
			driver_var.type = 'TRANSFORMS'

			target = driver_var.targets[0]
			target.id = bpy.data.objects[linked_armature].id_data
			target.bone_target = "au_f.MCH"
			target.transform_type = 'SCALE_Y'
			target.transform_space = 'LOCAL_SPACE'



			active_ob.select=False
			bpy.data.objects[linked_armature].select = True
			bpy.context.scene.objects.active = bpy.data.objects[linked_armature]

		return{'FINISHED'}

##############################Link Shape Keys to Armature##############################



##############################Animation##############################

class Animation_Apply(bpy.types.Operator) :
	
	bl_idname = 'mesh.anim_apply'
	bl_label = 'Apply'

	def execute(self, context):
		bpy.ops.object.mode_set(mode='POSE')
		active_ob = bpy.context.active_object
		frame_of_animation = context.scene.starting_frame+2


		if context.scene.anim_text=='':
			print("There is no text")

		else:				#simplify text
			anim_text = ''

			for i in context.scene.anim_text:
				if not i in string.punctuation:
					anim_text = anim_text+i

			text_list = anim_text.split()	

			for word_number in range (0, len(text_list)):

				text_list[word_number]=text_list[word_number].lower()

				#print(text_list[word_number])

				if text_list[word_number] in Adding_Dictionary.dictionary:
					word=text_list[word_number]
					#print(word)

					for phoneme_number in range (0, len(Adding_Dictionary.dictionary[text_list[word_number]])):
						phoneme=Adding_Dictionary.dictionary[text_list[word_number]][phoneme_number]
						#print(phoneme)

						#adding keyframes
						bpy.context.scene.frame_current = frame_of_animation-8
						bpy.data.objects[active_ob.name].pose.bones[phoneme].scale[1]=0.5
						bpy.data.objects[active_ob.name].pose.bones[phoneme].keyframe_insert(data_path="scale")
						bpy.context.scene.frame_current=frame_of_animation
						bpy.data.objects[active_ob.name].pose.bones[phoneme].scale[1]=1
						bpy.data.objects[active_ob.name].pose.bones[phoneme].keyframe_insert(data_path="scale")
						frame_of_animation=frame_of_animation+2
						bpy.context.scene.frame_current=frame_of_animation
						bpy.data.objects[active_ob.name].pose.bones[phoneme].scale[1]=0.5
						bpy.data.objects[active_ob.name].pose.bones[phoneme].keyframe_insert(data_path="scale")					

				else:
					print("I don't know this word")
					break_in_anim = len(text_list[word_number])
					print(break_in_anim)
					frame_of_animation=frame_of_animation+(4*break_in_anim)
					
				frame_of_animation=frame_of_animation+8

			context.scene.starting_frame = frame_of_animation+6
			bpy.context.scene.frame_current = context.scene.starting_frame
				

		bpy.ops.object.mode_set(mode='POSE', toggle=True)
		
		return{'FINISHED'}

##############################Animation##############################



##############################Registration##############################

def register() :


	bpy.types.Scene.dictionary_adress = bpy.props.StringProperty(name="Addres of dictionary file")
	bpy.types.Scene.armature_name = bpy.props.StringProperty(name="Armature to link name") 
	bpy.types.Scene.anim_text = bpy.props.StringProperty(name="Text to animation")
	bpy.types.Scene.starting_frame = bpy.props.IntProperty(name="Animation starting frame")


#end register
 
def unregister() :
	del bpy.types.Scene.anim_text


bpy.utils.register_module(__name__)

##############################Registration##############################
