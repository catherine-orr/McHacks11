import py_avataaars as pd

hair = input("what is your hair color? Type 'brown', 'black', 'red', or 'blonde'\n")
skin = input("what is your skin color? Type 'light', 'tanned', or 'dark_brown', or 'black\n")
top = input("what is your hairstyle? Type 'straight', 'curly', or 'dreads'\n")
length = input("what is your hair length? type 'long' or 'short'\n")
facial = input("do you have facial hair? type y or n\n")

def avatar_creator(skin, hair, top, facial):
	if skin == 'light': 
		skin = pd.SkinColor.LIGHT
	elif skin == 'tanned':
		skin = pd.SkinColor.TANNED
	elif skin == 'dark_brown':
		skin = pd.SkinColor.DARK_BROWN
	elif skin == 'black':
		skin = pd.SkinColor.BLACK

	if facial == 'y':
		facial = pd.FacialHairType.BEARD_LIGHT
	elif facial == 'n':
		facial = pd.FacialHairType.DEFAULT

	if hair == 'black':
		hair = pd.HairColor.BLACK
	elif hair == 'blonde':
		hair = pd.HairColor.BLACK
	elif hair == 'brown':
		hair = pd.HairColor.BROWN
	elif hair == 'red':
		hair = pd.HairColor.RED


	if top == 'straight':
		if length =='long':
			top = pd.TopType.LONG_HAIR_STRAIGHT
		else:
			top = pd.TopType.SHORT_HAIR_SHORT_FLAT
	elif top == 'curly':
		if length =='long':
			top = pd.TopType.LONG_HAIR_CURLY
		else:
			top = pd.TopType.SHORT_HAIR_SHORT_CURLY
	elif top == 'dreads':
		if length =='long':
			top = pd.TopType.LONG_HAIR_DREADS
		else:
			top = pd.TopType.SHORT_HAIR_DREADS_01

	avatar = pd.PyAvataaar(style = pd.AvatarStyle.CIRCLE, skin_color = skin, hair_color = hair, facial_hair_type = facial, top_type = top, mouth_type = pd.MouthType.SMILE, eye_type = pd.EyesType.WINK_WACKY, eyebrow_type = pd.EyebrowType.DEFAULT, nose_type = pd.NoseType.DEFAULT, accessories_type = pd.AccessoriesType.DEFAULT, clothe_type = pd.ClotheType.HOODIE, clothe_graphic_type = pd.ClotheGraphicType.BAT,)
	avatar.render_png_file("AVATAR.png")

avatar_creator(skin, hair, top, facial)
	




				   




