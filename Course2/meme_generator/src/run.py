from QuoteEngine.Ingestor import Ingestor
import argparse 

if __name__ =="__main__":


	parser = argparse.ArgumentParser(description="Meme Genrator")
	parser.add_argument('file', type=str)
	args = parser.parse_args()
	print(f'_data/DogQuotes/{args.file}')
	
	quotes = Ingestor.parse(f'_data/DogQuotes/{args.file}')

	print(quotes)

	 