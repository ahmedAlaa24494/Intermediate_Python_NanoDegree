
from QuoteEngine.Ingestor import Ingestor
from MemeEngine.MemeGenerator import MemeGenerator
import argparse 


if __name__ =="__main__":


	parser = argparse.ArgumentParser(description="Meme Genrator")
	parser.add_argument('--file', type=str,default="DogQuotesCSV.csv")
	args = parser.parse_args()
	print(f'_data/DogQuotes/{args.file}')
	
	quotes = Ingestor.parse(f'_data/DogQuotes/{args.file}')
	body , author = quotes[0].body , quotes[0].author
	print(body)
	print(author)
	mg = MemeGenerator("_data/meme_out")

	img_path  = '_data/photos/dog/xander_1.jpg'
	img = mg.make_meme(body, author, img_path)
	print(img)


	 