import os 
from PIL import Image, ImageDraw, ImageFont
import pathlib
import random


class MemeGenerator: 
	"""Generate Meme for Images"""

	def __init__(self, output_path:str):
		""" Intialize the MemeGenerator by defining the output directory
		
		Arguments : 
		output_path (str): the output to save generated Images
		"""

		# Create the dir if not exist 
		os.makedirs(output_path ,exist_ok=True)

		self.output_path = output_path


	def _load_image(self, path): 
		return Image.open(path)


	def _resize(self, image, width:int,height:int = None): 
		""" Resize an given image to an assigned width an height
		Arguments: 
		image : the given image to be resized 
		width(int or float) : the targeted width, can be int or float number
		height(int or float) : the targeted height, can be int or float number
		"""
		if not height: 
			h_w_ratio = image.size[1] / image.size[0]
			height = int(width*h_w_ratio)

			
		image = image.resize((width,height))

		return image 


	

	def _add_quote(self, img, body: str, author: str):

		"""add quote to image 

		Arguments:
			body (str): Body of the quote.
			author (str): Author of the quote.
		"""

		draw = ImageDraw.Draw(img)
		font_path = (pathlib.Path(__file__).parent.parent.absolute() / "_data/fonts/SourceSansPro-Black.ttf")
		font = ImageFont.truetype(str(font_path), 20, encoding="unic")

		text = f'"{body}" \n -{author}'

		try : 
			draw.text((0, 0),text,(255,255,255),font=font)
		except : 
			raise Exception("Could not add quote to the image!!!")

		return img

	def make_meme(
		self, body: str, author: str, img_path: str, width:int=300, height:int=None) -> str:
		"""Make meme from given image and a quote.

		Arguments:
			img_path (str): Path to image.
			text (str): Body of quote.
			author (str): Author of quote.
			width (int)Optional : resize width.
			height(int)Optional : resize height.


		Return:
			str: Path of saved meme.
		"""

		img = self._load_image(img_path)
		img = self._resize(img, width ,height )
		img = self._add_quote(img, body, author)

		original_name = img_path.split(".jpg")[0].split("/")[-1]
		save_path = os.path.join(
			self.output_path,
			f"{original_name}_modified_{random.randint(0, 1000000000)}.jpg",
		)
		img.save(save_path)

		return save_path



